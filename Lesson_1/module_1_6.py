my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print('Dict:', my_dict)
print('Existing value:', my_dict['Masha'])
print('Not existing value:', my_dict.get('Misha'))
my_dict.update({'Kamila': 1981, 'Artem': 1915})
print('Deleted value:', my_dict.pop('Egor'))
print('Modified dictionary:', my_dict)
my_set = {1, 'Яблоко', 42.314}
print('Set:', my_set)
my_set.update({13, (5, 6, 1.6)})
my_set.remove(1)
print('Modified set:', my_set)
