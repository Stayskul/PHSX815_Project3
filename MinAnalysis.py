from scipy.optimize import minimize as min
from scipy.optimize import fsolve
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
from Rando.Random import Random
import sys


#takes a .txt file, reads it, and makes a list
if __name__ == "__main__":
   
    haveH1=False
    myArray1=[]

    if '-input1' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile1 = sys.argv[p+1]
        haveH1 = True

    if haveH1:
        with open(InputFile1, "r") as f:
            myArray1 = f.read().split()

        for i in range(0, len(myArray1)):
            myArray1[i] = float(myArray1[i])

    

#defining a 1D function, which we what to minimize
    def f(sigx):
        mux=50
        
        mu=np.log(mux**2/np.sqrt(mux**2+sigx**4)) 
              
        sigma=np.log(1+((sigx**2/mux)**2))  #sigma^2
       #sigma=np.log(1+((sigx**2/mux)*2))  <--orginal
        
        res=0
        
        
        for i in myArray1:
            
            L=np.log(i*np.sqrt(2*sigma*np.pi))+(((np.log(i)-mu)**2)/(2*sigma))

            res+=L
            
        
            
        return np.round(res,8)
            
            

    #a starting guess for location of minimum
    x_start=10
    #result of minimization
    result=min(f, x_start)

    if result.success:
        print("the minimum is at:")
        print((result.x)**2)

    else:
        print("could not find minimum")
        print(result.message)

    #estimating error on estimated sigx using log(L(sigx)/L(sigx_best))<=-0.5

    def g(sigx):
        p=-f(np.sqrt(sigx))+f(result.x)+0.5
        return p
    

    sigxerr_guess=(8,12)
    sigx_err=fsolve(g,sigxerr_guess)
    print("error bounds are:")
    print(sigx_err)
    
    #Plots distribution in histogram

    if haveH1:
        n, bins, patches = plt.hist(myArray1, 50, facecolor='green', alpha=0.50, label="Plague Data")
    
    plt.ylabel('New Infections (number of cells infected)')
    plt.title('Rakghoul Plague Spread Data (collected every hour)')
    plt.grid(True)
    plt.legend(loc="upper right")

            

    plt.show()
