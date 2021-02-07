from campy.graphics.gobjects import GOval, GRect


class Robot:

    def __init__(self, height, weight, color='green'):
        self.h = height
        self.w = weight
        self.c = color

    def give_me_a_ball(self, size):
        ball = GOval(size, size)
        ball.color = self.c
        ball.filled = True
        ball.fill_color = ball.color
        return ball

    def self_intro(self):
        print(f'h={self.h}/w={self.w}')

    def bmi(self):
        height_in_meter = self.h/100
        print('bmi:', self.w/(height_in_meter**2))

    @staticmethod
    def say_hi():
        print('Hi')


class Robot2(Robot):
    def __init__(self, height2, weight2, color2='green', count2=3):
        super().__init__(height2, weight2, color=color2)
        self.count2=count2

    def start_count(self):
        for i in range(self.count2):
            print(i+1, end='...')
        print('')


class Robot3(Robot2):
    def __init__(self, height3, weight3, rect_color3, color3='green', count3=3):
        super().__init__(height3, weight3, color2=color3, count2=count3)
        self.r_c = rect_color3

    def give_me_a_rect(self, size):
        rect = GRect(size, size)
        rect.filled = True
        rect.fill_color = self.r_c
        return rect


if __name__ == '__main__':
    print('I am using robot.py')

if __name__ == 'robot':
    print('Thanks for using robot.py')
