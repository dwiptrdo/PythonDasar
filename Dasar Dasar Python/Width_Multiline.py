# width and multiline

# data
data_nama = 'Alfredo'
data_umur = 17
data_tinggi = 163.2
data_nomor_sepatu = 43

# string standard
data_string = f'nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}'
print(data_string)
print('\n')

# string multiline (dengan menggunakan enter \n)
data_string = f'nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}'
print(data_string)

# string multiline (kutip tiga)
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print(data_string)

# mengatur lebar
data_nama = 'Alfre'
data_string = f"""
nama = {data_nama:>5} 
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print(data_string)






