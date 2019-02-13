function spindle_driver

s = spindle;

dt = 0.001;
t = 0:dt:0.4;
dx = zeros(numel(t),1);
dx(201:230)=2;

pCa = 9.0 * ones(size(dx));
pCa(50:end) = 6.1;
Ca = 10.^-pCa;


holder = [];
for i=1:numel(t)
    i=i
    s.implement_time_step(dt,dx(i),Ca(i));
    
    holder.spindle_length(i) = s.spindle_length;
    holder.spindle_force(i) = s.spindle_force;
    
    holder.chain_hs_length(i) = s.chain_hs_length;
    holder.chain_series_length(i) = s.chain_series_length;
    holder.chain_force(i) = s.chain_force;
    
    holder.bag_hs_length(i) = s.bag_hs_length;
    holder.bag_series_length(i) = s.bag_series_length;
    holder.bag_force(i) = s.bag_force;
    
    if (i>1)
        v = (holder.bag_series_length(i)-holder.bag_series_length(i-1)) / dt;
        holder.f_series(i) = s.m_bag.series_viscosity * v + ...
                    s.m_bag.series_k_linear * s.bag_series_length;
    else
        holder.f_series(i) = 0;
    end
end

figure(1);
clf;
subplot(4,1,1);
hold on;
h(1) = plot(t,holder.spindle_length,'r-');
h(2) = plot(t,holder.bag_hs_length,'bo-');
h(3) = plot(t,holder.chain_hs_length,'g-');
ylabel('Length','Rotation',0);
legendflex(h,{'Spindle','Bag','Chain'});

subplot(4,1,2);
hold on;
h=[];
h(1) = plot(t,holder.bag_series_length,'bo-');
h(2) = plot(t,holder.chain_series_length,'g-');
ylabel({'Series','component','length'},'Rotation',0);
legendflex(h,{'Bag','Chain'});

subplot(4,1,3);
hold on;
h=[];
h(1)=plot(t,holder.spindle_force,'r-');
h(2)=plot(t,holder.bag_force,'b-');
h(3)=plot(t,holder.chain_force,'g-');
h(4)=plot(t,holder.f_series,'m-');
ylabel('Force','Rotation',0);
legendflex(h,{'Spindle','Bag','Chain','Sanity check'});

subplot(4,1,4);
plot(t,pCa,'b-');
ylabel('pCa','Rotation',0);

