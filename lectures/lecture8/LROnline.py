import numpy as np

class LROnline:
    """
    online linear regression

    Attributes:
        eta: learning rate
        beta: coefficient vector
        p: dimension of X
        beta_zero: intercept
        loss: 'sqr' or 'abs'
    """

    def __init__(self,dim,mu = 1.,decay=-0.5,
                 beta_init=None,beta_zero_init=None,loss='sqr'):
        """initialize and set beta"""
        self.mu = mu
        self.decay = decay
        self.p = dim
        self.t = 0
        self.loss = loss
        if beta_init:
            self.beta = beta_init
        else:
            self.beta = np.zeros(dim)
        if beta_zero_init:
            self.beta_zero = beta_zero_init
        else:
            self.beta_zero = 0.

    def predict(self,x):
        """
        Predict y with x
        arg: x
        """
        yhat = x @ self.beta + self.beta_zero
        return yhat

    def update_beta(self,x,y):
        """
        single step update, output loss
        args: x,y
        """
        if self.loss=='sqr':
            return(self._update_beta_sqr(x,y))
        if self.loss=='abs':
            return(self._update_beta_abs(x,y))

    def _update_beta_sqr(self,x,y):
        """
        single step update output sqr error loss
        args: x,y
        """
        yhat = self.predict(x)
        eta = 2 * (yhat - y)
        self.t += 1
        mu_curr = self.mu * self.t**self.decay
        self.beta += - mu_curr * eta * x
        self.beta_zero += - mu_curr * eta
        return (yhat - y)**2.

    def _update_beta_abs(self,x,y):
        """
        single step update output abs error loss
        args: x,y
        """
        yhat = self.predict(x)
        eta = np.sign(yhat - y)
        self.t += 1
        mu_curr = self.mu * self.t**self.decay
        self.beta += - mu_curr * eta * x
        self.beta_zero += - mu_curr * eta
        return np.abs(yhat - y)

