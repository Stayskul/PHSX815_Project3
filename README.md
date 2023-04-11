# PHSX815_Project3
contains the code and accompanying documents for project 3


project 3 uses code from my own repositories, homeworks, and past projects as well as prof Rogan's repostitories.

The code has 3 parts

The random.py: This needs to be placed in a named folder, and contains the random class, which is used in the rest of the codes.

The DataGen.py: Here, first specify the location of the random.py code, so that the code knows where to find it.
Next simply run: python3 DataGen.py -seed (seed#) -Nmeas (meas#) -sigx ? > filename.txt. This will create a set of data according to the specified distribution, and save the data to a .txt file.

The MinAnalysis.py: Here simply run python3 MinAnalysis.py -input1 filename.txt. This will first output an estimation for our parameter, which minimizes the negative log-likelihood, then it will output the lower and upper error bounds on our estimation. Finally, it outputs a histogram of our data.

Note: For the MinAnalyis.py file, you want to change the starting guess on the min function and the fsolve function, so it reflects what your true sigx is.
