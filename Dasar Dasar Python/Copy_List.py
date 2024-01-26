# Teknik menduplikat list

a = ['Aziz','Ali','Dwi']
print(f'a = {a}')

b = a # pass by reference
print(f'b = {b}')

# merubah data dari a
# ini akan merubah kedua list

a[1] = 'Fajar'
b.sort()
print(f'a = {a}')
print(f'b = {b}')

# address dari kedua list a dan b
print(f'address a = {hex(id(a))}')
print(f'address b = {hex(id(b))}')

# menduplikat list dengan copy

print('membuat list c dengan a.copy()')
c = a.copy() #full duplikat / data baru

print(f'address a = {hex(id(a))}')
print(f'address b = {hex(id(b))}')
print(f'address c = {hex(id(c))}')

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

print('kita ubah data 0')
c[0] = 'Munib'

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')


print('kita ubah data 1')
a[1] = 'Dodo'

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')


  