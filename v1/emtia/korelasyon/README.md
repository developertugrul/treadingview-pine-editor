# Emtia Korelasyon Paketi

## Ne Yapar?
Emtiaya özgü korelasyon analizi. DXY (Dolar Endeksi) ile korelasyonu, Altın/Gümüş oranını ve mevsimsel referans notlarını tek panelde gösterir.

## İçindekiler
1. **DXY Korelasyon Katsayısı (-1 ile +1)**
   - Normalize edilerek 0-100 arası gösterilir (50 = nötr)
   - Koyu kırmızı = Güçlü ters korelasyon (DXY ↑ = Emtia ↓)
   - Koyu yeşil = Güçlü pozitif korelasyon

2. **Altın/Gümüş Oranı (GSR)**
   - Altın fiyatı / Gümüş fiyatı
   - > 85: Gümüş tarihsel olarak ucuz
   - < 65: Altın görece ucuz

3. **Fiyat/MA50 Oranı**
   - Fiyatın ortalamadan yüzde sapması
   - +5%: Aşırı uzanma (satım dikkat)
   - -5%: Ortalama altında (alım fırsatı)

4. **Mevsimsel Notlar**
   - Ay başında referans etiket
   - Geçmiş ortalama baz alınır — garanti değil

## DXY Sembolü Ayarı
Dosyayı ekledikten sonra input kısmından DXY sembolünü değiştirebilirsin:
- TradingView'da "DXY" araması
- Farklı sağlayıcı: "USDOLLAR" da kullanılabilir

## Hangi Varlıklara Uygun?
| Sembol | DXY Korelasyon | Not |
|--------|----------------|-----|
| XAUUSD | Güçlü Negatif | Altın DXY'ye ters hareket |
| XAGUSD | Negatif | Gümüş de ters |
| CL (Petrol) | Orta Negatif | DXY kadar jeopolitik etkili |
| HG (Bakır) | Negatif | Küresel büyüme göstergesi |
| WHEAT/CORN | Zayıf | DXY etkisi düşük |

## Hangi Dosyalarla Çalışır?
| Dosya | Uyum |
|-------|------|
| sinyal-suite.pine | ✓✓✓ | DXY faktörü skor dahil |
| trend-suite.pine | ✓✓✓ | 52H + DXY |
| panel/ana-panel.pine | ✓✓✓ | DXY panelde gösterilir |

## Alert
- `DXY Risk` — DXY güçlenirken emtia baskı
- `GSR Yüksek (>85)` — Gümüş tarihsel ucuz
- `Korelasyon Döndü` — DXY korelasyonu yön değiştirdi

## Zaman Dilimi
| TF | Güvenilirlik |
|----|-------------|
| Haftalık | ⭐⭐⭐⭐⭐ |
| Günlük | ⭐⭐⭐⭐ |
| 4 Saatlik | ⭐⭐⭐ |
