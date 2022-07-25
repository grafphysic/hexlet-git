def count_all(items):
    result = {}
    for item in items:
        if item not in result:
                result[item] = 1
        else:
                result[item] = result[item] + 1
    return result
