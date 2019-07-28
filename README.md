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
## Projenin Çalışma Şeması

### Problemin Giriş
Girdi değerlerimiz öğrenci notu ve sınıfın ortalama notudur.
<ul>
  Öğrencinin Not Aralıkları:
    <li>
    İyi: 50-100-100
    </li>
    <li>
    Orta: 30-50-70
    </li>
    <li>
    Kötü: 0-0-50
    </li>
</ul>




