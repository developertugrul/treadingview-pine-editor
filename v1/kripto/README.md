# Kripto Para İndikatörleri
## BTC, ETH, Altcoin — Pine Script v6

---

## Klasördeki Dosyalar

| Dosya | Konum | İçerik |
|-------|-------|--------|
| `trend/trend-suite.pine` | Overlay | EMA 21/50/100/200, SuperTrend (3.5), Fibonacci, S/R, MTF |
| `momentum/momentum-suite.pine` | Alt panel | RSI, MACD, **Stochastic RSI** (kripto standart), Hacim |
| `volatilite/volatilite-suite.pine` | Overlay | BB (2.5), Keltner (2.0), Squeeze, ATR (2.5x) |
| `sinyaller/sinyal-suite.pine` | Overlay | 12 mum formasyonu, Konfluens, Webhook Alert |
| `panel/ana-panel.pine` | Overlay | MTF tablo (1S/4S/Günlük/Haftalık) |

---

## Kripto'ya Özel Farklar (Hisse'ye göre)

| Özellik | Hisse | Kripto |
|---------|-------|--------|
| SuperTrend Çarpan | 3.0 | **3.5** (daha volatil) |
| BB Çarpan | 2.0 | **2.5** |
| Keltner Çarpan | 1.5 | **2.0** |
| RSI OB/OS (Sabit) | 70/30 | **75/25** |
| Stochastic | Standard | **Stochastic RSI** tercih edilir |
| VWAP | İntraday | Yok (24/7 piyasa) |
| Fibonacci | Yok | Var (swing high/low'dan) |
| Pivot Lookback | 10 | **14** (daha uzun) |

---

## Zaman Dilimi Rehberi

| Zaman Dilimi | Kullanım | Güvenilirlik | Not |
|-------------|----------|--------------|-----|
| Haftalık (1H) | Uzun vadeli trend | ⭐⭐⭐⭐⭐ | BTC döngüsü analizi |
| Günlük (1G) | Swing trade | ⭐⭐⭐⭐⭐ | En güvenilir |
| 4 Saatlik (4S) | Kısa-orta vadeli | ⭐⭐⭐⭐ | Standart kripto TF |
| 1 Saatlik (1S) | Intraday | ⭐⭐⭐ | Giriş zamanlaması |
| 15 Dakikalık | Aktif trade | ⭐⭐ | Dikkatli kullan |
| 5 Dakikalık | Hızlı scalp | ⭐ | Sadece BTC/ETH'de |

**Öneri**: BTC Günlük trend → Altcoin 4S konfirm → 1S ile giriş zamanla.

---

## Fibonacci Seviyeleri

trend-suite içindeki Fibonacci seviyeleri **son N bar içindeki swing high-low'dan** hesaplanır:

- **%23.6** — Zayıf geri çekilme (trend güçlü)
- **%38.2** — Normal geri çekilme, ilk destek
- **%50.0** — Psikolojik orta seviye
- **%61.8** — **En kritik** — "Altın oran" geri çekilmesi
- **%78.6** — Derin geri çekilme (trend zayıflayabilir)

**Fibonacci + SuperTrend + Volume**: Fib 61.8 seviyesinde supertrend yükseliş + hacim spike = güçlü alım fırsatı.

---

## Stochastic RSI

Kripto piyasasında **Stochastic RSI** standart Stochastic'ten daha etkilidir:
- RSI'nın stochastic uygulaması
- Daha hızlı tepki verir
- %K ve %D kesişimleri güçlü sinyal verir
- **OS bölgesinde (%20 altı) kesişim**: Güçlü alım sinyali
- **OB bölgesinde (%80 üstü) kesişim**: Satış baskısı

---

## BTC Dominansı Not

Panel ve sinyaller BTC dominansını doğrudan çekmez, ama:
- BTC dominansı yükselirken: Altcoinler underperform eder
- BTC dominansı düşerken: Altseason — altcoin rallisi
- Bu bilgiyi `TOTAL3.D` grafiğini ayrı pencerede takip ederek kullan

---

## Alert Kurulumu

sinyal-suite webhook JSON formatı:
```json
{
  "event": "KRIPTO_AL",
  "ticker": "BTCUSDT",
  "price": 68500,
  "skor": 8,
  "formasyon": "Bull Engulfing",
  "tf": "240"
}
```

**Telegram Bot entegrasyonu için**: Webhook URL → Python Flask → Telegram Bot API

---

## Risk Yönetimi — Kripto Özeli

Kripto volatil olduğu için daha geniş stop-loss:
```
SL = Giriş - (2.5 × ATR)    [long]
SL = Giriş + (2.5 × ATR)    [short]
```

Pozisyon büyüklüğü = Maksimum risk tutarı / (Giriş - SL)

**Örnek**: 10,000 USDT portföy, %2 risk = 200 USDT risk
→ ATR = 1,500 USDT → Pozisyon = 200 / (2.5 × 1,500) = 0.053 BTC

---

## Senaryo Örneği — BTCUSDT Alım

1. **Günlük grafik**: EMA 21 > EMA 50 > EMA 100 ✓ SuperTrend yeşil ✓
2. **Fibonacci**: Fiyat 61.8% seviyesinde bounce ✓
3. **Stochastic RSI**: OS bölgesinden çıkış, kesişim yukarı ✓
4. **Squeeze**: Yeni bitti, yukarı momentum ✓
5. **Skor**: 8/10 ✓ → Güçlü AL sinyali
6. **ATR bazlı SL** → 2.5x ATR altına koy
