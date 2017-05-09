UC Davis Statistics 208 : Statistical Machine Learning
==============================

A Course on the Principles of Statistical Machine Learning with Examples in Python
-----------------------------

Machine learning is how to get computers to automatically learn and improve with experience. Experience comes in the form of data, improvement is with respect to some performance metric, and learning is done by a learning algorithm. There are always computational constraints, such as the architecture, computation time, bandwidth limitations, and so on. So we can more precisely restate the goal thus: to construct learning algorithms that use data to improve with respect to a performance metric and do so under computational constraints.

We will focus on principles of statistical machine learning in the prediction problems, regression and classification.  Conspicuously absent is any Bayesian methodology, hidden Markov models, unsupervised learning including density estimation, clustering, dimension reduction, network modelling, etc.  This course is not a broad overview of all of machine learning, but rather a tour of the key ideas in machine learning as told through these prediction tasks.  Typically, I have students tell me something along the lines of "I thought machine learning was about [insert random methodology here]".  Machine learning is a field, like physical chemistry or creative literature.  It is not defined by a couple of methods or a single task, and cannot be taught in a single quarter.  With that said, I want this course to lay the foundation for a rich understanding of machine learning.

<h2>Instructions</h2>

1. Class time will be for lectures and labs.  These will be posted in advance in their sections.  Labs are not graded, and you will have an opportunity to go over your results in class.
1. Homework will be due every week or so, starting with the second week. (50% of grade)
1. Discussions and questions should be posted on the [slack site](https://ucdsta208.slack.com).
1. A final project will be due at the end of the class.  [Instructions can be found here.](misc/final_proj.md)  (50% of grade)
1. You will need to install Python and the necessary packages to participate in this class.  See [the following instructions](lectures/lecture1/lecture1.md) for the installation.

<h2>Office Hours</h2>

- James: Wednesdays 9am-12pm in MSB 4107
- Chunzhe: Monday 1-3pm in MSB 1117
- Huang: Friday 1-3pm in MSB 1117

<h2>Textbooks</h2>

- Required: <a href="https://statweb.stanford.edu/~tibs/ElemStatLearn/">Elements of Statistical Learning</a> by Hastie, Tibshirani, and Friedman
- Recommended: <a href="http://www.springer.com/us/book/9783319307152">Python for Probability, Statistics, and Machine Learning</a> by Unpingco
- Recommended: <a href="http://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf">Convex Optimization by Boyd and Vandenberghe</a>

<h2>Syllabus</h2>

<h4>Introduction to Machine Learning</h4>

Principles: Over/under-fitting, training and testing, losses<br>
Reading: ESL Chapter 2
<table>
<tr><td width="50px">4/4</td><td width="100px"><a href="lectures/lecture1/lecture1.md">Lecture 1</a></td><td width="650px">Introduction to machine learning and Python I</td></tr>
<tr><td width="50px">4/6</td><td width="100px"><a href="lectures/lecture2/lecture2.md">Lecture 2</a></td><td width="650px">Introduction to machine learning and Python II, <a href="labs/lab1.ipynb">Lab 1</a></td></tr>
</table>

<h4>Regression (beyond Ordinary Least Squares)</h4>

Principles: Convex relaxation, computational intractability in subset selection<br>
Reading: ESL Chapter 3, [Boyd Chapter 1](http://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)
<table>
<tr><td width="50px">4/11</td><td width="100px"><a href="lectures/lecture3/lecture3.md">Lecture 3</a></td><td width="650px">Subset selection and ridge regression</td></tr>
<tr><td width="50px">4/13</td><td width="100px"><a href="lectures/lecture4/lecture4slides.pdf">Lecture 4</a></td><td width="650px">Convex optimization, <a href="labs/lab2.ipynb">Lab 2</a>, <a href="labs/lab2-soln.ipynb">Solutions</a></td></tr>
<tr><td width="50px">4/18</td><td width="100px"><a href="lectures/lecture5/lecture5.md">Lecture 5</a></td><td width="650px">The Lasso, <a href="labs/lab3.ipynb">Lab 3</a>, <a href="labs/lab3-soln.ipynb">Solns</a></td></tr>
</table>

<h4>Classification</h4>

Principles: Surrogate losses, generative and discriminative methods<br>
Reading: ESL Chapter 4
<table>
<tr><td width="50px">4/20</td><td width="100px"><a href="lectures/lecture6/lecture6slides.pdf">Lecture 6</a></td><td width="650px">Logistic regression</td></tr>
<tr><td width="50px">4/25</td><td width="100px"><a href="lectures/lecture7/lecture7slides.pdf">Lecture 7</a></td><td width="650px">Classification and Generative Methods, <a href="labs/lab4.ipynb">Lab 4</a></td></tr>
<tr><td width="50px">4/27</td><td width="100px"><a href="lectures/lecture8/lecture8slides.pdf">Lecture 8</a></td><td width="650px">Max-margin Methods</td></tr>
</table>

<h4>Unsupervised Learning</h4>

Principles: Compression, Dimension Reduction
Reading: ESL Chapter 14
<table>
<tr><td width="50px">5/2</td><td width="100px"><a href="lectures/lecture9-10/README.md">Lecture 9</a></td><td width="650px"><a href="lectures/lecture9-10/lecture9notes.pdf">Clustering (notes)</a></td></tr>
<tr><td width="50px">5/4</td><td width="100px"><a href="lectures/lecture9-10/README.md">Lecture 10</a></td><td width="650px"><a href="lectures/lecture9-10/lecture10notes.pdf">Dimension Reduction (notes)</a></td></tr>
</table>

<h4>Basis Expansion and Kernels</h4>

Principles: Feature extraction, the kernel trick, analysis/sythesis duality<br>
Reading: ESL Chapter 5
<table>
<tr><td width="50px">5/9</td><td width="100px"><a href="lectures/lecture11-12/lecture11notes.pdf">Lecture 11</a></td><td width="650px"><a href="lectures/lecture11-12/lecture11notes.pdf">Basis expansion and hi-di embeddings</a></td></tr>
<tr><td width="50px">5/11</td><td width="100px">Lecture 12</td><td width="650px">Smoothing splines and kernels</td></tr>
</table>

<h4>Resampling, Trees, and Aggregation</h4>

Principles: Interpretable models, statistical complexity, learning from experts<br>
Reading: ESL Chapters 7, 8
<table>
<tr><td width="50px">5/13</td><td width="105px">Lecture 13</td><td width="650px">Bootstrap and cross validation</td></tr>
<tr><td width="50px">5/16</td><td width="105px">Lecture 14</td><td width="650px">Trees, generalized additive models</td></tr>
<tr><td width="50px">5/18</td><td width="105px">Lecture 15</td><td width="650px">Boosting and Random Forests</td></tr>
</table>

<h4>Online Learning, Neural Networks, and Deep Learning</h4>

Principles: multi-layer architectures, non-convex optimization, online algorithms
<table>
<tr><td width="50px">5/23</td><td width="100px">Lecture 16</td><td width="650px">Stochastic gradient and online learning</td></tr>
<tr><td width="50px">5/25</td><td width="100px">Lecture 17</td><td width="650px">Neural Networks and Backpropogation</td></tr>
<tr><td width="50px">5/30</td><td width="100px">Lecture 18</td><td width="650px">Deep Learning</td></tr>
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
