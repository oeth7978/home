f = open("AAPL.csv", "r")
close_1 = []
lines = f.readlines()
lines.pop(0)
for line in lines:
    close_1.append(float(line.split(",")[5]))
f.close()

f = open("AMZN.csv")
close_2 = []
lines = f.readlines()
lines.pop(0)
for line in lines:
    close_2.append(float(line.split(",")[5]))
f.close()


returns_1 = []
returns_2 = []

i = 1
while i < len(close_1):
    returns_1.append((close_1[i] - close_1[i-1])/close_1[i-1])
    returns_2.append((close_2[i] - close_2[i-1])/close_2[i-1])
    i += 1

mean1 = 0
var1 = 0
mean2 = 0
var2 = 0
covar = 0

i = 0
while i<len(returns_1):
    mean1 += returns_1[i]
    mean2 += returns_2[i]
    i += 1
mean1 = mean1/len(returns_1)
mean2 = mean2/len(returns_2)

i = 0
while i<len(returns_1):
    var1 += (returns_1[i] - mean1)**2
    var2 += (returns_2[i] - mean2)**2
    covar += (returns_1[i] - mean1)*(returns_2[i] - mean2)
    i += 1
var1 = var1/len(returns_1)
var2 = var2/len(returns_2)
covar = covar/len(returns_1)


print("Stock 1 Mean return: " + str(mean1))
print("Stock 2 Mean return: " + str(mean2))
print("Stock 1 variance: " + str(var1))
print("Stock 2 variance: " + str(var2))
print("covariance: " + str(covar))

p_return = 0.5*mean1 + 0.5*mean2 
p_variance = (0.5**2)*var1 + (0.5**2)*var2 + 2*0.5*0.5*covar

print("portfolio return: " + str(p_return))
print("portfolio variance: " + str(p_variance))