
ham = " Ahmet YILMAZ "
print(ham.strip().lower())

satir = "TR-1001-AB,klavye,249.9,15"
kod, ad, fiyat, adet = satir.split(",")
fiyat_float = float(fiyat)
print(f"{ad} ({kod}) : {fiyat_float:.2f} TL x {adet}")

dosyalar = ["satis_ocak.csv", "notlar.txt", "satis_subat.csv", "rapor.xlsx"]
csv_dosyalari = []
for dosya in dosyalar:
    if dosya.endswith(".csv"):
        csv_dosyalari.append(dosya)

sonuc = " | ".join(csv_dosyalari)
print(sonuc)


kayitlar = [
    "  TR-1001-AB , Klavye , 249.9 , 15 ",
    "TR-1002-CD,MOUSE,89.5,40",
    "  tr-1003-ef , Monitör , 3499.0 , 3",
    "TR-1004-GH , Kulaklik , 159.75 , 0",
]

stoktaki_kodlar = []

for satirdaki_metinler in kayitlar:
    kod, ad, fiyat, adet = [eleman.strip() for eleman in satirdaki_metinler.split(",")]
    ad = ad.capitalize()
    kod = kod.upper()
    fiyat = float(fiyat)
    adet = int(adet)

    if adet == 0:
        print(f"{ad}: = STOKTA YOK!")
    else:        
        print(f"{ad} ({kod}): {fiyat:,.2f} TL x {adet} = {fiyat * adet:,.2f} TL")
        stoktaki_kodlar.append(kod)


print("\nStoktaki Ürün Kodlari:", " | ".join(stoktaki_kodlar))

