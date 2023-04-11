

% Crear valores de k y a
k = 0:0.1:400;
a = k;

% Crear una máscara booleana para seleccionar solo los valores de k y a que cumplen con la condición a>0 y k>116
mask = (a > 0) & (k < 116);

% Tracer la función solo para los valores de k y a que cumplen con la condición a>0 y k>116
plot(k(mask), f(k(mask), a(mask)), 'LineWidth', 2);
hold on

% Agregar etiquetas de eje y título de la gráfica
xlabel("k")
ylabel("a")
grid on
title('Gráfico de K vs a')

%Definimos el sistema inestable
Isys = TF(10,-2);
figure(2)
[y,t] = step(Isys);
plot(t,y)


%Definimos el sistema estable
Esys = TF(127,10);
figure(3)
[y,t] = step(Esys);
plot(t,y)

hold off


function sys = TF(k,a)
  num = [k, a*k];
  den = [1, 1, 1];
  sys = tf(num, den);
end


function res = f(k, a)
  res = (k.^2 + (64*a - 116).*k - 1260)./(k - 116);
end

