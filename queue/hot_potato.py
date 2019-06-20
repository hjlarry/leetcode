"""
故事讲的是，他和他的39个战友被罗马军队包围在洞中。他们决定宁愿死，也不成为罗马人的奴隶。
他们围成一个圈，其中一人被指定为第一个人，顺时针报数到第七人，就将他杀死。
约瑟夫斯是一个成功的数学家，他立即想出了应该坐到哪才能成为最后一人。
"""
from adt import ArrayQueue


def hot_potato(namelist, num):
    simqueue = ArrayQueue(10)
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
