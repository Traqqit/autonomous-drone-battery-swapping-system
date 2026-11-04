% Proposed 4R arm demonstration; angles in radians and lengths in metres.
% Run from the matlab folder. No Robotics System Toolbox required.
L = [0.285 0.250 0.095];
shoulderHeight = 0.30;
q0 = deg2rad([0 25 -55 20]);
q1 = deg2rad([120 50 -85 15]);
t = linspace(0,4,101);
s = t / 4;
blend = 3*s.^2 - 2*s.^3;
q = q0 + blend' * (q1 - q0);
xyz = zeros(length(t),3);
for i = 1:length(t)
    xyz(i,:) = fk4(q(i,:),L,shoulderHeight);
end
figure;
plot3(xyz(:,1),xyz(:,2),xyz(:,3),'LineWidth',2);
grid on; axis equal;
xlabel('X (m)'); ylabel('Y (m)'); zlabel('Z (m)');
title('Proposed 4R arm: tool-tip trajectory');
disp('Final tool position (m):'); disp(xyz(end,:));

function xyz = fk4(q,L,h)
    yaw = q(1);
    a = cumsum(q(2:4));
    r = sum(L .* cos(a));
    z = h + sum(L .* sin(a));
    xyz = [r*cos(yaw), r*sin(yaw), z];
end
