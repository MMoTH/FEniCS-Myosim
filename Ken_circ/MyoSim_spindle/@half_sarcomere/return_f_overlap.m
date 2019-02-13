function f_overlap = return_f_overlap(obj)
% Function returns f_overlap

x_no_overlap = obj.hs_length - obj.myofilaments.thick_filament_length;
x_overlap = obj.myofilaments.thin_filament_length - x_no_overlap;
max_x_overlap = obj.myofilaments.thick_filament_length -  ...
    obj.myofilaments.bare_zone_length;

if (x_overlap<0)
    f_overlap=0;
end

if ((x_overlap>0)&(x_overlap<=max_x_overlap))
    f_overlap = x_overlap/max_x_overlap;
end

if (x_overlap>max_x_overlap)
    f_overlap=1;
end

if (obj.hs_length<obj.myofilaments.thin_filament_length)
    f_overlap = 1.0 + obj.myofilaments.k_falloff * ...
        (obj.hs_length - obj.myofilaments.thin_filament_length);
    if (f_overlap < 0)
        f_overlap = 0;
    end
end