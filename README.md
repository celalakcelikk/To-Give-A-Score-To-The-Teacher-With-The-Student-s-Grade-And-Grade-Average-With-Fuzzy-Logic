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
      <li>Python Kodu:<code>ogrenci_iyi=fuzz.trimf(ogrenci,[50,100,100])</code></li>
      </ul>
    </li>
    <li>
    Orta: 30-50-70
      <ul>
      <li>Python Kodu:<code>ogrenci_orta=fuzz.trimf(ogrenci,[30,50,70])</code></li>
      </ul>
    </li>
    <li>
    Kötü: 0-0-50
    <ul>
<li>Python Kodu:<code>ogrenci_orta=fuzz.trimf(ogrenci,[0,0,50])</code></li>
      </ul>
    </li>
</ul>
<ul>
  Sınıfın Not Ortalaması:
    <li>
    İyi: 50-100-100
      <ul>
      <li><code>sinif_ort_iyi=fuzz.trimf(sinif_ort,[50,100,100])</code></li>
      </ul>
    </li>
    <li>
    Orta: 30-50-70
      <ul>
      <li><code>sinif_ort_orta=fuzz.trimf(sinif_ort,[30,50,70])</code></li>
      </ul>
    </li>
    <li>
    Kötü: 0-0-50
      <ul>
      <li><code>sinif_ort_kotu=fuzz.trimf(sinif_ort,[0,0,50])</code></li>
      </ul>
    </li>
</ul>

<ul>
<li><code></code></li>
</ul>
      
## Problemin Çıktısı

Çıktımız öğretmenin puan bilgisidir.



