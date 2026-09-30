"""
15 - String Metotlari
Konu: strip, lower, upper, capitalize, split, join, startswith/endswith, in, f-string format

Notlar:
- Metinler DEGISMEZDIR: metin.upper() metni degistirmez, YENI metin dondurur.
  Sonucu bir degiskene atmazsan kaybolur. (Listelerde tersi olacak: sort() listeyi degistirir.)
- split(",") -> metni bolup LISTE dondurur. Ayrac vermezsen bosluklardan boler.
- ", ".join(liste) -> listeyi birlestirip METIN dondurur. Ayrac basa yazilir.
- split her zaman METIN dondurur; hesap yapacaksan float()/int() ile cevir.
- f"{x:.2f}" iki ondalik, f"{x:,.2f}" binlik ayrac ekler.
  DIKKAT: Python varsayilan olarak Amerikan bicimi kullanir -> 3,748.50
  Turkce bicim (3.748,50) degildir. Rapor uretirken elle duzeltmek gerekir.
- lower() Turkce I harfini bilmez: "YILMAZ".lower() -> "yilmaz" (noktali i degil).
"""

# --- Alistirma 1: temizlik metotlari zincirleme calisir ---
ham = "   Ahmet YILMAZ  "
print(ham.strip().lower())

# --- Alistirma 2: split + unpacking + sayi donusumu + format ---
satir = "TR-1001-AB,klavye,249.9,15"
kod, ad, fiyat, adet = satir.split(",")   # dort parca -> dort degisken (unpacking)
fiyat_float = float(fiyat)                # split metin dondurur, :.2f sayi ister
print(f"{ad} ({kod}): {fiyat_float:.2f} TL x {adet}")

# --- Alistirma 3: filtreleme kalibi (bos liste -> dongu -> kosul -> append -> join) ---
dosyalar = ["satis_ocak.csv", "notlar.txt", "satis_subat.csv", "rapor.xlsx"]
csv_dosyalari = []
for dosya in dosyalar:
    if dosya.endswith(".csv"):
        csv_dosyalari.append(dosya)

sonuc = " | ".join(csv_dosyalari)   # join DONGUDEN SONRA, bir kez
print(sonuc)

# --- Birlestiren gorev: kirli kayitlari temizleyip raporlamak ---
kayitlar = [
    "  TR-1001-AB , Klavye , 249.9 , 15 ",
    "TR-1002-CD,MOUSE,89.5,40",
    "  tr-1003-ef , Monitör , 3499.0 , 3",
    "TR-1004-GH , Kulaklik , 159.75 , 0",
]

stoktaki_kodlar = []

for kayit in kayitlar:
    # once bol, sonra her parcayi ayri ayri temizle
    kod, ad, fiyat, adet = [eleman.strip() for eleman in kayit.split(",")]
    kod = kod.upper()
    ad = ad.capitalize()      # capitalize: ilk harf buyuk, gerisi kucuk
                              # title olsaydi her kelimeyi buyuturdu
    fiyat = float(fiyat)      # donusumler strip'ten SONRA
    adet = int(adet)

    if adet == 0:
        print(f"{ad}: stokta yok")
    else:
        print(f"{ad} ({kod}): {fiyat:,.2f} TL x {adet} = {fiyat * adet:,.2f} TL")
        stoktaki_kodlar.append(kod)

print("\nStoktaki urun kodlari:", " | ".join(stoktaki_kodlar))
