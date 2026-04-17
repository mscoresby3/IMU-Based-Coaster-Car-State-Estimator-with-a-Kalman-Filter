import matplotlib.pyplot as plt
import numpy

MAX = 10
g = 9.8

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

# These are the functions that need to be changed if needed
def height_func():
    return lambda x: 1.5 * (numpy.cos(x/2)+1)

def der_height_func():
    return lambda x: -0.75 * numpy.sin(x/2)

def doub_der_height_func():
    return lambda x: -0.375 * numpy.cos(x/2)

# These functions are not changed
def angle_func():
    return lambda x: numpy.arctan(der_height_func()(x))

def der_angle_func():
    return lambda x: doub_der_height_func()(x) / ( ( der_height_func()(x) ** 2 ) + 1 )

def acceleration_func():
    return lambda x: g * numpy.sin(-angle_func()(x))

def velocity_func():
    return lambda x: numpy.sqrt((2 * g * height_func()(0)) - (2 * g * height_func()(x)))

# use these functions
def get_x(step: float = 0.5, max: float = MAX):
    return [x for x in func_generator(lambda x: x, step, max=max)]

def get_height(step: float = 0.5, max: float = MAX):
    return [h for h in func_generator(height_func(), step, max=max)]

def get_der_height(step: float = 0.5, max: float = MAX):
    return [d_h for d_h in func_generator(der_height_func(), step, max=max)]

def get_angle(step: float = 0.5, max: float = MAX):
    return [a for a in func_generator(angle_func(), step, max=max)]

def get_der_angle(step: float = 0.5, max: float = MAX):
    return [d_a for d_a in func_generator(der_angle_func(), step=step, max=max)]

def get_acceleration(step: float = 0.5, max: float = MAX):
    return [y for y in func_generator(acceleration_func(), step, max=max)]

def get_velocity(step: float = 0.5, max: float = MAX):
    return [v for v in func_generator(velocity_func(), step, max=max)]


def test():
    step = 0.3
    x_points = get_x(step)
    height_points = get_height(step)
    d_h_points = get_der_height(step)
    angle_points = get_angle(step)
    der_angle_points = get_der_angle(step)
    acc_points = get_acceleration(step)
    vec_points = get_velocity(step)

    plt.plot(x_points, height_points, label='Height')
    plt.plot(x_points, d_h_points, label='Derivative of Height')
    plt.plot(x_points, angle_points, label='Angle')
    plt.plot(x_points, der_angle_points, label='Derivative of Angle')
    plt.plot(x_points, acc_points, label='Acceleration')
    plt.plot(x_points, vec_points, label='Velocity')
    plt.ylim(-3, 8)
    plt.xlim(0, MAX)
    plt.legend()
    plt.plot(x_points, [0 for _ in range(len(x_points))], color='k')
    plt.show()

if __name__ == "__main__":
    test()