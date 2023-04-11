

import math
import numpy as np

#################
# Random class
#################
# class that can generate random numbers
class Random:
    """A random number generator class"""

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)
        
        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    # function returns a random 64 bit integer
    def int64(self):
        with np.errstate(over='ignore'):
            self.m_u = np.uint64(self.m_u * np.uint64(2862933555777941757) + np.uint64(7046029254386353087))
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    # function returns a random floating point number between (0, 1) (uniform)
    def rand(self):
        return 5.42101086242752217E-20 * self.int64()

    # function returns a random integer (0 or 1) according to a Bernoulli distr.
    def Bernoulli(self, p=0.5):
        if p < 0. or p > 1.:
            return 1
        
        R = self.rand()

        if R < p:
            return 1
        else:
            return 0
        
    # function returns a random integer (1, 2, 3, 4) according to a Catagorical distr. (4-sided dice)
    def Foursided(self, p=0.25, q=0.50, s=0.75):
        if s < 0. or s > 1.:
            return 1

        R=self.rand()

        if R < p:
            return 1
        if R > p and R < q:
            return 2
        if R > q and R < s:
            return 3
        else:
            return 4
        

    # function returns a random double (0 to infty) according to an exponential distribution
    def Exponential(self, beta):
      # make sure beta is consistent with an exponential
      if beta <= 0.:
        beta = 1.

      R = self.rand()

      while R <= 0.:
        R = self.rand()

      X = -math.log(R)/beta

      return X


    #Skew Normal Distribution
    
    def SkewNorm(self, mux , sigx):

        R=np.random.standard_normal()

        mu=np.log(mux**2/np.sqrt(mux**2+sigx**2))
        
        sigma=np.sqrt(np.log(1+(sigx/mux)**2))

        X = np.exp(mu+sigma*R)


        return X
        
    def SkewNorm2(self, alpha, beta, mux):

        R=np.random.standard_normal()
        
        sigx=np.random.gamma(alpha, beta)

        mu=np.log(mux**2/np.sqrt(mux**2+sigx**2))
        
        sigma=np.sqrt(np.log(1+(sigx/mux)**2))

        X = np.exp(mu+sigma*R)


        return X
    
    #skewnorm with fixed mux
    def SkewNormfix(self, sigx):
        mux=50

        R=np.random.standard_normal()

        mu=np.log(mux**2/np.sqrt(mux**2+sigx**2))
        
        sigma=np.sqrt(np.log(1+(sigx/mux)**2))

        X = np.exp(mu+sigma*R)


        return X
