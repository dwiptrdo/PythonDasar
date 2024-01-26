# kalkulator sederhana

print(10*'=' + 'Kalkulator Sederhana' + 10*'=' + '\n\n')

angka_1 = float(input('Masukan Angka Pertama : '))
angka_2 = float(input('Masukan Angka Kedua : '))
operator = input('Mau diapakan angka angka di atas? (+, -, x, /) : ')

if operator == '+':
    hasil = angka_1 + angka_2
    print(f'Hasilnya adalah {hasil}')
elif operator == '-':
    hasil = angka_1 - angka_2
    print(f'Hasilnya adalah {hasil}')
elif operator == 'x':
    hasil = angka_1 * angka_2
    print(f'Hasilnya adalah {hasil}')
elif operator == '/':
    hasil = angka_1 / angka_2
    print(f'Hasilnya adalah {hasil}')
else:
    print('Perhatikan pengisiiannya apakah sudah benar?')
print('Terimakasih Sudah Mencoba Kalkulator Sederhana!')