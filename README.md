# savgol
A variant of the Savitzky-Golay filter algorithm for arbitrarily spaced data points.


    savgol(x, y, yerr, degree, min_points, min_distance, estimate_errors=True)
        A variant of the Savitzky-Golay fiter algorithm for arbitrarily spaced data points.
        
        Args:
            x: abscissas of data points
            y: ordinates of data points
            yerr: 1-sigma uncertainties of ordinates of data points
            degree: degree of locally fitted polynomials
            min_points: minimum number of data points within each filter window
            min_distance: at least one data point shall be at least this far away in x within each filter window
            estimate_errors: if True, perform error propagation
        
        Returns:
            A tuple (x, y_filtered, yerr_filtered, chi2) with filtered abscissas (identical to input abscissas), fitered ordinates, corresponding 1-sigma uncertainties, and a chi-squared value. The chi-squared value can serve as an indicator for the quality of the filtering. A value close to 1.0 can be considered optimal.
