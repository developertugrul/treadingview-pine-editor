# Kurlar Trend Paketi

## Ne Yapar?
Forex için uyarlanmış trend paketi. EMA 8/21/50/200, SuperTrend (3.0/14) ve **Daily Pivot seviyeleri** (R1/R2/S1/S2) içerir. Pivot seviyeleri günlük gün başında otomatik hesaplanır.

## Hisse Trend'den Farkları
- **Daily Pivot seviyeleri** eklendi (R1/R2/PP/S1/S2)
- SuperTrend periyodu 14 (forex daha uzun period gerektirir)
- VWAP yok
- Fibonacci yok

## Daily Pivot Kullanımı
- PP altında fiyat = Bugünkü açılış bearish
- S1 = İlk destek, S2 = Güçlü destek
- R1 = İlk direnç, R2 = Güçlü direnç
- Pivot kırılımı + momentum = Güçlü sinyal

## Hangi Dosyalarla Çalışır?
| Dosya | Uyum |
|-------|------|
| seans-suite.pine | ✓✓✓ | Seans + Pivot kombinasyonu |
| momentum-suite.pine | ✓✓✓ | Stochastic + Pivot |
| sinyal-suite.pine | ✓✓✓ | Pivot yakınlığı skor faktörü |

## Zaman Dilimi
| TF | Güvenilirlik |
|----|-------------|
| Günlük | ⭐⭐⭐⭐⭐ |
| 4 Saatlik | ⭐⭐⭐⭐⭐ |
| 1 Saatlik | ⭐⭐⭐⭐ |
| 15dk | ⭐⭐⭐ |

## Alert
`Golden Cross`, `Death Cross`, `ST Alım/Satım`
