'''Beberapa atribut penting dalam histogram pandas:
bins = jumlah_bins dalam histogram yang akan digunakan. Jika tidak didefinisikan jumlah_bins, maka function akan secara default menentukan jumlah_bins sebanyak 10.
by = nama kolom di DataFrame untuk di group by. (valuenya berupa nama column di dataframe tersebut).
alpha = nilai_alpha untuk menentukan opacity dari plot di histogram. (value berupa range 0.0 - 1.0, dimana semakin kecil akan semakin kecil opacity nya)
figsize = tuple_ukuran_gambar yang digunakan untuk menentukan ukuran dari plot histogram. Contoh: figsize=(10,12)

Syntax umum:
nama_dataframe[["nama_kolom]].hist(bins=jumlah_bin, by=nama_kolom, alpha=nilai_alpha,figsize=tuple_ukuran_gambar)
'''
import pandas as pd
import matplotlib.pyplot as plt
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# plot histogram kolom: price
order_df[["price"]].hist(figsize=(4, 5), bins=10, xlabelsize=8, ylabelsize=8)
plt.show()  # Untuk menampilkan histogram plot

#outliers
'''Syntax umum:
Q1=nilai_skor_df[["Score"]].quantile(0.25)
Q3=nilai_skor_df[["Score"]].quantile(0.75)
print(IQR=Q3-Q1)
print((nilai_skor_df<(Q1-1.5*IQR)) | (nilai_skor_df > (Q3+1.5*IQR)))
'''
Q1 = order_df[["product_weight_gram"]].quantile(0.25)
# Hitung quartile 3
Q3 = order_df[["product_weight_gram"]].quantile(0.75)
# Hitung inter quartile range dan cetak ke console
IQR = Q3-Q1
print(IQR)
#rename dataframe
'''Syntax umum:
-pake nama kolom
nama_dataframe.rename(colums={"column_name_before":"column_name_after"},inplace=True)
-pake indeks kolom
nama_dataframe.columns.value[no_of_column]="column_name_after"
'''
# Ganti nama kolom freight_value menjadi shipping_cost
order_df.rename(columns={"freight_value": "shipping_cost"}, inplace=True)
print(order_df)

#group.by
'''df["Score"].groupby([df["Name"]]).mean()'''
# Hitung rata rata dari price per payment_type
rata_rata = order_df["price"].groupby(order_df["payment_type"]).mean()
print(rata_rata)

#sorting
'''Syntax umum:
nama_dataframe.sort_values(by="nama_kolom")
ascending dari terkecil
descending terbesar
'''
# Hitung harga maksimum pembelian customer
sort_harga = order_df.sort_values(by="price", ascending=True)
print(sort_harga)
