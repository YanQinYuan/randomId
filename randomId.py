import random
import time
import xlwt


def write_to_xls(data, time_num):
    """把结果写入xls文件"""
    # 创建 xls 文件对象
    wb = xlwt.Workbook()
    # 新增一个表单
    sh = wb.add_sheet('A Test Sheet', cell_overwrite_ok=True)
    # 方法一：按位置添加数据,用 zip 打包，同时遍历两个 list
    for i, j in zip(range(time_num), data):
        sh.write(i, 0, j)

    # 方法二：把 data 变成一个迭代器
    # data_g = (x for x in data) 
    # for i in range(time_num):
    #     sh.write(i, 0, next(data_g))

    # 保存文件
    wb.save('example.xls')


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

def generator_times(time_num=10):
    """默认生成10个身份证号码"""
    user_input = input("\n 请问这位兄贵，您想生成几个号码？\n \n>>>")
    time_num = int(user_input)
    id_num = 0
    list_num = []
    str = ","
    for i in range(time_num):
        id_num = idcard_generator()
        list_num.append(id_num)
    return list_num, time_num

# 保存到 txt 文件
# if __name__ == '__main__':
#     with open('./file.txt', 'w') as f:
#         f.write(generator_times())


# 保存到 xls 文件
if __name__ == '__main__':
    list_num, time_num = generator_times()
    print("\n 生成成功，请查看 example.xls 文件夹。")
    write_to_xls(list_num, time_num)
