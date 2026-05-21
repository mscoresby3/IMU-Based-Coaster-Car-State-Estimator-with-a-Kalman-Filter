import numpy

MAX = 20

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
    return numpy.cos( time ) + 0.5

# don't touch these functions but feel free to use them

def a_x(time):
    return acceleration(time) * numpy.cos( angle(time) )

def a_y(time):
    return acceleration(time) * numpy.sin( angle(time) )


def get_time(step = 0.5, max = MAX):
    return [t for t in func_generator(lambda x: x, step, max)]

def get_acceleration(step = 0.5, max = MAX):
    return [a for a in func_generator(acceleration, step, max)]

def get_angle(step = 0.5, max = MAX):
    return [a for a in func_generator(angle, step, max)]

def get_der_angle(step = 0.5, max = MAX):
    return [d_a for d_a in func_generator(der_angle, step, max)]

def get_x_and_y(step = 0.5, max = MAX):
    x = [0]
    y = [0]
    v_x = [0]
    v_y = [0]
    acc = get_acceleration(step=step, max=max)
    angle = get_angle(step=step, max=max)
    for i in range(len(acc) - 1):
        v_x.append(v_x[-1] + (acc[i] * numpy.cos(angle[i]) * step))
        v_y.append(v_y[-1] + (acc[i] * numpy.sin(angle[i]) * step))

        x.append(x[-1] + (v_x[-1] * step))
        y.append(y[-1] + (v_y[-1] * step))
    
    return x, y

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    step = 0.2

    time_points = get_time(step=step)
    acceleration_points = get_acceleration(step=step)
    angle_points = get_angle(step=step)
    der_angle_points = get_der_angle(step=step)
    x, y = get_x_and_y(step=step)

    plt.plot(time_points, acceleration_points, label='Acceleration')
    plt.plot(time_points, angle_points, label='Angle')
    plt.plot(time_points, der_angle_points, label="Angle'")
    plt.legend()
    plt.plot(time_points, [0 for _ in range(len(time_points))], color='k')
    plt.show()
    plt.clf()

    plt.plot(x, y)
    plt.scatter(x, y)
    plt.show()