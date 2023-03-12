isim = "Ayşe Nur"
metin = "Hoşgeldin {name}".format(name="Ayşe Nur")
print(metin)

metin = f"Hoşgeldiniz "
print(metin)

for i in range(5):
    print("Ayşe Nur, Dilara, Defne, Hakan")
    print(i)
print("*******")
for i in range(1,5):
    print("Ayşe Nur, Dilara, Defne,Hakan")
    print(i)
print("*******")
for i in range(5):
    isimSoyİsim= input("Adınızı ve soy adınızı giriniz: ")
    print(i)
print("*******")

for i in range(len(isimSoyİsim)):
    print("Ayşe Nur, Dilara, Defne,Hakan")
    print(i)

print("*******")


# öğrenci kayıt sistemi

öğrenciKayıt=["Ayşe Nur Duman", "Dilara Yılmaz", "Defne Duman"]
print(öğrenciKayıt)

öğrenciKayıt.append("Hakan Duman")
print(öğrenciKayıt)

öğrenciKayıt.append("Büşra Duman")
print(öğrenciKayıt)

öğrenciKayıt.append("Furkan Duman")
print(öğrenciKayıt)

print("********")

for uygulama in öğrenciKayıt:
    print(uygulama)

i=0
while i <len(öğrenciKayıt):
    print(str(i)+ "no'lu öğrenci"+öğrenciKayıt[i])
    i+=1

for i in range(len(öğrenciKayıt)-1, -1,-1):
    print(str(i)+"no'lu öğrenci"+ öğrenciKayıt[i])
    del öğrenciKayıt[i]
    print(öğrenciKayıt)





