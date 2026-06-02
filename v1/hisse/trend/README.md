# Hisse Trend Paketi

## Ne Yapar?
EMA 8/21/50/200, SuperTrend ve dinamik destek/direnç seviyeleri ile hissenin genel trend yönünü belirler. VWAP intraday grafiklerde aktif olur. Multi-timeframe trend konfirmasyonu Daily/Weekly EMA'ya göre yapılır.

## İçindekiler
- **EMA 8/21/50/200**: Renk kodlu trend göstergesi
- **EMA 8/21 Fill**: Trend yönü görsel dolgusu
- **SuperTrend (10, 3.0)**: Dinamik trend takip
- **Dinamik S/R**: Son 3 pivot high/low seviyesi
- **VWAP**: Sadece intraday (otomatik kapanır günlük'te)
- **Daily/Weekly MTF Trend**: Büyük resim konfirmasyonu
- **Golden/Death Cross**: EMA 50/200 kesişim uyarısı

## Hangi Dosyalarla Çalışır?
| Dosya | Uyum | Açıklama |
|-------|------|----------|
| momentum-suite.pine | ✓✓✓ | RSI/MACD ile trend onayı |
| sinyal-suite.pine | ✓✓✓ | Mum formasyonu + trend kombinasyonu |
| volatilite-suite.pine | ✓✓ | Squeeze patlama yönü |
| ana-panel.pine | ✓✓✓ | MTF özet tablo |

## Zaman Dilimi Performansı
| TF | Sonuç | Önerilen Kullanım |
|----|-------|-------------------|
| Haftalık | ⭐⭐⭐⭐⭐ | Ana trend yönü |
| Günlük | ⭐⭐⭐⭐⭐ | Swing trade kararı |
| 4 Saatlik | ⭐⭐⭐⭐ | Giriş zamanlaması |
| 1 Saatlik | ⭐⭐⭐ | Intraday + VWAP aktif |
| 15 Dakikalık | ⭐⭐ | Sadece VWAP faydalı |

## Alert Türleri
- `Golden Cross` — EMA 50/200 kesişim (alım sinyali)
- `Death Cross` — EMA 50/200 ters kesişim (satım sinyali)
- `SuperTrend Alım` — ST yön değişimi (yeşile döndü)
- `SuperTrend Satım` — ST yön değişimi (kırmızıya döndü)
- `Güçlü Alım Sinyali` — MTF + ST aynı yönde

## Önerilen Parametreler
- **Swing trade**: SuperTrend 10/3.0, Pivot Lookback 10-15
- **Intraday**: SuperTrend 7/2.5, Pivot Lookback 5-8
- **EMA görünürlük**: Günlük'te EMA 50/200 en önemli; intraday'de 8/21 ön plana çıkar
