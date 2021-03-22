
print('Welcome to the simple calculator.')
print('---')
print('This calculator needs two integers')
var1 = input('First integer: ')
var2 = input('Second integer: ')

result_add = int(var1) + int(var2)
result_sub = int(var1) - int(var2)
result_mul = int(var1) * int(var2)
result_div = int(var1) / int(var2)

print('---')
print(var1+' + '+var2+' = '+str(result_add))
print(var1+' - '+var2+' = '+str(result_sub))
print(var1+' * '+var2+' = '+str(result_mul))
print(var1+' / '+var2+' = '+str(result_div))
