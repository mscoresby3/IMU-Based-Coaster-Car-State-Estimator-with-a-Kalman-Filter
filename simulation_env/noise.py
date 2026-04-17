import numpy

def additive_noise(points: list, deviation: float = 0.5):
    points = points[:]
    
    mean = 0
    std_dev = deviation
    num_samples = len(points)

    noise_data = numpy.random.normal(mean, std_dev, num_samples)

    for i in range(len(points)):
        points[i] += noise_data[i]
    
    return points

def bias_noise(points: list, deviation: float = 0.1):
    points = points[:]
    
    mean = 0
    std_dev = deviation
    num_samples = len(points)

    noise_data = numpy.random.normal(mean, std_dev, num_samples)

    for i in range(len(points)):
        points[i] += sum(noise_data[:i])
    
    return points

def test():
    import matplotlib.pyplot as plt
    import physics_funcs

    x_points = physics_funcs.get_x(max=20)
    O_points = [0 for _ in range(len(x_points))]
    O_points_noise = additive_noise(O_points)
    O_points_bias = bias_noise(O_points)

    plt.plot(x_points, O_points, label='Actual')
    plt.plot(x_points, O_points_noise, label='Additive Noise')
    plt.plot(x_points, O_points_bias, label='Bias Noise')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    test()