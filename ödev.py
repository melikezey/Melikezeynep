#int tam sayı
#float ondalikli sayi
#str Metin
#list (Liste)
#dict (sözlük)

sınıf=input ("Merhaba!Sana nasıl yardımcı olabilirim?")
print (f"Harika!Sınıf listeni oluşturmayı çok isterim.")

sayi = 14 #int
ondaliklisayi = 3.14, 5.5, 0.33, 4.18, 5.16 #float
metin = "Merhaba Dünya!" #Hello World! #str
liste = [1,2,3,4] #list
sozluk = {"Ad":"Zeynep","Yaş":"Aralıkta 11 ama 10"} #dict

print("Sayı:(1,2,3,4,)", type(sayi))
print("Ondalık Sayı:(3.14,5.15,6.16)", type(ondaliklisayi))
print("Metin:Lorem ipsum dolor sit amet consectetuer...", type(str))
print("Liste:", type(liste))
print("Sözlük", type(sozluk))

sinif = ["Ali Kerem AKBAŞ", "Elif KUŞ", "Ezgi SALİ", "Nehir ÇELİMLİ", "Rüzgar Taha ŞİMŞEK", "Selinay ATAKAN", "Zeynep Melike ERYÜREK"]
print(sinif[1]) #3.sıradaki eleman
print(sinif[2]) #liste 0,1,2,... şeklinde 0.elemandan başlayarak
print(sinif[3])
print(sinif[4])
print(sinif[5])
print(sinif[6])

sinif.append("Güven") #Listenin sonuna ekler.
sinif.insert(1,"Bade ÖGER")
sinif.insert(2,"Ediz ŞEN")
print(sinif)

sinif.remove("Bade Öger")
sinif.remove("Ediz ŞEN")
print(sinif)

silinen = sinif.pop() #Son elemanı siler ve yazdırır.
print("Silinen:",  silinen)
print(sinif)

sinav_sonuclari = [83,80,72,70,65,58,45]
sinav_sonuclari.sort() #Küçükten büyüğe sıralama.
print("Sıralanmış Sınav Sonuçları",sinav_sonuclari)

ara= int(input("Not sorgula:"))
if ara in sinav_sonuclari:
   print("Böyle bir sonuç var!")
else:
    print("Böyle bir sınav sonucu yok!")

