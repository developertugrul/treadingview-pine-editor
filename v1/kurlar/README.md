# Döviz Kurları İndikatörleri
## Forex — EURUSD, USDTRY, GBPUSD, USDJPY — Pine Script v6

---

## Klasördeki Dosyalar

| Dosya | Konum | İçerik |
|-------|-------|--------|
| `trend/trend-suite.pine` | Overlay | EMA, SuperTrend, Daily Pivot (R1/R2/S1/S2), S/R |
| `momentum/momentum-suite.pine` | Alt panel | RSI, MACD, **Stochastic**, CCI (forex standart) |
| `seans/seans-suite.pine` | Overlay | Tokyo/Londra/NY seans kutuları, Asian Range, Overlap |
| `sinyaller/sinyal-suite.pine` | Overlay | Mum formasyonları, Pivot ağırlıklı konfluens, Alertler |
| `panel/ana-panel.pine` | Overlay | MTF tablo + Seans bilgisi + Pivot seviyeleri |

---

## Forex'e Özel Özellikler

### Seans Analizi (seans-suite.pine)
Forex piyasası 24 saat açık olsa da hacim seanslarla değişir:

| Seans | UTC Saati | Özellik |
|-------|-----------|---------|
| **Tokyo** | 00:00 – 09:00 | Mavi arka plan, düşük hacim |
| **Londra** | 07:00 – 16:00 | Sarı arka plan, yüksek volatilite |
| **New York** | 12:00 – 21:00 | Kırmızı arka plan, yüksek hacim |
| **LD/NY Overlap** | 12:00 – 16:00 | **Yeşil** — EN YÜKSEK hacim 🔥 |
| **TK/LD Overlap** | 07:00 – 09:00 | **Sarı** — Londra açılışı 🔶 |

**Öneriler**:
- En önemli sinyaller **LD/NY overlap** zamanında verilenleridir
- Londra açılışı (07:00 UTC) çok güçlü hareket yapabilir
- Tokyo seansı düşük volatilite — işlem yapmaktan kaçın

### Asian Range
- Tokyo seansı boyunca oluşan high/low = **Asian Range**
- Londra açılışında bu range kırılırsa güçlü trend sinyali
- `seans-suite` dosyası Asian Range kırılımında alert verir

### Daily Pivot Seviyeleri
Her günün başında dünkü H/L/Close'dan hesaplanır:
```
PP = (H + L + C) / 3           — Pivot Noktası (gün için denge)
R1 = 2×PP - L                  — Birinci Direnç
R2 = PP + (H - L)              — İkinci Direnç
S1 = 2×PP - H                  — Birinci Destek
S2 = PP - (H - L)              — İkinci Destek
```

---

## Zaman Dilimi Rehberi

| Zaman Dilimi | Kullanım | Güvenilirlik | Not |
|-------------|----------|--------------|-----|
| Günlük (1G) | Uzun vadeli trend | ⭐⭐⭐⭐⭐ | Ana trend yönü |
| 4 Saatlik (4S) | Swing trade | ⭐⭐⭐⭐⭐ | En iyi Forex TF'i |
| 1 Saatlik (1S) | Giriş zamanlaması | ⭐⭐⭐⭐ | Seans kombinasyonuyla |
| 15 Dakikalık | Intraday | ⭐⭐⭐ | LD/NY overlap'te kullan |
| 5 Dakikalık | Hızlı trade | ⭐⭐ | Sadece açılışta |

**Kural**: Seans dışında işlem yapmaktan kaçın. Asian seansında (00-07 UTC) sinyal alma.

---

## Pip Hesabı

Panel içinde pip değeri otomatik gösterilir:
```
EURUSD: 1 pip = 0.0001
USDJPY: 1 pip = 0.01
USDTRY: 1 pip = 0.0001
```

SL hesabı:
```
SL (pip) = ATR / 0.0001    [major pairs]
Önerilen: SL = 1.5 × ATR (pip cinsinden)
```

---

## Stochastic — Forex'te Önemi

Forex'te Stochastic, RSI kadar önemlidir:
- **20 altında kesişim yukarı** = Güçlü alım sinyali
- **80 üstünde kesişim aşağı** = Güçlü satım sinyali
- **Pivot desteği + Stochastic OS** = En güçlü kombinasyon

---

## USDTRY Özeli

USDTRY için ek dikkat noktaları:
- TL siyasi/ekonomik olaylardan hızlı etkilenir
- Merkez Bankası faiz kararları ekstra volatilite
- Haftalık grafikte uzun vadeli trend daha güvenilir
- `korelasyon-suite` yoktur — sadece teknik analiz

---

## Alert Kurulumu

seans-suite alertları:
- `Londra Açılışı` — 07:00 UTC'de tetiklenebilir
- `LD/NY Overlap Başladı` — 12:00 UTC'de tetiklenebilir
- `Asian Range Kırılımı` — Yönlü kırılım

sinyal-suite webhook JSON:
```json
{
  "event": "KUR_AL",
  "ticker": "EURUSD",
  "price": 1.08750,
  "skor": 7,
  "formasyon": "Pin Bar",
  "seans": true,
  "tf": "60"
}
```

---

## Senaryo Örneği — EURUSD Alım

1. **Günlük grafik**: EMA 200 üstünde, SuperTrend yeşil ✓
2. **4S momentum**: RSI 52, Stochastic OS'tan çıkıyor ✓  
3. **Seans**: Londra seansı aktif ✓
4. **Pivot**: Fiyat S1 seviyesinde (2×PP - H) ✓
5. **Formasyon**: Pin Bar / Hammer mumu ✓
6. **Skor**: 7/10 → AL sinyali
7. **SL**: S1 altına 1.5 × ATR pip mesafe
8. **Hedef**: R1 seviyesi veya 2:1 R:R
