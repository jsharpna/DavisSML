UC Davis Statistics 208 : Statistical Machine Learning
==============================

Lecture Notes
--------------

A Course on the Principles of Statistical Machine Learning with Examples in Python
-----------------------------

Machine learning is how to get computers to automatically learn and improve with experience. Experience comes in the form of data, improvement is with respect to some performance metric, and learning is done by a learning algorithm. There are always computational constraints, such as the architecture, computation time, bandwidth limitations, and so on. So we can more precisely restate the goal thus: to construct learning algorithms that use data to improve with respect to a performance metric and do so under computational constraints.

We will focus on principles of statistical machine learning in the prediction problems, regression and classification.  Conspicuously absent is most Bayesian methodology and advanced concepts such as reinforcement learning.  This course is not a broad overview of all of machine learning, but rather a tour of the key ideas in machine learning as told through these prediction tasks.  Typically, I have students tell me something along the lines of "I thought machine learning was about [insert random methodology here]".  Machine learning is a field, like physical chemistry or creative literature.  It is not defined by a couple of methods or a single task, and cannot be taught in a single quarter.  With that said, I want this course to lay the foundation for a rich understanding of machine learning.

<h2>Instructions</h2>

1. Class time will be for lectures and labs.  These will be posted in advance in their sections.  Labs are not graded, and you will have an opportunity to go over your results in class.
1. Homework will be due every week or so, starting with the second week. (50% of grade)
1. Discussions and questions should be posted on the [slack site](http://ucdavis.slack.com): find the channel `2018-sta208`
1. During the quarter, I will try to check my email at the end of the day on weekdays: `prof.jsharpna@gmail.com` 
1. A final project will be due at the end of the class.  [Instructions can be found here.](misc/final_proj.md)  (50% of grade)
1. You will need to install Python and the necessary packages to participate in this class.  See [the following instructions](misc/install.md) for installation notes.

<h2>Office Hours</h2>

- Prof. James: 10-11 Tue, 10-11 Thu, 3-4 Fri (MSB 4107)
- Liwei Wu: 2-4 Wed (Stat TA room)
- Siteng Hao: 10-12 Fri (Stat TA room)

<h2>Textbooks</h2>

- Required: <a href="https://statweb.stanford.edu/~tibs/ElemStatLearn/">Elements of Statistical Learning</a> by Hastie, Tibshirani, and Friedman
- Recommended: <a href="http://www.springer.com/us/book/9783319307152">Python for Probability, Statistics, and Machine Learning</a> by Unpingco
- Recommended: <a href="http://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf">Convex Optimization by Boyd and Vandenberghe</a>

<h2>Homeworks</h2>

<h2>Syllabus</h2>

<h4>Introduction to Machine Learning</h4>

Principles: Over/under-fitting, training and testing, losses<br>
Reading: ESL Chapter 2
<table>
<tr><td width="50px">4/2</td><td width="100px"><a href="lectures/lecture1/lecture1.md">Lecture 1</a></td><td width="650px">Introduction to machine learning and Python I</td></tr>
<tr><td width="50px">4/4</td><td width="100px"><a href="lectures/lecture2/lecture2.md">Lecture 2</a></td><td width="650px">Introduction to machine learning and Python II, <a href="labs/lab1.ipynb">Lab 1</a></td></tr>
</table>

<h4>Regression (beyond Ordinary Least Squares)</h4>

Principles: Convex relaxation, computational intractability in subset selection<br>
Reading: ESL Chapter 3, [Boyd Chapter 1](http://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)
<table>
<tr><td width="50px">4/9</td><td width="100px"><a href="lectures/lecture3/lecture3slides.pdf">Lecture 3</a></td><td width="650px">OLS,  Matrix Decompositions, <a href="lectures/lecture3/Leave_one_out_CV.pdf">leave-1-out cross validation</a></td></tr>
<tr><td width="50px">4/11</td><td width="100px"><a href="lectures/lecture4/lecture3slides.pdf">Lecture 4</a></td><td width="650px">Subset selection and ridge regression, <a href="labs/lab2.ipynb">Lab 2</a>, <a href="labs/lab2-soln.ipynb">Solutions</a></td></tr>
<tr><td width="50px">4/16</td><td width="100px"><a href="lectures/lecture4/lecture4slides.pdf">Lecture 5</a></td><td width="650px">Convex optimization</td></tr>
<tr><td width="50px">4/18</td><td width="100px"><a href="lectures/lecture5/lecture5.md">Lecture 6</a></td><td width="650px">The Lasso, Discussion on HW1</td></tr>
</table>

<h4>Classification</h4>

Principles: Surrogate losses, generative and discriminative methods<br>
Reading: ESL Chapter 4
<table>
<tr><td width="50px">4/23</td><td width="100px"><a href="lectures/lecture6/lecture6slides.pdf">Lecture 7</a></td><td width="650px">Logistic regression</td></tr>
<tr><td width="50px">4/25</td><td width="100px"><a href="lectures/lecture7/lecture7slides.pdf">Lecture 7</a></td><td width="650px">Classification and Generative Methods, <a href="labs/lab3.ipynb">Lab 3</a>, <a href="labs/lab3-soln.ipynb">Solns</a></td></tr>
<tr><td width="50px">4/30</td><td width="100px"><a href="lectures/lecture8/lecture8slides.pdf">Lecture 8</a></td><td width="650px">Max-margin Methods</td></tr>
</table>

<h4>Unsupervised Learning</h4>

Principles: Compression, Dimension Reduction
Reading: ESL Chapter 14
<table>
<tr><td width="50px">5/2</td><td width="100px"><a href="lectures/lecture9-10/README.md">Lecture 9</a></td><td width="650px"><a href="lectures/lecture9-10/lecture9notes.pdf">Clustering (notes)</a></td></tr>
<tr><td width="50px">5/7</td><td width="100px"><a href="lectures/lecture9-10/README.md">Lecture 10</a></td><td width="650px"><a href="lectures/lecture9-10/lecture10notes.pdf">Dimension Reduction, <a href="labs/lab4.ipynb">Lab 4</a></a></td></tr>
</table>

<h4>Basis Expansion and Kernels</h4>

Principles: Feature extraction, the kernel trick, analysis/sythesis duality<br>
Reading: ESL Chapter 5
<table>
<tr><td width="50px">5/9</td><td width="100px"><a href="lectures/lecture11-12/lecture11notes.pdf">Lecture 11</a></td><td width="650px"><a href="lectures/lecture11-12/lecture11notes.pdf">Basis expansion and hi-di embeddings</a></td></tr>
<tr><td width="50px">5/14</td><td width="100px"><a href="lectures/lecture11-12/lecture12notes.pdf">Lecture 12</a></td><td width="650px">Kernels</td></tr>
</table>

<h4>Resampling, Trees, and Aggregation</h4>

Principles: Interpretable models, statistical complexity, learning from experts<br>
Reading: ESL Chapters 7, 8
<table>
<tr><td width="50px">5/14</td><td width="105px"><a href="lectures/lecture13-14/lecture14notes.pdf">Lecture 13</a></td><td width="650px">Bootstrap, Decision Trees, and Random Forests</td></tr>
<tr><td width="50px">5/16</td><td width="105px"><a href="lectures/lecture13-14/lecture15notes.pdf">Lecture 14</a></td><td width="650px">Boosting</td></tr>
</table>

<h4>Stochastic Optimization, Neural Networks</h4>
Principes: online learning, stochastic optimization, neural networks basics

<table>
<tr><td width="50px">5/21</td><td width="100px"><a href="lectures/lecture15-16/lecture16notes.pdf">Lecture 16</a></td><td width="650px">Stochastic gradient and online learning</td></tr>
<tr><td width="50px">5/23</td><td width="100px">Lecture 17</td><td width="650px">Gradient boosting</td></tr>
<tr><td width="50px">5/30</td><td width="100px"><a href="lectures/lecture17-18/lecture17notes.pdf">Lecture 18</a></td><td width="650px">Neural Networks</td></tr>
</table>

<h4>Miscellanea</h4>
<table>
<tr><td width="50px">6/4</td><td width="105px">Lecture 19</td><td width="650px">Networks and Manifold Learning</td></tr>
<tr><td width="50px">6/6</td><td width="105px">Lecture 21</td><td width="650px">Convolutional Nets</td></tr>
</table>



Repository Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── labs               <- notebook files for course labs (6 labs)
    │
    ├── homeworks          <- notebook files for homeworks (6 hws)
    │
    ├── lectures           <- notebook files for lectures (naming convention 
    │
    ├── references         <- Reference material, pdfs, etc.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
