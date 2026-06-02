# Döviz Kurları (Forex) — Profesyonel Notlar
### EURUSD, USDTRY, GBPUSD, USDJPY ve Tüm Döviz Çiftleri

---

> *"Forex piyasası günde 7 trilyon dolar işlem görür. Bunun büyük çoğunluğu kurumsal oyunculardır. Sen bu piyasada kimsinle oynuyorsun biliyor musun? Aynı masa etrafında oturduğu için değil, ama aynı piyasada var olduğu için bu soruyu sormak önemlidir."*

---

## Forex'i Anlayan Kişi Diğer Piyasaları Da Anlar

Forex piyasası teknik analizin en temiz çalıştığı yerdir. Neden?
- Gerçek likidite var (manipülasyon sınırlı major çiftlerde)
- Belirli saatlerde işlem yoğunlaşır (seanslar)
- Makroekonomik çerçeve sinyalleri destekler
- Teknik seviyeler (pivot, round number, EMA) geniş kitleler tarafından takip edilir

Ama bir tehlikesi var: Kaldıraç. Çoğu forex yatırımcısı kaldıraçla kayıp yaşar. Bu sistem kaldıraçsız/düşük kaldıraçlı yaklaşım için kurgulanmıştır.

---

## Seansları Anlamak — Sistemin Temeli

Bu bölümü ezber bilgi olarak değil gerçek anlayışla öğren.

### Dünya Döviz Seanları (UTC)

```
Seans         Açılış UTC    Kapanış UTC    Özellik
─────────────────────────────────────────────────
Tokyo         00:00          09:00         Dar hareket, JPY çiftleri aktif
Frankfurt     07:00          17:00         Avrupa açılışı
Londra        07:00          16:00         En yüksek hacimli seans
New York      12:00          21:00         Güçlü trend hareketleri
Londra+NY     12:00          16:00         GÜNÜN EN KRİTİK 4 SAATİ
```

### Seanslara Göre Ne Yapalım?

**Tokyo Seansı (00:00-09:00 UTC):**
USD/JPY, AUD/JPY aktiftir. EURUSD genellikle "Asian Range" içinde kalır.
Bu saatte EUR/USD'da yeni pozisyon açmak gürültüye girmektir. İzle, not al.

**Londra Açılışı (07:00-09:00 UTC):**
Büyük kurumsal oyuncular işe başlar. Asian Range sıklıkla kırılır. Bu kırılım yönüne bakılır.
Ama dikkat: Londra açılışında bazen "fake breakout" olur — Asian Range kırılır, sonra döner.
Gecenin haberleri bu saatte fiyatlanır.

**LD/NY Overlap (12:00-16:00 UTC):**
Bu 4 saat, günün geri kalanından daha önemlidir.
- En yüksek likidite
- En güçlü trend hareketleri
- Günlük pivot seviyeleri bu saatte test edilir
- NFP, CPI gibi büyük ABD verileri bu saatte açıklanır

**Pratik Kural:** EUR/USD, GBP/USD gibi çiftler için en güvenilir sinyaller LD/NY overlap dönemindedir. `seans-suite.pine` bunu yeşil arka planla gösteriyor zaten.

**Bir Akşam Pozisyon Açıp Tokyo'ya Bırakmak:**
Riskli. Tokyo'da EUR/USD rastgele gezebilir, stop-loss tetiklenebilir. Eğer bırakacaksan SL'yi geniş tut (ama bu R:R'i bozar) veya bırakma.

---

## Pivot Seviyeleri — Forex'in En Güçlü Referansı

Daily Pivot seviyeleri her gün yenilenir. Dünkü High, Low, Close'dan hesaplanır.

```
PP  = (H + L + C) / 3         Ana denge noktası
R1  = 2×PP - L                İlk direnç
R2  = PP + (H - L)            İkinci direnç
S1  = 2×PP - H                İlk destek
S2  = PP - (H - L)            İkinci destek
```

**Bu seviyeleri nasıl kullanırsın:**
- Sabah grafik açtığında bu seviyeleri işaretle
- PP altında açılış → Bugün satış baskısı daha ağır başlar
- PP üstünde açılış → Bugün alım baskısı daha ağır başlar
- S1'den bounce + LD/NY seansında + bullish mum → Güçlü alım setup'ı
- R1 kırılımı + hacim desteği + trend yönünde → Trend devam setup'ı

**Bir Önemli Püf Noktası:**
R1 ile R2 arasında fiyat gidip geliyorsa, büyük oyuncular bir sonraki yönü "tartışıyor" demektir. Bu bölgede yeni pozisyon açma. Kırılım sonrası gir.

> **Hocanın Notu:** Pivot seviyelerine "mucizevi çizgiler" olarak bakma. Bunlar pek çok yatırımcının baktığı ortak referans noktalardır. Çünkü çok kişi bakıyor, çünkü önem kazanıyor — self-fulfilling prophecy.

---

## Asian Range Stratejisi — Etkili Bir Edge

Bu strateji binlerce trader tarafından yıllardır kullanılır ve hâlâ çalışır.

**Nasıl İşler:**
1. Tokyo seansı boyunca (00:00-09:00 UTC) oluşan High ve Low belirlenir
2. Bunlar "Asian Range"dir (seans-suite.pine bunu çiziyor)
3. Londra açılışında (07:00 UTC itibaren) bu range kırılırsa:
   - Yukarı kırılım → Long fırsat
   - Aşağı kırılım → Short fırsat

**Kırılımın Güçlü Olması İçin:**
- Kırılım Londra seansında (07:00-11:00 UTC arası) gerçekleşmeli
- Hacimle desteklenmeli (volume spike)
- Trend günlük grafikteki yönüyle uyumlu olmalı
- Günlük momentum (RSI 45-60 arası) kırılım yönünü desteklemeli

**Dikkat:**
- Asian Range genişse (100+ pip) bu strateji daha az güvenilirdir
- Dar bir Asian Range (30-60 pip) sonrası kırılım = güçlü potansiyel hareket

---

## DXY — Herşeyin Sahibi

**DXY (USD Endeksi) Forex'in kalp atışıdır.** Tüm USD çiftleri DXY'ye bağlıdır.

DXY yükseliyorsa:
- EUR/USD düşer
- GBP/USD düşer
- AUD/USD düşer
- USD/TRY yükselir (TRY değer kaybeder)

DXY düşüyorsa:
- Yukarıdakilerin tersi

**Pratik Kural:**
- EUR/USD long almadan önce DXY grafiğine bak
- DXY yükseliş trendindeyse EUR/USD long = trendin karşısına gitme
- DXY düşüş trendindeyse EUR/USD long = trendle birlikte git

`seans-suite.pine` DXY verisi göstermiyor ama her analiz öncesi TradingView'da `DXY` yazıp 4 saatlik grafiğe bir saniye bakmak yeterlidir.

---

## Korelasyonlar — Bilmek Zorunda Olduğun Yapılar

Forex'te çiftler birbirleriyle ilişkilidir. Bu ilişkileri bilmeden "diversification" yapamazsın, aksine aynı trade'i iki kez açmış olursun.

**Pozitif Korelasyonlar (aynı yönde hareket):**
- EUR/USD ve GBP/USD: %80+ korelasyon
- EUR/USD ve AUD/USD: Genellikle pozitif
- Anlam: İkisini aynı anda uzun tutmak "iki kez" uzun olmaktır

**Negatif Korelasyonlar (ters yönde):**
- EUR/USD ve USD/CHF: Neredeyse tam ters
- EUR/USD ve USD/JPY: Kısmen ters
- Anlam: EUR/USD long + USD/CHF long = birbirini iptal eder

**Pratik Kural:** Aynı anda benzer korelasyonlu çiftlerde pozisyon tutma. Diversification sandığın şey aynı pozisyon olabilir.

---

## USDTRY — Özel Notlar

USD/TRY Türk yatırımcılar için ayrı bir kategori.

**Yapısal Farklılıklar:**
- USD/TRY tek yönlü tarihsel trend içindedir (uzun vadede TRY zayıflar)
- "Teknik analiz işe yaramaz" yanlış. Kısa vadede işe yarar ama arka plan her zaman TRY aleyhine
- Merkez Bankası müdahaleleri keskin terslemeler yaratabilir

**Ne Zaman İşlem Yapılır:**
- Kısa vadeli swing: 4S-Günlük grafik + pivot seviyeleri
- TCMB toplantısı dönemleri: ÇOK DİKKATLİ, karar öncesi pozisyon açma
- Seçim dönemleri, ekonomik kriz dönemleri: Sistematik analiz dışına çıkılabilir

**Pip Değeri:**
USD/TRY için pip değeri sürekli değişiyor (kur değiştikçe). Risk hesaplayıcıdaki pip hesabı bunu dinamik yapar.

---

## Dosya Kullanım Kılavuzu — Forex İçin

### `seans-suite.pine` — Zorunlu, Her Zaman Açık

1 saatlik veya 15 dakikalık grafikte her zaman açık olmalı.

- Seans arka planları gösteriyor
- Asian Range çiziyor
- Pivot seviyeleri gösteriyor

Yeşil alan (LD/NY Overlap) göründüğünde dikkat modu. En önemli sinyaller buradan gelir.

**Alert Kurulumu:**
- "Londra Açılışı" → Gün başlıyor, güne hazırlık
- "LD/NY Overlap Başladı" → En aktif dönem
- "Asian Break Yukarı/Aşağı" → Sabah fırsatı

### `trend-suite.pine` — Pivot + EMA Kombinasyonu

**En Güçlü Setup:**
Fiyat S1 desteğinde + EMA 21 üstünde + LD/NY seansında + Stochastic OS'tan çıkış = Pivot + Trend + Seans + Momentum = 4 faktör uyumlu.

**Daily Pivot ile EMA'yı nasıl okursun:**
- PP + EMA 200 aynı bölgedeyse → İki ayrı kaynak aynı noktayı gösteriyor → Çok güçlü destek/direnç
- S1 EMA 50 ile çakışıyorsa → Güçlü destek

### `momentum-suite.pine` — Stochastic'e Odaklan

Forex'te Stochastic standart RSI'dan daha yaygın kullanılır.

**Pivot + Stochastic Kombinasyonu:**
Fiyat S1'e geldi + Stochastic 20 altında iken %K %D'yi yukarı kesti = Klasik pivot bounce setup'ı.

**CCI (Commodity Channel Index):**
Momentum-suite'te CCI seçeneği var. Forex'te CCI +100'ün üstüne çıkması güçlü momentum demektir. Breakout setup'larında kullan.

### `risk-odül-hesaplayici.pine` — Pip Bazlı Hesap

Forex'te risk yönetimi pip bazlı yapılır.

**Pratik Hesap:**
```
ATR(14) değeri = örneğin 0.0025 (EUR/USD için)
Bu = 25 pip
SL = 1.5 × ATR = 37.5 pip
Portföy = 10.000 USD, Risk %1 = 100 USD
Lot = 100 USD / 37.5 pip = ?
→ Hesaplayıcı bunu otomatik yapıyor, sadece giriş ve SL gir
```

---

## Özel Stratejiler — Forex

### 1. Asian Range Breakout
```
Koşullar:
✓ Asian Range dar (30-60 pip EUR/USD için)
✓ Londra seansında kırılım (07:00-11:00 UTC)
✓ Kırılım günlük trend yönünde
✓ Hacim desteği var
→ ENTER kapanış bekleme → SL: Asian Range ortası → TP: R1 veya 2×Asian Range
```

### 2. Pivot Bounce + Stochastic OS
```
Koşullar:
✓ LD/NY overlap saatinde (12:00-16:00 UTC)
✓ Fiyat S1 veya PP bölgesine geldi
✓ Stochastic %K < 20 + %K %D'yi yukarı kesti
✓ Trend günlük EMA 50 üstünde
✓ Bullish mum formasyonu (Pin Bar idealdir)
→ ENTER → SL: S1'in altı + 1 × ATR → TP: R1
```

### 3. DXY Konfirmasyonu ile Trend Takip
```
Koşullar:
✓ EUR/USD günlük uptrend (EMA 21 > EMA 50 > EMA 200)
✓ DXY günlük downtrend
✓ 4S pullback var (EMA 21'e kadar geri çekilmiş)
✓ 4S RSI 40-55 arası (sağlıklı)
→ ENTER → SL: Son swing low → TP: Son swing high
```

---

## Haber Takvimi — Zorunlu Bilgi

Bu takvimi bilmeden Forex'te işlem yapma.

**Haftalık Kritik Veriler:**
| Veri | Saat (UTC) | Önem | Not |
|------|-----------|------|-----|
| NFP (ABD İstihdam) | Cuma 13:30 | ⭐⭐⭐ | En volatil andır |
| CPI (Enflasyon) | Salı/Çarşamba 13:30 | ⭐⭐⭐ | Fed faiz beklentisi |
| Fed Toplantısı | Çarşamba 19:00 | ⭐⭐⭐ | 6 haftada bir |
| TCMB Toplantısı | Değişken | ⭐⭐⭐ TRY için | TRY çiftleri |
| GDP | Çeyreklik | ⭐⭐ | Trend yön |

**Kural:** Bu verilerden 1 saat önce ve sonra pozisyon açma. Var olan pozisyonun SL'ini daralt veya kapat.

**Neden?** Bu anlarda anlık hareket 50-100 pip olabilir. Sisteminiz bunu hesaba katmaz.

---

## Psikoloji — Forex'e Özgü

### Kaldıraç Tuzağı
Forex brokerlar çoğunlukla 1:100, 1:200 kaldıraç sunar. Bu rakamlar cazip görünür. Gerçekte:
- 1:100 kaldıraç = %1 yanlış gidersen tümünü kaybedersin
- Bu sistem 1:10'un üzerinde kaldıraç için tasarlanmamıştır
- "Lot büyüklüğü" hesaplanırken kaldıraç sıfırdan düşünülmeli

### Piyasa "Beni Takip Ediyor" Yanılgısı
Pozisyon açtıktan sonra karşı yöne giderse "piyasa benim stop-loss'ımı gördü" düşüncesi yaygındır. Yüzde yüz yanlış. Piyasa seni bilmiyor. Stop-loss'un kötü ayarlandı.

### Günlük Hedef
"Bugün 50 pip kazanacağım" hedefi zararlıdır. Çünkü 50 pip olmayınca daha fazla risk alırsın. Daha fazla risk → daha fazla kayıp.

Hedef olmamalı. Sistem varsa sistem çalıştırılır, sistem yoksa işlem yapılmaz.

---

## Sistem Boşlukları — Forex İçin

### Boşluk 1: Ekonomik Takvim Entegre Değil
Sistem hangi gün-saatte veri açıklanacağını bilmiyor.

**Ne Yapabilirsin?**
- Forexfactory.com → "High Impact" etkinlikler → Her Pazar akşamı 5 dakika bak
- O haftaki kritik günleri not al
- Kritik veri günlerinde sinyal-suite'in eşiğini 8/10'a çıkar

### Boşluk 2: Spread Farkları Dikkate Alınmıyor
Risk-ödül hesaplayıcı spread'i hesaba katmıyor. NFP sonrası spread 10-20 pip'e çıkabilir.

**Ne Yapabilirsin?**
- TP hesaplarken spread + slippage için %5-10 pay bırak
- Seanslar arası (23:00-00:00 UTC) düşük likidite dönemlerinde işlem yapma

### Boşluk 3: Carry Trade Mantığı Yok
Yüksek faizli para birimi tutan pozisyon "faiz farkı" kazanır. Bu trade mantığı sistemde yok.

**Ne Yapabilirsin?**
- Kısa vadeli swing trade yapıyorsan bu önemli değil
- Uzun vadeli pozisyon taşıyorsan faiz swap oranlarına bak (broker platformunda görebilirsin)

### Boşluk 4: COT (Commitment of Traders) Raporu Yok
Her Cuma yayınlanan COT raporu, büyük spekülatörlerin (hedge fund) ve ticari operatörlerin pozisyon durumunu gösterir. "Akıllı para nerede" sorusunun cevabı.

**Ne Yapabilirsin?**
- CFTC websitesi (ücretsiz)
- Barchart.com COT data (ücretsiz, görsel)
- Haftalık 5 dakika bakış yeterli: "Net spekülatif pozisyon artıyor mu azalıyor mu?"
