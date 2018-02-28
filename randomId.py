import random
import time


def idcard_generator():
    """ 随机生成新的18为身份证号码 """
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    t = time.localtime()[0]
    x = '%02d%02d%02d%04d%02d%02d%03d' % (random.randint(10, 99), random.randint(1, 99), random.randint(
        1, 99), random.randint(t - 80, t - 18), random.randint(1, 12), random.randint(1, 28), random.randint(1, 999))
    y = 0
    for i in range(17):
        y += int(x[i]) * ARR[i]
    IDCard = '%s%s' % (x, LAST[y % 11])
    # birthday = '%s-%s-%s 00:00:00' % (IDCard[6:14][0:4], IDCard[6:14][4: 6], IDCard[6:14][6:8])
    return IDCard


if __name__ == '__main__':
    with open('./file.txt', 'w') as f:
        f.write(idcard_generator())
