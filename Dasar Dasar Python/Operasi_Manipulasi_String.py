# oprasi dan manipulasi string
# 1. menyambung string (concatenate)

nama_pertama = 'Alfredo'
nama_tengah = 'Dwi'
nama_akhir = 'Putra'

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 3. operator untuk string
# mengecek apakah ada komponen char atau string di string
a = 'a'
status = a in nama_lengkap
print('string ' + a + ' ada di ' + nama_lengkap + ' = ' + str(status))

# kebalikan
a = 'a'
status = a not in nama_lengkap
print('string ' + a + ' ada di ' + nama_lengkap + ' = ' + str(status))

# mengulang string
print('wk'*10)
print(11*'wk')

# indexing
print('index ke-0 : ' + nama_lengkap[0])
print('index ke-[0:6] : ' + nama_lengkap[0:7]) # yang diambil index 0 sampai  tapi ditulisnya [0:7]
print('index ke-[0,2,4,6,8,10] : ' + nama_lengkap[0:11:2]) # diambil dengan diloncatin 2

# item paling kecil
print('yang paling kecil = ' + min(nama_lengkap))

# item paling besar
print('yang paling besar = ' + max(nama_lengkap))

ascii_code = ord(' ')
print('ascii code untuk spasi adalah = ' + str(ascii_code))
data = 118
print('char untuk ascii 118 adalah ' + chr(data))

# 4. operator dalam bentuk method
data = 'alfredo dwi putra'
jumlah = data.count(a)
print('jumlah a pada ' + data + ' ' + str(jumlah))

# operator dalam bentuk methods
# merubah case dari string
# merubah semua ke uppercase

salam = 'haii!'
print('normal = ' + salam)
salam = salam.upper()
print('upper = ' + salam)

# merubah semua ke lower case
santai = 'AkU hEBat!'
print('normal = ' + santai)
santai = santai.lower()
print('lower = ' + santai)

# pengecekan dengan isX method
# contoh pengecekan lower case
salam = 'haloo'
apakah_lower = salam.islower() #hasilnya boolean
print(salam + ' is lower = ' + str(apakah_lower))
apakah_upper = salam.isupper() #hasilnya boolean
print(salam + ' is upper = ' + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- untuk angka saja
# isspace() <-- spasi, tab,  newline \n
# istitle() <-- semua kata dimulai dengan huruf besar

# isalpha:
apakahAlpha = salam.isalpha()
print(salam + ' is alpha = ' + str(apakahAlpha))

# istitle:
judul = 'String' # agar hasilnya True maka setiap awalan huruf harus kapital contoh: 'Malin Kundang'
is_judul = judul.istitle() # hasilnya boolean
print(judul + ' is title = ' + str(is_judul))

# mengecek komponen starswitch() endswitch()
# harus diperhatikan upper dan lower casenya
cek_start = 'Siap Mulai'.startswith('Siap')
print('start = ' + str(cek_start))

cek_end = 'Siap Mulai'.endswith('Mulai')
print('end = ' + str(cek_end))

# penggabungan komponen join() split()
# join()
pisah = ['I','Love','You'] # data list
gabung = ' '.join(pisah) # didalam single quote bisa diberikan apa saja
print('List ',pisah)
print('Join = ',gabung)
# split()
gabung = 'I Love You'
print('Split = ' + str(gabung.split(' '))) # jika di split maka akan kembali menjadi list

# alokasi karakter rjust(), ljust(), center()

kanan = 'kanan'.rjust(10, '=') # jika ingin tandanya selain spasi maka tambahkan argument lainnya
print("'" + kanan + "'")

kiri = 'kiri'.ljust(10)
print("'" + kiri + "'")

tengah = 'tengah'.center(10)
print("'" + tengah + "'")

# kebalikannya strip()
tengah = tengah.strip(' ') # untuk menghilangkan tanda/spasi
print("'" + tengah + "'")







