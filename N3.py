def reverse(n):
    n_str = [d for d in str(n)]
    n_str.reverse()
    if n < 0:
        n_str.insert(0, n_str.pop())
        
    return (''.join(n_str))
print(reverse(int(input())))