# membuat gabungan area rentang dari angka
# +++3---10+++

inputUser = float(input('Masukan angka kurang dari 3 atau lebih dari 10 = '))

# +++3---
# memeriksa angka kurang dari 3
kurangDari = (inputUser < 3)
print('kurang dari 3 =', kurangDari)

# ---10+++
# memeriksa angka lebih dari 10
lebihDari = (inputUser > 10)
print('lebih dari 10 =', lebihDari)

# menggunakan OR

lebihBenar = kurangDari or lebihDari
print('hasil dari OR = ', lebihBenar)


# ---3+++10---
inputUser = float(input('Masukan angka lebih dari 3 atau kurang dari 10 = '))

# ---3+++
lebihDari = inputUser > 3
print('lebih dari 3 = ', lebihDari)

# +++10---
kurangDari = inputUser < 10
print('kurang dari 10 = ',kurangDari)

# menggunakan AND
lebihBenar = lebihDari and kurangDari
print('hasil dari AND', lebihBenar)

# PR
# ---0+++5---8+++11---
# +++0---5+++8---11+++

print('\n===PR===PR===\n')

print("GABUNGAN")
InputData = float(input("Masukkan Data : "))

Angka1 = (InputData >= 0 and InputData <= 5)
print(Angka1)

Angka2 = (InputData >= 8 and InputData <= 11)
print(Angka2)

Hasilnya = Angka1 or Angka2
print("Answer :",Hasilnya)

print("IRISAN")
InputData = float(input("Masukkan Data : "))

Angka1 = (InputData <= 0 or InputData >= 5)
print(Angka1)

Angka2 = (InputData <= 8 or InputData >= 11)
print(Angka2)

Hasilnya = Angka1 and Angka2
print("Answer :",Hasilnya)