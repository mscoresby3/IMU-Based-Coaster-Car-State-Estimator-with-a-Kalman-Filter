import matplotlib.pyplot as plt
import numpy

MAX = 6.5

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
    return lambda x: -9.8 * numpy.sin(numpy.arctan(-0.75 * numpy.sin(x / 2)))

def acceleration_generator(step: float = 0.5):
    i = 0
    while i < MAX:
        yield acceleration_func()(i)
        i += step

def get_acceleration(step: float = 0.5):
    return [y for y in acceleration_generator(step)]


def main():
    step = 0.3
    x_points, y_points = get_x_y(step)
    acc_points = get_acceleration(step)
    # vec_points = get_velocity(step)

    plt.plot(x_points, y_points)
    plt.plot(x_points, acc_points)
    plt.ylim(0, 7)
    plt.xlim(0, 7)
    plt.show()

if __name__ == "__main__":
    main()