function series_force = return_series_force(obj,series_extension,time_step)
% Function returns force in series element

if (time_step<eps)
    series_force = obj.series_k_linear * series_extension;
else
    series_force = (obj.series_k_linear * series_extension) + ...
        (obj.series_viscosity * (series_extension - obj.last_series_extension) / ...
            time_step);
end