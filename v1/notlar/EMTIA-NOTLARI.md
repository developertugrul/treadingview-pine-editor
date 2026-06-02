# Emtia — Profesyonel Notlar
### Altın, Gümüş, Petrol, Bakır, Doğalgaz ve Tarım Emtiaları

---

> *"Emtia piyasası ham gerçekliğin piyasasıdır. Altın insanın korku ve belirsizlik karşısındaki refleksidir. Petrol küresel ekonominin nefesini ölçer. Bu sinyalleri okuyabilen biri finansal piyasaların tamamını daha iyi anlar."*

---

## Emtiayı Anlayan Piyasayı Anlar

Emtia piyasalarını diğer piyasalardan ayıran en önemli özellik: **Temel arz-talep gerçekleri teknik analizi yönlendirir**, teknik analiz temeli değil.

Bu ne anlama gelir?
- Petrol kuyusu kapanıyor haberi → Arz azalıyor → Teknik direnç kırılabilir
- Çin'in büyüme yavaşladığı haberi → Bakır talebi düşer → Teknik destek tutunamayabilir

Bu yüzden emtia analizinde "hikaye" önemlidir. Teknik seviyeyi gördün, ama o seviyeyi destekleyen veya zayıflatan bir temel faktör var mı?

---

## DXY — Emtia Analizinin Önkoşulu

Bunu ezbere bil: **Çoğu emtia USD bazlı fiyatlanır. Dolar güçlenince emtia ucuzlar (dolar bazında daha az ödenir), dolar zayıflayınca emtia pahalanır.**

Bu ters korelasyon %100 geçerli değildir her zaman, ama genel kural olarak:
```
DXY ↑ (Dolar güçleniyor) → XAUUSD, CL, HG baskı altında
DXY ↓ (Dolar zayıflıyor) → XAUUSD, CL, HG destekleniyor
```

Emtia analizine başlamadan önce `DXY` grafiğini aç. 4 saatlik ve günlük trendine bak. Bu bilgi sinyal kalitesini belirler.

`evrensel/korelasyon-suite.pine` bu ilişkiyi sayısal gösterir. Korelasyon katsayısı -0.5'in altındaysa ters korelasyon güçlü demektir.

---

## Altın (XAUUSD) — Korku Barometresi

Altın diğer emtialardan farklıdır çünkü **hem emtia hem para birimidir.**

### Altının Yükseldiği Durumlar
- Küresel belirsizlik artar (savaş, pandemi, finansal kriz)
- Reel faiz düşer (enflasyon artar ama faiz artışı gecikir)
- Dolar zayıflar
- Merkez bankaları altın alımı artar (son yıllarda Çin, Türkiye, Polonya)
- Borsa düşüşü sırasında "güvenli liman" akışı

### Altının Düştüğü Durumlar
- Reel faiz yükselir (faiz > enflasyon)
- Dolar güçlenir
- Risk iştahı artar (borsa yükselir, volatilite düşer)

### Pratik Kural — Altın için
Altın analizine şu soruyla başla: "Bu hafta reel faiz nerede gidiyor?"
- ABD 10 yıllık tahvil faizi - CPI enflasyon oranı = reel faiz
- Reel faiz yüksekse: Altın dezavantajlı
- Reel faiz düşüyorsa veya negatifse: Altın avantajlı

Bu bilgiyi sisteme ekleyemezsin ama FRED Economic Data sitesinde ücretsiz takip edebilirsin.

### Mevsimsellik — Altın
```
Ocak-Şubat:    Güçlü (Hindistan takı talebi, Çin Yeni Yılı)
Mart-Mayıs:    Zayıflar (yaz öncesi düşüş başlar)
Haziran-Ağustos: Sezonsal dip (yaz ayları)
Eylül-Kasım:   Güçlü (Hindistan düğün sezonu, yıl sonu talebi)
Aralık:        Karışık
```

`korelasyon-suite.pine` bunu her ay başında küçük bir not olarak gösteriyor. Bunlar historik ortalamalardır, her yıl geçerli olmayabilir. Yol gösterici, kural değil.

---

## Gümüş (XAGUSD) — Altının Volatil Kardeşi

Gümüş yarı para birimi yarı endüstriyel metaldir. Bu onu altından daha karmaşık yapar.

### Altın/Gümüş Oranı (GSR) — Önemli Gösterge

```
GSR = Altın Fiyatı / Gümüş Fiyatı
```

Tarihsel olarak 70-80 bandında olmuştur.

```
GSR > 85: Gümüş çok ucuz (tarihsel ortalamaya göre)
          → Altına göre gümüş değer kazanabilir
          → Portföyde altın azalt, gümüş artır stratejisi

GSR < 65: Altın görece ucuz
          → Gümüş fazla değer kazanmış olabilir
```

`korelasyon-suite.pine` bu oranı hesaplar ve grafikte gösterir.

### Gümüşün Özellikleri
- Altından %50-100 daha volatil
- Endüstriyel kullanım (güneş paneli, elektronik) talebini belirler
- Ekonomik büyüme dönemlerinde altından daha iyi performans gösterir
- Ekonomik daralma dönemlerinde altından daha kötü performans gösterir

---

## Petrol (CL1! / USOIL) — Küresel Ekonominin Nefesi

Petrol fiyatı sadece taşıt yakıtı değil, tüm üretim ve lojistik maliyetleri demektir. Bu yüzden petrol enflasyonun öncü göstergesidir.

### Petrolü Etkileyen Temel Faktörler

**Arz Tarafı:**
- OPEC+ kararları (genellikle her 2-3 ayda bir toplantı)
- ABD shale oil üretimi (haftalık Baker Hughes rig sayısı)
- Körfez krizi/jeopolitik risk
- Rusya üretimi ve ihracatı

**Talep Tarafı:**
- Çin ekonomik aktivitesi (petrolün en büyük ithalatçısı)
- Küresel PMI verileri (yüksek PMI = üretim aktivitesi = petrol talebi)
- Mevsim: Kış ısınma + Yaz sürüş sezonu

### Kritik Raporlar — Petrol

**EIA Haftalık Petrol Stok Raporu (Çarşamba 15:30 UTC):**
ABD petrol stok değişimi. Stok düşerse → Talep güçlü veya arz zayıf → Fiyat yükselir.
Stok arrarsa → Talep zayıf veya arz güçlü → Fiyat düşer.

Bu rapor öncesinde/sonrasında petrol fiyatı hareket eder. Rapor günü yeni pozisyon açma tavsiyem bu nedenle.

**API Raporu (Salı akşamı):**
EIA'nın gayri resmi ön göstergesi. EIA'dan önce yayınlanır. "Sürpriz" gelebilir.

### Mevsimsellik — Petrol
```
Ocak-Şubat:  Kış ısınma talebi
Mayıs-Ağustos: Sürüş sezonu, tatil talebi (ABD)
Eylül-Kasım:  Talep yavaşlar
```

---

## Bakır (HG) — Ekonomi Barosu

Bakır ekonomik aktivitenin en iyi öncü göstergelerinden biridir. İnşaat, otomobil, elektronik — her şeyde bakır var.

**"Dr. Copper" olarak da bilinir:** Bakır fiyatı yükseliyorsa global ekonomi büyüyor demektir.

Bakır + Küresel hisse senetleri çoğunlukla pozitif korelasyonludur.
Bakır düşüyor + Borsa düşüyor = Resesyon sinyali.

---

## Doğalgaz (NG1!) — En Mevsimsel Emtia

Doğalgaz mevsimselliği en belirgin emtiadır.

```
Kış (Aralık-Şubat): Isınma talebi → Fiyat yüksek
Yaz (Haziran-Ağustos): Serin hava/AC talebi → Fiyat görece düşük
Bahar/Sonbahar: Düşük talep dönemleri
```

Fakat: Hava beklenmedik sıcaklıklara (çok sıcak yaz veya çok soğuk kış) giderse sistem bu mevsimselliği bozar.

Doğalgaz teknik analizi zor bir emtiadır. Yüksek volatilite ve mevsimsel bozulmalar nedeniyle bu sistemi kullanırken çok dikkatli ol.

---

## Dosya Kullanım Kılavuzu — Emtia İçin

### `piyasa-rejimi.pine` — DXY ile Filtreleme

Emtia için benchmark seçimi önemli:
- Altın/Gümüş için: `TVC:DXY` — DXY Bear iken rejim Bull kabul et
- Petrol/Bakır için: Küresel büyüme proxy olarak `SP:SPX` kullanılabilir
- Genel: `BIST:XU100` yerine `TVC:DXY` veya `SP:SPX` daha anlamlı

> **Dikkat:** DXY ile emtia ters korelasyonlu olduğu için `piyasa-rejimi`'ne DXY koyduğunda piyasa rejimi "Bear" görünse (DXY Bear) bu emtia için aslında pozitif demektir. Bu kavramsal kafa karışıklığını yönet.

**Basit Kural:** DXY haftalık grafik EMA 200'ün altındaysa → Emtia için long sinyallerini daha güvenilir kabul et.

### `korelasyon-suite.pine` — Önce Aç, Sonra Diğerlerine Bak

Bu dosya emtia analizinde birinci basamaktır.

**Nelere Bak:**
1. **DXY korelasyonu:** Güncel korelasyon katsayısı nerede? (-0.5 altı = güçlü ters korelasyon, emtia için DXY önemli)
2. **DXY'nin son yönü:** Yükseliş mi düşüş mü? Emtia için ters yorumla.
3. **Altın/Gümüş Oranı:** 85 üstüyse gümüş ucuz, 65 altıysa altın ucuz.
4. **Mevsimsel Not:** Ay başında küçük etiket çıkıyor — referans için bak.

### `trend-suite.pine` — Haftalık'tan Başla

Emtia için haftalık grafik kritik. Günlük grafik gürültülü olabilir.

**52 Haftalık Seviyeleri Kullan:**
```
52H Zirveye < %5 mesafe → Güçlü direnç yakın, yeni long için dikkatli
52H Dibe   < %5 mesafe → Güçlü destek yakın, long fırsatı olabilir
52H'in kırılması → Büyük hareket potansiyeli
```

Bu seviyeler `trend-suite`'te otomatik işaretleniyor.

**EMA Kullanımı — Emtia Özel:**
- EMA 200 günlük = Uzun vadeli bull/bear sınırı
- EMA 20 günlük = Kısa vade momentum
- EMA 50 günlük = Bu iki arasındaki orta vade

Emtia trendleri hisse senetlerinden daha uzun sürebilir. 6-12 aylık trend zayıflama yaşamaması nadir değildir.

### `momentum-suite.pine` — RSI Diverjansı Emtia'da Güçlü

Altın özellikle RSI diverjanslarına tepki verir. Aylar süren düşüş sonrası RSI bullish divergence verirse ciddi dip sinyali olabilir.

**Volume Uyarısı:**
Bazı emtia spot grafiklerde (TradingView'da XAUUSD spot) hacim verisi anlamsız olabilir. Futures kontratlarında (GC1!, CL1!) hacim anlamlıdır.

`momentum-suite`'teki hacim analizi futures kontratı kullandığında daha güvenilirdir. Spot altın grafiğinde hacim verisi olmayabilir — bu normal.

### `risk-odül-hesaplayici.pine` — Emtia İçin SL Stratejisi

Emtia volatil olduğu için SL'yi geniş tutmak gerekebilir, bu da lot küçültür.

```
Altın (XAUUSD): ATR genellikle 15-30 USD arasında
SL = 2 × ATR = 30-60 USD mesafe

Petrol (CL): ATR genellikle 1-2 USD arasında
SL = 2 × ATR = 2-4 USD mesafe

Doğalgaz (NG): ATR çok değişken, 0.1-0.3 olabilir
SL = 2.5 × ATR (daha geniş)
```

---

## Özel Stratejiler — Emtia

### 1. Altın — DXY Zayıflama + Fibonacci Bounce
```
Koşullar:
✓ DXY haftalık trendde düşüş
✓ XAUUSD günlük EMA 200 üstünde
✓ Fibonacci 61.8% veya 50% bölgesinde pullback
✓ Haftalık RSI 45-60 arası (sağlıklı)
✓ Bullish mum formasyonu haftalık veya günlük
✓ Korelasyon-suite: DXY ters, emtia destekleniyor
→ ENTER → SL: Fibonacci altı + 1×ATR → TP: Son zirve veya 2:1 R:R
```

### 2. 52 Haftalık Dip Bounce
```
Koşullar:
✓ Fiyat 52H dibe < %3 mesafe
✓ Haftalık mum bullish (hammer, engulfing)
✓ RSI haftalık < 30 (veya diverjans)
✓ DXY zayıflama eğiliminde
→ Bu nadiren görülen ama yüksek beklentili setup
→ SL: 52H dibin %2-3 altı
```

### 3. Mevsimsel + Teknik Birleşim
```
Örnek: Altın Eylül-Ekim (güçlü mevsimsel dönem)
Koşullar:
✓ Eylül-Ekim dönemindeyiz
✓ Günlük trend Bull (EMA 200 üstü)
✓ Squeeze bitti veya bullish BoS var
✓ DXY aynı dönemde zayıf
→ Skor daha düşük olsa bile bu dönemde setuplara daha açık bakılabilir
```

---

## Emtia Özel Uyarılar

### OPEC+ Toplantıları (Petrol)
Bu toplantılar genellikle 6 haftada bir, bazen acil toplanırlar. Kararlar petrolü %5-10 hareket ettirebilir.
- Üretim kesintisi kararı → Petrol yükselir
- Üretim artışı kararı → Petrol düşer
OPEC toplantısı öncesi petrol pozisyonu taşıma riskli.

### Tarımsal Emtialar (Buğday, Mısır, Soya)
- Hava durumu raporları fiyatı ani hareket ettirir
- USDA raporları (aylık: World Agricultural Supply and Demand Estimates - WASDE) kritik
- Brezilya ve ABD hasat raporları
Tarımsal emtia teknik analizin dışına çıkabileceği için bu sistemi kullanırken çok dikkatli ol.

### Bakır ve PMI
Her ayın başında yayınlanan PMI verileri bakır fiyatı için öncü sinyaldir. PMI > 50 = büyüme = bakır talebi güçlü. Bu veriyi almadan bakır pozisyonu taşıma.

---

## Uzman Notu: Emtia Döngüsü

Emtia piyasaları büyük döngüler içinde hareket eder (commodity supercycle). Bu döngüler 10-15 yıl sürebilir.

2020'lerin başında başlayan döngü argümanları:
- Yıllarca yetersiz yatırım (kapasitesizlik)
- Enerji geçişi (bakır, lityum, nikel talebi artışı)
- Jeopolitik kısıtlamalar
- Enflasyonist baskılar

Bu bağlamda düşünürsen: Geçici bir "teknik düşüş" mü uzun vadeli bir geri çekilme mi diye sormayı bil.

---

## Sistem Boşlukları — Emtia İçin

### Boşluk 1: Temel Arz-Talep Verisi Yok
Sisteme petrol stok raporu, altın ETF akışı, bakır LME stokları girmiyor.

**Ne Yapabilirsin?**
- EIA haftalık rapor → EIA.gov (ücretsiz)
- Altın ETF akışları → Bloomberg veya WGC (World Gold Council) ücretsiz haftalık bülten
- LME bakır stokları → LME websitesi

Bu verilere haftada bir bakış yeterlidir. Trend değişimi analizi için kullanılır.

### Boşluk 2: COT Raporu (Commitment of Traders) Yok
Her Cuma yayınlanan COT raporu: "Büyük spekülatörler net long mu net short mu?"

Emtia piyasasında bu veri altın ve petrol için çok güçlüdür.

**Ne Yapabilirsin?**
- Barchart.com → Commitment of Traders → İlgili emtia → Net spekülatif pozisyon
- Spekülatörler tarihsel zirve net long → Fiyat zirveye yakın olabilir
- Spekülatörler tarihsel dip net short → Fiyat dip yakın olabilir

### Boşluk 3: Mevsimsel Veriler Yüzeysel
`korelasyon-suite`'teki mevsimsel notlar sadece yazılı referanstır, veri tabanlı değildir.

**Ne Yapabilirsin?**
- Seasonax.com (ücretli) detaylı emtia sezonalligi
- TradingView'da bazı ücretsiz mevsimsel indikatörler var (search: "seasonality")

### Boşluk 4: Spot vs Futures Fiyat Farkı (Contango/Backwardation)
Futures fiyatı spot fiyattan farklı olabilir. "Contango" (futures > spot) ETF tutanlara maliyet çıkarır. Bu sistem bunu hesaba katmıyor.

**Ne Yapabilirsin?**
- Kısa vadeli trading yapıyorsan önemsizdir
- Uzun vadeli tutma düşünüyorsan fiziksel ürün veya iyi yapılandırılmış ETF tercih et
