# Lecture 5: The Lasso

## Reading: ESL Section 3.4 - 3.6

## Lecture and Lab

1. The lecture slides can be found here: [lecture5slides.pdf](lecture5slides.pdf)
1. The lab for this week is [lab3.ipynb](../../labs/lab3.ipynb)

### Notes on installing glmnet (I was not successful on Windows, so will be using sklearn instead)
- In order to install glmnet you will probably need a gfortran compiler.  You should first try installing glmnet with pip: `pip install glmnet`
- If that fails due to a missing fortran compiler then you will need to install that on your system.  This should be easy on ubuntu/linux with a package manager, and similar on OS X.  On my windows machine I had to install it on cygwin.  I followed the instructions here: http://preshing.com/20141108/how-to-install-the-latest-gcc-on-windows/ and added the command `setup-x86.exe -q -P gcc-fortran` to the additional package install.  Now you should be able to `pip install glmnet`.
- I also had to download Visual C++ via visual studio: https://www.visualstudio.com/vs/visual-studio-express/ but I did not install any additional packages in the installer, and I installed the link here: http://aka.ms/vcpython27
- The glmnet-python site says that for OS X you need to use `brew install gcc` 
- I still had various issues on Windows, will be switching to sklearn lasso, etc.
