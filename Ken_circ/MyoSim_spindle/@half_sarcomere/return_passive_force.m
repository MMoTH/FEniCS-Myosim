function pf = return_passive_force(obj,hsl)
% Function returns passive force

switch (obj.parameters.passive_force_mode)
    case 'linear'
        pf = obj.parameters.k_passive * ...
            (hsl - obj.parameters.hsl_slack);
    case 'exponential'
        pf = obj.parameters.passive_sigma * ...
                (exp(hsl/obj.parameters.passive_L)-1);
    otherwise
        error('Passive force mode not defined');
end
        
        
