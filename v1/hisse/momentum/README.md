# Hisse Momentum Paketi

## Ne Yapar?
RSI diverjans tespiti, MACD histogram analizi, Stochastic ve hacim analizi ile momentum durumunu ölçer. Adaptif RSI eşikleri son 50 bara göre dinamik olarak ayarlanır. Ayrı alt panelde görünür — grafiği kirletmez.

## İçindekiler
- **RSI (14) + EMA(9) Sinyal**: Adaptif OB/OS eşikli
- **RSI Diverjans**: Bullish/Bearish ve Hidden diverjans tespiti
- **MACD (12/26/9)**: 4 renkli histogram (pozitif/artan, pozitif/azalan, vb.)
- **Stochastic (14/3/3)**: OS bölgesi kesişim sinyali
- **OBV**: On Balance Volume trend göstergesi
- **Hacim Analizi**: Göreceli hacim + Spike tespiti
- **Momentum Skoru**: 0-100 bileşik skor

## Hangi Dosyalarla Çalışır?
| Dosya | Uyum | Açıklama |
|-------|------|----------|
| trend-suite.pine | ✓✓✓ | Trend + Momentum kombinasyonu |
| sinyal-suite.pine | ✓✓✓ | Momentum + Formasyon onayı |
| volatilite-suite.pine | ✓✓ | Squeeze + Momentum |
| ana-panel.pine | ✓✓✓ | RSI ve MACD panelde gösterilir |

## Diverjans Tespiti
- **Bullish Diverjans**: Fiyat dip yaparken RSI yükselen dip → Trend dönüşü sinyali
- **Bearish Diverjans**: Fiyat zirve yaparken RSI düşen zirve → Satım sinyali
- **Hidden Bullish**: Fiyat yükselen dip, RSI düşen dip → Trend devam (long için)
- **Hidden Bearish**: Fiyat düşen zirve, RSI yükselen zirve → Trend devam (short için)

## Adaptif OB/OS Eşikler
Standart RSI 70/30 yerine son 50 barlık ortalama + 1.5 standart sapma kullanılır:
- Güçlü trendli piyasada eşikler 75/35'e kayabilir
- Yatay piyasada 65/35 gibi dar kalır

## Alert Türleri
- `RSI OS Çıkış (AL)` — Aşırı satımdan döndü
- `RSI OB Çıkış (SAT)` — Aşırı alımdan döndü
- `Bullish Diverjans` — Trend dönüşü sinyali
- `Bearish Diverjans` — Zirve sinyali
- `MACD Al/Sat` — MACD kesişim
- `Hacim Spike` — 2x ortalama hacim

## Zaman Dilimi Performansı
| TF | Sonuç | Not |
|----|-------|-----|
| Günlük | ⭐⭐⭐⭐⭐ | Diverjans en güvenilir |
| 4 Saatlik | ⭐⭐⭐⭐ | Standart kullanım |
| 1 Saatlik | ⭐⭐⭐ | Hızlı momentum tespiti |
| 15dk | ⭐⭐ | Gürültülü, dikkatli kullan |
