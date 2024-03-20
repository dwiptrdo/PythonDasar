# fungsi dengan kembalian


# template fungsi dengan kembalian
# def nama_fungsi(argument):
#     badan fungsi
#     return output

# fungsi kuadrat

def kuadrat(angka):
    '''Fungsi Kuadrat'''
    hasil = angka**2
    return hasil

y = kuadrat(6)
print(y)

print(kuadrat(5))

z = 10 + kuadrat(4)
print(z)

# fungsi tambah

def tambah(angka1, angka2):
    '''fungsi return dengan multi input'''
    return angka1 + angka2


a = tambah(12, 8)
print(a)


# fungsi dengan return banyak

def operasi_matematika(angka_1, angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah, kurang, kali, bagi

ta, ku, ka, ba = operasi_matematika(9, 5)

print(f"hasil tambah = {ta}")
print(f"hasil kurang = {ku}")
print(f"hasil kali = {ka}")
print(f"hasil bagi = {ba}")
