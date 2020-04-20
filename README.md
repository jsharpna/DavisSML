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
Due to Covid-19, I have recorded all of my lectures and am uploading them to Youtube.  They will be linked as they become available, and will be organized into playlists which correspond to a single lecture (between 1-2 hrs of content).  I have structured the lecture so that there are exercises that you can do on your own as you listen to the lecture.  Most of the exercises are at the end of a video and will be answered at the beginning of the next, but sometimes I will ask you to pause the video.  After I ask the question you should take the time to complete the exercise, then go on to hear the answer.

Lecture Notes
--------------

**Introduction to Machine Learning**

Principles: Bias-Variance, training and testing, losses, OLS and KNN<br>
Reading: ESL Chapter 2
<table>
<tr><td width="100px">Setup</td><td width="100px"><a href="https://www.youtube.com/playlist?list=PLCTcZfebNw2nHEvSg5BmQlZdYej-i_xEl">Videos</a></td><td width="650px">Data science workflow installations, first project repository</td></tr>
<tr><td width="100px">Lecture 1</td><td width="100px"><a href="lectures/lecture1/lecture1.ipynb">Notebook</a>-<a href="https://www.youtube.com/playlist?list=PLCTcZfebNw2ljcIu-iGRRhAOS1ZTVbJYv">Videos</a></td><td width="650px">Introduction to machine learning</td></tr>
<tr><td width="100px">Lecture 2</td><td width="100px"><a href="lectures/lecture2/lecture2.ipynb">Notebook</a>-<a href="https://www.youtube.com/playlist?list=PLCTcZfebNw2kr1NhjZSjAviUxl71Hq9x1">Videos</td><td width="650px">Model selection and bias-variance tradeoff</td></tr>
</table>

<h4>Regression (beyond Ordinary Least Squares)</h4>

Principles: Convex relaxation, computational intractability in subset selection<br>
Reading: ESL Chapter 3, [Boyd Chapter 1](http://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)
<table>
<tr><td width="100px">Lecture 3</td><td width="100px"><a href="lectures/lecture3/lecture3.ipynb">Notebook</a>-<a href="https://www.youtube.com/playlist?list=PLCTcZfebNw2mxrYqh5VbBMY-Llgj_TgjA">Videos</a></td><td width="650px">OLS,  Matrix Decompositions, Subset selection and ridge regression</td></tr>
<tr><td width="100px">Lecture 4</td><td width="100px"><a href="lectures/lecture4/lecture4.ipynb">Notebook</a>-<a href="https://www.youtube.com/playlist?list=PLCTcZfebNw2nXzWdFGnX0ca6EL-ri-ne2">Videos</a></td><td width="650px">Convex optimization, first order methods</td></tr>
  <tr><td width="100px">Lecture 5</td><td width="100px"><a href="lectures/lecture5/lecture5.ipynb">Notebook</a>-<a href="https://www.youtube.com/playlist?list=PLCTcZfebNw2lrzcuYnaDcxw30tkR-XAoJ">Videos</a></td><td width="650px">The Lasso</td></tr>
</table>

<h4>Classification</h4>

Principles: Surrogate losses, generative and discriminative methods<br>
Reading: ESL Chapter 4
<table>
  <tr><td width="100px">Lecture 6</td><td width="100px"><a href="lectures/lecture6/lecture6.ipynb">Notebook</a>-<a href="https://www.youtube.com/playlist?list=PLCTcZfebNw2lCidu4JOqSAO6f0XAH_9Bz">Videos</a></td><td width="650px">Generative methods, naive Bayes, discriminant analysis, ROC, PR</td></tr>
  <tr><td width="100px">Lecture 7</td><td width="100px"><a href="lectures/lecture7/lecture7.ipynb">Notebook</a>-<a href="https://www.youtube.com/playlist?list=PLCTcZfebNw2kZ5sz162zPbh8tP9VePI8l">Videos</a></td><td width="650px">Logistic regression, support vector machines, surrogate losses</td></tr>
<tr><td width="100px">Lecture 8</td><td width="100px">Notebook-Videos</td><td width="650px">Online learning, stochastic gradient descent, perceptron</td></tr>
</table>

<h4>Unsupervised Learning and HMMs</h4>

Principles: HMMs, Clustering, Dimension Reduction
Reading: ESL Chapter 14, ["An Introduction to Hidden Markov Models and Bayesian Networks"](http://mlg.eng.cam.ac.uk/zoubin/papers/ijprai.pdf), Zoubin Ghahramani
<table>    
<tr><td width="100px">Lecture 9</td><td width="100px">Notebook-Videos</td><td width="650px">Clustering</td></tr>
<tr><td width="100px">Lecture 10</td><td width="100px">Notebook-Videos</td><td width="650px">Dimension Reduction</td></tr>
<tr><td width="100px">Lecture 11</td><td width="100px">Notebook-Videos</td><td width="650px">Hidden Markov Models</td></tr>
</table>

<h4>Non-linear methods</h4>

Principles: basis expansion, kernel trick, bagging, boosting, neural nets<br>
Reading: ESL Chapter 5, 7, 8
<table>
<tr><td width="100px">Lecture 12</td><td width="100px">Notebook-Videos</td><td width="650px">Basis expansion and kernel trick</td></tr>
<tr><td width="100px">Lecture 13</td><td width="100px">Notebook-Videos</td><td width="650px">Bootstrap, Decision Trees, and Random Forests</td></tr>
<tr><td width="100px">Lecture 14</td><td width="100px">Notebook-Videos</td><td width="650px">Boosting</td></tr>
<tr><td width="100px">Lecture 15</td><td width="100px">Notebook-Videos</td><td width="650px">Neural Networks</td></tr>
</table>

<h4>Deep Learning</h4>
<table>
<tr><td width="100px">Lecture 16</td><td width="100px">Notebook-Videos</td><td width="650px">Convolutional nets</td></tr>
<tr><td width="100px">Lecture 17</td><td width="100px">Notebook-Videos</td><td width="650px">Recurrent neural nets</td></tr>
<tr><td width="100px">Lecture 18</td><td width="100px">Notebook-Videos</td><td width="650px">Tensorflow 1</td></tr>
<tr><td width="100px">Lecture 19</td><td width="100px">Notebook-Videos</td><td width="650px">Tensorflow 2</td></tr>
</table>
