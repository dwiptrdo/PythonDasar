# operator dictionary

data_dict = {
    "al":"Ali",
    "dw":"Dwi",
    "az":"Aziz"
}

# panjang dictionary
lendict = len(data_dict)
print(f'panjang dictionary: {lendict}')

# mengecek key exist atau tidak
KEY = "dw"
CHEKKEY = KEY in data_dict
print(f'apakah {KEY} ada di data_dict: {CHEKKEY}')

# mengakses value (read) dengan get
print(data_dict["dw"])
print(data_dict.get("al"))
print(data_dict.get("rh","data tidak ditemukan")) # cek key dengan message data tidak ditemukan

# mengupdate data
data_dict["al"] = "Rohman"
print(data_dict)
data_dict["rw"] = "Setiono"
print(data_dict)

data_dict.update({"al":"Ali"})
print(data_dict)
data_dict.update({"alf":"Alfredo"}) # kalau tidak ada, add saja
print(data_dict)

# menghapus data pada dictionary
del data_dict["alf"]
print(data_dict)

