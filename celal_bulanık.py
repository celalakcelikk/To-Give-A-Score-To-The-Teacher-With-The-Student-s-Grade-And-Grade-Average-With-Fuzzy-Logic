# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 21:41:26 2018

@author: celal
"""
#Kütüphaneler tanımlandı.
import numpy as np 
import skfuzzy as fuzz 
import matplotlib.pyplot as plt

#Girdi deger aralıkları olusturuldu.
ogrenci= np.arange(0,101,0.1)
sinif_ort=np.arange(0,101,0.1)
hocanin_notu=np.arange(0,11,0.1)

#Uyelik fonksiyonları olusruldu.
ogrenci_kotu=fuzz.trimf(ogrenci,[0,0,50])
ogrenci_orta=fuzz.trimf(ogrenci,[30,50,70])
ogrenci_iyi=fuzz.trimf(ogrenci,[50,100,100])

sinif_ort_kotu=fuzz.trimf(sinif_ort,[0,0,50])
sinif_ort_orta=fuzz.trimf(sinif_ort,[30,50,70])
sinif_ort_iyi=fuzz.trimf(sinif_ort,[50,100,100])

hocanin_notu_cok_kotu=fuzz.trimf(hocanin_notu,[0,0,2.5])
hocanin_notu_kotu=fuzz.trimf(hocanin_notu,[2,3.5,5])
hocanin_notu_orta=fuzz.trimf(hocanin_notu,[4,5.5,7])
hocanin_notu_iyi=fuzz.trimf(hocanin_notu,[6.5,7.5,8.5])
hocanin_notu_cok_iyi=fuzz.trimf(hocanin_notu,[8,10,10])

#Uylelik fonksiyonları grafikleştirildi.
fig, (ax0,ax1,ax2) = plt.subplots(nrows=3, figsize=(10, 12))

ax0.plot(ogrenci,ogrenci_kotu,'r',linewidth=2,label='Öğrencinin Kötü Notu')
ax0.plot(ogrenci,ogrenci_orta,'b',linewidth=2,label='Öğrencinin Orta Notu')
ax0.plot(ogrenci,ogrenci_iyi,'g',linewidth=2,label='Öp,ğrencinin İyi Notu')
ax0.set_title('Öğrencinin Notu',fontsize=20)
ax0.set_xlabel('Öğrencinin Not Aralıkları')
ax0.set_ylabel('Üyelik Dereceleri')

ax0.legend() 

ax1.plot(sinif_ort,sinif_ort_kotu,'r',linewidth=2,label='Sınıfın Ortalaması Kötü ')
ax1.plot(sinif_ort,sinif_ort_orta,'b',linewidth=2,label='Sınıfın Ortalaması Orta')
ax1.plot(sinif_ort,sinif_ort_iyi,'g',linewidth=2,label='Sınıfın Ortalaması İyi')
ax1.set_title('Sınıfın Ortlama Notu',fontsize=20)
ax1.set_xlabel('Sınıfın Not Ortalaması Aralıkları')
ax1.set_ylabel('Üyelik Dereceleri')
ax1.legend() 


ax2.plot(hocanin_notu,hocanin_notu_cok_kotu,'r',linewidth=2,label='Öğretmenin Notu Çok Kötü ')
ax2.plot(hocanin_notu,hocanin_notu_kotu,'b',linewidth=2,label='Öğretmenin Notu Kötü ')
ax2.plot(hocanin_notu,hocanin_notu_orta,'g',linewidth=2,label='Öğretmenin Notu Orta')
ax2.plot(hocanin_notu,hocanin_notu_iyi,'m',linewidth=2,label='Öğretmenin Notu İyi')
ax2.plot(hocanin_notu,hocanin_notu_cok_iyi,'y',linewidth=2,label='Öğretmenin Notu Çok İyi')
ax2.set_title('Öğretmenin Notu',fontsize=20)
ax2.set_xlabel('Öğretmenin Not Aralıkları')
ax2.set_ylabel('Üyelik Dereceleri')
ax2.legend()

for ax in (ax0, ax1, ax2): 
    ax.spines['top'].set_visible(True) 
    ax.spines['right'].set_visible(True) 
    ax.get_xaxis().tick_bottom() 
    ax.get_yaxis().tick_left()
 
plt.tight_layout() 
 
#Kulanıcı girişleri

ogrenci_puan=input('\tÖğrencinin notunu giriniz: ')
sinif_ort_puan=input('\tSınıfın notunu giriniz: ')
while (float(ogrenci_puan)<0 or float(ogrenci_puan)>100)  or (float(sinif_ort_puan)<0 or float(sinif_ort_puan)>100): 
    print('Lütfen öğrenci notu ile sınıf ortalamasını 0 ile 100 arasında giriniz!!!!!')
    ogrenci_puan=input('Lütfen tekrar öğrencinin notunu giriniz: ')
    sinif_ort_puan=input('Lütfen tekrar sınıfın notunu giriniz: ')

ogr_kotu=fuzz.interp_membership(ogrenci, ogrenci_kotu,float(ogrenci_puan))
ogr_orta=fuzz.interp_membership(ogrenci, ogrenci_orta,float(ogrenci_puan))
ogr_iyi=fuzz.interp_membership(ogrenci, ogrenci_iyi,float(ogrenci_puan))

sinif_kotu=fuzz.interp_membership(sinif_ort,sinif_ort_kotu,float(sinif_ort_puan))
sinif_orta=fuzz.interp_membership(sinif_ort, sinif_ort_orta,float(sinif_ort_puan))
sinif_iyi=fuzz.interp_membership(sinif_ort, sinif_ort_iyi,float(sinif_ort_puan))

#Kurallar uygulandı.

#Kural-1
Kural1= np.fmin(ogr_kotu,sinif_kotu)
Kontrol_kural1=np.fmin(Kural1,hocanin_notu_cok_kotu)

#Kural-2
Kural2= np.fmin(ogr_orta,sinif_kotu)
Kontrol_kural2=np.fmin(Kural2,hocanin_notu_kotu)

#Kural-3
Kural3= np.fmin(ogr_iyi,sinif_iyi)
Kontrol_kural3=np.fmin(Kural3,hocanin_notu_cok_iyi)

#Kural-4
Kural4= np.fmin(ogr_orta,sinif_orta)
Kontrol_kural4=np.fmin(Kural4,hocanin_notu_orta)

#Kural-5
Kural5= np.fmin(ogr_iyi,sinif_orta)
Kontrol_kural5=np.fmin(Kural5,hocanin_notu_iyi)

#Kural-6
Kural6= np.fmin(ogr_orta,sinif_iyi)
Kontrol_kural6=np.fmin(Kural6,hocanin_notu_iyi)


ctr0=np.zeros_like(hocanin_notu)

c1=np.fmax(Kontrol_kural1,Kontrol_kural2)
c2=np.fmax(Kontrol_kural3,Kontrol_kural4)
c3=np.fmax(Kontrol_kural5,Kontrol_kural6)
c4=np.fmax(c2,c3)
toplanan_kurallar= np.fmax(c1,c4)
#Durulama işlemleri yapıldı.
durulama_islemi= fuzz.defuzz(hocanin_notu,toplanan_kurallar,'mom')
islem_sonucu=fuzz.interp_membership(hocanin_notu,toplanan_kurallar,durulama_islemi)
#Sonuç grafiği çizildi. 
fig,ax4= plt.subplots(figsize=(10,4))
ax4.plot(hocanin_notu,hocanin_notu_cok_kotu,linewidth=2,linestyle='--',label='Öğretmenin Notu Çok Kötü')
ax4.plot(hocanin_notu,hocanin_notu_kotu,linewidth=2,linestyle='--',label='Öğretmenin Notu Kötü')
ax4.plot(hocanin_notu,hocanin_notu_orta,linewidth=2,linestyle='--',label='Öğretmenin Notu Orta')
ax4.plot(hocanin_notu,hocanin_notu_iyi,linewidth=2,linestyle='--',label='Öğretmenin Notu İyi')
ax4.plot(hocanin_notu,hocanin_notu_cok_iyi,linewidth=2,linestyle='--',label='Öğretmenin Notu Çok iyi')
ax4.fill_between(hocanin_notu,ctr0,toplanan_kurallar,facecolor='orange',alpha=0.7)
ax4.plot([durulama_islemi,durulama_islemi],[0,islem_sonucu],'k',linewidth=3,linestyle='-',alpha=0.9,label='Durulama İşlemi Sonucu')
ax4.legend(loc='right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True,framealpha=1) 
ax4.set_title('Sonuç',fontsize=20)
ax4.set_xlabel('Öğretmenin Not Aralıkları')
ax4.set_ylabel('Üyelik Dereceleri')

plt.tight_layout()
plt.show()
#Sonuçlar
print("\tÖğretmenin Notu: " , round(durulama_islemi,2))
print("\tÜyelik Derecesi: ",round(islem_sonucu,2))

















