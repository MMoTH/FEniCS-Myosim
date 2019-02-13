function check_new_force(obj,new_length)
% Function calculates the force for a given length

delta_hs_length = new_length - obj.hs_length;

switch (obj.kinetic_scheme)
    case '3state_with_SRX'
        bin_pops = obj.myofilaments.y(2+(1:obj.myofilaments.no_of_x_bins));
        temp_cb_force = ...
                obj.parameters.cb_number_density * obj.parameters.k_cb * 1e-9 * ...
                sum(bin_pops' .* ...
                    (obj.myofilaments.x + obj.parameters.x_ps + ...
                        (obj.parameters.compliance_factor * delta_hs_length)));
        delta_cb_force = temp_cb_force - obj.cb_force;
    otherwise
        error('Undefined kinetic scheme in check_new_force');
end

delta_passive_force = obj.return_passive_force(new_length) - ...
    obj.return_passive_force(obj.hs_length);

obj.check_force = obj.hs_force + delta_cb_force + delta_passive_force;