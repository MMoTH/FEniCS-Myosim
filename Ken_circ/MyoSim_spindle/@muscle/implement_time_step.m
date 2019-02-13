function implement_time_step(obj,time_step,delta_ml,Ca_vector)
% Function implements a time_step

obj.muscle_length = obj.muscle_length + delta_ml;

% Cycle through the half-sarcomeres implementing cross-bridge cycling
for hs_counter = 1:obj.no_of_half_sarcomeres
    obj.hs(hs_counter).implement_time_step(time_step,0, ...
            Ca_vector(hs_counter));
end

obj.impose_force_balance(time_step);

for hs_counter = 1:obj.no_of_half_sarcomeres
    obj.hs(hs_counter).update_forces;
end

% Update last length
obj.last_series_extension = obj.series_extension;