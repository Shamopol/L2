def newton(n, eps=0.001):
    a = float(n)
    prev_x = n
    while True:
        new_x = 0.5 * (prev_x + a / prev_x)
        if abs(new_x - prev_x) < eps:
            break
        prev_x = new_x
    return new_x
    
print(newton(int(input())))