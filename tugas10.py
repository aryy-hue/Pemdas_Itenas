import pandas as pd

# Data awal
data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

# Membuat DataFrame
df = pd.DataFrame(data)

# Pertanyaan 1:
# Menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini
df['Gaji'] = df['Gaji'].apply(lambda x: x * 1.05)

# Pertanyaan 2:
# Menampilkan DataFrame yang sudah diperbarui dan ringkasan perubahan
print("DataFrame setelah peningkatan gaji 5%:")
print(df)
print("\nRingkasan perubahan:")
print(df.describe())

# Pertanyaan 3:
# Evaluasi karyawan yang usianya di atas 30 tahun dan berikan peningkatan tambahan 2%
df['Gaji'] = df.apply(lambda row: row['Gaji'] * 1.02 if row['Usia'] > 30 else row['Gaji'], axis=1)

# Pertanyaan 4:
# Menampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan ringkasan hasilnya
print("\nDataFrame setelah peningkatan gaji tambahan 2%:")
print(df)
print("\nRingkasan hasil setelah peningkatan tambahan:")
print(df.describe())


