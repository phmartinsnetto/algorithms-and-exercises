def bubble_sort(list):
    end = len(list)
    for i in range(end-1, 0, -1):
        switched = False
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                switched = True
                print(list)
        if not switched:
            return list
    return list
