## savgol.py 
## A variant of the Savitzky-Golay filter algorithm for arbitrarily spaced data points.

import numpy as np


def savgol(x, y, yerr, degree, min_points, min_distance, estimate_errors = True):
    """A variant of the Savitzky-Golay fiter algorithm for arbitrarily spaced data points.

    Args:
      x: abscissas of data points
      y: ordinates of data points
      yerr: 1-sigma uncertainties of ordinates of data points
      degree: degree of locally fitted polynomials
      min_points: minimum number of data points within each filter window
      min_distance: at least one data point shall be at least this far away in x within each filter window
      estimate_errors: if True, perform error propagation

    Returns:
      A tuple (x, y_filtered, yerr_filtered, chi2) with filtered abscissas (identical to input abscissas), fitered ordinates, corresponding 1-sigma uncertainties, and a chi-squared value.
      The chi-squared value can serve as an indicator for the quality of the filtering. A value close to 1.0 can be considered optimal.
    """
    N = len(x)
    y_sg = np.ndarray(N)
    yerr_sg = np.zeros_like(y_sg)
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
        if estimate_errors: 
            y_mod = y_.copy()
            for j in range(points):
                dy = 0.1 * yerr_[j]
                y_mod[j] += 0.5 * dy
                coeff_pos = np.polyfit(x_, y_mod, degree, w = weights)
                y_mod[j] -= dy
                coeff_neg = np.polyfit(x_, y_mod, degree, w = weights)
                y_mod[j] = y_[j]
                df_dy = (coeff_pos[-1] - coeff_neg[-1]) / dy
                yerr_sg[i] = np.hypot(yerr_sg[i], df_dy * yerr_[j])
    res = y - y_sg
    reserr = np.hypot(yerr, yerr_sg)
    chi2 = np.var(res / reserr)
    return (x.copy(), y_sg, yerr_sg, chi2)










    