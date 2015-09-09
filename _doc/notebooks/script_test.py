
def big_list1(n):
    l = []
    for i in range(n):
        l.append(i)
    return l


def big_list2(n):
    return list(range(n))


def big_list(n):
    big_list1(n)
    big_list2(n)
