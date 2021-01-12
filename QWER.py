import random

data = ["Q", "W", "E", "R"]

# 试验次数
time = 100000000

q=w=e=r=0

for i in range(0, time, 1):
    num = random.randint(0, 3)
    # print("第" + str(i + 1) + "次系统随机按的技能是" + str(data[num]) + "技能。")
    if num == 0:
        q = q + 1
    if num == 1:
        w = w + 1
    if num == 2:
        e = e + 1
    if num == 3:
        r = r + 1

print(str(time) + "次试验结束。")
print("Q技能被按" + str(q) + "次，频率为" + str(q / time)+"。")
print("W技能被按" + str(w) + "次，频率为" + str(w / time)+"。")
print("E技能被按" + str(e) + "次，频率为" + str(e / time)+"。")
print("R技能被按" + str(r) + "次，频率为" + str(r / time)+"。")
