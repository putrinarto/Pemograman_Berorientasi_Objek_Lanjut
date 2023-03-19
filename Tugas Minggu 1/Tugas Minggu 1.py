#Nama :Rifki Fadilah
#Kelas:R1
#NIM  :210511011

print("Tugas Minggu 1")
print("="*50)
print(" ")

class SuhuCelcius:
    def __init__(self, celcius):
        self.celcius = celcius

    def farenheit(self):
        return (self.celcius * 9/5) + 32
    def reamur(self):
        return (self.celcius * 4/5)
    def kelvin(self):
        return (self.celcius + 273.15)


class SuhuFarenheit:
    def __init__(self, farenheit):
        self.farenheit = farenheit

    def celcius(self):
        return 5/9 * (self.farenheit - 32)
    def kelvin(self):
        return 5/9 * (self.farenheit - 32) +273
    def reamur(self):
        return 4/9 * (self.farenheit - 32)


class SuhuReamur:
    def __init__(self, reamur):
        self.reamur = reamur

    def celcius(self):
        return (5/4 * self.reamur)
    def farenheit(self):
        return (9/4 * self.reamur) + 32
    def kelvin(self):
        return (5/4 * self.reamur) + 273


class SuhuKelvin:
    def __init__(self, kelvin):
        self.kelvin = kelvin

    def celcius(self):
        return (self.kelvin - 273) 
    def farenheit(self):
        return 9/5 * (self.kelvin - 273) + 32
    def reamur(self):
        return 4/5 * (self.kelvin - 273)
#===============================================================
print("Suhu Celcius")
celcius1 = SuhuCelcius(75)
print(f"Konversi dari Celcius ke Farenheit: {celcius1.farenheit()}")
celcius2 = SuhuCelcius(60)
print(f"Konversi dari Celcius ke Reamur: {celcius2.reamur()}")
celcius3 = SuhuCelcius(90)
print(f"Konversi dari Celcius ke Kelvin: {celcius3.kelvin()}")
print("="*50)

print("Suhu Farenheit")
farenheit1 = SuhuFarenheit(75)
print(f"Konversi dari Farenheit ke Celcius: {farenheit1.celcius()}")
farenheit2 = SuhuFarenheit(60)
print(f"Konversi dari Farenheit ke Kelvin: {farenheit2.kelvin()}")
farenheit3 = SuhuFarenheit(90)
print(f"Konversi dari Farenheit ke Reamur: {farenheit3.reamur()}")
print("="*50)

print("Suhu Reamur")
reamur1 = SuhuReamur(75)
print(f"Konversi dari Reamur ke Celcius: {reamur1.celcius()}")
reamur2 = SuhuReamur(60)
print(f"Konversi dari Reamur ke Farenheit: {reamur2.farenheit()}")
reamur3 = SuhuReamur(90)
print(f"Konversi dari Reamur ke Kelvin: {reamur3.kelvin()}")
print("="*50)

print("Suhu Kelvin")
kelvin1 = SuhuKelvin(75)
print(f"Konversi dari Kelvin ke Celcius: {kelvin1.celcius()}")
kelvin2 = SuhuKelvin(60)
print(f"Konversi dari Kelvin ke Farenheit: {kelvin2.farenheit()}")
kelvin3 = SuhuKelvin(90)
print(f"Konversi dari Kelvin ke Reamur: {kelvin3.reamur()}")