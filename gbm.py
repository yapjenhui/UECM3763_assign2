import pylab as p

# Setup parameters
mu = 0.1; sigma = 0.26; S0 = 39;
n_path = 1000; n = n_partitions = 1000;
# Create Brownian paths
t = p.linspace (0,3,n+1);
dB = p.randn (n_path, n+1) / p.sqrt(n/3); dB[:,0] = 0;
B = dB.cumsum(axis=1);

#Calculate stock prices
nu = mu - sigma*sigma/2.0
S = p.zeros_like(B); S[:,0] = S0
S[:,1:] = S0*p.exp(nu*t[1:]+sigma*B[:,1:])
S1 = S[0:5]
p.xlabel('t');p.ylabel('X(t)');
p.title('Geometric Brownian Motion');
p.plot(t,S1.transpose());p.show();

#Calculate E[S(3)]
S3 = S[:,-1]
Expected_s3= S3.sum()/n_path
msg= 'The expected value of S(3) is %.13f' %Expected_s3
print(msg)

#Calculate Var[S(3)]
Var = (S3-Expected_s3)**2
Sum_v = Var.sum()/(n_path-1)
msg= 'The variance of S(3) is %.13f' %Sum_v
print(msg)

# Calculate P[S(3)> 39] & E[S(3)|S(3) > 39]
count=0; total=0;
for i in range(n_path): #means 0,1,2,3,4
    if S3[i]>39:
        count = count+1
        total = total+S3[i]
P = count/n_path
msg= 'P[S(3)> 39] is %.13f' %P
print (msg)

Cond_E = total/count
msg= 'E[S(3)|S(3) > 39] is %.13f' %Cond_E
print (msg)