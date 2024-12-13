def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

inner_function() #Ошибка NameError. Вне области функции test_function функция inner_function неопределена.