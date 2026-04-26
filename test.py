def return_list(k=4):
    a = [[]] * k
    a[1].append(k)
    return a

def retur_correct(k=4):
    a = [[] for i in range(k)]
    a[1].append(k)
    return a

print(return_list())
print(retur_correct())