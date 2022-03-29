### Todo
- Review and integrate info at [Homemade Machine Learning](https://github.com/trekhleb/homemade-machine-learning).

# ds-study-group
The three legs of data science:
1. **DevOps** (Unix, Python, Pandas, Scikit-learn, Matplotlib, Jupyter, Git, Github) 
2. **Statistics** (random variables, pdf, central moments, conditional probability, CLT, null hypothesis)
3. **Machine Learning** (linear regression, logistic regression, clusterting, dimension reduction, decision trees, MLP, back-prop, NLP, GAN)

## DevOps
- [The Linux command line for beginner](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview): This tutorial will teach you a little of the history of the command line, then walk you through some practical excercises to become familiar with a few basic commands and concepts. 

- [Git](https://git-scm.com/): Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

- [Python Resources](./python): Various aspects about the Python programming ecosystem including Pandas, Scikit Learn, TensorFlow and Torch.

- [Colab](https://colab.research.google.com/notebooks/intro.ipynb): olaboratory, or "Colab" for short, allows you to write and execute Python in your browser, with Zero configuration required Free access to GPUs. Jake Vanderplus video introduction to [Colab](https://www.youtube.com/watch?v=inN8seMm7UI).

### Dig deeper
- [DevOps Study Group](https://github.com/study-groups/devops-study-group): DevOps study group which touches on various aspects computer management. Useful for deploying projects. 

- [DataOps Study Group](https://github.com/study-groups/dataops-study-group): study group about big data.

- [GitHub](https://github.com/): defacto cloud storage for code.

- [GitLab](https://about.gitlab.com/): competition to GitHub. GitLab has beter [CI/CD](https://docs.gitlab.com/ee/ci/).
- [GitPod](https://www.gitpod.io/): VS Code in the cloud that works directly with Git repositories on GitLab or GitHub.

## Statistics


- [Statistics for Hackers](https://www.youtube.com/watch?v=Iq9DzN6mvYA) Jake Vanderplus's nice bridge between
Python and statistics.

- [Probability Theory and Mathematical Statistics at Penn State (Stat 414/415)](https://onlinecourses.science.psu.edu/stat414/)
  - In Section 1, one of our primary focuses will be to develop an understanding of the various ways in which we can assign a **probability to some chance event**. We'll also learn the fundamental properties of probability, investigate how probability behaves, and learn how to calculate the probability of a new chance event.

  - In Section 2, we'll explore **discrete random variables** and **discrete probability distributions**. The basic idea is that when certain conditions are met, we can derive formulas for calculating the probability of an event. Then, instead of returning to the basic probability rules we learned in Section 1 to calculate the probability of an event, we can use the new formulas we derived, provided that the certain conditions are met.

  - In Section 3, as the title suggests, we will investigate probability distributions of **continuous random variables**, that is, random variables whose possible outcomes fall on an infinite interval. It's in this section that you'll want to make sure your calculus skills of integration and differentiation are up to snuff before tackling many of the problems you'll encounter.
  
  - In Section 4, we'll extend many of the definitions and concepts that we learned in Sections 2 and 3 to the case in which we have **two random variables**. More specifically, we will (1) extend the definition of a probability distribution of one random variable to the **joint probability distribution of two random variables**, (2) learn how to use the **[correlation coefficient](https://online.stat.psu.edu/stat414/lesson/18)** as a way of quantifying the extent to which two random variables are linearly related, (3) extend the definition of the **conditional probability** of events in order to find the conditional probability distribution of one random variable given that another that has occurred, and (4) investigate a particular joint probability distribution, namely the bivariate normal distribution.
  
  - Finally, in Section 5, as the name of this section suggests, we will spend some time learning how to find the probability distribution of functions of random variables. For example, we might know the probability density function of X, but want to know instead the probability density function of X2. We'll learn several different techniques for finding the distribution of **functions of random variables**, including the distribution function technique, the change-of-variable technique and the **moment-generating function** technique. The more important functions of random variables that we'll explore will be those involving random variables that are independent and identically distributed. 


### Advanced Statistics
- [BIOS 735 - Introduction to Statistical Computing](https://biodatascience.github.io/statcomp/): by Michael Love and Naim Rashid. This class teaches important concepts and skills for statistical computing, numerical optimization, and machine learning using case studies. After this course, students will have a good understanding of the process of producing high-quality and sharable statistical programs (module 1, 3 weeks), algorithms for optimization and numerical integration (module 2, 6 weeks), and will be able to implement and apply some common and powerful machine learning methods (module 3, 3 weeks). Modules 1 and 3 were originally developed by Dr. Michael Love. [R based code](https://github.com/biodatascience/statcomp_src). 


- [Introduction to the Theory of Random Signals and Noise](https://archive.org/details/IntrductionToTheTheoryOfRandomSignalsAndNoise/page/n377/mode/2up): First 5 chapters of 
Davenport and Root's book properly describe what a random variable is. In the parlance of modern data science, a **random 
variable** is the name of a **column** in a data set and a **row** in a data set is an **event**. Note taht an event 
consists of mutltidensional sample of random variables which may be [correlated](https://en.wikipedia.org/wiki/Covariance_and_correlation).

- [Probability Theory: The Logic of Science by E.T. Jaynes](https://bayes.wustl.edu/etj/prob/book.pdf). From the preface: *The following material is addressed to readers who are already familiar with applied mathematics
at the advanced undergraduate level or preferably higher; and with some field, such as physics,
chemistry, biology, geology, medicine, economics, sociology, engineering, operations research, etc.,
where inference is needed.† A previous acquaintance with probability and statistics is not necessary;
indeed, a certain amount of innocence in this area may be desirable, because there will be less to
unlearn.*

- [Applied Statistics at Penn State (Stat 500)](https://newonlinecourses.science.psu.edu/statprogram/stat500)
- [Regression Methods at Penn State (Stat 501)](https://newonlinecourses.science.psu.edu/stat501/)
- [Statistical Thinking and Data Analysis by Cynthia Rudin](https://ocw.mit.edu/courses/sloan-school-of-management/15-075j-statistical-thinking-and-data-analysis-fall-2011/index.htm)

- [Statistics for Hackers](https://www.youtube.com/watch?v=Iq9DzN6mvYA) Jake Vanderplus's nice bridge between
Python and statistics.

## Machine Learning

### Supervised learning (labeled data) topics
- Linear regression
- Multi-dimensional linear regression
- Statsmodel analysis of variance
- Logistc regression
- Stats: bias/variance trade-off
- Stats: Receiver Operator Characteristc
- Math: Vector algebra
- Back prop over squared error surface
- Multiple Layer Preceptrons
- Math: Tensors (TensorFlow and PyTorch)
- Image classifciation

### Unsupervised learning via clustering
- High dimensional data => correlated data
- Dimensionality reduction via Singular Value Decompostion
- One hot encoding of natural language
- Embedding spaces for latent variables
- Sequential encoding via long, short term memory (LSTM)

### Semi-supervised competitive models
- Generative Pre-trained Transformers (GPT-2 ala Joel Grus)
- Generative adverserial networks (GANs ala Ian Goodfellow)

## Resources

### Online courses
- [CS230 Deep Learning at Stanford by Adrew Ng](https://cs230.stanford.edu/syllabus/): Dr. Ng is great. Founder of Coursea.
- [Stanford NLP](http://web.stanford.edu/class/cs224n/): Christopher Mannering et. al at Stanford.

### Projects
- [ds-projects](https://github.com/study-groups/ds-projects): Boot camp capstone projects.
- [Harvard NLP](https://nlp.seas.harvard.edu/code/) Collection of code and papers at Havard.

### Blogs
- [Chris Albon's extensive list of data science resources.](https://chrisalbon.com/)

### Data Sets
- [U.S. Bureau of Labor Statistics](https://www.bls.gov/)
- [Interesting Kaggle competitions](./kaggle/readme.md)

