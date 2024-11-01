immutable_var = 1, 'd', True, [0, 1]
#immutable_var[1] = 2 выдаст ошибку
#Кортеж неизменяемый объект, изменить можно только элементы списка внутри кортежа.
immutable_var[3][0] = 3
print('Immutable tuple:', immutable_var)
mutable_list = [1, 'd', True, [0, 1]]
mutable_list[2] = False
mutable_list[0] = 'a'
print('Mutable list:', mutable_list)