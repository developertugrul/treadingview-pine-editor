# Emtia Ana Panel

## Ne Yapar?
Emtia MTF dashboard. Hisse paneline ek olarak **DXY yönü** ve **52 Haftalık H/L'den uzaklık** tabloda gösterilir. Default TF'ler: Günlük/Haftalık/Aylık.

## Panel Ek Satırları (Hisse panelinden farklı)
- **DXY satırı**: "↑ BASKI" veya "↓ DESTEKLİ" — DXY yönü + 5 bar değişim yüzdesi
- **52H H/L satırı**: "Zirveye: -5.2%" ve "Dipten: +12.3%"
- **ATR satırı**: "SL=2xATR" önerisi

## Emtia Default TF'leri
- TF1: **Günlük** (hisse: 15dk)
- TF2: **Haftalık** (hisse: 1S)
- TF3: **Aylık** (hisse: 4S)

Emtiada uzun vadeli perspektif kritik. Günlük'ten kısa TF'ler gürültülüdür.

## Renk Teması
Emtia panel altın sarısı/kahverengi tonlarında görünür — karanlık modda koyu amber, açık modda krem rengi.

## DXY Renk Kodlaması
- Yeşil = DXY zayıflıyor (emtia destekleniyor)
- Kırmızı = DXY güçleniyor (emtia baskı altında)
- Amber/Sarı = DXY nötr

## Hangi Dosyalarla Çalışır?
| Dosya | Uyum |
|-------|------|
| korelasyon-suite.pine | ✓✓✓ |
| trend-suite.pine | ✓✓✓ |
| momentum-suite.pine | ✓✓✓ |
| sinyal-suite.pine | ✓✓✓ |

## Zaman Dilimi
| TF | Güvenilirlik |
|----|-------------|
| Haftalık | ⭐⭐⭐⭐⭐ |
| Günlük | ⭐⭐⭐⭐⭐ |
| 4 Saatlik | ⭐⭐⭐ |
