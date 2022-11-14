# a = r ^ 2 mod p
# p is prime

def p_of_1_mod_8(a, p):
    e = 0
    while ((p - 1) % (1 << (e + 1))) == 0:
        e += 1
        q = (p - 1) // (1 << e)
    for x in range(2, p):
        z = pow(x, q, p)
        if pow(z, (1 << (e - 1)), p) != 1:
            break
    y = z
    r = e
    x = pow(a, (q - 1) // 2, p)
    v = (a * x) % p
    w = (v * x) % p
    while w != 1:
        k = 1
        while True:
            if pow(w, (1 << k), p) == 1:
                break
            k += 1
        d = pow(y, (2 ** (r - k - 1)), p)
        y = pow(d, 2, p)
        r = k
        v = (d * v) % p
        w = (w * y) % p
    return v

def p_of_5_mod_8(a, p):
    v = pow(a * 2, (p - 5) // 8, p)
    i = (2 * a * v * v) % p
    r = a * v * (i - 1)
    r = r % p
    return r

def modular_squrare_root(a, p):
    if (p % 4) == 3:
        r = pow(a, (p + 1) // 4, p)
    elif (p % 8) == 5:
        r = p_of_5_mod_8(a, p)
    elif (p % 8) == 1:
        r == p_of_1_mod_8(a, p)
    return r
