## operasi

# index 0, 1, 2, dst
data = ['Dodo', 'Fajar', 'Munib']

# mengambil data dari list ini
data_0 = data[0]
print(f'data pertama (index 0) = {data_0}')

data_terakhir = data[-1]
print(f'data terakhir adalah = {data_terakhir}')

data_dodo = data[-3]
print(f'data Dodo = {data_dodo}')

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f'panjang data = {panjang_data}')

## manipulasi data list

# menambahkan item pada list sesuai posisi
print(f'data sebelum ditambah = \n{data}')

data.insert(1, 'Ali')
print(f'data sesudah ditambah = \n{data}')

# menambah di akhir list
data.append('Aziz')
print(f'data ditambah lagi = \n{data}')

# menambah list dengan list
data_baru = ['Farikhul', 'Rohman', 'Dwi']
data.extend(data_baru)
print(f'data gabungan = \n{data}')


# merubah data
# kita ubah data 2 menjadi Putra

data[2] = 'Putra'
print(f'data ubah = \n{data}')

# meremove data
data.remove('Aziz')
print(f'data remove = \n{data}')
# data.remove('aziz') akan error karena huruf harus sesuai yaitu ('Aziz)

# meremove data paling belakang
data_akhir = data.pop()
print(f'data akhir =\n{data}')

print(f'data yang dihapus = {data_akhir}')