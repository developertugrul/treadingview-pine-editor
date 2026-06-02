# Kripto Momentum Paketi

## Ne Yapar?
Kripto için uyarlanmış momentum analizi. RSI yerine **Stochastic RSI** kripto standardı olduğu için eklendi. OB/OS eşikleri 75/25 (kripto daha volatil). Hacim spike eşiği 2.5x.

## Hisse Momentum'dan Farkları
| Özellik | Hisse | Kripto |
|---------|-------|--------|
| RSI OB/OS (sabit) | 70/30 | **75/25** |
| Stochastic tipi | Standard Stochastic | **Stochastic RSI** |
| Hacim Spike Eşiği | 2.0x | **2.5x** |
| Momentum Skoru | OBV ağırlıklı | Stoch RSI de ekli |

## Stochastic RSI
- RSI değerinin stochastic uygulaması
- %K < 20 + Kesişim Yukarı → Güçlü alım (kripto'da çok etkili)
- %K > 80 + Kesişim Aşağı → Satım sinyali

## Hangi Dosyalarla Çalışır?
| Dosya | Uyum |
|-------|------|
| trend-suite.pine | ✓✓✓ |
| sinyal-suite.pine | ✓✓✓ |
| volatilite-suite.pine | ✓✓ |

## Zaman Dilimi
| TF | Güvenilirlik |
|----|-------------|
| Günlük | ⭐⭐⭐⭐⭐ |
| 4 Saatlik | ⭐⭐⭐⭐ |
| 1 Saatlik | ⭐⭐⭐ |
| 15dk | ⭐⭐ |

## Alert
`RSI OS Çıkış`, `RSI OB Çıkış`, `Bullish/Bearish Div`, `MACD Al/Sat`, `Hacim Spike`, `StochRSI OS Al`
