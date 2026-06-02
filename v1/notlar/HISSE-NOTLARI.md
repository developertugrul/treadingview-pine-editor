# Hisse Senedi — Profesyonel Notlar
### BIST + Global Hisseler için Detaylı Rehber

---

> *"BIST'te para kazanmak hem çok kolay hem çok zordur. Kolay çünkü çoğu katılımcı duygularıyla hareket eder. Zor çünkü sen de insansın ve aynı tuzaklara düşersin."*

---

## BIST'i Anlamak — Diğer Piyasalardan Farkı

BIST'i dünya borsalarından ayıran birkaç yapısal özellik var. Bunları bilmeden sistemi kullanmak eksik kalır.

**1. İnce Piyasa, Kolay Manipülasyon**
BIST'in birçok hissesinde günlük işlem hacmi küçüktür. Bu şu anlama gelir: Büyük bir oyuncu kolayca fiyatı hareket ettirebilir. Günlük hacmi 1-2 milyon TL olan bir hissede teknik analiz daha az güvenilirdir. Hacim 50 milyon TL+'dan büyük hisselerde teknik analiz anlamlı çalışır.

**Pratik Kural:** `momentum-suite` açıkken relative volume bakıyorsun ya — o sayı 0.3-0.5 ise "bu hacim konuşmuyor" demektir. Sinyal gelse bile girme.

**2. TL Devalüasyonunun Baskısı**
Türkiye'nin kronik enflasyon ve kur sorunu var. Bu şu anlama gelir:
- Dolar bazlı bir yatırımcı olarak BIST hissesi alıyorsan, hem hisse hem kur riskini alıyorsun
- TL'de "nominal fiyat arttı" ama dolar bazında ne oldu?
- Altın veya dolar endeksli hisseler (teknoloji, savunma, ihracat) enflasyon dönemlerinde daha iyi korunur
- Kur yükselişi → İhracatçılar kazanır, ithalatçılar zorlanır

**3. Yabancı Para Akışı**
Yabancı yatırımcılar BIST'in yaklaşık %60'ını elinde tutardı, son yıllarda bu oran düştü. Ama hâlâ önemli. Yabancı girişi/çıkışı fiyatları ciddi hareket ettirir. Foreks piyasasında TRY güçleniyorsa → yabancı girişi → BIST için pozitif. Bu `goreceli-guc-suite`'te benchmark olarak `BIST:XU100` yerine zaman zaman `USD/TRY` koyup bak.

**4. TCMB ve Merkez Bankası Kararları**
Türkiye Merkez Bankası kararları BIST'i derinden etkiler:
- Faiz artışı → Kısa vadede BIST'e baskı (para tahvile kayar) ama uzun vadede TL'yi güçlendirir
- Faiz indirimi → Kısa vadede BIST'e destek (ucuz para borsa girer) ama TL zayıflar

**Pratik Kural:** TCMB toplantısı günleri (genellikle ayın son Perşembesi veya belirli tarihler — takvimi takip et) pozisyon aç veya açık tutma. Karar sonrası yönü anlayınca gir.

---

## Hangi Hisselere Bakmalısın?

### Tercih Edilmesi Gerekenler
- **Büyük hacimli, likit hisseler:** THYAO, GARAN, SAHOL, FROTO, ISCTR, BIMAS, SISE, AGHOL
- **Sektör öncüleri:** Sektördeki en güçlü 2-3 hisse (goreceli-guc ile tespit et)
- **Güçlü bilançolar:** En azından yılda bir bilançoya bak — teknik analiz temel analizi geçersiz kılmaz

### Dikkatli Olunması Gerekenler
- **Düşük hacimli hisseler:** Günlük 5-10 milyon TL altı
- **Sert düşmüş "ucuz görünen" hisseler:** "Bu kadar düştü artık çıkar" düşüncesi tehlikelidir. Düşen bir hisse daha da düşebilir.
- **Haberle hareket eden hisseler:** KAP açıklamalarıyla aniden uçan/düşen hisseler spekülatif. Teknik analiz burada işe yaramaz.

---

## Dosya Kullanım Kılavuzu — Hisse İçin

### `piyasa-rejimi.pine` — Her Şeyden Önce
```
Benchmark: BIST:XU100
Zaman Dilimi: Haftalık
```
- XU100 haftalık EMA 200'ün altındaysa: O hafta içinde yeni long açma eğilimi düşür
- XU100 Bear rejiminde: Sadece en güçlü hisselerde, sadece en yüksek skorlarda işlem yap
- XU100 Bull rejiminde: Sistem normal çalışır, eşikler gevşeyebilir

### `trend-suite.pine` — Yön Pusolası

**Hisse için en kritik EMA'lar:**
- **EMA 200 (günlük):** Uzun vadeli Bull/Bear sınırı. Fiyat altındaysa başka seçeneklere bak.
- **EMA 50 (günlük):** Orta vadeli trend. Fiyat EMA50 altına düştüğünde swing pozisyon tutmak riskli.
- **EMA 21 (günlük):** Momentum takipçisi. Güçlü bir uptrend'de fiyat bu EMA'yı destek olarak kullanır.

**VWAP Kullanımı (intraday — çok önemli):**
VWAP sadece intraday (15 dakika, 1 saat) grafiklerde anlamlıdır. `trend-suite` günlük grafikte açıkken VWAP otomatik gizlenir, merak etme.

- Fiyat VWAP üstünde açılıyor → O günkü güç alıcı tarafta
- Fiyat VWAP altına düşüyor → O günkü momentum satıcıda
- **Altın kural:** Sabah VWAP üstüne çıkan bir hisse öğleden sonra genellikle daha güçlü seyreder

**Golden Cross/Death Cross:**
- Günlük Golden Cross (EMA50/200 kesişimi): Uzun vadeli trend değişimi. Gerçekleştiğinde alert kur, hemen girme — genellikle geri çekilip test eder.
- Death Cross: Uzun pozisyonları gözden geçir.

> **Hocanın Notu:** EMA'lar "gecikmeli" göstergedir. Sana fiyatın nerede olduğunu değil, ne yönde gittiğini söyler. "EMA 200 burada olduğu için alırım" değil, "EMA 200 üstündeyken alınan sinyaller daha güvenilir" şeklinde düşün.

### `piyasa-yapisi-suite.pine` — Yapıyı Oku

**BIST'te Break of Structure nasıl görünür?**
Bir hisse 3 aydır HH/HL yapıyordu. Sonra son Higher Low'u aşağı kırdı (LL oluştu) — bu bir Bearish BoS'tur. "Trend bitti, en azından yavaşladı" anlamına gelir.

**Pratik:** BoS sinyali geldiğinde pozisyon taşıma. Yeni yön belirlenene kadar kenara çekil.

### `momentum-suite.pine` — Gücü Ölç

**Hisse için en değerli sinyal: RSI Divergence**
```
Bullish Divergence:
- Fiyat yeni bir dip yaptı (önceki dipten düşük)
- RSI yeni bir dip YAPMADI (önceki dipten yüksek)
= "Satış gücü tükeniyor, dönüş yakın olabilir"
```
Bu sinyal günlük grafikte geldiğinde çok güçlüdür. Ama tek başına yeterli değil — trend desteği, hacim, formasyon da gelmeli.

**OBV (On Balance Volume):**
OBV fiyattan önce hareket eder çoğu zaman. OBV yeni zirve yapıyor ama fiyat hâlâ eski zirvenin altında = gizli güç, bir sonraki hamlede fiyat takip edebilir.

### `volatilite-suite.pine` — Patlama Yakalamak

Hisse senedinde BB Squeeze çok güçlü bir araçtır. Bir hisse uzun süre sıkıştığında (Squeeze aktif), o sıkışmanın kırıldığı an büyük hareket gelir.

**Püf Noktası:** Squeeze başladığında soyut olarak "bekle" değil, SL ve TP seviyelerini önceden belirle. Çünkü hareket geldiğinde çok hızlıdır, düşünmeye vakit kalmaz.

**Squeeze Süresi = Hareket Büyüklüğü:**
- 5-10 bar squeeze → Küçük hareket
- 15-25 bar squeeze → Önemli hareket
- 30+ bar squeeze → Potansiyel büyük breakout

### `goreceli-guc-suite.pine` — Hisse Seçiminin Sırrı

Bu araç profesyonellerin amatörlerden ayrıldığı yerdir.

**Senaryo:** BIST %3 düştü. THYAO sadece %0.5 düştü. Göreceli Güç = THYAO çok güçlü.
Piyasa düzeldığinde THYAO daha çok çıkacaktır.

**Senaryo 2:** BIST %2 çıktı. SAHOL %4 çıktı. Göreceli Güç pozitif. SAHOL lideri.

**Nasıl Kullanırsın:**
1. `goreceli-guc-suite.pine` aç, benchmark = BIST:XU100
2. RS Çizgisi artıyorsa → Bu hisse endeksten güçlü = LONG için prefer et
3. RS Çizgisi düşüyorsa → Bu hisse endeksten zayıf = Aynı sektörde güçlü olanı ara

> **"Savunmacı Güç"** en nadir ve en değerli sinyaldir: Piyasa düşerken RS yüksek kalıyor. Bu, büyük paraların bu hisseyi tercih ettiğinin işaretidir.

### `risk-odül-hesaplayici.pine` — Hesap Yapmadan Girme

Hisse için stop-loss nereye koyulur?

```
Agresif SL: Son önemli pivot low'un %1-2 altı
Konservatif SL: Son önemli destek bölgesinin altı
ATR Bazlı SL: Giriş fiyatı - (1.5 × ATR(14))
```

**Önemli:** Stop-loss round number'ların hemen altına koyma. "Stop-loss 84.50'nin altında" yerine "Stop-loss 83.75'te" — çünkü 84.50 civarında herkesin stop-u var, manipülatörler bilir.

---

## Özel Stratejiler — Hisse

### 1. Pullback in Uptrend (En Güvenilir Setup)
```
Koşullar:
✓ Haftalık EMA 200 üstünde
✓ Günlük HH/HL yapısı devam ediyor
✓ EMA 21 veya 50'ye geri çekiliyor (pullback)
✓ RSI 40-55 arasında (aşırı satıma girmeden)
✓ Hacim pullback sırasında düşüyor (normal satış, panik değil)
✓ Bullish mum formasyonu (Hammer, Engulfing)
→ ENTER → SL: Son pivot low altı → TP: Önceki zirve
```

### 2. Squeeze Breakout
```
Koşullar:
✓ BB Squeeze 15+ bar aktif
✓ Squeeze bitti
✓ Momentum yönü: pozitif
✓ Günlük trend aynı yönde
✓ Hacim Squeeze kırılımında artıyor
→ ENTER → SL: Squeeze'nin içi (alt band) → TP: Hareket büyüklüğüne göre
```

### 3. Bullish Divergence Reversal
```
Koşullar:
✓ Fiyat downtrend içinde yeni dip
✓ RSI günlük divergence veriyor
✓ Haftalık trend henüz bozulmamış (LH/LL değil)
✓ Önemli destek bölgesinde
✓ Bullish mum formasyonu
→ ENTER → SL: Son dip altı → TP: Son LH seviyesi
```

---

## Zamanlamanın Püf Noktaları

### BIST Açılış Saati — 10:00-10:30
Bu yarım saatte çoğu gece haberi fiyatlanır. Büyük boşluklar açılır. Yeni pozisyon açmak için en kötü zamandır.
- **Yapılması gereken:** Seyreti, nereye gittiğini gör.
- **10:30 sonrası:** Yön belirlenmiş olur, giriş için daha güvenli.

### Öğleden Sonra 13:00-14:00
BIST'te genellikle "öğle durgunluğu" yaşanır. Hacim düşer, fiyat sallanır. Bu saatte açılan pozisyonlar gürültüye maruz kalır.

### Kapanışa 1 Saat Kala — 17:00+
Günlük kapanışa doğru kurumsal alım/satım aktifleşir. "Günlük kapanış fiyatı" çok önemlidir — güçlü kapanış sabah açılışa da momentum verir.

### Haftalık Kapanış — Cuma 18:00
Haftalık kapanış fiyatı belki en önemli fiyattır. Bir hissenin haftalık grafikte EMA 200'ün üstünde kapanması çok farklı bir anlam taşır.

---

## Risk Yönetimi — Hisse Özel

### Pozisyon Boyutu
- Tek hisse: Portföyün max %10-15'i
- Tek sektör: Portföyün max %30'u
- Toplam açık pozisyon: Portföyün max %60-70'i (geri kalanı nakit/hazır)

### Trailing Stop
Pozisyon +2 ATR kâra geçtiğinde SL'yi giriş fiyatına çek (kırılmaz kural: kâra dönen trade artık zarar yapmaz).
+3 ATR kâra geçtiğinde SL'yi +1 ATR'ye çek.

### Temettü Tarihleri
BIST'te temettü dağıtımı sonrası fiyat "eksiye düşer" (temettü ex-date). Bu sürpriz değil, beklenebilir. Temettü tarihine yakın açtığın uzun pozisyon bu düşüşü hesaba katmalı.

---

## Sık Yapılan Hatalar — Hisse

1. **"Düştü çıkar" mantığıyla %50-%60 düşmüş hisseleri almak.** Bunlar düşmüş değil, dönüşüme girmiş olabilir.
2. **Haberlere dayalı işlem yapmak.** "Şirketten iyi haber çıktı, alayım" — bu bilgi zaten fiyatlanmış.
3. **Çok fazla çeşitlendirme.** 20 farklı hisse tutmak bir portföy stratejisi değil, kararsızlığın örtüsüdür.
4. **Stop-Loss koymamak.** "Bu güvenli hisse, düşmez." — Her hisse düşer.
5. **Mevsimsel tuzaklar.** Yaz ayları (Temmuz-Ağustos) BIST'te hacim düşer, fiyatlar teknik analizden sapabilir.

---

## Sistem Boşlukları — Hisse İçin

### Boşluk 1: Temel Analiz Entegre Değil
Bu sistem tamamen teknikal. Bir şirketin borç yükü, büyüme oranı, kâr marjı sisteme yansımıyor.

**Ne Yapabilirsin?**
- Sadece "sağlıklı bilançolu" hisseleri izleme listene al
- isyatirim.com.tr → Temel analiz ekranı → Filtrele: Yüksek kâr marjı, düşük borç
- Bu filtreyi geçen hisseler arasından teknik sinyal ara

### Boşluk 2: Sezonsal Veriler Yok
BIST'te bazı sektörler mevsimseldir. Turizm sektörü yaz öncesi güçlenir, inşaat kış döneminde zayıflar.

**Ne Yapabilirsin?**
- Sektöre göre mevsimsel beklentiyi manuel olarak bil
- Zirve dönemine yaklaşıldığında pozisyon büyüklüğünü azalt

### Boşluk 3: Kurumsal Akış Verisi Yok
Kim alıyor, kim satıyor? Yabancı mı yerli mi? Bu veri BIST'te kamuya açılmıyor.

**Ne Yapabilirsin?**
- BIST Takas verileri (Bistech) yayınlanır — büyük işlemleri görebilirsin
- goreceli-guc artıyorsa → muhtemelen akıllı para giriyor
- Hacim spike + fiyat artışı + RS güçleniyor = kurumsal alım olabilir

### Boşluk 4: Stop-Loss Seviyeleri Dinamik Değil
Sistem sabit ATR çarpanı kullanıyor. Piyasanın volatilite rejimi değiştiğinde (örn. pandemi dönemi) bu çarpan yeterli olmayabilir.

**Ne Yapabilirsin?**
- Volatilite yüksekse (BB genişse): ATR çarpanını 2.5'e çıkar
- Volatilite düşükse (BB darsa): ATR çarpanını 1.5'e indir
- `risk-odül-hesaplayici`'deki `atr_mult` parametresini buna göre ayarla
