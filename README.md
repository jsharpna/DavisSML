UC Davis Statistics 208 : Statistical Machine Learning
==============================

A Course on the Principles of Statistical Machine Learning with Examples in Python

Machine learning is how to get computers to automatically learn and improve with experience. Experience comes in the form of data, improvement is with respect to some performance metric, and learning is done by a learning algorithm. There are always computational constraints, such as the architecture, computation time, bandwidth limitations, and so on. So we can more precisely restate the goal thus: to construct learning algorithms that use data to improve with respect to a performance metric and do so under computational constraints.

<h2>Instructions</h2>

1. Class time will be for lectures and labs.  These will be posted in advance in their sections.  Labs are not graded, and you will have an opportunity to go over your results in class.
1. Homework will be due every week or so, starting with the second week. (50% of grade)
1. Discussions and questions should be posted on the slack site.
1. A final project will be due at the end of the class.  (50% of grade)
1. You will need to install Python and the necessary packages to participate in this class.  See the following instructions for the installation.

<h2>Textbooks</h2>
* Required: <a href="http://www-bcf.usc.edu/~gareth/ISL/">A Introduction to Statistical Learning</a> by James, Witten, Hastie, and Tibshirani
* Recommended: <a href="http://www.springer.com/us/book/9783319307152">Python for Probability, Statistics, and Machine Learning</a> by Unpingco

<h2>Syllabus</h2>
<h4>Part 1 : Supervised learning and general concepts</h4>
<h4>Introduction to Machine Learning</h4>
<table>
<tr><td width="50px">3/28</td><td width="100px">Lecture 1</td><td width="650px">Introduction to Machine Learning</td></tr>
<tr><td width="50px">3/30</td><td width="100px">Lecture 2</td><td width="650px"> Nearest neighbors regression: a first look at the bias-variance tradeoff</td></tr>
</table>

<h4>Learning with representations: How to not underfit</h4>
<table>
<tr><td width="50px">4/4</td><td width="100px">Lecture 3</td><td width="650px">Basis expansion</td></tr>
<tr><td width="50px">4/6</td><td width="100px">Lecture 4</td><td width="650px">Kernels and the kernel trick</td></tr>
<tr><td width="50px">4/11</td><td width="100px">Lecture 5</td><td width="650px">Gradient methods</td></tr>
</table>

<h4>The bias-variance tradeoff: How to not overfitting</h4>
<table>
<tr><td width="50px">4/13</td><td width="100px">Lecture 6</td><td width="650px"> Model selection, information criteria, and cross-validation
</td></tr>
<tr><td width="50px">4/18</td><td width="100px">Lecture 7</td><td width="650px">Sparsity and the L1 penalty</td></tr>
</table>

<h4>Advanced topics in supervised learning</h4>
<table>
<tr><td width="50px">4/20</td><td width="105px">Lecture 8</td><td width="100%">Model aggregation : bagging and boosting</td></tr>
<tr><td width="50px">4/25</td><td width="105px">Lecture 9</td><td>Support vector machines</td></tr>
<tr><td width="50px">4/27</td><td width="105px">Lecture 10</td><td>Neural networks</td></tr>
</table>

<h4>Part 2 : Beyond supervised learning</h4>
<h4>Unsupervised learning</h4>
<table>
<tr><td width="50px">5/2</td><td width="100px">Lecture 11</td><td width="650px">Clustering</td></tr>
<tr><td width="50px">5/4</td><td width="100px">Lecture 12</td><td width="650px">Spectral methods</td></tr>
</table>

<h4>Matrix and network learning </h4>
<table>
<tr><td width="50px">5/9</td><td width="100px">Lecture 13</td><td width="650px">Gaussian graphical models</td></tr>
<tr><td width="50px">5/11</td><td width="100px">Lecture 14</td><td width="650px">Matrix completion and link prediction</td></tr>
</table>

<h4>Sequential learning</h4>
<table>
<tr><td width="50px">5/16</td><td width="100px">Lecture 15</td><td width="650px">Multi-armed bandits</td></tr>
<tr><td width="50px">5/18</td><td width="100px">Lecture 16</td><td width="650px">Hidden markov models</td></tr>
<tr><td width="50px">5/23</td><td width="100px">Lecture 17</td><td width="650px">Active learning</td></tr>
</table>

<h4>Final project presentations</h4>
<table>
<tr><td width="50px">5/25</td><td width="100px">Group 1</td><td width="650px"></td></tr>
<tr><td width="50px">6/1</td><td width="100px">Group 2</td><td width="650px"></td></tr>
<tr><td width="50px">6/6</td><td width="100px">Group 3</td><td width="650px"></td></tr>
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
