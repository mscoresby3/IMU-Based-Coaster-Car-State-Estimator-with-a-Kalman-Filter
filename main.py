import matplotlib.pyplot as plt

import simulation_env.physics_funcs as physics_funcs
import simulation_env.noise as noise

import filters.raw_data as raw_data
from filters.complementary_filter import complementary_filter

def main(step, comp_ratio):
    time_points = physics_funcs.get_time(step=step)
    acceleration_points = physics_funcs.get_acceleration(step=step)
    angle_points = physics_funcs.get_angle(step=step)
    der_angle_points = physics_funcs.get_der_angle(step=step)

    der_angle_points_noise = noise.bias_noise(der_angle_points, step / 3)
    acceleration_points_noise = noise.additive_noise(acceleration_points)

    acc_angle_points = raw_data.acc_to_angle(acceleration_points_noise)
    gyro_angle_points = raw_data.gyro_to_angle(der_angle_points_noise, step)
    comp_filter_points = complementary_filter.filter_list(acceleration_points_noise, der_angle_points_noise, step, ratio=comp_ratio)

    fig, ((row1_col1_fig, row1_col2_fig, row1_col3_fig), (row2_col1_fig, row2_col2_fig, row2_col3_fig)) = plt.subplots(2, 3, figsize=(18, 12))

    row1_col1_fig.plot(time_points, acceleration_points, label='Accleration')
    row1_col1_fig.plot(time_points, der_angle_points, label='Deriviative of Angle')
    row1_col1_fig.set_title('Real data')
    row1_col1_fig.legend()

    row1_col2_fig.plot(time_points, acceleration_points_noise, label='Noise Accleration')
    row1_col2_fig.plot(time_points, der_angle_points_noise, label='Noise Deriviative of Angle')
    row1_col2_fig.set_title('Noise data')
    row1_col2_fig.legend()

    row1_col3_fig.plot(time_points, [acceleration_points_noise[i] - acceleration_points[i] for i in range(len(acceleration_points))], label='Accleration')
    row1_col3_fig.plot(time_points, [der_angle_points_noise[i] - der_angle_points[i] for i in range(len(der_angle_points))], label='Angle')
    row1_col3_fig.plot(time_points, [0 for _ in range(len(time_points))], color='k')
    row1_col3_fig.set_ylim(-1, 1)
    row1_col3_fig.set_title('Difference')
    row1_col3_fig.legend()

    row2_col1_fig.plot(time_points, angle_points, label='Angle')
    row2_col1_fig.set_ylim(-1.5, 1.5)
    row2_col1_fig.set_title('Actual Angle')
    row2_col1_fig.legend()

    row2_col2_fig.plot(time_points, acc_angle_points, label='Accelerometer')
    row2_col2_fig.plot(time_points, gyro_angle_points, label='Gyroscope')
    row2_col2_fig.plot(time_points, comp_filter_points, label='Complementary Filter')
    row2_col2_fig.set_ylim(-1.5, 1.5)
    row2_col2_fig.set_title('Filters')
    row2_col2_fig.legend()

    row2_col3_fig.plot(time_points, [acc_angle_points[i] - angle_points[i] for i in range(len(angle_points))], label='Accelerometer')
    row2_col3_fig.plot(time_points, [gyro_angle_points[i] - angle_points[i] for i in range(len(angle_points))], label='Gyroscope')
    row2_col3_fig.plot(time_points, [comp_filter_points[i] - angle_points[i] for i in range(len(angle_points))], label='Complementary filter')
    row2_col3_fig.set_ylim(-1.5, 1.5)
    row2_col3_fig.set_title('Filters Diff')
    row2_col3_fig.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main(0.05, 0.9)