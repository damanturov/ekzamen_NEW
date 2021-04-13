def func_list(*args):
    return ['Element', 'start', *args, 'finish']
print(func_list(*['Hello', 5, 'go']))
