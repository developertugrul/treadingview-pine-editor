# Evrensel Araçlar
## Tüm Varlık Sınıflarında Çalışır

Bu klasördeki dosyalar herhangi bir kategoriye özgü değildir. Hisse, kripto, kurlar ve emtia grafiklerinde kullanılabilir.

---

## Dosyalar

| Dosya | Öncelik | Ne Yapar |
|-------|---------|----------|
| `piyasa-yapisi-suite.pine` | ⭐⭐⭐ KRİTİK | HH/HL/LH/LL, Break of Structure, Order Block, FVG |
| `ichimoku-suite.pine` | ⭐⭐⭐ ÖNEMLİ | Tenkan/Kijun/Kumo, TK Cross, ideal sinyal |
| `risk-odül-hesaplayici.pine` | ⭐⭐⭐ KRİTİK | SL/TP/Pozisyon Boyutu, R:R kontrolü |
| `goreceli-guc-suite.pine` | ⭐⭐ ÖNEMLİ | Hisse vs Endeks karşılaştırması, Alfa |

---

## Kullanım Önceliği

### Her Analizde Kullanılmalı
```
piyasa-yapisi-suite  → "Trendin yapısı ne? HH/HL mi?"
risk-odül-hesaplayici → "Risk ve ödülüm ne?" (her trade'den önce)
```

### Sık Kullanılmalı
```
ichimoku-suite       → Trend + S/R + Momentum tek görünümde
goreceli-guc-suite   → "Bu hisse güçlü mü yoksa piyasayla mı gidiyor?"
```

---

## piyasa-yapisi-suite.pine

Profesyonel analizin temel taşı. Fiyat yapısını okur:

- **HH (Higher High)** = Yükselen zirve → Güçlü uptrend
- **HL (Higher Low)** = Yükselen dip → Uptrend devam
- **LH (Lower High)** = Düşen zirve → Downtrend başlıyor
- **LL (Lower Low)** = Düşen dip → Güçlü downtrend

**Break of Structure (BoS):** Mevcut trendin kırıldığı nokta. En önemli alert.
- Bearish BoS → Fiyat önemli bir Higher Low'u kırdı → Trend döndü
- Bullish BoS → Fiyat önemli bir Lower High'ı kırdı → Trend döndü

**Fair Value Gap (FVG):** Kurumsal alım/satım bıraktığı boşluklar. Bu boşluklara fiyat genellikle geri döner.

**Order Block:** Kurumların kalabalık emir verdiği bölgeler. Yeşil/kırmızı kutular.

---

## ichimoku-suite.pine

Kurumsal kanalların en çok kullandığı tek indikatör. 5 şeyi bir arada gösterir:

| Bileşen | Periyot | Anlam |
|---------|---------|-------|
| Tenkan-sen | 9 | Kısa vade momentum |
| Kijun-sen | 26 | Orta vade denge |
| Senkou A | 26 ileriye | Dinamik destek |
| Senkou B | 52 ileriye | Güçlü S/R |
| Chikou | 26 geriye | Onay sinyali |

**İdeal Bullish Sinyal** (hepsi aynı anda olursa çok güçlü):
1. Fiyat Bulut üstünde
2. TK Bullish Cross (Tenkan Kijun'u yukarı kesti)
3. Bulut yeşil
4. Chikou fiyatın üstünde

**Zayıf/Gelişmekte Sinyal:** Sadece TK Cross, diğerleri henüz değil.

---

## risk-odül-hesaplayici.pine

**Her trade girişinden önce açılmalı.** Parametreleri gir, otomatik hesaplar:
- TP1, TP2, TP3 fiyatları
- Pozisyon büyüklüğü (lot/hisse)
- Portföyün yüzde kaçını risk aldığın
- R:R < 1:2 ise kırmızı UYARI: GİRME

Tablo sağ üstte görünür. Çizgiler grafik üstüne işlenir.

**Altın Kural:** `risk_pct = 1.0` (her trade'de portföyün maks %1'i risk)

---

## goreceli-guc-suite.pine

Alt panel indikatörü. BIST hisseleri için benchmark: `BIST:XU100`

**Benchmark Seçimi:**
- BIST hissesi → `BIST:XU100`
- ABD hissesi → `SP:SPX` veya `NASDAQ:NDX`
- Kripto altcoin → `CRYPTOCAP:BTC.D`
- Altın → karşılaştırmak için `TVC:DXY`

**Okuması:**
- RS > 0 ve yükseliyor → Hisse endeksten güçlü → BUY tarafı
- RS < 0 ve düşüyor → Hisse endeksten zayıf → Kaçın veya SAT
- Piyasa düşerken RS > 0 → "Savunmacı Güç" → ⭐ Nadiren görülür, çok değerli sinyal

---

## Önerilen Kullanım Düzeni

```
Haftalık grafik:
  ├── piyasa-yapisi-suite  (büyük yapı)
  └── ichimoku-suite       (cloud pozisyonu)

Günlük grafik:
  ├── trend-suite          (EMA + SuperTrend)
  ├── piyasa-yapisi-suite  (HH/HL tespiti)
  └── goreceli-guc-suite   (endeks karşılaştırması)

4 Saatlik grafik:
  ├── sinyal-suite         (giriş sinyali)
  └── risk-odül-hesaplayici (SL/TP hesabı)
```
