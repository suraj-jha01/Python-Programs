ms =input('enter martial status:')
s = input ('enter sex:')
age =int(input('enter age:'))
if (ms == 'm') or (ms == 'u' and s == 'm' and age>30)\
    or(ms == 'u' and s == 'f' and age>25):
    print('insured')
else:
    print('not insured')
