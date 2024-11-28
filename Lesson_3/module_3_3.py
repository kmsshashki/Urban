def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(4, 6, 4)
print_params('one', 'two')
print_params(False)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [55.5, {4, 5, 6}, {'e': 1, 'n': '2', 'd': [3]}]
values_dict = {'a':False, 'b':(2, 3, 4), 'c':'Задача'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)