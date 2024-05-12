# savgol
A variant of the Savitzky-Golay filter algorithm for arbitrarily spaced data points.


    savgol(x, y, yerr, degree, min_points, min_distance, estimate_errors=True)
        A variant of the Savitzky-Golay fiter algorithm for arbitrarily spaced data points.
        
        Args:
            x (array-like of float): abscissas of data points
            y (array-like of float): ordinates of data points
            yerr (array-like of float): 1-sigma uncertainties of ordinates of data points
            degree (int): degree of locally fitted polynomials
            min_points (int): minimum number of data points within each filter window
            min_distance (float): at least one data point shall be at least this far away in x within each filter window
            estimate_errors (bool): if True (default), perform error propagation
        
        Returns:
            A tuple (x, y_filtered, yerr_filtered, chi2) with filtered abscissas (identical to input abscissas), fitered ordinates, corresponding 1-sigma uncertainties, and a chi-squared value. The chi-squared value can serve as an indicator for the quality of the filtering. A value close to 1.0 can be considered optimal.
