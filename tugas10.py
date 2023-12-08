import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
for i in range(len(df)):
    df.at[i, 'Gaji'] = (lambda x: x * 1.05)(df.at[i, 'Gaji'])

# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("DataFrame setelah peningkatan gaji 5%:")
print(df)
print()

# Pertanyaan 3:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
for i in range(len(df)):
    if df.at[i, 'Usia'] > 30:
        df.at[i, 'Gaji'] = (lambda x: x * 1.02)(df.at[i, 'Gaji'])

# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print("DataFrame setelah peningkatan gaji tambahan:")
print(df)
print()
print("Ringkasan hasil:")
print(df.describe())
