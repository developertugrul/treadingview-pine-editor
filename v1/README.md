# Profesyonel Trading Göstergeler Sistemi
## Pine Script v6 — Dark Mode Uyumlu — Multi-Timeframe

---

## Genel Bakış

Bu sistem, TradingView Pine Editör'ünde kullanmak için tasarlanmış **22 profesyonel indikatör dosyası** içerir. Her dosya, birden fazla uyumlu indikatörü bir araya getirir ve **dark mode / light mode otomatik uyum** sağlar.

---

## Klasör Yapısı

```
claude/
├── hisse/       ← BIST + Global Hisseler
├── kripto/      ← BTC, ETH ve tüm kriptolar
├── kurlar/      ← EURUSD, USDTRY, Forex çiftleri
└── emtia/       ← Altın, Gümüş, Petrol, Tarım
```

Her klasör şu alt klasörleri içerir:
- `trend/`        — EMA, SuperTrend, S/R seviyeleri
- `momentum/`     — RSI, MACD, Stochastic, Hacim
- `volatilite/`   — Bollinger Bands, Keltner, BB Squeeze
- `sinyaller/`    — Mum formasyonları, Konfluens, Alertler
- `panel/`        — Multi-timeframe özet dashboard

---

## Nasıl Kullanılır?

### 1. TradingView'a Ekle
1. TradingView grafiğini aç
2. Alttaki **Pine Editor**'a tıkla (veya Alt+P)
3. İlgili `.pine` dosyasının içeriğini kopyala
4. Editor'e yapıştır → **Add to chart** tıkla
5. İstersen birden fazla indikatörü aynı anda ekleyebilirsin

### 2. Önerilen Minimum Kombinasyon
Her varlık türü için en az şunları ekle:
```
trend-suite.pine     (overlay — grafik üstünde)
momentum-suite.pine  (ayrı panel — altında)
sinyal-suite.pine    (overlay — grafik üstünde)
```

### 3. Tam Sistem (5 Dosya)
```
trend-suite.pine    → Yön ve destek/direnç
momentum-suite.pine → RSI/MACD durumu
volatilite-suite.pine → Sıkışma/patlama
sinyal-suite.pine   → Al/Sat sinyalleri + Alertler
ana-panel.pine      → Tüm özet bir tabloda
```

---

## Dosyalar Arası Uyum Matrisi

| Kombinasyon | Güç | Kullanım |
|-------------|-----|----------|
| trend + momentum | ✓✓✓ | Temel sistem |
| trend + volatilite | ✓✓✓ | Breakout tespiti |
| sinyal + panel | ✓✓✓ | Karar desteği |
| trend + momentum + sinyal | ✓✓✓✓ | Güçlü sistem |
| 5 dosya birlikte | ✓✓✓✓✓ | Tam sistem |

---

## Dark Mode Uyumu

Tüm dosyalar `chart.bg_color` kullanarak otomatik tema algılar:
- **Dark Mode**: Parlak renkler (neon yeşil, parlak kırmızı)
- **Light Mode**: Koyu renkler (koyu yeşil, koyu kırmızı)

Renk değişimi otomatiktir — ek ayar gerekmez.

---

## Alert Sistemi

Her dosyada iki tip alert bulunur:

**1. alertcondition()** — TradingView UI'dan ayarlanır:
- Grafik açıkken: Sağ üstteki alarm zili → Alert oluştur → Condition seçimi

**2. alert()** — Kod içinde tetiklenir:
- Webhook URL ile dış servislere JSON gönderebilirsin
- Telegram, Discord, Email gibi servislere bağlanmak mümkün

### Webhook Kurulumu
1. TradingView Alert oluştur
2. **Webhook URL** alanına servisin URL'ini gir
3. JSON formatı otomatik gönderilir:
```json
{"event":"AL","ticker":"THYAO","price":85.5,"skor":8,"formasyon":"Bull Engulfing","tf":"60"}
```

---

## AI Entegrasyonu

Pine Script, ML modeli çalıştıramaz ama şunları yapar:
- **Adaptif eşikler**: RSI OB/OS otomatik uyarlanır (ATR/Std.dev bazlı)
- **Piyasa rejimi**: ADX tabanlı trend/yatay ayrımı
- **Konfluens skoru**: 10 faktörlü ağırlıklı sinyal puanı

**Dış AI için**: Webhook alertleri → Python Flask → ML Model → Karar

---

## Timeframe Rehberi

| Varlık | Swing Trade | Giriş Zamanlaması | Scalping |
|--------|-------------|-------------------|----------|
| Hisse  | Günlük (1G) | 4 Saatlik (4S)   | 1S / 15dk |
| Kripto | Günlük (1G) | 4 Saatlik (4S)   | 1S       |
| Kurlar | Günlük (1G) | 4 Saatlik (4S)   | 15dk / 5dk |
| Emtia  | Haftalık (1H) | Günlük (1G)    | 4S       |

---

## Varlık Özelinde Notlar

### Hisse (BIST + Global)
- VWAP yalnızca **intraday** (15dk, 1S, 4S) zaman dilimlerinde anlamlıdır
- Günlük grafikte VWAP otomatik kapanır
- BIST için özellikle **USDTRY** korelasyonuna dikkat et

### Kripto
- **24/7 piyasa** — seans kavramı yok
- Default ATR çarpanı **3.5** (daha volatil)
- **Stochastic RSI** standart Stochastic yerine daha faydalı
- BTC/ETH dominans beklentisi sinyale eklenebilir

### Kurlar (Forex)
- **UTC saat diliminde** grafik açmak önerilir
- Seans overlapleri (LD/NY 12:00-16:00 UTC) en yüksek hacim
- **Daily Pivot** seviyeleri günlük yön için kritik referanstır
- Pip bazlı risk yönetimi: SL = 1.5-2x ATR (pip)

### Emtia
- **DXY** (Dolar endeksi) ters korelasyona dikkat — DXY güçlenirse emtia baskı altında
- **52 haftalık H/L** seviyeleri kritik direnç/destek
- Mevsimsel notlar referans amaçlıdır (historik ortalama)

---

## Confluence Skor Sistemi

Skor 0-10 arası, her faktör 1 puan ekler:
1. Fiyat EMA 200 üstünde
2. Fiyat EMA 50 üstünde
3. SuperTrend yükseliş yönünde
4. RSI sağlıklı bölgede (45-70)
5. MACD histogram pozitif
6. Hacim ortalamanın üstünde (1.3x+)
7. BB Squeeze sonu patlama
8. Boğa mum formasyonu
9. MTF (Daily/Weekly) aynı yönde
10. Destek/Pivot seviyesine yakın

**≥ 7/10**: Güçlü sinyal — pozisyon düşünülebilir  
**≥ 9/10**: Çok güçlü — büyük pozisyon

---

## Risk Yönetimi Önerisi

Stop-Loss için ATR kullan (her dosyada `atr_c` değeri panelde görünür):
```
SL = Giriş - (2 × ATR)    [long pozisyon]
SL = Giriş + (2 × ATR)    [short pozisyon]
```

Hedef: R:R = minimum 1:2 (risk:ödül)

---

*Sistem sürümü: Pine Script v6 — Dark Mode Uyumlu*
