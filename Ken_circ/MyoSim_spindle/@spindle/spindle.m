classdef spindle < handle
    
    properties
        % These are properties that can be accessed from outside the
        % spindle class
        
        spindle_length;
        spindle_force = 0;
        
        chain_force = 0;
        chain_hs_length;
        chain_series_length;
        
        bag_force = 0;
        bag_hs_length;
        bag_series_length;
        
        % Muscle objects - which are really a half-sarcomere in
        % series with a viscosity and a spring in series
        m_chain = [];
        m_bag = [];
        
        
    end
    
    properties (SetAccess = private)
        % These are properties that can only be accessed from within
        % the spindle class
        
    end
    
    methods
        
        % Constructor
        function obj = spindle(varargin)
            
            % Set up spindle
            chain_props.no_of_half_sarcomeres = 1;
            chain_props.series_k_linear = 1e4;
            chain_props.series_viscosity = 0;
        
            bag_props.no_of_half_sarcomeres = 1;
            bag_props.series_k_linear = 1e2;
            bag_props.series_viscosity = 1e0;
            
            % Start by creating the bag and chain
            obj.m_chain = muscle(chain_props);
            impose_force_balance(obj.m_chain,0);
            
            obj.m_bag = muscle(bag_props);
            impose_force_balance(obj.m_bag,0);
            
            obj.spindle_length = obj.m_chain.muscle_length;
        end
        
        % Other methods
        implement_time_step(obj,time_step,delta_hs,Ca_concentration);
    end
    
end
    
            
        