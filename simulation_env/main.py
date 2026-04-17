import matplotlib.pyplot as plt

import physics_funcs
import noise

def main():
    step = 0.3

    x_points = physics_funcs.get_x(step)
    height_points = physics_funcs.get_height(step)
    angle_points = physics_funcs.get_angle(step)
    angle_rate_points = physics_funcs.get_der_angle(step)
    acc_points = physics_funcs.get_acceleration(step)
    vec_points = physics_funcs.get_velocity(step)

    angle_points_noise = noise.bias_noise(angle_rate_points, 0.05)
    acc_points_noise = noise.additive_noise(acc_points)

    fig, (col1_fig, col2_fig, col3_fig) = plt.subplots(1, 3, figsize=(18, 6))

    col1_fig.plot(x_points, vec_points, label='Velocity')

    col1_fig.plot(x_points, height_points, label='Actual Height')
    col1_fig.plot(x_points, acc_points, label='Actual Acceleration')
    col1_fig.plot(x_points, angle_points, label='Actual Angle')
    col1_fig.plot(x_points, angle_rate_points, label='Actual Angle Rate of Change')
    col1_fig.plot(x_points, [0 for _ in range(len(x_points))], color='k')
    col1_fig.set_title("Actual Physics States")
    col1_fig.legend(loc='upper right')

    col2_fig.plot(x_points, angle_points_noise, label='Noise Angle')
    col2_fig.plot(x_points, acc_points_noise, label='Noise Acceleration')
    col2_fig.plot(x_points, [0 for _ in range(len(x_points))], color='k')
    col2_fig.set_title("Sensor Noise")
    col2_fig.legend(loc='upper right')

    col3_fig.plot(x_points, [angle_rate_points[i] - angle_points_noise[i] for i in range(len(angle_rate_points))], label='Angle')
    col3_fig.plot(x_points, [acc_points[i] - acc_points_noise[i] for i in range(len(acc_points))], label='Acceleration')
    col3_fig.plot(x_points, [0 for _ in range(len(x_points))], color='k')
    col3_fig.set_title("Difference")
    col3_fig.legend(loc='upper right')

    for ax in [col1_fig, col2_fig, col3_fig]:
        ax.set_ylim(-3, 8)
        ax.set_xlim(0, physics_funcs.MAX)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()