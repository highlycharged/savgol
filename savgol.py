import numpy as np
import pylab


def polyfit(x, y, yerr, degree):
    x0 = np.mean(x)
    weights = 1.0 / yerr
    coeff = np.polyfit(x - x0, y, degree, w = weights)
    y0 = coeff[-1]
    return (x0, y0)


def savgol(x, y, yerr, degree, points):
    indices = np.argsort(x)
    x_ = x[indices]
    y_ = y[indices]
    yerr_ = yerr[indices]
    N = len(x)
    K = N - points
    x_sg = np.ndarray(K)
    y_sg = np.ndarray(K)
    for i in range(K):
        i_begin = i
        i_end = i_begin + points
        x0, y0 = polyfit(x_[i_begin:i_end], y_[i_begin:i_end], yerr_[i_begin:i_end], degree)
        x_sg[i] = x0
        y_sg[i] = y0
    return (x_sg, y_sg)
        

def savgol2(x, y, yerr, degree, min_points, min_distance):
    N = len(x)
    y_sg = np.ndarray(N)
    for i in range(N):
        d = abs(x - x[i])
        indices = np.argsort(d)
        points = min_points
        while d[indices[points - 1]] < min_distance:
            points += 1
            if points >= N:
                points = N - 1
                break
        indices = indices[:points]
        x_ = x[indices] - x[i]
        y_ = y[indices]
        yerr_ = yerr[indices]
        weights = 1.0 / yerr_
        coeff = np.polyfit(x_, y_, degree, w = weights)
        yi = coeff[-1]
        y_sg[i] = yi
    return (x, y_sg)
        
            


N = 200
x = N * np.random.rand(N)
y = (0.5 * x / N) + np.sin(10.0 * x / N)
yerr = (np.ones_like(y) * 0.02) + (np.random.rand(N) * 0.1)
y += yerr * np.random.randn(N)
pylab.errorbar(x, y, yerr, fmt = 'o', zorder = 1)
x_sg, y_sg = savgol(x, y, yerr, 2, 10)
pylab.scatter(x_sg, y_sg, color = 'red', zorder = 2)
x_sg2, y_sg2 = savgol2(x, y, yerr, 2, 10, 10.0)
pylab.scatter(x_sg2, y_sg2, color = 'green', zorder = 3)
pylab.show()




    