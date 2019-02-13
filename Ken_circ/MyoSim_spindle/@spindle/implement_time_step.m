function implement_time_step(obj,time_step,delta_sl,Ca_conc)
% Function implements a time-step on a spindle

obj.spindle_length = obj.spindle_length + delta_sl;

% Implement time_step on components
obj.m_chain.implement_time_step(time_step,delta_sl,Ca_conc);
obj.m_bag.implement_time_step(time_step,delta_sl,Ca_conc);

% Calculate force
obj.chain_force = obj.m_chain.muscle_force;
obj.chain_hs_length = obj.m_chain.hs(1).hs_length;
obj.chain_series_length = obj.m_chain.series_extension;

obj.bag_force = obj.m_bag.muscle_force;
obj.bag_hs_length = obj.m_bag.hs(1).hs_length;
obj.bag_series_length = obj.m_bag.series_extension;

obj.spindle_force = obj.chain_force + obj.bag_force;

