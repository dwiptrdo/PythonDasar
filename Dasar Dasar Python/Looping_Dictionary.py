# looping dictionary

teman_teman = {
    "alf":"Alfredo Dwi Putra",
    "ali":"Fajar Ali Rohman",
    "aziz":"Munib Farikhul Aziz"
}

# looping first key (yang keluar adalah keynya)

for teman in teman_teman:
    print(teman)

# operator untuk mengambil item / iterables
# menggunakan keys
print('\nKEYS')
keys =teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

# menggunakan values
print('\nVALUES')
values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)

# menggunakan items
print('\nITEMS')
items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)

for key,value in teman_teman.items():
    print(f'key = {key} value = {value}')