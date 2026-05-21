import numpy

MAX = 30

def func_generator(func, step: float = 0.5, max: float = MAX):
    """
    To be used in a list comprehension
    func: lambda function
    step: how far to increase
    returns a generator
    """
    i = 0
    while i < max:
        yield func(i)
        i += step

# edit these functions
def angle(time):
    return numpy.sin( ( time / 4 ) ** 2)

def der_angle(time):
    return numpy.cos( (time / 4) ** 2) * (time / 8)

def acceleration(time):
    return numpy.sin(angle(time))

# don't touch these functions but feel free to use them


def get_time(step = 0.5, max = MAX):
    return [t for t in func_generator(lambda x: x, step, max)]

def get_acceleration(step = 0.5, max = MAX):
    return [a for a in func_generator(acceleration, step, max)]

def get_angle(step = 0.5, max = MAX):
    return [a for a in func_generator(angle, step, max)]

def get_der_angle(step = 0.5, max = MAX):
    return [d_a for d_a in func_generator(der_angle, step, max)]

if __name__ == "__main__":
    print('The code that is now running is for testing')

    import matplotlib.pyplot as plt

    step = 0.2

    time_points = get_time(step=step)
    acceleration_points = get_acceleration(step=step)
    angle_points = get_angle(step=step)
    der_angle_points = get_der_angle(step=step)

    plt.plot(time_points, acceleration_points, label='Acceleration')
    plt.plot(time_points, angle_points, label='Angle')
    plt.plot(time_points, der_angle_points, label="Angle'")
    plt.legend()
    plt.plot(time_points, [0 for _ in range(len(time_points))], color='k')
    plt.show()