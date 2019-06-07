# 递归求列表的和
def list_sum(lists):
    if len(lists) == 1:
        return lists[0]
    return lists[0] + list_sum(lists[1:])


print(list_sum([10, 20, 3]))

