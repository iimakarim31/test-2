# definisikan data arraynya
data = [12, 9, 30, "A", "M", 99, 82, "J", "N", "B"]

# memisahkan huruf dan angkanya
huruf = sorted([x for x in data if isinstance(x, str)]) 
angka = sorted([x for x in data if isinstance(x, int)]) 

# gabungkan lagi ke urutan abjad didepan lalu angka di belakang
hasil = huruf + angka
print(hasil)