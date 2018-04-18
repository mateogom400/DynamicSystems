%% Ejemplo 4: Sistema con dos resistencias y 2 capacitancias térmicas
% Parámetros
C1 = 1e5;
C2 = 2e5;
R1 = 1e-3;
R2 = 5e-3;
theta_a = 300;
qbar_i = 1e3;

% Punto de equilibrio
thetabar_1 = theta_a + (R1+R2)*qbar_i;
thetabar_2 = theta_a + R2*qbar_i;

% Iteración del método numérico
tf = 10000;
N = 10000;
h = tf/N;
t = linspace(0,tf,N);
Theta = zeros(N,2);
Theta(1,1) = theta_a;
Theta(1,2) = theta_a;
for i = 1:N-1
    k1 = dX_dt_sys1(Theta(i,:),t(i),qbar_i);
    k2 = dX_dt_sys1(Theta(i,:)+0.5*h*k1,t(i)+0.5*h,qbar_i);
    Theta(i+1,:) = Theta(i,:) + h*k2;
end

% Gráfica de los resultados
figure(1), hold on
plot(t,Theta(:,1),'r')
plot(t,Theta(:,2),'b')
plot(t,thetabar_1*ones(1,N),'r--')
plot(t,thetabar_2*ones(1,N),'b--')
hold off
legend('theta1','theta2','thetabar1','thetabar26')

function Xdot = dX_dt_sys1(X,t,qi)
% Parámetros
    C1 = 1e5; C2 = 2e5; R1 = 1e-3; R2 = 5e-3; theta_a = 300;
    theta1 = X(1);
    theta2 = X(2);
    theta1_dot = (1/C1)*(qi - (theta1-theta2)/R1);
    theta2_dot = (1/C2)*((theta1-theta2)/R1 - (theta2-theta_a)/R2);
    Xdot = [theta1_dot, theta2_dot];
end