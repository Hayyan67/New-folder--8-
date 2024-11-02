class employee:
    def __init__(self):
        print('EMPLOYEE CREATED')

def create_obj():
    print('Making object...')
    obj = employee()
    print('Function end...')
    return obj

print('Callin Create_obj() function...')
obj = create_obj()
print('Program End...')