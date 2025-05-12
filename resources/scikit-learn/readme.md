# Selected Scikit-learn examples

## Datasets

- [Data set loading examples](https://scikit-learn.org/stable/datasets/index.html#sample-generators): 
Includes toy data sets, real-world data sets including 20newsgroups labled faces, 
TCP/IP data and California housing. Also included are generators for classification, BiClusteing,
regression data and multi-label data.


## Regression

- [Plot Ridge alpha coefficients as a function of the L2 regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html#sphx-glr-auto-examples-linear-model-plot-ridge-coeffs-py)
Shows how each coefficient of independent variables vary with respect to alpha.

- [Effect of transforming he targets in regression model](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html#sphx-glr-auto-examples-compose-plot-transformed-target-py)

- [Robust linear model estimation using RANSAC](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ransac.html):
Shows how to robustly fit a linear model to faulty data using the RANSAC algorithm.

## Dimension reduction

- [Decomposing signals in components (matrix factorization problems)](https://scikit-learn.org/stable/modules/decomposition.html#decompositions)
Shows Exact PCA and probabilistic interpretation, Incremental PCA, Kernel PCA,  Truncated singular 
value decomposition and latent semantic analysis
  - [Latent Direchlet Allocation](http://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf) by Blei, Ng and Jordan. See section 4.4 for geometric
  interpretation.

- [Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#sphx-glr-auto-examples-text-plot-document-clustering-py)
Simple k-means clustering using TF-IDF on the 20Newsgroups data. Includes use of silhoutte score.

- [Topic extraction with Non-negative Matrix Factorization and Latent Dirichlet Allocation](https://scikit-learn.org/stable/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html#sphx-glr-auto-examples-applications-plot-topics-extraction-with-nmf-lda-py)
Non-negative Matrix Factorization is applied with two different objective functions: 
the Frobenius norm, and the generalized Kullback-Leibler divergence. 
The latter is equivalent to Probabilistic Latent Semantic Indexing.
