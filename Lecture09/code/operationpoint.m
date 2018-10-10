A1 = 2;
A2 = 3;
rho = 1000;
k1 = 3e-5;
k2 = 5e-5;
pa = 1.013e5;
g = 9.807;
a2 = -7.5e-9;
a1 = 5e-7;
a0 = 1e-3;

syms p1 p2

[p1,p2] = meshgrid(linspace(pa,pa+100,101),linspace(pa,pa+100,101));

F1 = (rho*g/A1)*(a2*(p1-pa)^2 + a1*(p1-pa) + a0 - k1*sqrt(p1-p2));
F2 = (rho*g/A2)*(k1*sqrt(p1-p2) - k2*sqrt(p2-pa));

%%
F1_R = F1;
F1_R(find(imag(F1) ~= 0)) = nan;
F2_R = F2;
F2_R(find(imag(F2) ~= 0)) = nan;
surf(p1,p2,F1_R), hold on, surf(p1,p2,F2_R), hold off
xlabel('p_1'), ylabel('p_2'), zlabel('F1')
axis VIS3D
