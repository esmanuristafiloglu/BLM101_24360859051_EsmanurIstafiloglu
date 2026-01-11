#==========================
#RLE(Run-Length-Encoding)
#SIKISTIRMA FONKSİYONU
#==========================

def rle_encode(text):
    # eğer girilen metin boş ise boş string döndür
    if not (text):
        return ""
    #sıkıştırılmış sonucu tutan değişken
    encoded=""
    #aynı karakterin kaç kez tekrar ettiğini saymak için sayaç
    count=1
    #metnin 2. karakterinden başlayarak sona kadar döngü
    for i in range(1,len(text)):
        #eğer mevcut karakter bir öncekiyle aynıysa
        if text[i]==text[i-1]:
            #sayaç arttırılır
            count+=1
        else:
            #farklı karakter geldiğinde
            #sayı+önceki karakter encoded stringine eklenir
            encoded +=str(count)+text[i-1]
            #sayaç sıfırlanır(yeni karakter için)
            count=1

    #döngü bittikten sonra son karakter grubu eklenir
    encoded += str(count)+text[i-1]
    #sıkıştırılmış metin geri döndürülür
    return encoded

#===========================
#RLE(Run-Length Encoding)
#AÇMA(DECODE) FONKSİYONU
#===========================

def rle_decode(encoded_text):
    #çözülmüş metni tutacak değişken
    decoded=""
    #rakamları biriktirmek için geçici değişken
    count=""
    #sıkıştırılmış metindeki her karakter için döngü
    for char in encoded_text:
        #eğer karakter bir rakamsa
        if char.isdigit():
            #rakamlar birden fazla basamaklı olabilir
            count += char
        else:
            #karakter harf ise
            #harf, count kadar decoded stringine eklenir
            decoded +=char * int(count)
            #sayaç sıfırlanır
            count=""
    return decoded


#==============================
#SIKIŞTIRMA ORANI HESAPLA
#==============================
def compression_ratio(original, compressed):
    #sıkıştırma oranı formülü
    return (1-len(compressed)/len(original))*100

#==============================
#ANA PROGRAM
#==============================

#kullanıcıdan metin girişi alınır
text=input("Metni giriniz: ")

#metin RLE ile sıkıştırılır
encoded = rle_encode(text)

#sıkıştırılmış metin tekrar eski haline getirilir
decoded=rle_decode(encoded)

#sıkıştırma oranı hesaplanır
ratio = (compression_ratio(text, encoded))

#sonuçlar ekrana yazdırılır
print("\n---Sonuçlar---")
print("Orijinal Metin      :",text)
print("Sıkıştırılmış Metin :",encoded)
print("Çözümlenmiş Metin   :",decoded)
print("Sıkıştırma Oranı    :%{:.2f}".format(ratio))
