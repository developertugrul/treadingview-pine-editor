# Kurlar Seans Paketi

## Ne Yapar?
Forex'e özgü seans analizi. Tokyo, Londra, New York seanslarını renkli arka planla işaretler. Asian Range'i tespit eder, kırılımlarında alert verir. Daily Pivot seviyeleri ek referans olarak gösterilir.

## İçindekiler
- **Tokyo Seansı** (00:00-09:00 UTC): Mavi arka plan
- **Londra Seansı** (07:00-16:00 UTC): Sarı arka plan
- **New York Seansı** (12:00-21:00 UTC): Pembe arka plan
- **LD/NY Overlap** (12:00-16:00 UTC): Yeşil arka plan 🔥
- **TK/LD Overlap** (07:00-09:00 UTC): Sarı-yeşil arka plan
- **Asian Range**: Tokyo seansı high/low — günlük referans
- **Pivot Seviyeleri**: PP/R1/R2/S1/S2

## Seans Önemi
En güvenilir sinyaller **LD/NY Overlap** döneminde gelir (12:00-16:00 UTC):
- Hem Londra hem New York açık
- En yüksek hacim ve likidite
- Trend hareketleri genellikle bu dönemde başlar veya güçlenir

## Asian Range Stratejisi
Asian Range Breakout — Forex'in en popüler stratejilerinden:
1. 09:00 UTC'de Tokyo kapanır → Asian Range kilitlenir
2. Londra açılışında (07:00 UTC) veya sonrasında range kırılırsa:
   - Yukarı kırılım → Long fırsat
   - Aşağı kırılım → Short fırsat
3. Hacim kontrolü şart (gürültüyü filtreler)

## Hangi Dosyalarla Çalışır?
| Dosya | Uyum |
|-------|------|
| trend-suite.pine | ✓✓✓ | Pivot + Seans kombinasyonu |
| sinyal-suite.pine | ✓✓✓ | Seans faktörü skor ekler |
| momentum-suite.pine | ✓✓ | Stochastic + seans |
| panel/ana-panel.pine | ✓✓✓ | Panel'de seans gösterilir |

## Alert
- `Londra Açılışı` — 07:00 UTC
- `NY Açılışı` — 12:00 UTC
- `LD/NY Overlap Başladı` — 12:00 UTC
- `Asian Break Yukarı/Aşağı` — Range kırılımı

## Saat Dilimi Notu
TradingView grafiğini **UTC** veya **Sunucu saatine** göre ayarla. Seans saatleri UTC bazlıdır.

## Zaman Dilimi
| TF | Güvenilirlik |
|----|-------------|
| 1 Saatlik | ⭐⭐⭐⭐⭐ | Seans kutularını görüntüle |
| 15 Dakikalık | ⭐⭐⭐⭐ | Asian breakout |
| 4 Saatlik | ⭐⭐⭐ | Genel seans rengi |
| Günlük+ | ⭐ | Anlamsız |
