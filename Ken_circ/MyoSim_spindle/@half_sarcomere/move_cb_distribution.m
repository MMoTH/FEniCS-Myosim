function move_cb_distribution(obj,delta_hsl)

% Adjust for filament compliance
delta_x = delta_hsl * obj.parameters.compliance_factor;

% Shift populations by interpolation
switch (obj.kinetic_scheme)
    case '3state_with_SRX'
        % 3state SRX model
        interp_positions = obj.myofilaments.x - delta_x;
        bin_indices = 2+(1:obj.myofilaments.no_of_x_bins);
        obj.myofilaments.y(bin_indices) = ...
            interp1(obj.myofilaments.x,obj.myofilaments.y(bin_indices), ...
                interp_positions, ...
                'linear',0)';
    otherwise
        error(sprintf( ...
            '%s kinetics scheme not yet implemented in move_cb_distributions'));
end
        
