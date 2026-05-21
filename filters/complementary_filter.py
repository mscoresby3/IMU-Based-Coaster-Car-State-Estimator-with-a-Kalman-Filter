import numpy

class complementary_filter:
    
    @staticmethod
    def get_angle_from_acc(acc_data):
        return numpy.arcsin(acc_data)
    
    @staticmethod
    def filter_list(acc_points: list, gyro_points: list, step, ratio: float = 0.98) -> list:
        filter = complementary_filter(acc_points[0])
        angle_data = [filter.angle]
        for i in range(1, len(acc_points)):
            angle_data.append(filter.step(gyro_points[i], acc_points[i], step, ratio=ratio))
        return angle_data

    def __init__(self, acc_data):
        self.angle = complementary_filter.get_angle_from_acc(acc_data)

    def step(self, gyro_data, acc_data, step, ratio: float = 0.98):
        assert 0 <= ratio and ratio <= 1, f'ratio out of bounds: {ratio}'
        self.angle = ratio * (self.angle + gyro_data * step) + (1 - ratio) * complementary_filter.get_angle_from_acc(acc_data)
        return self.angle

if __name__ == "__main__":
    print('The code that is now running is for testing')