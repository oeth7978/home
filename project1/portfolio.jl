using Pkg
Pkg.add("CSV")


using CSV

df1 = CSV.File("AAPL.csv")
df2 = CSV.File("AMZN.csv")
close1 = getproperty(df1, Symbol("Adj Close"))
close2 = getproperty(df2, Symbol("Adj Close"))

returns1 = []
returns2 = []

n = length(close1)

for i in 2:n
    push!(returns1, (close1[i]-close1[i-1])/close1[i-1])
    push!(returns2, (close2[i]-close2[i-1])/close2[i-1])
end


return_mean1 = 0
return_mean2 = 0
n = length(returns1)
for i in 1:n
    global return_mean1, return_mean2
    return_mean1 += returns1[i]
    return_mean2 += returns2[i]
end
return_mean1 = return_mean1/n
return_mean2 = return_mean2/n


return_variance1 = 0
return_variance2 = 0
covariance = 0
for i in 1:n
    global return_variance1, return_variance2, covariance
    return_variance1 += (returns1[i] - return_mean1)^2
    return_variance2 += (returns2[i] - return_mean2)^2
    covariance += (returns1[i] - return_mean1)*(returns2[i]-return_mean2)
end
return_variance1 = return_variance1/n
return_variance2 = return_variance2/n
covariance = covariance/n

println(string("Stock 1 Mean return: ", return_mean1))
println(string("Stock 2 Mean return: ", return_mean2))
println(string("Stock 1 variance: ", return_variance1))
println(string("Stock 2 variance: ", return_variance2))


p_return = 0.5*return_mean2 + 0.5*return_mean1
p_var = (0.5^2)*return_variance2 + (0.5^2)*return_variance1 + 2*0.5*0.5*covariance
println(string("portfolio return: ", p_return))
println(string("portfolio variance: ", p_var))