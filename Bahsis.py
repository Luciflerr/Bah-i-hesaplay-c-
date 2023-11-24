print("Hoşgeldiniz bu bir tip hesaplayıcıdır.")
# Bahşiş tutarı:

# Girdiyi kaydetmek için mesela müşteriye ücret toplamda ne kadar tuttu verisini kaydetmek için musteri = yaptık. verdiği cevap musteri uzerinden kaydediliyor.

musteri = float(input("Ücret toplamda ne kadar tuttu?"))

tip = int(input("Ne kadar bahşiş vermek istersin? 10, 12 veya 15?"))

kisi = int(input("Toplam kişi sayısı?"))

musteri_tip = tip / 100 * musteri + musteri

kisi_basi = musteri / kisi

print(kisi_basi)