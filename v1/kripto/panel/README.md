# Kripto Ana Panel

## Ne Yapar?
Kripto için uyarlanmış MTF dashboard. Default TF'ler: 1S/4S/Günlük/Haftalık. Hisse panelinden farklı olarak kripto temasında (koyu mavi) görünür ve ATR'yi yüzde olarak gösterir.

## Panel Satırları
1. Fiyat + anlık değişim
2. Trend (SuperTrend 3.5)
3. EMA 200 üstünde/altında
4. RSI (OB/OS eşikleri: 75/25 kripto)
5. MACD yönü
6. Volatilite / Squeeze
7. Konfluens Skoru
8. ATR ve Yüzde (SL hesabı için)

## Kripto Özeli
- RSI eşikleri 75/25 (hisse: 70/30)
- SuperTrend çarpan 3.5 hesaplanır
- ATR yüzde gösterimi: `(ATR/close) × 100` — pozisyon büyüklüğü için kritik
- Default TF: 1S / 4S / Daily / **Weekly** (hissede 15dk/1S/4S/Daily)

## Zaman Dilimi Ayarı
- **Uzun vadeli**: Daily/Weekly/Monthly
- **Orta vadeli**: 4S/Daily/Weekly
- **Aktif trade**: 1S/4S/Daily

## SL/TP Referansı
Panel alt satırında ATR yüzdesi görünür:
- ATR = 1500 USDT, Fiyat = 68000 → ATR% = 2.2%
- Önerilen SL = 2.5 × ATR = 3750 USDT mesafe
