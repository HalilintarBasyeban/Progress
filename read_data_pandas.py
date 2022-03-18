import pandas as pd

csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")

#memilih kolom age, baris kedua (karena mulai dari 0=1 maka, 1 = 2)
print(csv_data['Age'].iloc[1])

#menampilkan cuplikan dataset
print("Cuplikan Dataset:")

#tampil dataset dengan menggunakan function pandas head
print(csv_data.head())