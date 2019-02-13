classdef muscle < handle
    
    properties
        % These are properties that can be accessed from outside the
        % muscle class
        
        no_of_half_sarcomeres = 1;
        series_k_linear = 1e4;
        series_viscosity = 0;
        muscle_length;
        muscle_force = 0;
        
        % A holder for an array of half_sarcomeres
        hs = half_sarcomere;
    end
    
    properties (SetAccess = private)
        % These are properties that can only be accessed from within the
        % muscle class
        
        series_extension;
        last_series_extension;
        
    end
    
    methods
        
        % Constructor
        function obj = muscle(varargin)
            
            % Set up muscle
            
            % Start by updating variables
            muscle_props = varargin{1}
            
            obj.no_of_half_sarcomeres = muscle_props.no_of_half_sarcomeres;
            obj.series_k_linear = muscle_props.series_k_linear;
            obj.series_viscosity = muscle_props.series_viscosity;
            
            % Now create half_sarcomeres, updating muscle length as we go
            obj.muscle_length = 0;
            for hs_counter = 1:obj.no_of_half_sarcomeres
                obj.hs(hs_counter) = half_sarcomere();
                obj.muscle_length = obj.muscle_length + ...
                    obj.hs(hs_counter).hs_length;
            end

            % Implement force balance
            impose_force_balance(obj,0);
            
            % Store last series extension
            obj.last_series_extension = obj.series_extension;
        end
        
        % Other methods
        impose_force_balance(obj,dt);
        series_extension = return_series_extension(obj,muscle_force,time_step);
        series_force = return_series_force(obj,series_extension,time_step);
        implement_time_step(obj,time_step,delta_ml,Ca_vector);
    end
end
            
        