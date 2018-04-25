%% Code for example 1: least squares identification of linear system
% Create low-pass GBN with ETsw = 20
N = 1000;
U1 = gbngen(N,20);
U2 = gbngen(N,20);

%% Simulate the process
Ao = [1 -0.97];
Bo = [0 0.5];
Yo1 = filter(Bo,Ao,U1);
Yo2 = filter(Bo,Ao,U2);

%% Add 1% and 10% output disturbances
v = filter(1,[1 -0.9],randn(N,1));
v01 = v/std(v)*sqrt(0.01)*std(Yo1);
Y01 = Yo1 + v01;
v = filter(1,[1 -0.9],randn(N,1));
v01 = v/std(v)*sqrt(0.01)*std(Yo2);
Y02 = Yo2 + v01;

%% Estimate 1st order model - Construct Phi matrix
n = 1;
Phi = zeros(N-n-1,2*n);
row = 1;
for t = n:N-1
    Phi(row,:) = [-Y01(t:-1:t-n+1)' U1(t:-1:t-n+1)'];    
    row = row + 1;
end

%% Estimate 1st order model
theta = (Phi'*Phi)^(-1)*Phi'*Y01(2:end);
b1 = theta(2);
a1 = theta(1);
Am = [1 a1];
Bm = [0 b1];

%% Simulation of the models
Ym = filter(Bm,Am,U2);

%% Plot model fit
t =1:N;
figure;
plot(t ,Yo2,'b',t ,Y02,'r');
legend('respuesta experimental','respuesta modelo')
xlabel('Samples')















