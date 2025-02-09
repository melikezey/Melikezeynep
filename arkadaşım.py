#Bade benimle tanışıyor

ad=input("Adın ne?")
print (f"Merhaba {ad}! Ben Bade!Memnun oldum!")

sınıf=input("Kaçıncı sınıfa gidiyorsun?")
print (f"Aaa!Bende {sınıf} gidiyorum.")

ödev=input("2 HAFTA SONRA...Beraber ödev yapalım mı?")
print (f"{ödev} bencede!Başlayalım!")

sayı1=float(input("Birinci sayı:"))
sayı2=float(input("İkinci sayı:"))
print("İşlemimiz çarpma bu arada: + - / *")
işlem= input("İşlem:")

if işlem   == "+":
    print("Sonuç", sayı1 + sayı2)
elif işlem == "-":
    print("Sonuç", sayı1 - sayı2)
elif işlem == "*":
    print("Sonuç", sayı1 * sayı2)
elif işlem == "/":
    print("Sonuç", sayı1 / sayı2)
else:
    print("Geçersiz işlem")

ikinci=input("İkinci etkinlik neydi?")
print(f"Doğru {ikinci} etkinliğini yapalım!")

sayı=int(input("Sayıyı girelim:"))

#Bade sayıların tek mi çift mi olduğunu bana söylüyor

if sayı % 2 == 0:
    print(f"{sayı} çift sayıdır.")
else:
    print(f"{sayı} tek sayıdır.")

üçüncü=input("Üçüncü etkinliikk:")
print(f"Eveet senin yaşını bilmeyi çok isterim.")

#Bade yaş hesaplıyor
yıl=int(input("Doğum yılın nedir?"))
print(f"Sen {2025-yıl} yaşındasın!Aynı sınıfa da gittiğimiz için yaşlarımızın yakın olması normal!")

dördüncü=input("Hadi dördüncü etkinliği yapalım!Peki dördüncü etkinlik nedir?")
print(f"Doğru {dördüncü}")

#Bade iki sayıyla dört işlem yapıyor

sayı1=int(input("Birinci sayıyı alalım: "))
sayı2=int(input("İkinci sayıyı alalım: "))

print(f"Toplam: {sayı1 + sayı2}")
print(f"Çıkarma: {sayı1 - sayı2}")
print(f"Çarpma: {sayı1 * sayı2}" )
print(f"Bölme: {sayı1 / sayı2}")

