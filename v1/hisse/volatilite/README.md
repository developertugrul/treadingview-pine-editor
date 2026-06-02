# Hisse Volatilite Paketi

## Ne Yapar?
Bollinger Bands ve Keltner Channel kombinasyonu ile BB Squeeze tespit eder. Sıkışma dönemlerini renkli arka planla işaretler, patlama yönünü momentum ile tahmin eder.

## İçindekiler
- **Bollinger Bands (20, 2.0)**: %B değeri ve band genişliği
- **Keltner Channel (20, 1.5 ATR)**: Bant referansı
- **BB Squeeze**: BB Keltner içindeyken sıkışma
- **Squeeze Momentum**: Patlama yönü tahmini
- **ATR Bantları**: Dinamik risk seviyeleri
- **Volatilite Rejim Etiketi**: "DÜŞÜK VOL / SIKIŞ" vs "PATLAMA"
- **Band Genişlik Persentil**: Son 50 bara göre band ne kadar dar?

## BB Squeeze Mantığı (Lazybear)
```
Squeeze Aktif  = BB üst < KC üst  VE  BB alt > KC alt
Squeeze Bitti  = Aktif → Değil   (PATLAMA!)
Patlama Yönü   = Momentum pozitif → Yukarı
                 Momentum negatif → Aşağı
```

Squeeze döneminde arka plan sarıya döner → Patlama için hazır ol!

## Hangi Dosyalarla Çalışır?
| Dosya | Uyum | Açıklama |
|-------|------|----------|
| trend-suite.pine | ✓✓✓ | Patlama yönü = trend yönü mi? |
| momentum-suite.pine | ✓✓ | Squeeze + RSI kombinasyonu |
| sinyal-suite.pine | ✓✓✓ | Squeeze patlama konfluens skora ekler |

## Alert Türleri
- `Squeeze Başladı` — Sıkışma döneminin başı
- `Squeeze Bitti (Patlama)` — En önemli alert!
- `Yukarı Patlama` — Patlama + pozitif momentum
- `Aşağı Patlama` — Patlama + negatif momentum
- `BB Yukarı/Aşağı Kırılım` — Band kırılımı

## Zaman Dilimi Performansı
| TF | Sonuç | Not |
|----|-------|-----|
| Günlük | ⭐⭐⭐⭐⭐ | Uzun squeeze daha güçlü patlama |
| 4 Saatlik | ⭐⭐⭐⭐ | Standart intraday |
| 1 Saatlik | ⭐⭐⭐ | Küçük hareketler |
| 15dk | ⭐⭐ | Çok fazla false squeeze |

## Squeeze Süresi
- Squeeze ne kadar uzun → Patlama o kadar güçlü
- 5-10 bar: Küçük hareket
- 20+ bar: Önemli breakout
