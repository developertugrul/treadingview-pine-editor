# Kurlar Momentum Paketi

## Ne Yapar?
Forex için uyarlanmış momentum analizi. **Stochastic (14/3/3)** ve **CCI (20)** standart Forex göstergeleri olarak eklendi. RSI OB/OS eşikleri 70/30 (standart).

## Forex Özeli
- **Stochastic**: Forex'te en çok kullanılan indikatörlerden biri
  - OS bölgesinde kesişim yukarı = güçlü alım
  - Seans + Stochastic OS = En iyi kombinasyon
- **CCI**: Overbought/oversold ile trend dönüş tespiti
  - +100 üstü = Güçlü trend / Aşırı alım
  - -100 altı = Güçlü düşüş / Aşırı satım

## Hangi Dosyalarla Çalışır?
| Dosya | Uyum |
|-------|------|
| seans-suite.pine | ✓✓✓ | Aktif seans + Momentum |
| trend-suite.pine | ✓✓✓ | Pivot + Stochastic OS |
| sinyal-suite.pine | ✓✓✓ | Stochastic skor faktörü |

## Alert
`RSI OS/OB Çıkış`, `Bull/Bear Diverjans`, `Stoch Al/Sat`, `MACD Al`

## Zaman Dilimi
| TF | Güvenilirlik |
|----|-------------|
| 4 Saatlik | ⭐⭐⭐⭐⭐ |
| Günlük | ⭐⭐⭐⭐⭐ |
| 1 Saatlik | ⭐⭐⭐⭐ |
| 15dk (LD/NY) | ⭐⭐⭐ |
