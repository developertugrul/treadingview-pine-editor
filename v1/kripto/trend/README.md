# Kripto Trend Paketi

## Ne Yapar?
Hisse trend paketinin kripto için uyarlanmış versiyonu. EMA 21/50/100/200, SuperTrend (3.5), Fibonacci geri çekilme seviyeleri ve dinamik S/R ile kripto trend analizi yapar. 24/7 piyasaya uygun — VWAP yok, Fibonacci var.

## Hisse Trend'den Farkları
| Özellik | Hisse | Kripto |
|---------|-------|--------|
| SuperTrend Çarpan | 3.0 | **3.5** |
| EMA seti | 8/21/50/200 | 21/50/100/200 |
| VWAP | İntraday aktif | Yok |
| Fibonacci | Yok | **Var** |
| Pivot Lookback | 10 | **14** |
| MTF default TF | Daily | Daily |

## Fibonacci Seviyeleri
Son N bar'ın swing high-low'una göre otomatik çizilir:
- **61.8% altın oran** — En kritik geri çekilme
- **50.0%** — Psikolojik seviye
- **38.2%** — Zayıf geri çekilme (trend güçlü)

## Hangi Dosyalarla Çalışır?
| Dosya | Uyum | Açıklama |
|-------|------|----------|
| momentum-suite.pine | ✓✓✓ | StochRSI + trend |
| volatilite-suite.pine | ✓✓✓ | Squeeze + trend yönü |
| sinyal-suite.pine | ✓✓✓ | Fibonacci + formasyon |

## Zaman Dilimi
| TF | Güvenilirlik |
|----|-------------|
| Haftalık | ⭐⭐⭐⭐⭐ |
| Günlük | ⭐⭐⭐⭐⭐ |
| 4 Saatlik | ⭐⭐⭐⭐ |
| 1 Saatlik | ⭐⭐⭐ |

## Alert
`Golden Cross`, `Death Cross`, `ST Alım`, `ST Satım`, `Güçlü Kripto Alım`
