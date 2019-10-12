def diamond(n):
    if n < 0 or n % 2 == 0:
        return None
    k = 1
    star = "*"
    s = "*"
    result = ""
    while k <= n:
        result = result + s.center(n, " ").rstrip() + "\n"
        k = k + 2
        s = star * k
    k = k - 4
    s = star * k
    while k >= 1:
        result = result + s.center(n, " ").rstrip() + "\n"
        k = k - 2
        s = star * k
    return result
