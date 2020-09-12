import numpy as np

# Set nr.1
# y_ = [17.8, 39.0, 12.8, 24.2, 17.2]
# x_ = [13.7, 23.2, 6.9, 16.8, 12.3]

# set nr.2
y_ = [0.4621, -0.0618, 0.0804, 0.2287, 0.4590, 0.2032, 0.4120, -0.0953, -0.1775, -0.4306]
x_ = [0.1574, -0.0340, 0.1830, 0.0835, 0.0665, 0.1245, -0.0219, 0.0744, 0.0555, 0.1027]


class Calc:

    def __init__(self, x, y):

        # observations
        self.obs = np.size(x)

        # x
        self.x = np.array(x)
        self.ra_x = self.arithmetic_mean(x=self.x)
        self.rg_x = self.geometric_mean(x=self.x)
        self.x_mean_x = self.x_meanx(x=self.x, mean=self.ra_x)
        self.variance_x = self.sample_var(x_mean_x=self.x_mean_x)
        self.variance_std_x = self.sample_var_std(sample_var=self.variance_x)

        # y
        self.y = np.array(y)
        self.ra_y = self.arithmetic_mean(x=self.y)
        self.rg_y = self.geometric_mean(x=self.y)
        self.y_mean_y = self.x_meanx(x=self.y, mean=self.ra_y)
        self.variance_y = self.sample_var(x_mean_x=self.y_mean_y)
        self.variance_std_y = self.sample_var_std(sample_var=self.variance_y)

        # xy
        self.covariance = self.covariance_calc()
        self.correlation = self.correlation_calc()

        # beta
        self.beta = self.beta_calc()

        # alpha
        self.alpha = self.alpha_calc()

        # skewness
        self.skewness = self.skewness_calc(y_mean_y=self.y_mean_y, sigma=self.variance_y)

        # kurtosis
        self.kurtosis = self.kurtosis_calc(y_mean_y=self.y_mean_y, sigma=self.variance_y)
        self.excess_kurt = self.kurtosis - 3

    def arithmetic_mean(self, x):
        sum_x = np.sum(x)
        return sum_x * 1/self.obs

    def geometric_mean(self, x):
        return np.product(x)**(1/self.obs) - 1

    def sample_var(self, x_mean_x):
        return np.sum(x_mean_x**2) / (self.obs - 1)

    def sample_var_std(self, sample_var):
        return sample_var**(1/2)

    def covariance_calc(self):
        return np.sum(np.multiply(self.x_mean_x, self.y_mean_y)) / (self.obs - 1)

    def correlation_calc(self):
        return self.covariance / (self.variance_std_x * self.variance_std_y)

    def x_meanx(self, x, mean):
        return x - mean

    def beta_calc(self):
        top = np.sum(np.multiply(self.x, self.y)) - self.obs * self.ra_x * self.ra_y
        bottom = np.sum(self.x**2) - self.obs * self.ra_x**2
        return top / bottom

    def alpha_calc(self):
        return self.ra_y - self.beta * self.ra_x

    def skewness_calc(self, y_mean_y, sigma):
        return (1/(self.obs - 1)) * np.sum(y_mean_y**3) / sigma**(3/2)

    def kurtosis_calc(self, y_mean_y, sigma):
        return (1/(self.obs - 1)) * np.sum(y_mean_y**4) / sigma**2


calc = Calc(x=x_, y=y_)

print("(x) Arithmetic mean      : {}\n".format(calc.ra_x) +
      "(x) Sample Variance      : {}\n".format(calc.variance_x) +
      "(x) Sample Variance std  : {}\n".format(calc.variance_std_x))

print( "(y) Arithmetic mean      : {}\n".format(calc.ra_y) +
      "(y) Sample Variance      : {}\n".format(calc.variance_y) +
      "(y) Sample Variance std  : {}\n".format(calc.variance_std_y))

print("(xy) Covariance          : {}\n".format(calc.covariance) +
      "(xy) Correlation         : {}\n".format(calc.correlation))

print("(b) Beta                 : {}\n".format(calc.beta) +
      "(a) Alpha                : {}\n".format(calc.alpha))

print("(skew) Skewness          : {}\n".format(calc.skewness) +
      "(kurt) kurtosis          : {}\n".format(calc.kurtosis) +
      "(kurt-3) excess kurtosis : {}".format(calc.excess_kurt))
