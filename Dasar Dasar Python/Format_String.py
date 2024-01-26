# format string
# contoh generic
# string
nama = 'alfredo'
format_str = f'Halo {nama}'
print(format_str)

# angka
angka = 2005.5
format_str = f'angka {angka}'
print(format_str)

# boolean
boolean = False
format_str = f'bool {boolean}'
print(format_str)

# bilangan bulat
angka = 15
format_str = f'bilangan bulat {angka:d}'
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f'jutaan {angka:,}'
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f'desimal {angka:.2f}'
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f'desimal {angka:08.2f}'
print(format_str)

# menamilkan tanda + atau -
angka_mines = -10
angka_plus = +10.123
format_mines = f'mines = {angka_mines:+d}'
format_plus = f'plus = {angka_plus:+.2f}'
print(format_mines)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f'persen = {persentase:.2%}'
print(format_persen)

# melakukan operasi aritmatika di dalam placeholde
harga = 10000
jumlah = 5
format_string = f'harga total = {harga*jumlah:,}'
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f'binary = {bin(angka)}'
format_octal = f'octal = {oct(angka)}'
format_hex = f'hex = {hex(angka)}'

print(format_binary)
print(format_octal)
print(format_hex)


