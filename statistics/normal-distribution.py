# Import all libraries for this portion of the blog post
from scipy.stats import  norm
import numpy as np
import math  

n = 300
mu = p = 0.55
sigma = math.sqrt((p * (1 - p) / n))


def calcZScore(valX, mu, sigma):
    return (valX - mu)/sigma

def rangeCDF(mu, sigma, lowend, highend): 
    high_zscore = calcZScore(highend, mu, sigma)
    low_zscore = calcZScore(lowend, mu, sigma)
    return norm.cdf(high_zscore) - norm.cdf(low_zscore)
    

def lessThanXCDF(mu, sigma, highend):
    zscore = calcZScore(highend, mu, sigma)
    return norm.cdf(zscore)

def largerThanXCDF(mu, sigma, lowend):
    zscore = calcZScore(lowend, mu, sigma)
    return 1 - norm.cdf(zscore)

probableVal = lessThanXCDF(mu, sigma, 0.5) #rangeCDF(mu, sigma, 0.79, 0.81)

print(probableVal)