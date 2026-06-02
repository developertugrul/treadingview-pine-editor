# Kripto Para — Profesyonel Notlar
### BTC, ETH ve Altcoin Piyasaları için Detaylı Rehber

---

> *"Kripto piyasası insanlık tarihinin gördüğü en büyük spekülatif oyundur. Bu hem fırsat hem tuzak demektir. Farkı bilen kazanır, bilmeyen öğretim ücreti öder."*

---

## Kripto'yu Diğer Piyasalardan Ayıran 5 Şey

Kripto sadece "daha volatil bir hisse senedi" değildir. Temel yapısı farklıdır.

**1. BTC Her Şeyin Babasıdır**
BTC düşerken altcoin alma. Bu kural yüzlerce kez kanıtlanmıştır. BTC %5 düştüğünde altcoinler %15-20 düşer. BTC %5 çıktığında altcoinler %10 çıkabilir. Piyasa yapısı hiyerarşiktir.

Her analiz öncesi BTCUSDT günlük grafiğine bak. BTC Bear trendindeyse altcoin analizleri geçersizdir.

**2. 24/7 Piyasa — Hafta Sonu Farkı**
Hisse senedinden farklı olarak kripto haftanın 7 günü açıktır. Ama bu fark yaratır:
- Hafta sonu hacim düşer, manipülasyon kolaydır
- Pazartesi sabahı kurumsal reaksiyon gelir (gece haberleri fiyatlanır)
- Büyük likidite sağlama genellikle Pazartesi-Perşembe dönemindedir

**Pratik Kural:** Cuma akşamı açık büyük pozisyon taşımak risklidir. Hafta sonunda fiyat her iki tarafa da gidebilir.

**3. Likidite Sweepleri — "Kukla Oynatma"**
Kripto'nun büyük oyuncuları (whale'ler) kasıtlı olarak "obvious" stop-loss seviyelerini arar ve fiyatı oraya kadar iter — insanları siler — sonra gerçek yöne döner.

Bu neden önemli? Round number'ların (30.000, 40.000 gibi) hemen altındaki stop-loss'lar çok hassas. Büyük oyuncular oraya "bakmayı" sever.

**Pratik Kural:** Stop-loss'ları round number'ların tam altına koyma. 30.000 yerine 29.650 gibi "awkward" seviyelere koy.

**4. Funding Rates — Görünmez El**
Vadeli işlem (futures) piyasasında "funding rate" adlı bir maliyet var. Long pozisyon sahipleri short pozisyon sahiplerine (veya tam tersi) periyodik ödeme yapar. Bu oran piyasa yönelimini gösterir:
- Funding çok pozitif = Piyasa "çok long" = Tersine dönme riski
- Funding negatif = Piyasa "short yüklenmiş" = Sürpriz yükseliş olabilir

Bu veri Pine Script'e çekilemiyor ama Binance/Bybit'te ücretsiz görebilirsin.

**5. Altcoin Sezonu — Döngüsel Dinamik**
BTC rallisi başlar → BTC dominansı yükselir → ETH BTC'yi geçmeye başlar → ETH rally eder → Sonra büyük altcoinler (BNB, SOL) → Sonra mid-cap → Sonra small-cap → BTC dominansı düşer

Bu döngünün neresindeyiz? `goreceli-guc-suite`'te benchmark olarak BTC.D (BTC Dominans) kullan. BTC.D düşüyorken altcoin piyasası aktif demektir.

---

## BTC Dominansı — Ana Gösterge

BTC Dominansı nasıl okunur:
```
BTC.D yükseliyor + BTC fiyatı yükselen → Normal bull run, BTC öncü
BTC.D yükseliyor + BTC fiyatı düşüyor → Risk-off, herkes altcoinden çıkıyor
BTC.D düşüyor   + BTC fiyatı yükselen → Altcoin sezonu başlıyor
BTC.D düşüyor   + BTC fiyatı düşüyor  → Bear market tüm piyasada
```

`goreceli-guc-suite`'te altcoinlerin benchmark'ı her zaman BTCUSDT olmalı. Altcoin BTC'den güçlüyse o altcoin lider demektir.

---

## Dosya Kullanım Kılavuzu — Kripto İçin

### `piyasa-rejimi.pine` — Kripto Versiyonu

**Benchmark Ayarı:**
- Kripto genel piyasa için: `CRYPTOCAP:TOTAL` (toplam kripto piyasa değeri)
- BTC odaklı: `BTCUSDT` veya `INDEX:BTCUSD`
- Altcoin odaklı: `CRYPTOCAP:TOTAL2` (BTC hariç toplam)

**Uyarı:** Kripto'da piyasa rejimi değişimi hisse piyasasından çok daha hızlıdır. 2 haftada Bull'dan Bear'a geçilebilir. Haftalık grafikte bile rejim değişimini gözlemle.

### `trend-suite.pine` — Kripto Özeli

**EMA Yapısı Kripto'da Nasıl Okunur:**

```
EMA 21: Hızlı momentum → altına düşerse kısa vadeli zayıflık
EMA 50: Orta vadeli trend → altına düşerse trend bozuk
EMA 200: Uzun vadeli bull/bear sınırı → MUTLAK REFERANS
```

BTC günlük EMA 200 altında kapandığında: Altcoin alımı yapma.

**Fibonacci Seviyeleri — Kripto'da Neden Bu Kadar Önemli:**
Kripto piyasası teknik analize çok uyar çünkü büyük oyuncular da teknik analiz yapar. Fibonacci 61.8% "altın oran" seviyesi kripto'da tekrar tekrar test edilir.

Nasıl kullanırsın: `trend-suite` dosyasındaki Fibonacci parametresi — lookback'i son büyük hareketin başlangıcına ayarla. En sık bounce yapılan seviye genellikle 61.8%'dir.

**Önemli Fibonacci Seviyeleri:**
- 23.6%: Zayıf geri çekilme (trend çok güçlü)
- 38.2%: Orta geri çekilme (sağlıklı)
- 50.0%: Psikolojik orta nokta
- **61.8%:** Altın oran — en güvenilir bounce noktası
- 78.6%: Derin geri çekilme (trend zayıflayabilir)

### `momentum-suite.pine` — StochRSI'ın Önemi

Kripto'da standart RSI yetmez. StochRSI çok daha hassastır.

**StochRSI Okuma:**
```
%K < 20 + %K %D'yi yukarı kesti → Güçlü Alım sinyali
%K > 80 + %K %D'yi aşağı kesti → Satım sinyali
```

**Dikkat:** StochRSI çok hızlı hareket eder. Günlük veya en az 4 saatlik grafikte kullan. 15 dakikada StochRSI sinyali = gürültü.

**Hacim — Kripto'da Daha Kritik:**
Kripto'da büyük hacimsiz yükselişler genellikle sürdürülemez. BTC %5 çıktı ama hacim ortalamanın altındaysa? "Fırsat" değil "tuzak" olabilir.

`momentum-suite`'te relative volume 2.5x üstüne çıktıktan sonra yönü teyit etmek güçlü bir sinyal.

### `volatilite-suite.pine` — Squeeze Kripto'da Patlayıcı

Kripto'da BB Squeeze sonrası hareketler hisse senedinden çok daha büyüktür. Yüzlerce, bazen binlerce dolarlık BTC hareketi tek bir Squeeze patlamasından kaynaklanabilir.

**Kripto'ya Özel Squeeze Yaklaşımı:**
- BB Çarpanı 2.5, KC Çarpanı 2.0 (hisse'den geniş) — daha derin sıkışmalar yakalar
- Squeeze 20+ bar devam ediyorsa ve BTCUSDT da Squeeze'deyse: Patlama çok büyük olabilir

**Eş Zamanlı BTC + Altcoin Squeeze:**
Hem BTC hem de aldığın altcoin aynı anda Squeeze'deyse, BTC Squeeze patladığında altcoin daha sert hareket eder.

### `evrensel/piyasa-yapisi-suite.pine` — Likidite Anlayışı

Kripto'da piyasa yapısı aracını "likidite" perspektifiyle oku:
- **Equal Highs (EQH):** Yukarıda likidite birikmiş → Büyük oyuncular oraya bakıyor
- **Equal Lows (EQL):** Aşağıda likidite birikmiş → Stop-loss avı

Kripto'da sık görülen senaryo: Fiyat bir önceki swing high'ı süpürür (stop-loss'ları toplar) sonra tersine döner. Buna "liquidity sweep" veya "stop hunt" denir.

Bu bilgiyle sistemi nasıl kullanırsın: EQH görüldüğünde direkt break olarak değil, "burada likidite var, büyük oyuncular buraya bakıyor" olarak oku. Direniş yaşanırsa gerçek kırılım demektir.

### `risk-odül-hesaplayici.pine` — Kripto İçin Özel

**Kripto'da SL Nereye?**
Kripto çok volatil. "Normal" stop-loss'lar kolayca tetiklenir.

```
Kısa vade (1S/4S): SL = 2 × ATR altı
Orta vade (Günlük): SL = 2.5 × ATR altı
Uzun vade (Haftalık): SL = Son önemli swing low altı
```

**ATR Yüzdesi (Kripto'da Önemli):**
Ana panel'in alt satırında ATR% görünür: `(ATR / close) × 100`

Örnek: BTC 65.000 USDT, ATR = 2.500 → ATR% = 3.8%
Bu %3.8 tek bir günde normal "gürültü" anlamına gelir.
SL = 2.5 × ATR = 9.25% uzaklık → Bu büyük pozisyonlarda çok para yakar.
Kripto'da pozisyon boyutunu hisseye göre küçük tut.

---

## Özel Stratejiler — Kripto

### 1. BTC Weekly EMA 200 Bounce
```
Koşullar:
✓ BTC ilk kez haftalık EMA 200'e geliyor (aylar sonra ilk kez)
✓ Haftalık Bullish mum formasyonu (Hammer, Engulfing)
✓ RSI haftalık 30-40 arası (aşırı satım)
✓ StochRSI OS bölgesinde kesişim
→ Bu birkaç yılda bir görülen "döngü alımı"dır
→ Büyük pozisyon, SL: EMA 200 belirgin altı
```

### 2. Altcoin Fibonacci 61.8% + BTC Güçlü
```
Koşullar:
✓ BTC uptrend devam ediyor (EMA 200 üstü, HH/HL)
✓ Altcoin BTC karşısında 61.8% geri çekilmede
✓ Haftalık veya günlük Bullish mum formasyonu
✓ StochRSI OS kesişimi
→ Yüksek R:R setup
```

### 3. Squeeze Patlama + Trend Konfirm
```
Koşullar:
✓ Günlük/4S Squeeze 20+ bar aktif
✓ Squeeze bitti, momentum pozitif
✓ BTC aynı anda uptrend
✓ Hacim Squeeze kırılımında güçlü
→ ENTER (kapanış beklenmeli) → SL: Squeeze alt bandı
```

---

## Psikolojik Tuzaklar — Kripto'ya Özgü

### FOMO (Fear of Missing Out)
Bir coin %50 çıktı. "Kaçırdım" hissi. Şimdi girsem %20 daha çıkar mı diye düşünüyorsun.

**Gerçek:** %50 çıkmış bir coin büyük çıkışlara maruz kaldı demektir. "Geç kalmış" büyük ihtimalle doğru sezgi. Girmemen büyük olasılıkla doğru karar.

**Kural:** Alert yoksa giriş yoktur. Alert veren setup'lar değerlendirilir, "hep çıktı gözüyle bakılan" coinler değil.

### "Bu Sefer Farklı"
Her bull run'da insanlar "bu sefer kripto ana akım oldu, düşmez" der. Bull run'un zirvesinde en çok bu cümle duyulur.

**Kural:** Halving döngüleri, BTC'nin tarihsel davranışı pattern gösterir. Bu pattern tekrar etmeyebilir ama yok saymak daha riskli.

### Leverage (Kaldıraç) Tuzağı
Kripto borsaları %100'e kadar kaldıraç sunar. Bu "10x kaldıraçla 10 kat kazan" değil, "10x kaldıraçla %10 yanlış gidersen tümünü kaybedersin" demektir.

**Kural:** Bu sistem kaldıraçsız (spot) kurgulanmıştır. Kaldıraç kullanıyorsan tüm parametreleri sıfırdan düşün.

---

## Alert Kurulumu — Kripto İçin

**Mutlaka Kurulacaklar:**
1. BTC Günlük SuperTrend değişimi (yön değişimi)
2. BTC EMA 200 altı kapanış (Bear sinyali)
3. Altcoin StochRSI OS bölgesi kesişimi (alım setup)
4. Volatilite Squeeze patlama (büyük hareket)
5. piyasa-yapisi → Bullish BoS (trend dönüşü)

**Kurmaman Gerekenler:**
- Her 15 dakikada RSI eşiği aşımı — bu sadece "uyanık tut" alarmıdır, faydasız

---

## Sistem Boşlukları — Kripto İçin

### Boşluk 1: Funding Rate ve Open Interest Verisi Yok
Bu iki veri kripto'da sentiment göstergesi olarak çok önemlidir.

**Ne Yapabilirsin?**
- CryptoQuant (ücretli ama çok güçlü)
- Bybit veya Binance'de Funding Rate sayfası (ücretsiz, elle kontrol)
- Kural olarak: Trade öncesi funding rate'e bak. Çok yüksek pozitifse long için dikkatli ol.

### Boşluk 2: On-Chain Verisi (Blockchain Analizi) Yok
Exchange'lere BTC girişi arttıysa satış baskısı demektir. Exchange'lerden BTC çıkıyorsa uzun vadeli tutma eğilimi (bullish).

**Ne Yapabilirsin?**
- Glassnode (ücretsiz temel tier yeterli)
- CryptoQuant netflow verisi
- Haftalık bir bakış yeterlidir

### Boşluk 3: Altcoin Rotasyon Sinyali Yok
Hangi sektör (DeFi, Layer2, AI tokens) güç kazanıyor? Sistem bunu görmüyor.

**Ne Yapabilirsin?**
- CoinGecko sektör bazlı performans ekranı
- "Bu hafta hangi sektör en çok çıktı?" sorusunun cevabı

### Boşluk 4: Stablecoin Dominansı Takibi Yok
USDT dominansı yükseliyorsa para kripto'dan çıkıyor demektir.

**Ne Yapabilirsin?**
- TradingView'da `CRYPTOCAP:USDT.D` grafiği aç
- Yükseliyor + BTC düşüyor = dikkat
- Düşüyor = kripto'ya para giriyor = bullish backdrop
