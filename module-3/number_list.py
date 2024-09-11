list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
# for i in range(len(list_)):
    # new_list.insert(0, list_[i])
for i in range(len(list_)):
    list_[i] = len(list_)-i
print(*new_list)


