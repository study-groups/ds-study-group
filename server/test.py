from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from yellowbrick.regressor import residuals_plot

from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, shuffle=True)

model = LinearRegression()

viz = residuals_plot(model, X_train, y_train, X_test, y_test)
