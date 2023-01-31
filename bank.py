def bank(a, years):
    if a == 0:
        return a
    for i in range(years):
        a *= 1.1
    return a
