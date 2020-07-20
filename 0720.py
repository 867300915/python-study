def aa(str, substr):
    return str.replace(substr, "", str.count(substr)-1)


def bb(arr1, arr2):
    resultList = list(set(arr1+arr2))
    return resultList


print(aa("abcdedede", "de"))
print(bb([1, 2, 3, 4], [2, 3, 4, 5]))
