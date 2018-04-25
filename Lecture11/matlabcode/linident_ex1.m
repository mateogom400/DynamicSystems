%% Code for example 1: least squares identification of linear system
% Create low-pass GBN with ETsw = 20
N = 1000;
U1 = gbngen(N,20);
U2 = gbngen(N,20);

%% Simulate the process
Ao = [1 -0.97];
Bo = [0 0.5];
Yo = filter(Bo,Ao,U1);
Yo2 = filter(Bo,Ao,U2);

%% Add 1% and 10% output disturbances
v = filter(1,[1 -0.9],randn(N,1));
v01 = v/std(v)*sqrt(0.01)*std(Yo);
Y01 = Yo + v01;
v10 = v/std(v)*sqrt(0.1)*std(Yo);
Y10 = Yo + v10;

%% Estimate 1st order model
THarx01 = arx([Y01 U1],[1 1 1]);
THarx10 = arx([Y10 U1],[1 1 1]);

%% Estimate 1st order output error model for 10% noise data
THoe10 = oe([Y10 U1],[1,1,1]);

%% Simulation of the models
Yh01 = idsim(U2,THarx01);
Yh10 = idsim(U2,THarx10);

%% Calculate step responses
Nstp = 200;
STPo = filter(Bo,Ao,ones(Nstp,1));
STP01 = idsim(ones(Nstp,1),THarx01);
STP10 = idsim(ones(Nstp,1),THarx10);
STPoe10 = idsim(ones(Nstp,1),THoe10);

%% Plot model fit
t =1:N;
figure;
subplot(211),plot(t ,Yo2,'-r',t ,Yh01,'--b');
title('Fit of 1st order ARX model, estimation data');
%axis([0 N -20 20])
subplot (212) ,plot (t ,Yo2,'-r',t ,Yh10,'--b');
title('Fit of 1st order ARX model, estimation data');
%axis([0 N -20 20])
xlabel('Samples')
% Plot step responses
figure;
subplot (211),plot (1:Nstp,STPo,'-r' , 1:Nstp,STP01,'--b') ;
title ('Step responses of the process (solid) and of ARX model, 1% noise');
subplot(212),
plot (1:Nstp, STPo, '-r' ,1:Nstp,STP10, '--b' , 1:Nstp,STPoe10, '-.k') ;
title ('Step responses of the process (solid) and of ARX model, 10%. noise');
xlabel('Samples')

















