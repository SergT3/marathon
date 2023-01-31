def regrouper(the_list):
    length = len(list)
    if length == 0 or length == 1 or length == 2:
        return the_list
    result = []
    if length % 3 == 0:
        for j in range(3):
            temp = []
            for i in range(length // 3):
                temp.append(the_list[i + (length // 3 * j)])
            result.append(temp)
        return result
    if length % 3 == 2:
        for j in range(2):
            temp = []
            for i in range(length // 3):
                temp.append(the_list[i + (((length // 3) + 1) * j)])
            result.append(temp)
        temp = []
        for k in range(length % 3):
            temp.append(k + (((length // 3) + 1) * 2))
        result.append(temp)
    return result




