# Hisse Sinyal Paketi

## Ne Yapar?
12 farklı mum formasyonu tespit eder, grafik formasyonlarını (double top/bottom, breakout) algılar ve 10 faktörlü konfluens skoru ile AL/SAT sinyalleri üretir. Webhook uyumlu dinamik alert içerir. Bu dosya diğer 4 dosyanın mantığını içselleştirir.

## İçindekiler
### Mum Formasyonları (12 adet)
**Boğa (AL):**
- Hammer, Bull Engulfing, Dragonfly Doji, Pin Bar
- Morning Star, Three White Soldiers, Inverted Hammer

**Ayı (SAT):**
- Hanging Man, Bear Engulfing, Gravestone Doji, Bear Pin Bar
- Evening Star, Three Black Crows, Shooting Star

### Grafik Formasyonları
- Double Top / Double Bottom (yaklaşık tespit)
- Consolidation Breakout (konsolidasyon kırılımı)
- Higher Highs / Lower Lows trend channel

### Konfluens Skoru (0-10)
Her faktör 1 puan:
1. EMA 200 üstünde
2. EMA 50 üstünde
3. SuperTrend yükseliş
4. RSI sağlıklı (45-70)
5. MACD histogram pozitif
6. 1.3x+ hacim
7. Squeeze sonu patlama
8. Boğa mum formasyonu
9. MTF (Daily) aynı yönde
10. Destek seviyesine yakın

## Hangi Dosyalarla Çalışır?
| Dosya | Uyum | Açıklama |
|-------|------|----------|
| trend-suite.pine | ✓✓✓ | Skor faktörleri için veri |
| momentum-suite.pine | ✓✓✓ | RSI/MACD skor faktörleri |
| volatilite-suite.pine | ✓✓✓ | Squeeze skor faktörü |
| ana-panel.pine | ✓✓✓ | Panel skorları gösterir |

## Alert Sistemi
### alertcondition (TradingView UI'dan ayarla):
- `AL Sinyali` (≥6/10)
- `SAT Sinyali` (≥6/10)
- `Güçlü AL` (≥8/10)
- `Güçlü SAT` (≥8/10)
- `Bull Engulfing`, `Bear Engulfing`
- `Morning Star`, `Evening Star`
- `Breakout Yukarı`, `Breakout Aşağı`

### Webhook JSON:
```json
{
  "event": "AL",
  "ticker": "THYAO",
  "price": 85.5,
  "skor": 8,
  "formasyon": "Bullish Engulfing",
  "tf": "60"
}
```

## Zaman Dilimi Performansı
| TF | Sonuç | Not |
|----|-------|-----|
| Günlük | ⭐⭐⭐⭐⭐ | En güvenilir formasyonlar |
| 4 Saatlik | ⭐⭐⭐⭐ | İyi skor güvenilirliği |
| 1 Saatlik | ⭐⭐⭐ | Hızlı sinyal |
| 15dk | ⭐⭐ | Çok fazla false positive |

## Min Skor Önerisi
| TF | AL Skor | SAT Skor |
|----|---------|----------|
| Günlük | 6-7 | 6-7 |
| 4 Saatlik | 6 | 6 |
| 1 Saatlik | 5-6 | 5-6 |
