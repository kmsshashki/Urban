call = 0
def count_calls():
    global call
    call += 1

def string_info(string):
    count_calls()
    result = tuple([len(string), string.upper(), string.lower()])
    return result

def is_contains(string, list_to_search):
    count_calls()
    list_to_search = [elem.upper() for elem in list_to_search]
    if string.upper() in list_to_search:
        return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(call)