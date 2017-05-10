import random
#打乱排序
list = [1,2,3,4,5,6,7,8,9]
random.shuffle(list)
print(list)
#冒泡排序
for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j]>list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]
print(list)