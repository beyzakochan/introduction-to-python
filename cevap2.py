# -*- coding: utf-8 -*-
"""cevap2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IXyAIK0qW8VR4S2zG-CevMOIBboppsIH
"""

#max komutunu kullanmadan tam olarak çözemedim
#string değerleri listeye ekleme aşamasında sorun yaşadım
#araştırmalarımla bulabildiklerimi tamamlamaya çalıştım ama temiz güzel bir kod
#olmadı. Liste, dictionary konularına çalışmaya başladım detaylı.

information = {} 
n =5
k=5
ls = [] 
ds = []
av = []
for i in range(0, n): 
    a,b= input("öğrencilerin isim ve soysimlerini giriniz ").split()
    ds.append((a,b))
    x,y,z = input("öğrencilerin notlarını giriniz midterm, final, homework ").split()
    t=int(x)
    r=int(y)
    w=int(z)
    avarage=(t+r+w)/3
    ls.append((x,y,z))
    av.append(avarage)
    

information = dict(zip(ds,ls))
print("öğrencilerin notlarının listesi sırasıyla midterm, final, homework=",ls)
print("\n")
print("öğrencilerin isimlerinin listesi=",ds)
print("\n")
print("bilgilerin dictionary olarak yazımı",information)
print("\n")
sorted(ls)
print("ortalamarının listesi",av)
print("\n")

av.index(max(av))
print("TEBRİİKLEER EN BAŞARILI ÖĞRENCİ!!",ds[av.index(max(av))])