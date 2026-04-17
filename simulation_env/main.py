import matplotlib.pyplot as plt

import physics_funcs
import noise

def main():
    step = 0.5

    x_points = physics_funcs.get_x(step)
    height_points = physics_funcs.get_height(step)
    angle_points = physics_funcs.get_angle(step)
    acc_points = physics_funcs.get_acceleration(step)

    height_points_noise = noise.create_noise(height_points)
    angle_points_noise = noise.create_noise(angle_points)
    acc_points_noise = noise.create_noise(acc_points)

    plt.plot(x_points, height_points, label='Height')
    plt.plot(x_points, angle_points, label='Actual Angle')
    plt.plot(x_points, acc_points, label='Actual Acceleration')

    plt.plot(x_points, angle_points_noise, label='Noise Angle')
    plt.plot(x_points, acc_points_noise, label='Noise Acceleration')

    plt.ylim(-3, 7)
    plt.xlim(0, physics_funcs.MAX)
    plt.legend()
    plt.plot(x_points, [0 for _ in range(len(x_points))], color='k')
    plt.show()

if __name__ == "__main__":
    main()