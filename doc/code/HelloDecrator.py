import random
from time import sleep, time


def calc_time(fun):

    def wrapper(*args, **kwargs):

        before = time()
        result = fun(*args, **kwargs)
        after = time()

        print("游戏时间", after - before)

        return result
    return wrapper


@calc_time
def play(t=3, level=20):

    print("小花正在打游戏%d" % level)

    sleep(t)

    print("游戏结束")

    return 'Happy'


def can_play(can):
    def can_play_wraper(fun):
        def wrapper():
            if random.randrange(10) > can:
                fun()
            else:
                print('do homework')
        return wrapper
    return can_play_wraper


@can_play(10)
def play_game():
    print("Happy to play")



if __name__ == '__main__':
    # play()

    # calc_time(play)

    # result = play(t=5, level=10)
    #
    # print(result)

    play_game()