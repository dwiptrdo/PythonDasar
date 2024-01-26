# latihan koversi satuan temperatur
# program konversi celcius ke lainnya

print("PROGRAM KONVERSI TEMPERATURE")
print("\nKONVERSI CELCIUS KE LAINNYA")
celcius = float(input("Masukan Suhu :"))
print("suhunya adalah", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("suhunya adalah", reamur, "Reamur")

# fahrenheit 
fahrenheit = ((9/5) * celcius) + 32
print("suhunya adalah", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhunya adalah", kelvin, "Kelvin")


# program konversi fahrenheit ke lainnya
print("\nKONVERSI FAHRENHEIT KE LAINNYA")

# fahrenheit ke kelvin
fahrenheit_kelvin = ((fahrenheit - 32) * 5/9) + 273.15
print("suhunya adalah", fahrenheit_kelvin, "Kelvin")

# program konversi kelvin ke lainnya
print("\nKONVERSI KELVIN KE LAINNYA")

# program konversi kelvin ke lainnya
kelvin_fahrenheit = (1.8 * (kelvin - 273)) + 32
print("suhunya adalah", kelvin_fahrenheit, "Ffahrenheit")
