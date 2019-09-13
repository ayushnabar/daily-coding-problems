def first_Recurring(string):
    temp = set()
    for c in string:
        if c in temp:
            return c
        temp.add(c)
    return None
