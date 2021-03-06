r = [1, 1, 2]

def breed():
    global r
    
    iter = 0
    yield((iter, 1))                            # r[0]

    iter += 1
    yield(iter, 1)                            # r[1]

    iter += 1
    yield(iter, 2)                            # r[2]

    n = 1

    # r[3] ...
    while True:
        # Do the odd one first - R[2n + 1] = R[n - 1] + R[n] + 1
        value = r[n - 1] + r[n] + 1
        r.append(value)
        iter += 1
        yield(iter, value)

        n += 1

        # Next do the even one - R[2n] = R[n] + R[n + 1] + n
        value = r[n] + r[n + 1] + n
        r.append(value)
        iter += 1
        yield(iter, value)

def jtanswer(str_S):
    v = -1
    s = int(str_S)
    for (n, v) in breed():
        if (s == v):
            return n

def seekto(target):
    for (nn, vv) in breed():
        if vv == target:
            return (nn, vv)

if __name__ == '__main__':

    for it in breed():
        print it
        if it[0] > 99999999:
            break
