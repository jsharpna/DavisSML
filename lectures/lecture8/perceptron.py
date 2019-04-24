import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def sim_y(X, beta, beta_zero):
    """Simulate y from X and beta"""
    s = X @ beta - beta_zero
    p = 1. / (1 + np.exp(-s))
    Y = 2*np.random.binomial(1,p) - 1
    return Y

def plot_data(X,Y,beta,beta_zero,filename=None):
    """Plot the 2-dim data with separator line"""
    plt.scatter(X[Y==1,0], X[Y==1,1],marker='$+$')
    plt.scatter(X[Y==-1,0], X[Y==-1,1],marker='$-$')
    ybds = [-beta_zero / beta[1], 
            -(beta_zero + beta[0]) / beta[1] ]
    plt.plot([0,1],ybds,'r-')
    plt.xlim([0,1])
    plt.ylim([0,1])
    if filename:
        plt.savefig(filename)
        plt.clf()
    else:
        plt.show()

class Perceptron:
    """
    Rosenblatt's perceptron, online learner

    Attributes:
        eta: learning rate
        beta: coefficient vector
        p: dimension of X
        beta_zero: intercept
    """

    def __init__(self,eta,dim,
                 beta_init=None,beta_zero_init=None):
        """initialize and set beta"""
        self.eta = eta
        self.p = dim
        if beta_init:
            self.beta = beta_init
        else:
            self.beta = np.zeros(dim)
        if beta_zero_init:
            self.beta_zero = beta_zero_init
        else:
            self.beta_zero = 0.

    def predict(self,x):
        """predict y with x"""
        s = x @ self.beta + self.beta_zero
        yhat = 2*(s > 0) - 1
        return yhat

    def update_beta(self,x,y):
        """single step update output 0/1 loss"""
        yhat = self.predict(x)
        if yhat != y:
            self.beta += self.eta * y * x
            self.beta_zero += self.eta * y 
        return yhat != y

if __name__=='__main__':
    # Initialize data, beta, simulate y
    n = 200 
    X = np.random.uniform(0,1,n*2)
    X = X.reshape((n,2))
    beta = np.array([20,-10])
    beta_zero = 4.
    Y = sim_y(X,beta,beta_zero)
    # Initialize perceptron
    perc = Perceptron(.5,2)
    loss = []
    t_iter = 40
    # Iterate through the data, updating perceptron
    for t,(x,y) in enumerate(zip(X,Y)):
        loss.append(perc.update_beta(x,y))
        if t % t_iter == t_iter - 1:  # Every t_iter plot
            plot_data(X[:t,:],Y[:t],perc.beta,perc.beta_zero,
                      "perc_{}.png".format(t//t_iter))
