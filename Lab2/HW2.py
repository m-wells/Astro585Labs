# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

N=1000000;
println("rand: ", 1./(@elapsed x=rand(N)));
println(".+: ",1./(@elapsed x.+x));

# <codecell>

srand(42);
Nobs = 100;
z = zeros(Nobs);
sigma = 2. * ones(Nobs);
y = z + sigma .* randn(Nobs);
normal_pdf(z, y, sigma) = exp(-0.5*((y-z)/sigma)^2)/(sqrt(2*pi)*sigma);

function log_likelihood(y::Array, sigma::Array, z::Array)
   n = length(y);
   sum = zero(y[1]);
   for i in 1:n
    sum = sum + log(normal_pdf(y[i],z[i],sigma[i]));
   end;
   return sum;
end

# <codecell>

function calc_time_log_likelihood(Nobs::Int, M::Int=1)
    z=zeros(Nobs)
    sigma=2.*ones(Nobs);
    y=z+sigma.*randn(Nobs);
    println("log_likelihood: ",1./(@elapsed x=log_likelihood(y,sigma,z)));
    println(".+: ",1./(@elapsed x.+x));
end

# <codecell>

calc_time_log_likelihood(100)

# <codecell>

calc_time_log_likelihood(100)

# <codecell>

calc_time_log_likelihood(100)

# <codecell>

using PyPlot
n_list=[2^i for i=1:10]
elapsed_list=map(calc_time_log_likelihood,n_list)
plot(log10(n_list),log10(elapsed_list),color="red",linewidth=2,marker="+",markersize=12);
xlabel("log(N)");ylabel("log(Time/s)");

