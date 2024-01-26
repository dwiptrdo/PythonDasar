# continue, pass, break

# pass --> dia berfungsi sebagai dummy, tidak akan di eksekusi


# angka = 0

# while angka <5:
#     angka += 1 
#     if angka == 3:
#         pass

#     print(angka)

# continue

angka = 0

print(f'angka sekarang {angka}')

while angka < 5:
    angka += 1
    print(f'angka sekarang {angka}') # aksi 1

    if angka == 3:
        print('nice!')
        continue # akan membuat loop loncat ke step selanjutanya

    print('haloo') # aksi 2

print('hebatt!')


# break
# contoh 1

angka = 0


while angka < 5:
    angka += 1
    print(f'angka sekarang {angka}') # aksi 1

    if angka == 3:
        print('nice!')
        break

    print('haloo') # aksi 2

print('hebatt!\n')


# contoh 2

data_int = int(input('hitung sampai : '))

angka = 0


while True:
    angka += 1
    print(f'angka sekarang {angka}') # aksi 1

    if angka == data_int:
        print('nice!')
        break

    print('haloo') # aksi 2

print('hebatt!')
