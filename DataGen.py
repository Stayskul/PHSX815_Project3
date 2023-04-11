#a program to generate random number data according to a distribution

import sys
import numpy as np

# import our Random class from python/Random.py file
sys.path.append(".")
from Rando.Random import Random

# main function for our coin toss Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    

    # default seed
    seed = 5555

    #mean of lognorm 
    mux=0.75

    #sigma of lognorm
    sigx=0.25

    # default number of time measurements - per experiment
    Nmeas = 1000

    # default number of experiments
    Nexp = 1

    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-mux' in sys.argv:
        p = sys.argv.index('-mux')
        mutemp = float(sys.argv[p+1])
        if mutemp > 0:
            mux = mutemp
    if '-sigx' in sys.argv:
        p = sys.argv.index('-sigx')
        sigtemp = float(sys.argv[p+1])
        if sigtemp > 0:
            sigx = sigtemp
    if '-Nmeas' in sys.argv:
        p = sys.argv.index('-Nmeas')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Nmeas = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    # class instance of our Random class using seed
    random = Random(seed)

    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        for e in range(0,Nexp):
            for t in range(0,Nmeas):
                outfile.write(str(random.SkewNormfix(sigx))+" ")
                #outfile.write(str(np.random.lognormal(mu, sigma))+" ")
            outfile.write(" \n")
        outfile.close()
    else:
        for e in range(0,Nexp):
            for t in range(0,Nmeas):
                print(random.SkewNormfix( sigx), end=' ')
                #print(np.random.lognormal(mu, sigma), end=' ')
            print(" ")
