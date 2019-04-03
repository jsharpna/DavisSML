UC Davis Statistics 208 : Statistical Machine Learning
==============================

A Course on the Principles of Statistical Machine Learning with Examples in Python
-----------------------------

Machine learning is how to get computers to automatically learn and improve with experience. Experience comes in the form of data, improvement is with respect to some performance metric, and learning is done by a learning algorithm. There are always computational constraints, such as the architecture, computation time, bandwidth limitations, and so on. So we can more precisely restate the goal thus: to construct learning algorithms that use data to improve with respect to a performance metric and do so under computational constraints.

We will focus on principles of statistical machine learning in the prediction problems, regression and classification.  Conspicuously absent is most Bayesian methodology and advanced concepts such as reinforcement learning.  This course is not a broad overview of all of machine learning, but rather a tour of the key ideas in machine learning as told through these prediction tasks.  Typically, I have students tell me something along the lines of "I thought machine learning was about [insert random methodology here]".  Machine learning is a field, like physical chemistry or creative literature.  It is not defined by a couple of methods or a single task, and cannot be taught in a single quarter.  With that said, I want this course to lay the foundation for a rich understanding of machine learning.

**Instructions:** The lectures will mostly be jupyter notebooks.  To follow along with the slides use the following command in the lecture folder.

```
jupyter nbconvert lecture[# here].ipynb --to slides --post serve
```


Lecture Notes
--------------

**Introduction to Machine Learning**

Principles: Over/under-fitting, training and testing, losses, OLS and KNN<br>
Reading: ESL Chapter 2
<table>
<tr><td width="50px">4/1</td><td width="100px"><a href="lectures/lecture1/lecture1.ipynb">Lecture 1</a></td><td width="650px">Introduction to machine learning</td></tr>
<tr><td width="50px">4/3</td><td width="100px"><a href="lectures/lecture2/lecture2.ipynb">Lecture 2</a></td><td width="650px">Model selection and bias-variance tradeoff</td></tr>
</table>

<h4>Regression (beyond Ordinary Least Squares)</h4>

Principles: Convex relaxation, computational intractability in subset selection<br>
Reading: ESL Chapter 3, [Boyd Chapter 1](http://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)
<table>
<tr><td width="50px">4/8</td><td width="100px">Lecture 3</td><td width="650px">OLS,  Matrix Decompositions, Subset selection and ridge regression</td></tr>
<tr><td width="50px">4/10</td><td width="100px">Lecture 4</td><td width="650px">Convex optimization, first order methods</td></tr>
<tr><td width="50px">4/15</td><td width="100px">Lecture 5</td><td width="650px">The Lasso</td></tr>
</table>

<h4>Classification</h4>

Principles: Surrogate losses, generative and discriminative methods<br>
Reading: ESL Chapter 4
<table>
<tr><td width="50px">4/17</td><td width="100px">Lecture 6</td><td width="650px">Generative methods, naive Bayes, discriminant analysis, ROC, PR</td></tr>
<tr><td width="50px">4/22</td><td width="100px">Lecture 7</td><td width="650px">Logistic regression, support vector machines, surrogate losses</td></tr>
<tr><td width="50px">4/24</td><td width="100px">Lecture 8</td><td width="650px">Online learning, stochastic gradient descent, perceptron</td></tr>
</table>

<h4>Unsupervised Learning</h4>

Principles: HMMs, Clustering, Dimension Reduction
Reading: ESL Chapter 14
<table>    
<tr><td width="50px">4/29</td><td width="100px">Lecture 9</td><td width="650px">Clustering</td></tr>
<tr><td width="50px">5/1</td><td width="100px">Lecture 10</td><td width="650px">Dimension Reduction</td></tr>
<tr><td width="50px">5/6</td><td width="100px">Lecture 11</td><td width="650px">Hidden Markov Models</td></tr>
</table>

<h4>Non-linear methods</h4>

Principles: basis expansion, kernel trick, bagging, boosting, neural nets<br>
Reading: ESL Chapter 5, 7, 8
<table>
<tr><td width="50px">5/8</td><td width="100px">Lecture 12</td><td width="650px">Basis expansion and kernel trick</td></tr>
<tr><td width="50px">5/13</td><td width="105px">Lecture 13</td><td width="650px">Bootstrap, Decision Trees, and Random Forests</td></tr>
<tr><td width="50px">5/15</td><td width="105px">Lecture 14</td><td width="650px">Boosting</td></tr>
<tr><td width="50px">5/20</td><td width="100px">Lecture 15</td><td width="650px">Neural Networks</td></tr>
</table>

<h4>Deep Learning</h4>
<table>
<tr><td width="50px">5/22</td><td width="105px">Lecture 19</td><td width="650px">Deep learning</td></tr>
<tr><td width="50px">5/29</td><td width="105px">Lecture 20</td><td width="650px">Convolutional nets</td></tr>
<tr><td width="50px">6/3</td><td width="105px">Lecture 21</td><td width="650px">Recurrent neural nets</td></tr>
<tr><td width="50px">6/5</td><td width="105px">Lecture 22</td><td width="650px">Generative adversarial networks</td></tr>
</table>
