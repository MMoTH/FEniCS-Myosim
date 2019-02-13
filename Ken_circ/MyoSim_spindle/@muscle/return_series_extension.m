function series_extension = return_series_extension(obj,muscle_force,time_step)
% Function returns force in series element

if ((time_step<eps)|(obj.series_viscosity<eps))
    series_extension = muscle_force / obj.series_k_linear;
else
    series_extension = ...
        ((muscle_force * time_step / obj.series_viscosity) + ...
                obj.last_series_extension) / ...
        (1 + (time_step * obj.series_k_linear / obj.series_viscosity));
end
