Installation notes for python and jupyter
=======================

The easiest way to install if you have a Mac, Windows, or Linux, is to use anaconda.
If you are installing python 3, then you can download and follow the instructions for anaconda 3 at the [anaconda download page](https://www.anaconda.com/download/#linux) and you can find the installation instructions [at the conda page](https://www.anaconda.com/download/).

After you download conda then open a terminal (if you are on windows search for the anaconda prompt) and type `conda list`, this is how you see what is installed.  You will definitely need the following packages:
- ipython
- jupyter
- numpy
- scipy
- scikit-learn
- pandas

And you can install one of these with `conda install numpy`. 
(Alternatively you can use `apt-get install ...` in ubuntu or your favorite package manager in linux.)

Common issues
=======================

### Path variable
When you type in `python` in the prompt you should see 
```
Python 3.6.1 |Anaconda 4.4.0 (64-bit)| ...
```
with perhaps a few details changed, but it should be 3.6 say anaconda.  If not then you should look at your path variable by typing `echo $PATH` into your terminal.  What happens is that when you type `python` it starts looking for python in the directories in your PATH, and it will go with the first one it finds.  So you should google how to change your PATH variable on your OS.  You need to remove the old python installation from the PATH and include the new anaconda install.  (For me conda is installed in my `/usr/local` directory.)

### Starting Jupyter
I recommend that you always start jupyter from the terminal, instead of using the anaconda explorer tool.  Just open a terminal and type `jupyter notebook`.  You can navigate to the directory you want by using the `cd` and `ls` commands before starting jupyter or within jupyter after you start it up.  You can find [more instructions here](https://jupyter.readthedocs.io/en/latest/running.html).
