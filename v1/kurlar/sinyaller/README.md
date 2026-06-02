# Kurlar Sinyal Paketi

## Ne Yapar?
Forex için uyarlanmış sinyal paketi. Konfluens skorunda **Stochastic OS** ve **Pivot desteği** faktörleri kritik ağırlık taşır. **Aktif seans bonusu** ile seans dışı sinyaller otomatik -1 puan cezalanır.

## Hisse Sinyal'den Farkları
| Faktör | Hisse | Kurlar |
|--------|-------|--------|
| Faktör 6 | 1.3x Hacim | **Stochastic OS (≤30)** |
| Faktör 10 | Destek yakın | **Pivot (S1/PP) yakın** |
| Ek faktör | Yok | **Seans bonusu** (+1/-1) |

## Seans Bonusu
- `sinyal_guclu ≥ 5` VE aktif seans → Sinyal gösterilir
- Seans dışı (Asya/Kapalı) sinyal → Skor -1 penalty
- Etiket: "✓ Seans" veya "⚠ Dışı"

## Pivota Yakın Bonus
Fiyat S1 veya PP seviyesine ATR×0.5 mesafedeyse +1 puan eklenir. Bu kombinasyon çok güçlü:
- **S1 desteği + Stochastic OS + Boğa mum** = 3 faktör aynı anda

## Hangi Dosyalarla Çalışır?
| Dosya | Uyum |
|-------|------|
| seans-suite.pine | ✓✓✓ | Seans bilgisi |
| trend-suite.pine | ✓✓✓ | Pivot seviyeleri |
| momentum-suite.pine | ✓✓✓ | Stochastic |
| panel/ana-panel.pine | ✓✓✓ | Özet tablo |

## Alert
`Kur AL/SAT`, `Güçlü AL (8+)`

Webhook JSON seans bilgisiyle:
```json
{"event":"KUR_AL","ticker":"EURUSD","price":1.0875,"skor":7,"seans":true}
```

## Zaman Dilimi
| TF | Güvenilirlik |
|----|-------------|
| 4 Saatlik | ⭐⭐⭐⭐⭐ |
| 1 Saatlik (LD/NY) | ⭐⭐⭐⭐ |
| Günlük | ⭐⭐⭐⭐ |
| 15dk | ⭐⭐⭐ |
