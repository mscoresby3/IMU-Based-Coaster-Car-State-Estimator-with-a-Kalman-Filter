import matplotlib.pyplot as plt
import numpy

MAX = 10

def func():
    return lambda x: 1.5 * (numpy.cos(x/2)+1)

def func_generator_x(step: float = 0.5):
    i = 0
    while i < MAX:
        yield func()(i)
        i += step

def func_generator_y(step: float = 0.5):
    i = 0
    while i < MAX:
        yield i
        i += step

def get_x_y(step: float = 0.5):
    return [x for x in func_generator_y(step)], [y for y in func_generator_x(step)]

def acceleration_func():
    return lambda x: 9.8 * numpy.sin(numpy.arctan(0.75 * numpy.sin(0.5 * x)))

def acceleration_generator(step: float = 0.5):
    i = 0
    while i < MAX:
        yield acceleration_func()(i)
        i += step

def get_acceleration(step: float = 0.5):
    return [y for y in acceleration_generator(step)]

def velocity_func():
    return lambda x: numpy.sqrt((1.5 * (numpy.cos(0/2)+1)) - 1.5 * (numpy.cos(x/2)+1))

def velocity_generator(step: float = 0.5):
    i = 0
    while i < MAX:
        yield velocity_func()(i)
        i += step

def get_velocity(step: float = 0.5):
    return [v for v in velocity_generator(step)]

def main():
    step = 0.3
    x_points, y_points = get_x_y(step)
    acc_points = get_acceleration(step)
    vec_points = get_velocity(step)

    plt.plot(x_points, y_points, label='Height')
    plt.plot(x_points, acc_points, label='Acceleration')
    plt.plot(x_points, vec_points, label='Velocity')
    plt.ylim(-3, 7)
    plt.xlim(0, MAX)
    plt.legend()
    plt.plot(x_points, [0 for _ in range(len(y_points))], color='k')
    plt.show()

if __name__ == "__main__":
    main()