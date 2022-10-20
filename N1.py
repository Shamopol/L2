def palindrome(n):
    n_list = [int(d) for d in str(n)]
    return n_list == list(reversed(n_list))

print(palindrome(224))
print(palindrome(242))
print(palindrome(52325))
print(palindrome(21123))

