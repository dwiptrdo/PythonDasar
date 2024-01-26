# Operasi list

data_angka = [1,3,5,7,3,6,5,3,5,2,8,7,2,3,6,6,9,1,4,3]
print(f'data angka = \n{data_angka}')
# count data

jumlah_data_3 = data_angka.count(3)
jumlah_data_6 = data_angka.count(6)

print(f'jumlah data 3 = {jumlah_data_3}')
print(f'jumlah data 6 = {jumlah_data_6}')

# ambil posisi data (index)

data = ['Ali','Dodo','Putra','Aziz']
print(f'data = {data}')

index_dodo = data.index('Dodo')
index_aziz = data.index('Aziz')
print(f'index si Dodo = {index_dodo}')
print(f'index si Aziz = {index_aziz}')

# mengurutkan list
# int
print(f'data angka sebelum sort = \n{data_angka}')
data_angka.sort()
print(f'data angka sort = \n{data_angka}')

# str
print(f'data = {data}')
data.sort()
print(f'data sort = {data}')

# balik listnya
data_angka.reverse()
data.reverse()
print(f'data direverse = \n{data_angka} \n{data}')