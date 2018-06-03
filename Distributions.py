import math
from matplotlib import pyplot as plt


#CONTINUOUS DISTRIBUTION
#Discrete distribution : associates values with discrete outcomes
#Uniform distribution
#represent continuous distribution with probability density function (pdf)

def uniform_pdf(input):
    if input >= 0 and input < 1:
        return 1
    else:
        return 0

print(uniform_pdf(0.3))


#CUMULATIVE DISTRIBUTIVE FUNCTION (cdf) --> probability of random variable <= to a value
def uniform_cdf(input):
    if input < 0:
        return 0
    elif input < 1:
        return input
    else:
        return 1


#NORMAL DISTRIBUTION : bell shaped curve
#mu = mean, sigma = standard deviation
#mean --> where bell itself is centered & standard dev. --> width of curve
def normal_pdf(input, mu=0, sigma=1):
    den = math.sqrt(2 * math.pi)
    return (math.exp(-(input-mu) ** 2 /  2 / sigma ** 2)/(den * sigma))
y = [input / 20.0 for input in range(-60,60)]
plt.plot(y, [normal_pdf(input, sigma=1) for input in y], '-', color = "pink", label='mu=0,sigma=1')
plt.plot(y, [normal_pdf(input, sigma=0.6) for input in y], '--', color="green", label='mu=0,sigma=0.6')
plt.plot(y, [normal_pdf(input, sigma=3) for input in y], ':', color="blue", label='mu=0, sigma=3')
plt.plot(y, [normal_pdf(input, sigma=-2) for input in y], '-', color="purple", label='mu=0, sigma=-2')
plt.legend()
plt.show()

#Cumulative Distributive Function for normal distribution with Math.erf (error)
def normal_cdf(input, mu=0, sigma=1):
    return (1+math.erf(input-mu)/math.sqrt(2)/sigma)/2
y = [input/20.0 for input in range(-60, 60)]
plt.plot(y, [normal_cdf(input, sigma=1) for input in y], '-', label='mu=0, sigma=1')
plt.plot(y, [normal_cdf(input, sigma=2) for input in y], '--', label='mu=0, sigma=2')
plt.plot(y, [normal_cdf(input, mu=1.5) for input in y], ':', label='mu=1.5, sigma=1')
plt.plot(y, [normal_cdf(input, mu=1) for input in y], ':', label='mu=1, sigma=1')
plt.legend()
plt.show()