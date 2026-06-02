# Emtia İndikatörleri
## Altın · Gümüş · Petrol · Bakır · Tarım — Pine Script v6

---

## Klasördeki Dosyalar

| Dosya | Konum | İçerik |
|-------|-------|--------|
| `trend/trend-suite.pine` | Overlay | EMA 20/50/100/200, SuperTrend, **52 Haftalık H/L**, S/R |
| `momentum/momentum-suite.pine` | Alt panel | RSI, MACD, Stochastic, Hacim, OBV |
| `korelasyon/korelasyon-suite.pine` | Alt panel | **DXY korelasyonu**, Altın/Gümüş oranı, Mevsimsel notlar |
| `sinyaller/sinyal-suite.pine` | Overlay | Mum formasyonları, DXY ağırlıklı konfluens, Alertler |
| `panel/ana-panel.pine` | Overlay | MTF tablo + DXY + 52H Seviyeleri |

---

## Emtiaya Özel Özellikler

### DXY Korelasyonu (Çok Önemli!)

Çoğu emtia ile ABD Doları **ters korelasyonludur**:

| DXY Hareketi | Etki |
|-------------|------|
| DXY ↑ (dolar güçleniyor) | Emtia ↓ (baskı altında) |
| DXY ↓ (dolar zayıflıyor) | Emtia ↑ (destekleniyor) |

Bu nedenle:
- **sinyal-suite** DXY yönünü konfluens skoruna ekler
- **panel** DXY yönünü ve değişimini gösterir
- **korelasyon-suite** anlık korelasyon katsayısını hesaplar

**Not**: USDTRY gibi USD/TL çiftleri pozitif korelasyon gösterebilir (ters mantık). Hangi emtiaya bakıyorsan DXY etkisini kontrol et.

### Altın/Gümüş Oranı (GSR)

`korelasyon-suite` içinde GSR (Gold/Silver Ratio) paneli:
- **GSR > 85**: Gümüş tarihsel olarak ucuz → Gümüş alımı düşünülebilir
- **GSR < 65**: Altın görece ucuz → Altın alımı avantajlı
- Tarihsel ortalama: ~70-80

### 52 Haftalık Seviyeleri

`trend-suite` dosyası yıllık zirve ve dip seviyelerini işaretler:
- 52H Zirve = Güçlü direnç (kırılırsa rally)
- 52H Dip = Güçlü destek (kırılırsa düşüş)
- Panel zirveye/dibe yüzde uzaklığı gösterir

### Mevsimsellik

`korelasyon-suite` içindeki mevsimsel notlar **tarihi ortalama** referansıdır:

| Ay | Altın | Petrol | Tarım |
|----|-------|--------|-------|
| Ocak-Şubat | Güçlü | Kış talebi | Düşük stok |
| Mayıs-Ağustos | Zayıf (yaz) | Sürüş sezonu | Hasat öncesi |
| Eylül-Kasım | **Güçlü** | Düşüş | Hasat sonrası |

---

## Zaman Dilimi Rehberi

| Zaman Dilimi | Kullanım | Güvenilirlik | Not |
|-------------|----------|--------------|-----|
| Aylık (1Ay) | Uzun vadeli pozisyon | ⭐⭐⭐⭐⭐ | Altın/Petrol için |
| Haftalık (1H) | Swing trade | ⭐⭐⭐⭐⭐ | En güvenilir emtia TF |
| Günlük (1G) | Kısa-orta vadeli | ⭐⭐⭐⭐ | Giriş zamanlaması |
| 4 Saatlik (4S) | Aktif trade | ⭐⭐⭐ | DXY ile birlikte kullan |
| 1 Saatlik (1S) | İntraday | ⭐⭐ | Sadece aktif saatlerde |

**Öneri**: Emtiada haftalık trend kritik. Günlük ile giriş, haftalık ile yön.

---

## Varlığa Özel Parametreler

### Altın (XAUUSD)
- SuperTrend Çarpan: 3.0 (default)
- RSI OB/OS: 70/30 (standard)
- DXY korelasyonu: **Negatif** (güçlü)
- Fibonacci: 61.8% çok kritik

### Petrol (CL1! / USOIL)
- Daha volatil — ATR çarpanı 2.5-3.0 önerilebilir
- OPEC kararları ani volatilite
- Stok raporları (Çarşamba EIA) hacim spike

### Gümüş (XAGUSD)
- Altından daha volatil
- Altın/Gümüş oranı ile birlikte değerlendir
- Sanayi talebi altına göre daha önemli

### Doğalgaz (NG1!)
- Yüksek mevsimsellik
- BB Squeeze etkili
- Kış/yaz sezonu farkı büyük

---

## Alert Kurulumu

sinyal-suite webhook JSON (DXY yönü dahil):
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

DXY yönü alertleri (korelasyon-suite):
- `DXY Risk` — DXY güçlenirken emtia baskı
- `GSR Yüksek (>85)` — Gümüş tarihsel ucuz
- `Korelasyon Döndü` — DXY korelasyonu değişti

---

## Senaryo Örneği — XAUUSD Alım

1. **Haftalık grafik**: EMA 200 üstünde, uzun vadeli yükseliş ✓
2. **Günlük trend**: SuperTrend yeşil, EMA 50 > EMA 200 ✓
3. **DXY**: Dolar zayıflıyor (DXY ↓) → Altın destekleniyor ✓
4. **Fibonacci**: 61.8% seviyesinde bounce ✓
5. **Momentum**: RSI 52 (sağlıklı), MACD pozitif ✓
6. **Mum**: Pin Bar / Hammer formasyonu ✓
7. **Skor**: 8/10 → Güçlü AL sinyali
8. **52H seviyesi**: 52H dipten uzakta, zirveye %8 mesafe ✓
9. **Karar**: Alım — SL = 2 × ATR altı, hedef = son direnç veya 52H zirve
