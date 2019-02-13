function evolve_kinetics(obj,time_step)
% Function updates kinetics for thick and thin filaments

switch (obj.kinetic_scheme)
    case '3state_with_SRX'
        update_3state_with_SRX(obj,time_step);
    otherwise
        error('Undefined kinetic scheme in half_sarcomere class');
end