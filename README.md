# To Give A Score To The Teacher With The Student's Grade And Grade Average With Fuzzy Logic
0-100 arasında öğrenci notu ve 0-100 arasında sınıfın ortalama notu alınarak 0-10 arasında öğretmene puan verilmesidir. Örnek olarak Öğrencinin notu 50 olsun, sınıfın ortalaması 23 olsun. Öğretmenin puanı 3.5 oluyor. Üçgen üyelik fonksiyonu kullandım. Bulanık çıkarım yöntemi olarak Mamdani(Max-min) yöntemini kullandım. Durulama fonksiyonu olarak Mean of Maximum kullandım. 

## Projede Kullanılan IDE'ler ve İndirme Linki
<ul>
  <li>Proje Python 3 ile yazılmıştır.</li>
  <li>Anaconda & Spyder
      <ul>
         <li>İndirme Linki: https://www.anaconda.com/distribution/ </li>
       </ul>  
  </li>
  <li>PyCharm
      <ul>
         <li>İndirme Linki: https://www.jetbrains.com/pycharm/download/#section=windows </li>
       </ul>  
  </li>
</ul>

## Projenin Çalışması İçin Gerekli Kütüphaler ve İndirme Linkleri

<ul>
  <li>Scikit Fuzzy
    <ul>
          <li><code>pip install scikit-fuzzy</code></li>
    </ul>  
  </li>
  <li>Matplotlib
    <ul>
          <li><code>pip install matplotlib</code></li>
    </ul>  
  </li>
  <li>Numpy
    <ul>
          <li>Python programlama dili kurduğunuzda otomatik olarak numpy kütüphaneside yükler.</li>
    </ul>  
  </li>
 </ul>
 
## Projenin Çalışma Adımları

### Problemin Girdileri
Girdi değerlerimiz öğrenci notu ve sınıfın ortalama notudur.
<ul>
  Öğrencinin Not Aralıkları:
    <li>
    İyi: 50-100-100
      <ul>
      <li>Python Kodu: <code>ogrenci_iyi=fuzz.trimf(ogrenci,[50,100,100])</code></li>
      </ul>
    </li>
    <li>
    Orta: 30-50-70
      <ul>
      <li>Python Kodu: <code>ogrenci_orta=fuzz.trimf(ogrenci,[30,50,70])</code></li>
      </ul>
    </li>
    <li>
    Kötü: 0-0-50
    <ul>
<li>Python Kodu: <code>ogrenci_orta=fuzz.trimf(ogrenci,[0,0,50])</code></li>
      </ul>
    </li>
</ul>
<ul>
  Sınıfın Not Ortalaması Puan Aralıkları:
    <li>
    İyi: 50-100-100
      <ul>
      <li>Python Kodu: <code>sinif_ort_iyi=fuzz.trimf(sinif_ort,[50,100,100])</code></li>
      </ul>
    </li>
    <li>
    Orta: 30-50-70
      <ul>
      <li>Python Kodu: <code>sinif_ort_orta=fuzz.trimf(sinif_ort,[30,50,70])</code></li>
      </ul>
    </li>
    <li>
    Kötü: 0-0-50
      <ul>
      <li>Python Kodu: <code>sinif_ort_kotu=fuzz.trimf(sinif_ort,[0,0,50])</code></li>
      </ul>
    </li>
</ul>
     
### Problemin Çıktısı

Çıktımız öğretmenin puan bilgisidir.

<ul>
  Öğretmenin Puan Aralıkları:
    <li>
    Çok İyi:8-10-10
      <ul>
      <li>Python Kodu: <code>hocanin_notu_cok_iyi=fuzz.trimf(hocanin_notu,[8,10,10])</code></li>
      </ul>
    </li>
  <li>
    İyi:6.5-7.5-8.5
      <ul>
      <li>Python Kodu: <code>hocanin_notu_iyi=fuzz.trimf(hocanin_notu,[6.5,7.5,8.5])</code></li>
      </ul>
    </li>
  <li>
    Orta:4-5.5-7
      <ul>
      <li>Python Kodu: <code>hocanin_notu_orta=fuzz.trimf(hocanin_notu,[4,5.5,7])</code></li>
      </ul>
    </li>
    <li>
    Kötü: 2-3.5-5
      <ul>
      <li>Python Kodu: <code>hocanin_notu_kotu=fuzz.trimf(hocanin_notu,[2,3.5,5])</code></li>
      </ul>
    </li>
    <li>
    Çok kötü: 0-0-2.5
    <ul>
<li>Python Kodu: <code>hocanin_notu_cok_kotu=fuzz.trimf(hocanin_notu,[0,0,2.5])</code></li>
      </ul>
    </li>
</ul>

### Bulanık Sistem Tasarımı

Aşağıdaki resimde görüldüğü gibi öğrenicinin not aralıkları ile sınıfın not aralıkları, hocaya verilecek olan puan aralıklarını sözel olarak yazılıp tablo halinde oluşturuldu.

<img src="https://github.com/celalakcelikk/To-Give-A-Score-To-The-Teacher-With-The-Student-s-Grade-And-Grade-Average-With-Fuzzy-Logic/blob/master/iimages/bulanik_mantik_tasar%C4%B1m%C4%B1.png">

### Giriş ve Çıkış Değer Aralıklarının Tanımlanması

<ul>
    <li>
    Öğrencinin notu= 0 ile 100 arasında belirlendi.
      <ul>
      <li>Python Kodu: <code>ogrenci= np.arange(0,101,0.1)</code></li>
      </ul>
    </li>
      <li>
    Sınıfın not ortalaması=0 ile 100 arasında belirlendi.
      <ul>
      <li>Python Kodu: <code>sinif_ort=np.arange(0,101,0.1)</code></li>
      </ul>
    </li>
      <li>
    Öğretmenin puanı=0 ile 10 arasında belirlendi.
      <ul>
      <li>Python Kodu: <code>hocanin_notu=np.arange(0,11,0.1)</code></li>
      </ul>
    </li> 
 </ul>

### Bulandırma 


Aşağıdaki resimde görüldüğü gibi gerçek hayatta olması çok zor olan öğretmen puan aralıklarını çıkarıp sistemi bulanıklaştırıldı ve tablo halinde oluşturuldu.

<img src="https://github.com/celalakcelikk/To-Give-A-Score-To-The-Teacher-With-The-Student-s-Grade-And-Grade-Average-With-Fuzzy-Logic/blob/master/iimages/bulandirma.png">

### Üyelik İşlemleri

Üçgen üyelik fonksiyonunu kullanıldı çünkü daha verimli sonuçlar alındı. 

<ul>
    <li>
    Öğrencinin üyelik fonksiyonları: 
      <ul>
      <li>Python Kodu: <code>ogrenci_kotu=fuzz.trimf(ogrenci,[0,0,50])</code></li>
        <li>Python Kodu: <code>ogrenci_orta=fuzz.trimf(ogrenci,[30,50,70])</code></li>
        <li>Python Kodu: <code>ogrenci_iyi=fuzz.trimf(ogrenci,[50,100,100])</code></li>
      </ul>
    </li>
      <li>
    Sınıfın not ortalaması üyelik fonksiyonları: 
      <ul>
      <li>Python Kodu: <code>sinif_ort_kotu=fuzz.trimf(sinif_ort,[0,0,50])</code></li>
        <li>Python Kodu: <code>sinif_ort_orta=fuzz.trimf(sinif_ort,[30,50,70])</code></li>
        <li>Python Kodu: <code>sinif_ort_iyi=fuzz.trimf(sinif_ort,[50,100,100])</code></li>
      </ul>
    </li>
      <li>
    Öğretmenin puanı üyelik fonksiyonları: 
      <ul>
      <li>Python Kodu: <code>hocanin_notu_cok_kotu=fuzz.trimf(hocanin_notu,[0,0,2.5])</code></li>
        <li>Python Kodu: <code>hocanin_notu_kotu=fuzz.trimf(hocanin_notu,[2,3.5,5])</code></li>
        <li>Python Kodu: <code>hocanin_notu_orta=fuzz.trimf(hocanin_notu,[4,5.5,7])</code></li>
        <li>Python Kodu: <code>hocanin_notu_iyi=fuzz.trimf(hocanin_notu,[6.5,7.5,8.5])</code></li>
        <li>Python Kodu: <code>hocanin_notu_cok_iyi=fuzz.trimf(hocanin_notu,[8,10,10])</code></li>
      </ul>
    </li> 
 </ul>

Grafiksel gösterimi aşağıdaki gibidir.

<img src="https://github.com/celalakcelikk/To-Give-A-Score-To-The-Teacher-With-The-Student-s-Grade-And-Grade-Average-With-Fuzzy-Logic/blob/master/iimages/grafik.PNG">

### Bulanık Çıkarım Yöntemi

Mamdani bulanık çıkarım tiplerinden max-min çıkarımı kullandım. Sonuçlar daha verimli oldu.

### Bulanık Kuralların Belirlenmesi 
<ul>
    <li>
      Kural-1
      <ul>
        <li>Öğrencinin notu kötü ve sınıfın ortalama notu kötü = Öğretmenin puanı çok kötü</li>
      <li>Python Kodu: <code>Kural1= np.fmin(ogr_kotu,sinif_kotu)</code><br>
                    <code>Kontrol_kural1=np.fmin(Kural1,hocanin_notu_cok_kotu)</code></li>
      </ul>
    </li>
      <li>
    Kural-2
      <ul>
        <li>Öğrencinin notu orta ve sınıfın ortalama notu kötü = Öğretmenin puanı kötü</li>
      <li>Python Kodu: <code>Kural2= np.fmin(ogr_orta,sinif_kotu)</code><br>
                    <code>Kontrol_kural2=np.fmin(Kural2,hocanin_notu_kotu)</code></li>
      </ul>
    </li>
       <li>
    Kural-3
      <ul>
        <li>Öğrencinin notu iyi ve sınıfın ortalama notu iyi = Öğretmenin puanı çok iyi</li>
      <li>Python Kodu: <code>Kural3= np.fmin(ogr_iyi,sinif_iyi)</code><br>
                    <code>Kontrol_kural3=np.fmin(Kural3,hocanin_notu_cok_iyi)</code></li>
      </ul>
    </li>
  <li>
    Kural-4
      <ul>
        <li>Öğrencinin notu orta ve sınıfın ortalama notu orta = Öğretmenin puanı orta</li>
      <li>Python Kodu: <code>Kural4= np.fmin(ogr_orta,sinif_orta)</code><br>
                    <code>Kontrol_kural4=np.fmin(Kural4,hocanin_notu_orta)</code></li>
      </ul>
    </li>
  <li>
    Kural-5
      <ul>
        <li>Öğrencinin notu iyi ve sınıfın ortalama notu orta = Öğretmenin puanı iyi</li>
      <li>Python Kodu: <code>Kural5= np.fmin(ogr_iyi,sinif_orta)</code><br>
                    <code>Kontrol_kural5=np.fmin(Kural5,hocanin_notu_iyi)</code></li>
      </ul>
    </li>
  <li>
    Kural-6
      <ul>
        <li>Öğrencinin notu orta ve sınıfın ortalama notu iyi = Öğretmenin puanı iyi</li>
      <li>Python Kodu: <code>Kural6= np.fmin(ogr_orta,sinif_iyi)</code><br>
                    <code>Kontrol_kural6=np.fmin(Kural6,hocanin_notu_iyi)</code></li>
      </ul>
    </li>
  <li>
    ctr0=np.zeros_like(hocanin_notu)
</li>
  <li>
c1=np.fmax(Kontrol_kural1,Kontrol_kural2)
    </li>
  <li>
c2=np.fmax(Kontrol_kural3,Kontrol_kural4)
    </li>
  <li>
c3=np.fmax(Kontrol_kural5,Kontrol_kural6)
    </li>
  <li>
c4=np.fmax(c2,c3)
    </li>
  <li>
toplanan_kurallar= np.fmax(c1,c4)
    </li>
   </li>
 </ul>
 
### Durulama

<ul>
    <li>
      Durulama yöntemlerinden Mean of Maximum – En Büyük Üyelik dereceli elemaların orta noktası yöntemi kullandım çünkü diğer    yöntemlere göre daha optimum sonuçlar alındı.
      <ul>
      <li>Python Kodu: <code>durulama_islemi= fuzz.defuzz(hocanin_notu,toplanan_kurallar,'mom')</code></li>
      </ul>
    </li>
  </ul>

### Sistem Üzerinde Oluşturulan Çıktı

#### Girdiler
<img src="https://github.com/celalakcelikk/To-Give-A-Score-To-The-Teacher-With-The-Student-s-Grade-And-Grade-Average-With-Fuzzy-Logic/blob/master/iimages/girdi.png">
