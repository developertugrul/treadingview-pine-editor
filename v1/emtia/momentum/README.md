# Emtia Momentum Paketi

## Ne Yapar?
Emtia için uyarlanmış momentum analizi. RSI, MACD ve Stochastic ile birlikte **OBV** (On Balance Volume) emtia hacim analizinde önemli rol oynar. Renk teması altın tonlarında.

## Özellikler
Hisse momentum ile aynı yapıda, emtia renk temasıyla:
- RSI adaptif eşikler
- Bullish/Bearish diverjans tespiti
- MACD normalize histogram
- Stochastic OS/OB sinyali
- OBV trend konfirmasyonu
- Hacim spike (2x eşik)

## Emtia Hacim Notu
Altın, Petrol gibi emtialarda hacim bazen güvenilmezdir (futures kontraktları). OBV yerine **fiyat hareketi** + **MACD** kombinasyonu daha güvenilir:
- Hacim yoksa (çizgili grafik) hacim spike alertları devre dışı bırak
- Futures kontraktlarda (CL1!, GC1!) hacim genellikle vardır

## Hangi Dosyalarla Çalışır?
| Dosya | Uyum |
|-------|------|
| trend-suite.pine | ✓✓✓ |
| korelasyon-suite.pine | ✓✓✓ |
| sinyal-suite.pine | ✓✓✓ |

## Alert
`RSI OS/OB`, `Bull/Bear Div`, `MACD Al/Sat`, `Hacim Spike`

## Zaman Dilimi
| TF | Güvenilirlik |
|----|-------------|
| Haftalık | ⭐⭐⭐⭐⭐ |
| Günlük | ⭐⭐⭐⭐⭐ |
| 4 Saatlik | ⭐⭐⭐ |
