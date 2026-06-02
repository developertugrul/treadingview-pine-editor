# Emtia Trend Paketi

## Ne Yapar?
Emtia için uyarlanmış trend paketi. EMA 20/50/100/200, SuperTrend ve **52 Haftalık High/Low** seviyeleri içerir. 52H seviyelerine yaklaşıldığında etiket ve alert oluşturur. Default konfirmasyon TF: Haftalık.

## Hisse Trend'den Farkları
| Özellik | Hisse | Emtia |
|---------|-------|-------|
| EMA seti | 8/21/50/200 | **20/50/100/200** |
| 52H Seviyeleri | Yok | **Var** |
| MTF default | Daily | **Weekly** |
| VWAP | İntraday | Yok |
| Fibonacci | Yok | Yok (kripto'da var) |
| Renk teması | Yeşil/Kırmızı | **Altın/Yeşil** |

## 52 Haftalık Seviyeler
- **52H Zirve**: Yıllık en yüksek → Güçlü direnç
  - Kırılırsa: Büyük ralliy mümkün
  - Test edilirse: Satış baskısı
- **52H Dip**: Yıllık en düşük → Güçlü destek
  - Kırılırsa: Panik satış
  - Bounce yaparsa: Değerli alım fırsatı

## Emtia EMA'ları
Emtia için EMA 20 (kısa) ve EMA 100 (orta) özellikle önemlidir:
- EMA 20 = Anlık momentum yönü
- EMA 100 = Orta vade trend
- EMA 200 = Uzun vade bull/bear sınırı

## Hangi Dosyalarla Çalışır?
| Dosya | Uyum |
|-------|------|
| korelasyon-suite.pine | ✓✓✓ | DXY + 52H |
| momentum-suite.pine | ✓✓✓ | RSI + OBV |
| sinyal-suite.pine | ✓✓✓ | DXY dahil skor |

## Alert
`Golden Cross`, `Death Cross`, `ST Alım/Satım`, `52H Zirveye Yakın`, `52H Dibe Yakın`

## Zaman Dilimi
| TF | Güvenilirlik |
|----|-------------|
| Aylık | ⭐⭐⭐⭐⭐ |
| Haftalık | ⭐⭐⭐⭐⭐ |
| Günlük | ⭐⭐⭐⭐ |
| 4 Saatlik | ⭐⭐⭐ |
