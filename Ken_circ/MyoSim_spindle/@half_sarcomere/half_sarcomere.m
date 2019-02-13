classdef half_sarcomere < handle
    
    properties
        % These are properties that can be accessed from outside the
        % half-sarcomere class
        
        hs_length = 1300;   % the length of the half-sarcomere in nm
        hs_force;           % the stress (in N m^(-2)) in the half-sarcomere

        f_overlap;
        f_on;
        f_bound;
        
        cb_force;
        passive_force;
        
        state_pops;
        
        Ca = 10^(-9.0);     % Ca concentration (in M)
        
        kinetic_scheme = '3state_with_SRX';
        
        check_force = 0;    % temp force used during force balance
        
        myofilaments = [];  % a structure that holds the data for
                            % half-sarcomere kinetics
                            % precise format depends on the kinetic scheme
                            
        parameters = [];    % a structure that holds the model parameters
                            % precise format depends on the kinetic scheme


    end
    
    properties (SetAccess = private)
        % These are properties that can only be accessed from within
        % the half-sarcomere class
                           
    end
    
    methods
        
        % Constructor
        function obj = half_sarcomere(varargin)
            
            % Set up kinetic scheme
            switch (obj.kinetic_scheme)
                
                case '3state_with_SRX';
                    % 3 state model SRX model described by Campbell,
                    % et al. 2018
                    obj.myofilaments.bin_min = -10;
                            % min x value for myosin distributions in nm
                    obj.myofilaments.bin_max = 10;
                            % max x value for myosin distributions in nm
                    obj.myofilaments.bin_width = 0.5;
                            % width of bins for myosin distributions in nm
                    obj.myofilaments.x = ...
                        obj.myofilaments.bin_min : ...
                            obj.myofilaments.bin_width : ...
                                obj.myofilaments.bin_max;
                            % array of x_bin values
                    obj.myofilaments.no_of_x_bins = ...
                        numel(obj.myofilaments.x);
                            % no of x_bins
                    
                    obj.myofilaments.thick_filament_length = 815;
                            % length of thick filaments in nm
                    obj.myofilaments.thin_filament_length = 1120;
                            % length of thin filaments in nm
                    obj.myofilaments.bare_zone_length = 80;
                            % length of thick filament bare zone in nm
                    obj.myofilaments.k_falloff = 0.0024;
                            % defines how f_overlap falls hs_length shortens
                            % below optimal
                    
                    % Set up the y vector which is used for the kinetics
                    obj.myofilaments.y_length = ...
                        obj.myofilaments.no_of_x_bins + 4;
                    obj.myofilaments.y = ...
                        zeros(obj.myofilaments.y_length,1);
                    
                    % Start with all the cross-bridges in M1 and all
                    % binding sites off
                    obj.myofilaments.y(1)=1.0;
                    obj.myofilaments.y(end-1) = 1.0;
                    
                    % Set parameters
                    obj.parameters.k_1 = 1.83;
                    obj.parameters.k_force = 2.34e-4;
                    obj.parameters.k_2 = 100;
                    obj.parameters.k_3 = 3820;
                    obj.parameters.k_4_0 = 3610;
                    obj.parameters.k_4_1 = 0.216;
                    obj.parameters.k_cb = 0.001;
                    obj.parameters.x_ps = 3.18;
                    obj.parameters.k_on = 2.59e8;
                    obj.parameters.k_off = 200;
                    obj.parameters.k_coop = 5.64;
                    
                    obj.parameters.passive_force_mode = 'exponential';
                    obj.parameters.passive_sigma = 1.0e-12;
                    obj.parameters.passive_L = 38;

                    obj.parameters.compliance_factor = 0.5;
                            % proportion of delta_hsl that the
                            % cb distribution is moved
                    obj.parameters.cb_number_density = 6.9e16;
                            % number of cbs in a half-sarcomere with a
                            % cross-sectional area of 1 m^2
                            
                    obj.parameters.k_boltzmann = 1.38e-23;
                            % Boltzmann's constant (J K^-1)
                    obj.parameters.temperature = 288;
                            % Temperature (K)
                            
                    obj.parameters.max_rate = 5000;
                            % Max rate (in s^-1) allowed in ODEs
                otherwise
                    error(sprintf( ...
                        '%s kinetics scheme not yet implemented in half_sarcomere class', ...
                        obj.kinetic_scheme));
            end
            
            % Initialise forces
            obj.cb_force = 0;
            obj.passive_force = return_passive_force(obj,obj.hs_length);
            obj.hs_force = obj.cb_force + obj.passive_force;

            % Intialise_populations
            obj.f_on = 0;
            obj.f_bound = 0;
        end
        
        % Other methods
        f_overlap = return_f_overlap(obj);
        pf = return_passive_force(obj,hsl);
        
        evolve_kinetics(obj,time_step);
        update_3state_with_SRX(obj,time_step);
        
        move_cb_distribution(obj,delta_hsl);
        update_forces(obj);
        
        check_new_force(obj,new_length);

        implement_time_step(obj,time_step,delta_hsl,Ca_concentration);
        
    end
end
            
            
            
            
            
        
        