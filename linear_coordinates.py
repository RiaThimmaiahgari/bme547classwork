def calculate_yval(tuple1, tuple2, x):
    slope = calculate_slope(tuple1, tuple2)
    intercept = calculate_intercept(tuple1, slope)
    y_val = (slope*x) + intercept
    return y_val

def calculate_slope(tuple1, tuple2):
    slope = (tuple2[1]-tuple1[1])/(tuple2[0]-tuple1[0])
    return slope

def calculate_intercept(tuple, slope):
    intercept = tuple[1] - (tuple[0]*slope)
    return intercept

#print(calculate_yval((3, 2), (1, 4), 2))