
N=1000; fp=1000; k=25; t=0:N-1; t=t/fp;
f1=cos(0.5*(2*pi*k)*t.^2);
f2=sin(100*pi*t);
f3=0.1*sin(100*pi*t-0.2*pi);

M=10;mi=0.1;
a=zeros(1, M);
for n=M:N
    f1(n)=f1(n)+f2(n);
    e(n)=f1(n)-f3(n-M+1: n)*flip(a)';
    a=a+mi.*flip(f3(n-M+1:n))*e(n)/(0.001+sum(f3(n-M+1:n).^2));
end

figure(1)
plot(f2);
hold on;
plot(e);
plot(f1);

%Z2
N=1000; fp=1000; n=1:N;
f1=cos(20*pi*(n/fp).^2);
f2=f1+0.3*randn(size(f1));
mi=0.01; eps=0.0012; mi=0.025;
I=50;

a=zeros(1, I);
for n=I+1:N
    u(n)=f2(n-I: n-1)*flip(a)';
    e(n)=f2(n)-u(n);
    a=a+mi.*flip(f2(n-I+1:n))*e(n)/(eps+sum(f2(n-I+1:n).^2));
end
figure(2)
plot(u);
hold on;
plot(f1)