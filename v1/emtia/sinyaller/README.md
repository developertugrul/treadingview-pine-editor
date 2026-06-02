# Emtia Sinyal Paketi

## Ne Yapar?
Emtia için uyarlanmış sinyal paketi. Konfluens skorunda **DXY yönü** kritik faktör olarak yer alır. Webhook JSON mesajına `dxy_yon` bilgisi eklenir. 52 Haftalık seviyelere yakınlık skor faktörüdür.

## Hisse Sinyal'den Farkları
| Faktör | Hisse | Emtia |
|--------|-------|-------|
| Faktör 6 | 1.3x Hacim | 1.5x Hacim |
| Faktör 9 | MTF Daily | **MTF Haftalık** |
| Faktör 10 | Destek/Pivot | **52H Dip veya Destek** |
| Ek: DXY | Yok | **DXY zayıflıyor (+1 AL puan)** |
| Renk teması | Yeşil/Kırmızı | **Altın/Yeşil** |

## DXY Faktörü Açıklaması
AL Skor için: `not dxy_yukari ? 1 : 0`
- DXY zayıflıyorsa → Emtia pozitif → +1 puan
- DXY güçleniyorsa → Emtia baskı → 0 puan

SAT Skor için: `dxy_yukari ? 1 : 0`
- DXY güçleniyorsa → Emtia satım baskısı → +1 puan

## Alert
`Emtia AL/SAT`, `Güçlü AL (8+)`

Webhook JSON DXY bilgisiyle:
```json
{
  "event": "EMTIA_AL",
  "ticker": "XAUUSD",
  "price": 2350.50,
  "skor": 8,
  "formasyon": "Bull Engulfing",
  "dxy_yon": "asagi",
  "tf": "D"
}
```

## Hangi Dosyalarla Çalışır?
| Dosya | Uyum |
|-------|------|
| korelasyon-suite.pine | ✓✓✓ | DXY analizi |
| trend-suite.pine | ✓✓✓ | 52H seviyeleri |
| momentum-suite.pine | ✓✓✓ | RSI/OBV |
| panel/ana-panel.pine | ✓✓✓ | Özet |

## Zaman Dilimi
| TF | Güvenilirlik |
|----|-------------|
| Haftalık | ⭐⭐⭐⭐⭐ |
| Günlük | ⭐⭐⭐⭐⭐ |
| 4 Saatlik | ⭐⭐⭐ |
