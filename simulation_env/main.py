import matplotlib.pyplot as plt

import physics_funcs
import noise

def main(step):
    time_points = physics_funcs.get_time(step=step)
    acceleration_points = physics_funcs.get_acceleration(step=step)
    # angle_points = physics_funcs.get_angle(step=step)
    der_angle_points = physics_funcs.get_der_angle(step=step)
    x, y = physics_funcs.get_x_and_y(step=step)

    der_angle_points_noise = noise.bias_noise(der_angle_points)
    acceleration_points_noise = noise.additive_noise(acceleration_points)

    fig, (col1_fig, col2_fig, col3_fig) = plt.subplots(1, 3, figsize=(18, 6))

    col1_fig.plot(time_points, acceleration_points, label='Accleration')
    col1_fig.plot(time_points, der_angle_points, label='Deriviative of Angle')
    col1_fig.set_title('Real data')
    col1_fig.legend()

    col2_fig.plot(time_points, acceleration_points_noise, label='Noise Accleration')
    col2_fig.plot(time_points, der_angle_points_noise, label='Noise Deriviative of Angle')
    col2_fig.set_title('Noise data')
    col2_fig.legend()

    col3_fig.plot(time_points, [acceleration_points_noise[i] - acceleration_points[i] for i in range(len(acceleration_points))], label='Accleration')
    col3_fig.plot(time_points, [der_angle_points_noise[i] - der_angle_points[i] for i in range(len(der_angle_points))], label='Angle')
    col3_fig.set_title('Difference')
    col3_fig.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main(0.2)