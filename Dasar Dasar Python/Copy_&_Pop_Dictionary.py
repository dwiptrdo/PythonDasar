## Copy dictionary

teman_teman = {
    "alf":"Alfredo Dwi Putra",
    "ali":"Fajar Ali Rohman",
    "aziz":"Munib Farikhul Aziz"
}

friends = teman_teman.copy()

print(f'teman teman {teman_teman}\n')
print(f'friends {friends}\n')

teman_teman["alf"]="Dia si paling Hebat!"
print(f'teman teman {teman_teman}\n')
print(f'friends {friends}\n')

## Pop dictionary (berdasarkan key)
dataAli = friends.pop("ali")
print(f'data Ali {dataAli}\n')
print(f'friends {friends}\n')

# popitem dictionary (yang terakhir)
dataTerakhir = friends.popitem()
print(f'data terakhir {dataTerakhir}\n')
print(f'friends {friends}\n')

