#p25 is first quartile (25th percentile)
#p75 is third quartile (75th percentile)


def inside_2(l1, l2, u1, u2, p25, p75):
    l = 0
    u = 0
    if l1 >= p25:
        if l2 <= p75:
            l = l2 - l1
        else:
            l = p75 - l1
    else:
        if l2 <= p75 and l2 >= p25:
            l = l2 - p25
    if u2 <= p75:
        if u1 >= p25:
            u = u2 - u1
        else:
            u = u2 - p25
    else:
        if u1 >= p25 and u1 <= p75:
            u = p75 - u1
    t = l + u
    return t

def inside_1(l, u, p25, p75):
    t = 0
    if l >= p25:
        if u <= p75:
            t = u - l
        else:
            t = p75 - l
    else:
        if u <= p75 and u >= p25:
            t = u - p25
    return t

def highway(p25, p75):
    iqr = p75 - p25
    ng = inside_2(0, 40, 115, 200, p25, p75) / iqr
    s = inside_2(40, 55, 105, 115, p25, p75) / iqr
    g = inside_2(55, 70, 95, 115, p25, p75) / iqr
    e = inside_1(70, 95, p25, p75) / iqr
    stat = max(ng, s, g, e)
    if stat == ng:
        print("not good")
    elif stat == s:
        print("satisfactory")
    elif stat == g:
        print("good")
    else:
        print("excellent")

def city(p25, p75):
    iqr = p75 - p25
    ng = inside_1(70, 200, p25, p75) / iqr
    s = inside_1(60, 70, p25, p75) / iqr
    g = inside_2(0, 20, 50, 60, p25, p75) / iqr
    e = inside_1(20, 50, p25, p75) / iqr
    stat = max(ng, s, g, e)
    if stat == ng:
        return("not good")
    elif stat == s:
        return("satisfactory")
    elif stat == g:
        return("good")
    else:
        return("excellent")

