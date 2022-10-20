def div(n, d):
    return [num for num in n if num % d == 0]
num_list = [335, 339, 336, 500, 552, 555, 999, 995, 992]
print('Делятся на 2: ')  
print(div(num_list, 2))
print('Делятся на 3: ')  
print(div(num_list, 3))
print('Делятся на 5: ')  
print(div(num_list, 5))

