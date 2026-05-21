import numpy

def acc_to_angle(acc_data):
    new_data = []
    for point in acc_data:
        new_data.append(numpy.arcsin(point))
    return new_data

def gyro_to_angle(gyro_data, step, start_angle = 0):
    new_data = []
    current_angle = start_angle
    for point in gyro_data:
        current_angle += point * step
        new_data.append(current_angle)
    return new_data