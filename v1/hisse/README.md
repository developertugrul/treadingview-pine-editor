# Hisse Senedi İndikatörleri
## BIST + Global Hisseler — Pine Script v6

---

## Klasördeki Dosyalar

| Dosya | Konum | İçerik |
|-------|-------|--------|
| `trend/trend-suite.pine` | Grafik üstü (overlay) | EMA 8/21/50/200, SuperTrend, S/R, VWAP, MTF |
| `momentum/momentum-suite.pine` | Ayrı alt panel | RSI (diverjans), MACD, Stochastic, Hacim, OBV |
| `volatilite/volatilite-suite.pine` | Grafik üstü (overlay) | BB, Keltner, Squeeze, ATR bantları |
| `sinyaller/sinyal-suite.pine` | Grafik üstü (overlay) | 12 mum formasyonu, Konfluens 0-10, Alertler |
| `panel/ana-panel.pine` | Grafik üstü (overlay) | MTF özet tablo (15dk/1S/4S/Günlük) |

---

## Önerilen Kullanım Kombinasyonları

### Swing Trade (Günlük/Haftalık grafik)
```
✓ trend-suite.pine        — Yön tespiti
✓ momentum-suite.pine     — RSI/MACD onayı
✓ sinyal-suite.pine       — Formasyon + Alert
```

### Intraday (1S / 4S grafik)
```
✓ trend-suite.pine        — EMA yapısı + VWAP
✓ momentum-suite.pine     — Momentum durumu
✓ volatilite-suite.pine   — Squeeze tespiti
✓ sinyal-suite.pine       — Giriş sinyali
```

### Tam Sistem (tüm dosyalar birlikte)
```
trend + momentum + volatilite + sinyal + panel
→ En kapsamlı analiz
→ Panel sağ üstte özet tabloyu gösterir
```

---

## Zaman Dilimi Rehberi

| Zaman Dilimi | Kullanım | Güvenilirlik | Not |
|-------------|----------|--------------|-----|
| Haftalık (1H) | Uzun vadeli yön | ⭐⭐⭐⭐⭐ | Swing trader referansı |
| Günlük (1G) | Swing trade | ⭐⭐⭐⭐⭐ | En güvenilir sinyaller |
| 4 Saatlik (4S) | Kısa-orta vadeli | ⭐⭐⭐⭐ | İyi giriş zamanlaması |
| 1 Saatlik (1S) | Intraday | ⭐⭐⭐ | Hızlı ama daha gürültülü |
| 15 Dakikalık | Scalping | ⭐⭐ | Dikkatli kullan |
| 5 Dakikalık | Scalping | ⭐ | Çok gürültülü |

**Öneri**: Günlük grafikte yön bul → 4 saatlik ile giriş zamanla → 1 saatlik ile confirm et.

---

## Hisseye Özel Notlar

### VWAP Kullanımı
- VWAP **sadece intraday** zaman dilimlerinde (15dk-4S) anlamlıdır
- Günlük ve üstünde VWAP otomatik olarak gizlenir
- VWAP altında fiyat = gün içi zayıf
- VWAP üstünde fiyat = gün içi güçlü

### BIST Özeli
- **10:00-18:00** BIST işlem saatleri (piyasa saati)
- USDTRY'nin BIST üzerindeki etkisi büyük — kur yükselişi çoğu hissede baskı
- Özellikle ihracat ağırlıklı hisseler (savunma, tekstil) kurdan pozitif etkilenir

### Hacim Analizi
- Hacim spike (2x ortalama) = önemli hareket sinyali
- Yüksek hacimli günlük kapanışlar: pozisyon değişimi anlamı
- Düşük hacimdeki hareketler güvenilir değil

---

## Alert Kurulumu

### TradingView'da Alert Oluşturma
1. `sinyal-suite.pine` dosyasını grafiğe ekle
2. Üst çubukta **Alarm Zili** ikonuna tıkla (Alerts)
3. **Create Alert** → Condition'dan indikatörü seç
4. Tetikleyici seç: "AL Sinyali", "SAT Sinyali", "Güçlü AL" vb.
5. Bildirim yöntemi: Email, Push notification, Webhook

### Webhook (JSON) Alert
sinyal-suite içindeki webhook modunda gelen JSON:
```json
{
  "event": "AL",
  "ticker": "THYAO",
  "price": 85.50,
  "skor": 8,
  "formasyon": "Bullish Engulfing",
  "tf": "60"
}
```

---

## Parametreler ve Önerilen Değerler

### trend-suite.pine
| Parametre | Default | Önerilen (Swing) | Önerilen (Intraday) |
|-----------|---------|-----------------|---------------------|
| SuperTrend Periyot | 10 | 10-14 | 7-10 |
| SuperTrend Çarpan | 3.0 | 3.0 | 2.5-3.0 |
| Pivot Lookback | 10 | 10-15 | 5-10 |

### momentum-suite.pine
| Parametre | Default | Not |
|-----------|---------|-----|
| RSI Periyot | 14 | Değiştirme — standart |
| Adaptif OB/OS | Açık | Daha akıllı eşikler |
| MACD | 12/26/9 | Değiştirme — standart |

### sinyal-suite.pine
| Parametre | Default | Not |
|-----------|---------|-----|
| AL için Min Skor | 6 | Günlük için 6-7, Saatlik için 5-6 |
| SAT için Min Skor | 6 | Yukarıdaki ile aynı |
| Alert Min Skor | 7 | Sadece yüksek güven alertleri |

---

## Senaryo Örneği — THYAO Alım

1. **Günlük grafikte bak**: trend-suite → EMA 50 üstünde, SuperTrend yeşil ✓
2. **momentum-suite → RSI**: 52, MACD histogram pozitif, hacim ortalama üstü ✓
3. **volatilite-suite**: Squeeze yeni bitti, yukarı yön ✓
4. **sinyal-suite**: Bullish Engulfing formasyonu, Skor 8/10 ✓
5. **panel**: 4 zaman diliminin 3'ünde yeşil ✓
6. **Karar**: Alım fırsatı — ATR baz alarak SL belirle, 2:1 hedef koy
