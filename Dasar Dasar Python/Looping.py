# latihan perulangan membuat segitiga

sisi = 10

# 1. menggunakan For

# dummy variable

print('\nMenggunakan For')

count = 1

for i in range(sisi):
    print('*'*count)
    count += 1
print('End')


# 2. menggunakan While

print('\nMenggunakan While')

count = 1

while True:
    print('*'*count)
    count += 1

    if count > sisi:
        break

print('End')


# 3. hanya ganjil saja

print('\nMenggunakan While')

count = 1

while True:
    if (count%2):
        # print jika ganjil
        print('*'*count)
        count += 1
    else:
        # akan kembali keatas jika ganjil
        count += 1
        continue

    if count > sisi:
        break

print('End')


# 4. hanya ganjil saja dan menggunakannya untuk membuat segitiga sama kaki

print('\nMenggunakan While')

count = 1
spasi = int(sisi/2)

while True:
    if (count%2):
        # print jika ganjil
        print(' '*spasi,'*'*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali keatas jika ganjil
        count += 1
        continue

    if count > sisi:
        break

print('End')






















