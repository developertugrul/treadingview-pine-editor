# Kurlar Ana Panel

## Ne Yapar?
Forex MTF dashboard. Hisse paneline ek olarak **aktif seans bilgisi** ve **Daily Pivot seviyeleri** tabloda gösterilir. Pip değerini otomatik hesaplar.

## Panel Ek Satırları (Hisse panelinden farklı)
- **Seans satırı**: "LD/NY OVERLAP 🔥" veya "Londra 🟡" gibi aktif seans bilgisi
- **Pivot satırı**: PP / R1 / S1 değerleri
- **ATR (pip)**: ATR pip cinsinden → SL hesabı

## SL Hesabı (pip)
Panel alt satırında gösterilir:
```
Pip Değeri = ATR / (syminfo.mintick × 10)
Önerilen SL = 1.5 × ATR pip
```

Örnek: ATR = 0.0015, pip = 1.5 → SL = 2.25 pip mesafe × lot büyüklüğü

## Default TF'ler
- TF1: 15dk
- TF2: 1S
- TF3: 4S
- TF4: Günlük

## Hangi Dosyalarla Çalışır?
| Dosya | Uyum |
|-------|------|
| seans-suite.pine | ✓✓✓ |
| trend-suite.pine | ✓✓✓ |
| momentum-suite.pine | ✓✓✓ |
| sinyal-suite.pine | ✓✓✓ |

## Zaman Dilimi
| TF | Güvenilirlik |
|----|-------------|
| 1 Saatlik | ⭐⭐⭐⭐⭐ |
| 4 Saatlik | ⭐⭐⭐⭐ |
| 15dk | ⭐⭐⭐ |
