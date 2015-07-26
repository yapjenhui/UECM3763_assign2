import pylab as p

# Setup parameters
n_path = 5; n = n_partition = 1000; t=1.0;
alpha = 1.0; theta = 0.064;sigma=0.27; X0 = 3.0;

# Create Brownian paths
dt = t/n; T = p.linspace(0,t,n+1);
dB = p.randn (n_path, n+1) * p.sqrt(dt); dB[:,0] = 0;
B = dB.cumsum(axis=1);
X = p.zeros_like(B)

# Solution for mean reversion
X[:,0]= X0
for col in range (n):
    X[:,col+1] = X[:,col]+ alpha*(theta-X[:,col])*dt + [sigma*X[:,col]]*dB[:,col+1]
p.xlabel('t');p.ylabel('R(t)');
p.title('Mean Reversion Model');
p.plot(T,X.transpose());p.show();

# calculate expectation value of R(1)
R1 = X[:,-1]
Expected_r1= R1.sum()/n_path
msg= 'The expected value of R(1) is %.13f' %Expected_r1
print(msg)

# calculate P[R(1)> 2]
count=0;
for i in range(5): #means 0,1,2,3,4
    if R1[i]>2:
        count = count+1
P = count/n_path
msg= 'P[R(1)> 2] is %.13f' %P
print (msg)