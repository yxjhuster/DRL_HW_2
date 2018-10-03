import numpy as np
import scipy.stats as stats

class defined_distribution(stats.rv_continuous):
    def _pdf(self, x):
        # return 1/2 * (1 + x)
        # return np.exp(-(x - 3)**2/ 2.)/(np.sqrt(2.0 * np.pi))/0.0227
        return np.exp(-x**2 / 2.) / np.sqrt(2.0 * np.pi)/0.6827
        # return 15/16 * (x ** 2) * ((1.0 + x) ** 2)


def pdf_p(x):
    return 1/2 * (1 + x)


def pdf_q(x, type_num):
    if type_num == 0:
        #we should normalized the pdf 0.0227
        return np.exp(-(x - 3) ** 2 / 2.) / (np.sqrt(2.0 * np.pi))/0.0227
    elif type_num == 1:
        #we should normalized the pdf 0.6827
        return np.exp(-x ** 2 / 2.) / np.sqrt(2.0 * np.pi)/0.6827
    elif type_num == 2:
        return 15/16 * x ** 2 * (1.0 + x) ** 2

def sample_distribution(num):
    sum = 0
    var = float(0)
    distribution = defined_distribution(a=-1, b=1)
    # distribution = defined_distribution()
    sample = distribution.rvs(size=num)
    # print(sample)
    for i in range(num):
       x = sample[i]
       # if x > 1 or x < -1:
       #     x = 0
       value = 3/2 * x**2 * (1+x)
       ### section 2
       # p = pdf_p(x)
       p = pdf_q(x, 0)
       q = distribution._pdf(x)
       sum += p/q * value
       #### section 3
       # sum += value
    expectation = float(sum / num)
    for i in range(num):
        x = sample[i]
        value = 3 / 2 * x ** 2 * (1 + x)
        p = pdf_p(x)
        # q = pdf_q(x, 2)
        q = distribution._pdf(x)
        value = p/q * value
        var += (value - expectation)**2
    var = var / num
    return expectation, var


def weighted_sample_distribution(num):
    sum = 0
    sum_p_q = 0.
    var = float(0)
    distribution = defined_distribution(a=-1, b=1)
    sample = distribution.rvs(size=num)
    for i in range(num):
        x = sample[i]
        p = pdf_p(x)
        q = distribution._pdf(x)
        sum_p_q += p/q
    for i in range(num):
       x = sample[i]
       value = 3/2 * x**2 * (1+x)
       p = pdf_p(x)
       q = distribution._pdf(x)
       sum += p/q / sum_p_q * value
    expectation = sum
    for i in range(num):
        x = sample[i]
        value = 3 / 2 * x ** 2 * (1 + x)
        p = pdf_p(x)
        q = distribution._pdf(x)
        value = p/q * value
        var += (value - expectation)**2
    var = var / num
    return expectation, var


# expectation, variance = sample_distribution(1000)
expectation, variance = weighted_sample_distribution(1000)
print("Expectation: %f" % expectation)
print("Variance: %f" % variance)