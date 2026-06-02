# Kullanım Rehberi — Profesyonel Sistem
### Bir Hocanın Notları: Nasıl Düşünmeli, Ne Zaman Hareket Etmeli

---

> *"İyi bir analist sinyali doğru okur. İyi bir trader sinyali doğru okur ama bazen yine de girmez. Fark işte orada."*

---

## Bu Sistemi Kimler Kullanmamalı?

Başlamadan önce dürüst olmak gerekiyor. Bu sistem şu durumda olan biri için uygun değil:

- **Her gün mutlaka işlem yapması gerekiyor hisseden biri:** Piyasada her gün "setup" yoktur. Yokken beklemek da bir karardır — ve genellikle en doğrusudur.
- **Stop-Loss koymayı reddeden biri:** Bu sistem seni zarara karşı korur, ama sen korumazsan sistem de koruyamaz.
- **Kaybetmeyi kabullenemeyen biri:** Kayıplar bu işin bir parçasıdır. Sistemi ne kadar iyi kurarsan kur, kaybedeceksin. Mesele kazanıp kazanmamak değil, kazançların kayıplarından büyük olması.

Bunları söylüyorum çünkü çoğu insan sistemi veya indikatörü suçlar. Asıl sorun genellikle araç değil, kullanandır.

---

## Temel Felsefe: Az Karar, Yüksek Kalite

Yılda 200 trade yapmak mı, 40 trade yapmak mı daha iyi? 

Cevap net: **40 iyi trade, 200 rastgele trade'den her zaman üstündür.**

Bu sistem sana her gün sinyal üretmek için değil, **kaliteli fırsatları ayırt etmen** için kuruldu. 

> **Altın Kural:** Eğer 3 dakikada "bu iyi bir setup" diyemiyorsan, değildir.

---

## Sistemin Mimarisi — Hangi Dosya Ne İçin?

```
KATMAN 0 — MAKRO FİLTRE (Her şeyden önce)
  └── evrensel/piyasa-rejimi.pine
      "Bu sinyale güvenilebilir mi? Piyasa bana yardımcı mı karşı mı?"

KATMAN 1 — TREND (Yön nerede?)
  └── [kategori]/trend/trend-suite.pine
  └── evrensel/piyasa-yapisi-suite.pine (Yapıdan emin değilsen)
      "Trendin içindeyim mi, karşısında mıyım?"

KATMAN 2 — MOMENTUM (Güç var mı?)
  └── [kategori]/momentum/momentum-suite.pine
      "Bu hareket tükenmekte mi, güçleniyor mu?"

KATMAN 3 — GİRİŞ (Setup var mı?)
  └── [kategori]/sinyaller/sinyal-suite.pine
  └── [kategori]/volatilite/volatilite-suite.pine
      "Somut bir sebep var mı girmek için?"

KATMAN 4 — KARAR (Risk uygun mu?)
  └── evrensel/risk-odül-hesaplayici.pine
  └── evrensel/goreceli-guc-suite.pine
      "Eğer girsem, ne kadar kaybederim? Mantıklı mı?"
```

Her katmanı geçmeden bir sonrakine gitme. **4. katmana gelemiyorsan zaten girmeyeceksin.**

---

## Analiz Sırası — Adım Adım

### ─── ADIM 0: Grafik Açmadan Önce (2 dakika) ───

Bu adımı atlayan bir analistle çalışmam.

**Her sabah şu soruları sor:**

1. **"Bugün piyasada ne var?"**
   - Merkez Bankası kararı var mı? (TCMB, Fed, ECB)
   - Major ekonomik veri açıklanacak mı? (CPI, NFP, GDP)
   - Jeopolitik/haber riski var mı?
   - *Evet varsa:* O veri açıklanmadan 30-60 dakika önce pozisyon açma. Zaten açıksa çık veya SL'ni daralt.

2. **"Genel piyasa ne tarafta?"**
   - `piyasa-rejimi.pine` haftalık grafikte açık tutulmalı
   - BIST100 / S&P500 / BTC günlük EMA 200'ün neresinde?
   - *Makro Bear ise:* O gün long sinyalleri için çıta çok yüksek tut.

3. **"DXY bugün ne yapıyor?"** (Emtia ve EM hisseleri için)
   - DXY güçleniyorsa: Emtia ve gelişen piyasa hisseleri için sinyaller bu gün daha az güvenilir.

> **Hocanın Notu:** "Çalışmadan önce ortamı oku" ilkesi sadece ticaret için değil, hayatta da geçerlidir. Sahaya çıkmadan önce hava durumuna bakarsın. Grafiğe bakmadan önce makro duruma bak.

---

### ─── ADIM 1: Haftalık Grafik — "Hangi Taraftayım?" (2 dakika) ───

Haftalık grafiği her analiz öncesi açmıyorsan, grafiği hiç açma.

**Kontrol Et:**
- [ ] `piyasa-yapisi-suite.pine` → **Yapı:** HH/HL mi (uptrend) yoksa LH/LL mi (downtrend)?
- [ ] `trend-suite.pine` → EMA 200: Fiyat üstünde mi altında mı?
- [ ] `ichimoku-suite.pine` (opsiyonel) → Bulut altında mı üstünde mi?
- [ ] 52 Haftalık H/L'ye mesafe nedir? (Emtia/hisse için kritik)

**Haftalık Yapıya Göre Karar:**

```
HH + HL + EMA200 üstünde → "Long tarafındayım, setupleri değerlendiriyorum"
LH + LL + EMA200 altında → "Short tarafındayım veya beklemedeyim"
Karma yapı / EMA200 yakını → "Çok dikkatli, mini pozisyonlar en fazla"
```

> **Kritik Uyarı:** Haftalık trende karşı pozisyon açmak "ekstra güçlü" sebep gerektirir. "RSI düşük" yeterli sebep değildir. Ayı trendinde RSI daha da düşüktür.

---

### ─── ADIM 2: Günlük Grafik — "Yapı ve Momentum" (3 dakika) ───

**Kontrol Et:**
- [ ] `piyasa-yapisi-suite.pine` → Son BoS (Break of Structure) var mı?
- [ ] `trend-suite.pine` → EMA 50/200 hizalaması, SuperTrend yönü
- [ ] `momentum-suite.pine` → RSI: 40-60 arasında mı (sağlıklı)? Diverjans var mı?
- [ ] Hacim: Son yükseliş günleri güçlü hacimliydi mi?

**RSI Okuma Rehberi:**
```
RSI 30-45: Zayıf alan (alım için izle ama acele etme)
RSI 45-60: Sağlıklı uptrend (en iyi alım bölgesi)
RSI 60-70: Güçlü momentum (var olanı tut, yeni giriş için geç)
RSI 70+:   Aşırı alım (yeni LONG girme, stop-loss'ları sık)
RSI 30-:   Aşırı satım (SHORT kapatma veya LONG hazırlık — AMA trend kontrol et)
```

> **Hocanın Notu:** "RSI düşük, alırım" en tehlikeli düşünce biçimlerinden biridir. Güçlü bir downtrend'de RSI 30'a düşebilir, oradan 15'e düşebilir. RSI tek başına bir şey söylemez. Sadece trendin içinde momentum için söyler.

**Break of Structure (BoS) Önem Sırası:**
- Haftalık BoS > Günlük BoS > 4S BoS
- Haftalık BoS geldiğinde sistem bir hafta boyunca o yönde işlem arar.

---

### ─── ADIM 3: 4 Saatlik / 1 Saatlik — "Setup Var mı?" (3 dakika) ───

**Bu katmanı atla eğer:**
- Günlük trend karşındaysa
- Piyasa rejimi Bear ise
- Major haber 2 saatten az uzaktaysa

**Kontrol Et:**
- [ ] `sinyal-suite.pine` → Skor kaç? Hangi faktörler eksik?
- [ ] `volatilite-suite.pine` → Squeeze bitti mi? Yön pozitif mi?
- [ ] `momentum-suite.pine` → Stochastic/RSI OS'tan dönüyor mu?
- [ ] Mum formasyonu: Kapanış güçlü mü? Gövde büyük mü?

**Skor Yorumlama — Rejime Göre:**
```
Bull Rejimde:    6/10 → Değerlendirilebilir, 7+/10 → Güçlü
Yatay Rejimde:  7/10 → Min. eşik, 8+/10 → Güçlü
Bear Rejimde:   8/10 bile şüpheli, 9/10 → Belki
```

> **Hocanın Notu:** Skor tek başına yeterli değil. 8/10 skor ama hacim yok = şüpheli. 6/10 skor ama haftalık BoS + squeeze patlama = güçlü. Puanı mekanik okuma, yorumla.

---

### ─── ADIM 4: Risk Hesabı — Girişten ÖNCE (2 dakika) ───

Bu adımı es geçen bir öğrencim olmaz.

**`risk-odül-hesaplayici.pine`'ı Aç ve:**

1. **Stop-Loss Nereye?**
   - Son pivot low'un 1-2 ATR altı (long için)
   - "Burada dursa yanlışlandım" noktası
   - **Asla** round number'ların tam üstü (85.00 TL gibi) — orada herkesin stop-u var

2. **Hedef Nerede?**
   - Minimum 1:2 R:R — her seferinde
   - İlk hedef: Yakın direnç / pivot
   - İkinci hedef: Büyük S/R veya 52H zirve
   - **Asla** "bakacağım çıkarım" — hedef önceden belirlenmeli

3. **Kaç Lot?**
   - Hesaplayıcı otomatik söylüyor
   - %1 risk kuralından sapma — psikolojik rahatlık için

> **Hocanın Notu:** "Ama bu hisse çok iyi görünüyor, biraz daha girebilirim" düşüncesi hesaplayıcının söylediğinden iki kat girmek anlamına gelir. Bu 'conviction' değil, FOMO'dur. Fark edilmesi zordur; fark edilince zaten geç olmuştur.

---

### ─── ADIM 5: Son Kontrol — "Her Şey Uyumlu mu?" (30 saniye) ───

`panel/ana-panel.pine` aç, son bir bakış:

```
Piyasa Rejimi = Bull          ✓
Günlük trend = Bull            ✓
Haftalık yapı = HH/HL          ✓
Skor ≥ 7 (veya rejime göre)   ✓
R:R ≥ 1:2                      ✓
SL belirli                     ✓
Haber riski yok                ✓
→ Pozisyon aç + Alert kur
```

Bir tane bile ✗ varsa: **Neden var? Kabul edebilir mi?**

---

## Trade Sonrası Rutin

Bir trade kapandıktan sonra — kazanınca veya kaybedince — şunu yap:

**Trade Defterine Yaz (5 dakika):**
```
Sembol:
Tarih/Saat:
Giriş Fiyatı:
Stop-Loss:
Hedef:
R:R Oranı:
Skor (sinyal-suite):
Piyasa Rejimi:
Giriş Sebebi (1-2 cümle):
Çıkış Sebebi:
Sonuç (TL/Pip/USD):
Hatam ne oldu? / Ne iyi gitti?
```

Ayda bir defteri gözden geçir. Pattern çıkacak: Hangi setuplarda kazanıyorsun, hangilerde kaybediyorsun. Kaybettiğin setup'ları kesmek kazandığın setup'ları artırmaktan daha hızlı geliştirir seni.

---

## Psikoloji — Kimse Bunu Yazmayor

### Kazandıktan Sonra
Kazanma serisi tehlikelidir. Beyin "ben iyi bir trader'ım, hep kazanacağım" moduna geçer. Sonraki işlemde skor 5/10 bile olsa "bu sefer olur" der. **Kazanma serisi sırasında daha büyük LOT değil, aynı LOT.**

### Kaybettikten Son
Kayıp serisi de tehlikeli. "Zarar kapatayım" düşüncesi seni aynı günde daha büyük pozisyonlara iter. Bu "tilt" durumudur — pokerciler bilir. **Kaybetme serisinde: Lotları küçült veya o gün kapat.**

### "Kaçırıyorum" Hissi
Bir hisse %15 çıktı, sen giremiyorsun. "Neden girmedim, şimdi de girsem mi?" İşte bu noktada girmemelisin. Rally başlamış olan bir harekete girmek, treni hareket edince koşarak atlamaya benzer. Düşersin.

> **Kural:** "Kaçırdım" hissiyle girilen trade, neredeyse her zaman kaybeder.

---

## Varlık Bazında Hızlı Referans

| Kategori | Önce Bak | Sonra Bak | Kritik Dosya |
|----------|----------|----------|--------------|
| **Hisse** | BIST100 rejimi | Sektör | goreceli-guc + piyasa-rejimi |
| **Kripto** | BTC Günlük | BTC Dominansı | volatilite + StochRSI |
| **Kurlar** | Seans zamanı | DXY yönü | seans-suite + pivot |
| **Emtia** | DXY yönü | 52H seviyeleri | korelasyon + piyasa-rejimi |

---

## Alert Kurulumu — Grafik Başında Oturma

Sistemi doğru kullananlar grafik başında oturmaz. Alert kurar, sinyal gelince bakar.

**Kurulması Gereken Alertler (öncelik sırasıyla):**
1. `sinyal-suite` → "Güçlü AL" (8/10+)
2. `piyasa-rejimi` → "Bull/Bear Rejimi Başladı"
3. `volatilite-suite` → "Squeeze Patlama"
4. `piyasa-yapisi-suite` → "Bullish/Bearish BoS"
5. `trend-suite` → "Golden/Death Cross" (long-term trend)

**Kurmaman Gereken Alertler:**
- Her türlü sinyal-suite sinyali (6/10+ gibi) — çok fazla uyarı, hepsine bakarsın, anlam kaybeder
- 15 dakikalık grafikte herhangi bir alert — çok gürültü

---

## Sistemin Boşlukları — Dürüst Değerlendirme

> Bu bölüm sistemi seven birine zor gelen ama söylenmesi zorunlu olan gerçekleri içeriyor.

### Boşluk 1: Skor Sistemi Doğrulanmamış
10 faktörlü skor sistemi teorik olarak mantıklı, ama **hiç backtesti yapılmamıştır**. Gerçekte 8/10 skor 5/10 skordan daha mı karlı? Bilinmiyor.

**Nasıl Kapatırsın?**
- 4-8 hafta paper trading yap (gerçek para yok, kâğıt üstünde)
- Her sinyali not al: Tarih, sembol, skor, giriş, SL, TP, sonuç
- 20+ trade sonra istatistik çıkar
- Win rate ve ortalama R:R hesapla
- Beklenen değer = (Win% × Ort. Kazanç) - (Loss% × Ort. Kayıp)
- Bu pozitifse sistemi canlıya al

### Boşluk 2: Volume Profile (VPVR) Yok
Profesyonellerin en çok kullandığı araçlardan biri: Hangi fiyat seviyelerinde çok işlem yapıldı? Bunlar gerçek destek/direnç'tir.

**Nasıl Kapatırsın?**
- TradingView Premium aboneliği al → "Fixed Range Volume Profile" built-in var
- Pivot-tabanlı S/R ile birlikte kullan, hacim kümesi + pivot = çok güçlü seviye

### Boşluk 3: Faktörler Eşit Ağırlıklı
Sistemde her faktör 1 puan. Ama "günlük RSI diverjansı" ile "hacim 1.3x" aynı ağırlıkta olmamalı.

**Nasıl Kapatırsın?**
- Şimdilik pratik değil — backtest olmadan ağırlık atamak keyfi olur
- Backtestten sonra hangi faktörler gerçekten önemliyse onlara 2 puan ver

### Boşluk 4: Kripto Funding Rates ve On-Chain Verisi Eksik
Binance/Bybit'te funding rate negatife geçmesi kısa vadeli dip sinyalidir. Exchange netflow (borsadan çıkan BTC) uzun vadeli bullish'tir. Bunlar Pine Script'e çekilemiyor.

**Nasıl Kapatırsın?**
- CryptoQuant veya Glassnode ücretsiz/ücretli tier kullan
- Sadece haftalık kontrol yeterli (her gün bakmak gerekmez)

### Boşluk 5: Temel Analiz Bağlantısı Yok
Bir şirketin borsa değeri 10x artmış, F/K oranı 150. Teknik analiz "AL" diyor. Ama temel tablo berbatsa bu nasıl değerlendirilecek?

**Nasıl Kapatırsın?**
- Hisse senedi için: Kısa vadeli (1-4 hafta) trade'lerde temel analiz ikincil
- Uzun vadeli pozisyon (birkaç ay+) tutacaksan temel analiz kritik
- isyatirim.com.tr / finansinvestment / KAP takibi sisteme entegre edilemez ama alışkanlık haline getirilmeli

### Boşluk 6: Trade Defteri Entegre Değil
Sistem sinyaller üretir ama sonuçları takip etmez. Hangi sinyaller karlı, hangileri zararlı?

**Nasıl Kapatırsın?**
- Google Sheets trade defteri (basit ama yeterli)
- Notion veya Excel
- Bu rehberin sonundaki şablon kullan

---

*Notlar sonu: Detaylı varlık bazında notlar için → notlar/ klasörü*
