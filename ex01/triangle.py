def is_triangle(a, b, c):
    if a < b + c and b < a + c and c < b + a:
        if a > 0 and b > 0 and c > 0:
            return True
    return False
