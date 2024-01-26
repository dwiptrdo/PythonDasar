# Date and Time

import datetime as dt

# contoh:
hari_ini = dt.date.today()
print(hari_ini)
print(f'hari ini adalah hari {hari_ini:%A}')

tanggal = dt.date(2006,4,10)
print(tanggal)
print(f'hari itu adalah hari {tanggal:%A}')

# aplikasi sederhana penghitung Umur

print('Masukan Tanggal, Bulan, dan Tahun anda')
tanggal = int(input('Tanggal \t:'))
bulan = int(input('Bulan \t\t:'))
tahun = int(input('Tahun \t\t:'))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f'Tanggal lahir anda adalah {tanggal_lahir}')

print(f'Hari ini tanggal {hari_ini}')
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30

print(f'Harinya adalah {tanggal_lahir:%A}')
print(f'Jumlah hari yang telah dilewati adalah {umur_hari}')
print(f'Umur anda adalah {umur_tahun}, Sisa bulan {umur_bulan}')

