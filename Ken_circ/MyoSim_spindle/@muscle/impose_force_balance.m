function impose_force_balance(obj,time_step)
% Function updates the length of each half-sarcomere and
% the series component to maintain force balance

% Create a vector p which has the lengths of each half-sarcomere
% followed by the muscle force
for hs_counter = 1:obj.no_of_half_sarcomeres
    p(hs_counter) = obj.hs(hs_counter).hs_length;
end
p(obj.no_of_half_sarcomeres+1) = obj.muscle_force;

% Now try and impose force balance
opt = optimoptions('fsolve','Display','none');
new_p = fsolve(@muscle_system,p,opt);

% Unpack the new_p array and implement
for hs_counter = 1:obj.no_of_half_sarcomeres
    dhsl = new_p(hs_counter) - obj.hs(hs_counter).hs_length;
    obj.hs(hs_counter).move_cb_distribution(dhsl);
    obj.hs(hs_counter).hs_length = new_p(hs_counter);
end
obj.series_extension = return_series_extension(obj,new_p(end),time_step);
obj.muscle_force = new_p(end);

% test = return_series_force(obj,obj.series_extension,time_step)
% cc = (test-obj.muscle_force)
% if (abs(cc)>1e-4)
%     error('ken');
% end

    % Nested function
    function x = muscle_system(p)
        x=zeros(numel(p),1);
        for i=1:obj.no_of_half_sarcomeres
            check_new_force(obj.hs(i),p(i));
            x(i) = obj.hs(i).check_force - p(end);
        end
        new_series_extension = obj.muscle_length - ...
            sum(p(1:obj.no_of_half_sarcomeres));
        x(end) = return_series_force(obj,new_series_extension,time_step) - ...
            p(end);
    end
end
