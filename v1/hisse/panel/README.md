# Hisse Ana Panel (Dashboard)

## Ne Yapar?
Grafik üstünde sağ köşede tüm indikatörlerin özet tablosunu gösterir. 4 farklı zaman dilimini (varsayılan: 15dk/1S/4S/Günlük) yan yana karşılaştırır. Renkli hücreler ile anlık karar desteği sağlar.

## Panel Yapısı
```
┌──────────────┬─────────┬─────┬──────┬──────┬──────┐
│ BIST:THYAO   │ Anlık   │ 15M │  1S  │  4S  │  1G  │
├──────────────┼─────────┼─────┼──────┼──────┼──────┤
│ Fiyat        │ 85.50   │ +1% │      │      │      │
│ Trend        │ YUKARI  │  ↑  │  ↑   │  ↑   │  ↑   │
│ EMA 200      │ Üstünde │  ✓  │  ✓   │  ✓   │  ✓   │
│ RSI (14)     │  58.4   │ 62  │  55  │  51  │  48  │
│ MACD         │ ↑POZ    │  +  │  +   │  -   │  -   │
│ Volatilite   │ NORMAL  │ sq  │ norm │ norm │ norm │
│ Skor /10     │  7.0    │  5  │  6   │  7   │  6   │
│ ATR / Hacim  │ 2.50    │1.2x │      │      │      │
└──────────────┴─────────┴─────┴──────┴──────┴──────┘
```

## Renk Kodları
- 🟢 Yeşil = Bullish / Pozitif
- 🔴 Kırmızı = Bearish / Negatif
- 🟡 Sarı = Nötr / Dikkat
- ⚫ Gri = Belirsiz

## Hangi Dosyalarla Çalışır?
Bu dosya **tüm diğer 4 dosyayı tamamlar**. Sinyalleri tek tabloda gösterir.

| Bağımsız Kullanım | Uyum | Not |
|------------------|------|-----|
| Tek başına | ✓✓ | Hızlı genel bakış için yeterli |
| + trend-suite | ✓✓✓ | Grafik + Tablo birlikte |
| + tüm dosyalar | ✓✓✓✓✓ | Tam sistem |

## Zaman Dilimi Ayarı
Panel'de TF1/TF2/TF3/TF4 parametrelerini değiştirebilirsin:
- **Swing trade**: 4S / Günlük / Haftalık / Aylık
- **Intraday**: 15dk / 1S / 4S / Günlük
- **Scalping**: 5dk / 15dk / 1S / 4S

## Panel Konumu
Panel konumu seçenekleri:
- Sağ Üst (default)
- Sağ Alt
- Sol Üst
- Sol Alt

Küçük ekranda "Küçük" boyutu seç → Daha az yer kaplar.

## Karar Kuralı
**Hücrelerin çoğu yeşil + Skor ≥ 7 + En az 2 TF aynı yönde** = Güvenilir sinyal
