# Data science Papers
A collection of papers and supporting material.

- [Least Squares Quantization in PCM](http://www-evasion.imag.fr/people/Franck.Hetroy/Teaching/ProjetsImage/2007/Bib/lloyd-1982.pdf). By SP Lloyd. First time k-means clustering was described (Voronoi tiling). PCM is Pulse Code Modulation.PCM converts an analog input to a digital output. It's an Analog to Digital (A/D) converter.
  - [ECE789 Chapter 2](https://web.njit.edu/~shi/courses/ECE789/ch2.pdf).
  Good lecture notes frow New Jersey Information Services and Technology on advanced statisical image processing with many tie-ins to data science. Chapter 2 describes PCM quantization and it's statistical analysis.
  - [EE 398 Quantization notes](https://web.stanford.edu/class/ee398a/handouts/lectures/05-Quantization.pdf). Bernd Girod's 
  class at Stanford. Great techncal explanation of Lloyd's algorithm (the basis of k-means clustering).

- [Predicting Good Probabilities with Supervised Learning](https://www.cs.cornell.edu/~alexn/papers/calibration.icml05.crc.rev3.pdf)
Paper by Alexandru Niculescu-Mizil and Rich Caruana from Cornell. 
Good overview of log-loss (the idea of mis-classifying labeled data).
  - [understanding-binary-cross-entropy-log-loss](https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-visual-explanation-a3ac6025181a)

- [A Mathematical Theory of Communications](http://math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf). Claude
Shannon's master work. Part 1: Discrete Noiseless Systems (first 18 pages) is quite tractable. Includes a
clear introduction to Markov Procceses.
  - [Andrew Ng's Notes on Markov decision processes](http://cs229.stanford.edu/notes/cs229-notes12.pdf) 
  - [Pavlov.js](https://github.com/NathanEpstein/Pavlov.js/) Pavlov.js uses Markov Decision Processes to implement reinforcement learning. It is written in C++ and compiled to JavaScript.

- [Predicting Good Probabilities With Supervised 
  Learning](https://www.cs.cornell.edu/~alexn/papers/calibration.icml05.crc.rev3.pdf) 
  By Alexandru Niculescu-Mizil. "We examine the relationship between the predictions
  made by different learning algorithms and
  true posterior probabilities

  - [Comparison of Calibration of Classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html#id2)

## B-list
- [Degrees of Freedom](http://www.nohsteachers.info/pcaso/ap_statistics/PDFs/DegreesOfFreedom.pdf) by Helen M. Waler. 
Presents t-statistic as a ratio of two circles on a plane in N dimensional space. Numerator is sample_mean - population_mean 
and denominator is the standard error, s, of the mean measurement. The fluctuation of this ratio from sample to
sample produces what is known as the t-distribution. (the distribution under the null hypothesis for a t-test).
