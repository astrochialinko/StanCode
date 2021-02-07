from robot import Robot, Robot2, Robot3
from campy.graphics.gwindow import GWindow


def main():

    w = GWindow()

    # r1 = Robot(183, 70, color='magenta')
    # ball1 = r1.give_me_a_ball(100)
    # w.add(ball1, 200, 100)
    # r1.self_intro()
    # r1.bmi()
    # r1.say_hi()
    #
    # r2 = Robot(160, 45, color='navy')
    # r2.self_intro()
    # r2.bmi()
    # r2.say_hi()
    #
    # Robot.say_hi()

    robot2_1 = Robot2(183, 70, color2='megenta', count2=10)
    robot2_1.start_count()
    robot2_1.say_hi()
    robot2_1.bmi()

    robot3 = Robot3(170, 65, 'tomato', color3='red', count3=100)
    robot3.self_intro()
    robot3.bmi()
    ball3 = robot3.give_me_a_ball(100)
    rect3 = robot3.give_me_a_rect(100)
    w.add(rect3)
    w.add(ball3, 150, 200)


if __name__ == '__main__':
    main()