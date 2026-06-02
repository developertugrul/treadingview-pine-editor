# Kripto Sinyal Paketi

## Ne Yapar?
Kripto için uyarlanmış sinyal paketi. Mum formasyonları, konfluens skoru ve webhook alert içerir. Stochastic RSI OS sinyali 10. faktör olarak eklendi.

## Hisse Sinyal'den Farkları
| Özellik | Hisse | Kripto |
|---------|-------|--------|
| Skor faktörü 6 | Hacim (1.3x+) | Hacim (1.5x+) |
| Skor faktörü 10 | Destek yakın | **StochRSI OS veya destek** |
| SuperTrend Çarpan | 3.0 | 3.5 |
| BB/KC Squeeze | 2.0/1.5 | 2.5/2.0 |
| Min Skor önerisi | 6 | **6** (kripto'da daha gürültülü) |
| Konsolidasyon kırılımı | %5 | **%6** |

## Konfluens Skoru (0-10)
1. EMA 200 üstünde
2. EMA 50 üstünde
3. SuperTrend (3.5) yükseliş
4. RSI 45-75 arası (kripto)
5. MACD pozitif
6. Hacim 1.5x+ (kripto)
7. Squeeze patlama
8. Boğa mum formasyonu
9. MTF Daily aynı yönde
10. **StochRSI OS veya Destek** (kripto)

## Alert
`Kripto AL/SAT`, `Güçlü AL (8+)`, `Breakout ↑/↓`

Webhook JSON:
```json
{"event":"KRIPTO_AL","ticker":"ETHUSDT","price":3200,"skor":8,"formasyon":"Bull Engulfing","tf":"240"}
```

## Zaman Dilimi
| TF | Güvenilirlik |
|----|-------------|
| Günlük | ⭐⭐⭐⭐⭐ |
| 4 Saatlik | ⭐⭐⭐⭐ |
| 1 Saatlik | ⭐⭐⭐ |
