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

<ul>
<li><code></code></li>
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
      <li>
    Sınıfın not ortalaması=0 ile 100 arasında belirlendi.
      <ul>
      <li>Python Kodu: <code>sinif_ort=np.arange(0,101,0.1)</code></li>
      </ul>
    </li>
    <li>
      <li>
    Öğretmenin puanı=0 ile 10 arasında belirlendi.
      <ul>
      <li>Python Kodu: <code>hocanin_notu=np.arange(0,11,0.1)</code></li>
      </ul>
    </li>
    <li>
 </ul>

