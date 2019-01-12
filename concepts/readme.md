# Data Science Concepts

## Statistics
- [Omnibus test](https://en.wikipedia.org/wiki/Omnibus_test). Omnibus tests are a kind of statistical test. They test whether the explained variance in a set of data is significantly greater than the unexplained variance, overall. One example is the F-test in the analysis of variance. 
- [Akaike information criterion (AIC)](https://en.wikipedia.org/wiki/Akaike_information_criterion)The Akaike information criterion (AIC) is an estimator of the relative quality of statistical models for a given set of data. Given a collection of models for the data, AIC estimates the quality of each model, relative to each of the other models. Thus, AIC provides a means for model selection.

- [Maximum Likelihood Estimation](https://towardsdatascience.com/a-gentle-introduction-to-maximum-likelihood-estimation-9fbff27ea12f). "In statistics, maximum likelihood estimation (MLE) is a method of estimating the parameters of a statistical model given observations, by finding the parameter values that maximize the likelihood of making the observations given the parameters. MLE can be seen as a special case of the maximum a posteriori estimation (MAP) that assumes a uniform prior distribution of the parameters, or as a variant of the MAP that ignores the prior and which therefore is unregularized."

- [p-value](https://en.wikipedia.org/wiki/P-value) The p-value is used in the context of null hypothesis testing in order to quantify the idea of statistical significance of evidence. A claim is assumed valid if its counter-claim is improbable. That is, a low p-value means it was unlikely predicted value was by chance. Conversely, given high p-value, we rejectthe null hypothesis implies that the correct hypothesis lies in the logical complement of the null hypothesis. However, unless there is a single alternative to the null hypothesis, the rejection of null hypothesis does not tell us which of the alternatives might be the correct one.

- [One and Two Tailed Tests](https://stats.idre.ucla.edu/other/mult-pkg/faq/general/faq-what-are-the-differences-between-one-tailed-and-two-tailed-tests/) The default among statistical packages performing tests is to report two-tailed p-values.  Because the most commonly used test statistic distributions (standard normal, Student’s t) are symmetric about zero, most one-tailed p-values can be derived from the two-tailed p-values.

- [Standard Error](https://en.wikipedia.org/wiki/Standard_error) In regression analysis, the term "standard error" refers either to the square root of the reduced chi-squared statistic or the standard error for a particular regression coefficient (as used in, e.g., confidence intervals). SE of the Mean = sigma_population / sqrt(n). Since sigma_population is seldom known, SE ~= sigma_sample/sqrt(n). A practical result: Decreasing the uncertainty in a mean value estimate by a factor of two requires acquiring four times as many observations in the sample. Or decreasing the standard error by a factor of ten requires a hundred times as many observations.

- [Confidence Intervals](https://en.wikipedia.org/wiki/Confidence_interval) The principle behind confidence intervals was formulated to provide an answer to the question raised in statistical inference of how to deal with the uncertainty inherent in results derived from data that are themselves only a randomly selected subset of a population. There are other answers, notably that provided by Bayesian inference in the form of credible intervals.

- [Coefficient of Determination (R-squared)](https://en.wikipedia.org/wiki/Coefficient_of_determination) 
R2 = 1 - SS_res / SS_tot. In a general form, R2 can be seen to be related to the fraction of variance unexplained (FVU), since the second term compares the unexplained variance (variance of the model's errors) with the total variance (of the data): R2 = 1 - FVU. Suppose R2 = 0.49. This implies that 49% of the variability of the dependent variable has been accounted for, and the remaining 51% of the variability is still unaccounted for.
- [Adjusted R2](http://blog.minitab.com/blog/adventures-in-statistics-2/multiple-regession-analysis-use-adjusted-r-squared-and-predicted-r-squared-to-include-the-correct-number-of-variables)
Use the adjusted R-square to compare models with different numbers of predictors
Use the predicted R-square to determine how well the model predicts new observations and whether the model is too complicated

- [Chi-squared test](https://en.wikipedia.org/wiki/Chi-squared_test) A chi-squared test, also written as χ2 test, is any statistical hypothesis test where the sampling distribution of the test statistic is a chi-squared distribution when the null hypothesis is true. Used for categorical data.


- [F-test](https://en.wikipedia.org/wiki/F-test) An F-test is any statistical test in which the test statistic has an F-distribution under the null hypothesis whose shape depends on degree of freedom. The F test statistic is the ratio
of two independent chi-squared variables divided by their degrees of freedom. It is most often used when comparing statistical models that have been fitted to a data set, in order to identify the model that best fits the population from which the data were sampled. 
  - [f-statistic-value-test](https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/f-statistic-value-test/)

- [ANOVA](https://people.richland.edu/james/lecture/m170/ch13-1wy.html) Image a table with k columns of variables (between grou variation) and N  rows of samples (within group variation).
There is the between group variation and the within group variation. If the variance caused by the interaction between the samples is much larger when compared to the variance that appears within each group, then it is because the means aren't the same.

- [F-distribution](https://en.wikipedia.org/wiki/F-distribution)
The F-distribution is the distribution under null hypothesis in the analysis of variance (ANOVA), 
In this case degree of freedom is (k-1) for mean-squared error between groups, s_b^2  and (N-k) for the variance due to the differences within individual samples, denoted s_w^2  (Mean Square Within groups). This is the within group variation divided by its degrees of freedom (N-k). F = s_b^2 / s_w^2. The F test statistic is found by dividing the between group variance by the within group variance. The degrees of freedom for the numerator are the degrees of freedom for the between group (k-1) and the degrees of freedom for the denominator are the degrees of freedom for the within group (N-k).


- [Degrees of Freedom](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)) While introductory textbooks may introduce degrees of freedom as distribution parameters or through hypothesis testing, it is the underlying geometry that defines degrees of freedom, and is critical to a proper understanding of the concept.  The term itself was popularized by English statistician and biologist Ronald Fisher beginning with his 1922 work on chi squares. The distribution under null hypothesis in ANOVA is the F-test, named after him.

- [Interquartile range](https://en.wikipedia.org/wiki/Interquartile_range) Building block of box plot. Alternative
to speaking of probability distribution's standard deviation.

- [Q-Q Plot](https://en.wikipedia.org/wiki/Q%E2%80%93Q_plot)
In statistics, a Q–Q (quantile-quantile) plot is a probability plot, which is a graphical method for comparing two probability distributions by plotting their quantiles against each other.

- [Normal probability plot](https://en.wikipedia.org/wiki/Normal_probability_plot)
he normal probability plot is a graphical technique to identify substantive 
departures from normality. This includes identifying outliers, skewness, kurtosis, 
a need for transformations, and mixtures. Normal probability plots are made of raw data, r
esiduals from model fits, and estimated parameters.
- [Boltzman Machine](https://en.wikipedia.org/wiki/Boltzmann_machine) A Boltzmann machine
(also called stochastic Hopfield network with hidden units) is a type of stochastic 
recurrent neural network (and Markov random field).
- [Markov random field](https://en.wikipedia.org/wiki/Markov_random_field)r undirected 
  graphical model is a set of random variables having a Markov property described by an undirected graph.
- [Restrcted Boltzmann Machine](https://en.wikipedia.org/wiki/Restricted_Boltzmann_machine)
A restricted Boltzmann machine (RBM) is a generative stochastic artificial 
neural network that can learn a probability distribution over its set of inputs.
  - . RBMs have found applications in dimensionality reduction, classification, 
  collaborative filtering, feature learning and topic modelling.
  They can be trained in either supervised or unsupervised ways, depending on the task.
-[Expectation Maximization with Gaussian Mixture Models](http://www.aishack.in/tutorials/expectation-maximization-gaussian-mixture-model/)
how to model multivariate data with a Gaussian Mixture Model. 
For training this model, we use a technique called Expectation Maximization.
- [Cross Entropy](https://en.wikipedia.org/wiki/Cross_entropy) In information theory, the cross entropy between two probability distributions {\displaystyle p} p and {\displaystyle q} q over the same underlying set of events measures the average number of bits needed to identify an event drawn from the set, if a coding scheme is used that is optimized for an "artificial" probability distribution {\displaystyle q} q, rather than the "true" distribution {\displaystyle p} p.
  -Related to [Kullback-Leibler divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)

## Dimension reduction

- [Correspondence Analysis](https://en.wikipedia.org/wiki/Correspondence_analysis).
All data should be on the same scale for CA to be applicable, keeping in mind that the method treats rows and columns equivalently. It is traditionally applied to contingency tables — CA decomposes the chi-squared statistic associated with this table into orthogonal factors.

  - [Intro to CA](https://www.mathematica-journal.com/2010/09/an-introduction-to-correspondence-analysis/).
 "Cross tabulations (also known as cross tabs, or contingency tables) often arise in data analysis, whenever data can be placed into two distinct sets of categories. In market research, for example, we might categorize purchases of a range of products made at selected locations; or in medical testing, we might record adverse drug reactions according to symptoms and whether the patient received the standard or placebo treatment." 
 
  - [How Correspondence analysis works](https://www.displayr.com/how-correspondence-analysis-works/) Correspondence 
  analysis is a data science tool for summarizing tables. This post explains the basics of how it works. 
  It focuses on how to understand the underlying logic without entering into an explanation of the actual math.

- [Geometric Data Analysis](https://en.wikipedia.org/wiki/Geometric_data_analysis) comprises geometric aspects of image analysis, pattern analysis and shape analysis or the approach of multivariate statistics that treats arbitrary data sets as clouds of points in n-dimensional space.

  - [Slides on GDA](../slides/gda-le-roux-slides.pdf) which 
    show the connction between PCA, MCA and GDA.
    
- [Multiple correspondence analysis](https://en.wikipedia.org/wiki/Multiple_correspondence_analysis)
In statistics, multiple correspondence analysis (MCA) is a data analysis technique 
for nominal categorical data, used to detect and represent underlying structures 
in a data set. It does this by representing data as points in a low-dimensional Euclidean space. 


- [Tutorial on Principal Component Analysis](https://arxiv.org/pdf/1404.1100.pdf)
- [PCA on Quora](https://www.quora.com/What-is-the-difference-between-PCA-and-SVD)
- [PCA For categorical features](https://stackoverflow.com/questions/40795141/pca-for-categorical-features)

- [What is the intuitive relationship between SVD 
  and PCA?](https://math.stackexchange.com/questions/3869/what-is-the-intuitive-relationship-between-svd-and-pca)


## Bayesian
- [Bayesian_inference](https://en.wikipedia.org/wiki/Bayesian_inference)
- [Conjugate priors](https://en.wikipedia.org/wiki/Conjugate_prior)

## Hypothesis testing
- [P-Value by StatQuest](https://www.youtube.com/watch?v=5Z9OIYA8He8)

## Categorical variables
- [Chi Squared example](https://www.youtube.com/watch?v=1Ldl5Zfcm1Y)
  - [Chi-squared test on wikipedia](https://en.wikipedia.org/wiki/Chi-squared_test)

## Regression
- [Multiple Regression](https://people.richland.edu/james/ictcm/2004/multiple.html)  <- Fav, simple and clear
- [Regression Analysis ala Stata](https://stats.idre.ucla.edu/stata/output/regression-analysis-2/) 
- [Regression Tutorial with Analysis Examples, by Jim](http://statisticsbyjim.com/regression/regression-tutorial-analysis-examples/)
- [Reading a regresion table](http://svmiller.com/blog/2014/08/reading-a-regression-table-a-guide-for-students/)
- [Princeton Regression Intro](https://dss.princeton.edu/online_help/analysis/regression_intro.htm)
- [Princeton Interpreting regression output](https://dss.princeton.edu/online_help/analysis/interpreting_regression.htm)
- [Statsmodel documentation](https://www.statsmodels.org/stable/index.html)
- [Stats Models vs SKLearn for Linear Regression](https://becominghuman.ai/stats-models-vs-sklearn-for-linear-regression-f19df95ad99b)
- [The Simple Linear Regression Model at Penn State](https://newonlinecourses.science.psu.edu/stat501/node/253/)
- [Light Gradient Boosting](https://lightgbm.readthedocs.io/en/latest/)

## Random Forest
- [Hyperparameter Tuning the Random Forest in Python](https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74)
- [CPSC540 Machine Learning at University of British Columbia](https://www.cs.ubc.ca/~nando/540-2013/)
 - [Machine Learning: a Probabilistic Perspective] (https://www.cs.ubc.ca/~murphyk/MLbook/index.html) by Kevin Patrick Murphy
 - [Decision Tree lecture at](https://www.cs.ubc.ca/~nando/540-2013/lectures/l8.pdf)
 - [Random Forest](https://www.cs.ubc.ca/~nando/540-2013/lectures/l9.pdf)
- [Machine learning - Random forests YouTube lecture](https://www.youtube.com/watch?v=3kYujfDgmNk)


## Data Analtics
- [Exploratory Data Analysis - Principles of Graphics](https://www.youtube.com/watch?v=YcHAPmDL_wQ). Video from Open Education Lab.

## Data simulation
- [Simulate Regression Model](https://blogs.sas.com/content/iml/2017/01/25/simulate-regression-model-sas.html)
- [Generating correlated random variables](https://www.youtube.com/watch?v=QCqsJVS8p5A)
- [Generating Multivariate Gaussian Random Numbers](http://www.aishack.in/tutorials/generating-multivariate-gaussian-random/)
- [Synthetic cardiovascular data](https://laderast.github.io/cvdRiskData/)

## Graph theory
- [A-gentle-introduction-to-graph-theory](https://medium.com/basecs/a-gentle-introduction-to-graph-theory-77969829ead8)
- [https://becominghuman.ai/to-all-data-scientists-the-one-graph-algorithm-you-need-to-know-59178dbb1ec2](https://becominghuman.ai/to-all-data-scientists-the-one-graph-algorithm-you-need-to-know-59178dbb1ec2)
Connected Components: you can think of Connected Components in very layman’s terms as sort of a hard clustering algorithm 
which finds clusters/islands in related/connected data.
- [Connected Components in MapReduce and Beyond](https://ai.google/research/pubs/pub43122)
  
## Platforms
- [neural-net-from-scratch-with-pytorch](https://medium.com/@tomgrek/building-your-first-neural-net-from-scratch-with-pytorch-56b0e9c84d54)

## Packages
-[Introduction to the Syuzhet Package](https://cran.r-project.org/web/packages/syuzhet/vignettes/syuzhet-vignette.html)
The package comes with four sentiment dictionaries and provides a method for accessing 
the robust, but computationally expensive, sentiment extraction tool developed in the NLP group at Stanford.

 -[Stanford's CoreNLP](https://stanfordnlp.github.io/CoreNLP/)
 
## Datasets
- [lightgbm-baseline pet adoption](https://www.kaggle.com/peterhurford/pets-lightgbm-baseline-with-all-the-data)
  good kernel example
- [How much did it rain?](https://www.kaggle.com/c/how-much-did-it-rain/data)
- [Just Do it Tweets](https://www.kaggle.com/kappa123/exploring-justdoit-tweets)
- [Measures of Human Mobility Using Mobile Phone Records Enhanced with GIS Data](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0133630)
- [human+activity+recognition+using+smartphones](https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones)

## Papers
- [A survey of results on mobile phone datasets analysis](https://arxiv.org/pdf/1502.03406.pdf)
- [Vincent D. Blondel on Arxiv](https://arxiv.org/search/physics?searchtype=author&query=Blondel%2C+V+D)
  - Includes: [Clean up or mess up: 
    thD4D-Senegal: The Second Mobile Phone Data for Development 
    Challengee effect of sampling biases on measurements of degree distributions 
    in mobile phone datasets](https://arxiv.org/abs/1609.09413), 
    [Markov modeling of online inter-arrival times](https://arxiv.org/abs/1509.04857),
    [Sensitivity analysis of a branching process evolving on 
    a network with application in epidemiology](https://arxiv.org/abs/1509.01860),
    [Estimating Food Consumption and Poverty Indices with Mobile Phone Data](https://arxiv.org/abs/1412.2595),
    [Data for Development: the D4D Challenge on Mobile Phone Data](https://arxiv.org/abs/1210.0137)
- [Structural Bayesian Linear Regression for
Hidden Markov Models](https://www.merl.com/publications/docs/TR2013-071.pdf)
- [A Linear Regression and Markov Chain Model
For the Arabian Horse Registry](https://apps.dtic.mil/dtic/tr/fulltext/u2/a267097.pdf)

## Neural Networks
- [A visual proof that neural nets can compute any function](http://neuralnetworksanddeeplearning.com/chap4.html)

## Misc
[Latent Variable Models (lava)](https://github.com/kkholst/lava)
-[CMS at LHC](http://opendata.cern.ch/docs/observing-higgs-over-one-petabyte-new-cms-open-data)
The CMS Collaboration at CERN is pleased to announce the release of the third batch of high-level 
open data from the CMS detector at the Large Hadron Collider (LHC), available on the 
- [CERN Open Data portal](http://opendata.cern.ch/)
- [Toolkit for Multivariate Data Analysis with ROOT](https://root.cern.ch/tmva)
  - [TMVA Users Guide](https://root.cern.ch/download/doc/tmva/TMVAUsersGuide.pdf)
  - [TMVA Summary](https://root.cern.ch/tmva/summary)
  
- [ML cheat sheet](https://ml-cheatsheet.readthedocs.io/en/latest/index.html)
