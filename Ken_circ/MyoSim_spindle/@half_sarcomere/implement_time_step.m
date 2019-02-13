function implement_time_step(obj,time_step,delta_hsl,Ca_concentration)

% Update Ca
obj.Ca = Ca_concentration;

% Update kinetics
obj.evolve_kinetics(time_step);

% Move distributions
obj.move_cb_distribution(delta_hsl);

% Update forces
obj.update_forces;

% Store pops
switch (obj.kinetic_scheme)
    case '3state_with_SRX'
        obj.state_pops.M1 = obj.myofilaments.y(1);
        obj.state_pops.M2 = obj.myofilaments.y(2);
        obj.state_pops.M3 = ...
            sum(obj.myofilaments.y(2+(1:obj.myofilaments.no_of_x_bins)));
    otherwise
        error('Undefined kinetic scheme in half_sarcomere class');
end
