import numpy

def additive_noise(points: list, deviation: float = 0.3, max = 1):
    """
    Takes in a list of points and add gaussain white noise to it
    """
    points = points[:]
    
    mean = 0
    std_dev = deviation
    num_samples = len(points)

    noise_data = numpy.random.normal(mean, std_dev, num_samples)

    for i in range(len(points)):
        points[i] += noise_data[i]
        if points[i] > max:
            points[i] = max
        elif points[i] < -1 * max:
            points[i] = -1 * max
    
    return points

def bias_noise(points: list, deviation: float = 0.1):
    """
    Takes in a list of points and adds gaussain white noise to it with a bias over time
    """
    points = points[:]
    
    mean = 0
    std_dev = deviation
    num_samples = len(points)

    noise_data = numpy.random.normal(mean, std_dev, num_samples)

    current = 0
    for i in range(len(points)):
        current += noise_data[i]
        points[i] += current
    
    return points

if __name__ == "__main__":
    print('The code that is now running is for testing')

    import matplotlib.pyplot as plt
    import physics_funcs

    x_points = physics_funcs.get_time(max=20)
    O_points = [0 for _ in range(len(x_points))]
    O_points_noise = additive_noise(O_points)
    O_points_bias = bias_noise(O_points)

    plt.plot(x_points, O_points, label='Actual')
    plt.plot(x_points, O_points_noise, label='Additive Noise')
    plt.plot(x_points, O_points_bias, label='Bias Noise')
    plt.legend()
    plt.show()