%% Primera funcion
num = [1];
den = [1,1,1];
%% Segunda funcion
num = [10,10];
den = [2,1,1,1];
%% Tercera funcion
num = [20,20,1];
den = [1,2,30];
%% Bode
sys = tf(num,den)
disp(sys.Variable);
bode(sys)
[mag,phase,w] = bode(sys);
%% Generar vectores
save("bode-mag1.mat","mag")
save("bode-phase1.mat","phase")
save("bode-W1.mat","w")

