# looping dari list

# for loop
print('\nFor Loop')
kumpulan_angka = [1,5,3,8,3,2,5,1,5,7,4]

for angka in kumpulan_angka:
    print(f'angka = {angka}')

peserta = ['Ali', 'Dwi', 'Aziz', 'Putra']

for nama in peserta:
    print(f'nama = {nama}')

# for loop dan range
print('\nFor Loop and range')
kumpulan_angka = [10,9,2,5,6,3,7]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f'angka = {kumpulan_angka[i]}')

# while loop
print('\nWhile Loop')
kumpulan_angka = [10,9,2,5,6,3,7]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f'angka = {kumpulan_angka[i]}')
    i += 1

# list comprehension
print('\nList Comprehension')
data = ['Ali', 'Dwi', 'Aziz', 'Putra']

[print(f'data = {i}') for i in data]

angka = [10,9,2,5,6,3,7]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print('\nEnumerate')
data_list = ['Dodo', 1,2,3,'Ali']

for index,data in enumerate(data_list):
    print(f'index = {index}, data = {data}')