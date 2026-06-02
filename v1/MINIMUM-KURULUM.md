# Minimum Geçerli Kurulum
## Profesyonel İçin: Az Ama Doğru

---

## Neden "Az" Daha İyidir?

9 indikatör açmak analiz değil, **analiz felci**dir.
- Her çelişen sinyal belirsizlik yaratır
- Kural belirsizleşir, disiplin bozulur
- "Şu yeşil bu kırmızı, bekleyeyim" → Hiç işlem yapılmaz

Bir profesyonel **3-4 indikatör** kullanır. Gerisini bilgi olarak bilir, her gün açmaz.

---

## Günlük Minimum Kurulum (3 + 1 Panel)

### Her Grafik Açıldığında Açık Olacaklar:

```
1. evrensel/piyasa-rejimi.pine     ← "Bu sinyale güvenilebilir mi?"
2. [kategori]/trend/trend-suite.pine ← "Yön nerede?"
3. [kategori]/sinyaller/sinyal-suite.pine ← "Setup var mı?"
```

### Trade Girerken Ekle:
```
4. evrensel/risk-odül-hesaplayici.pine ← "Kaç lot, nerede SL, nerede TP?"
```

### Sadece Gerekince Ekle:
```
5. evrensel/piyasa-yapisi-suite.pine   ← Yapıdan emin değilsen
6. evrensel/ichimoku-suite.pine        ← Uzun vade pozisyon için
7. [kategori]/momentum/momentum-suite.pine ← Diverjans var mı?
```

---

## Kullanım Kuralları (Yazılı Olmalı, Kırılmaz)

### Kural 1 — Rejim Filtresi
```
Piyasa Rejimi = BEAR → Long sinyali gelirse: GEÇE
Piyasa Rejimi = BULL → Confluence ≥ 6 ise değerlendir
Piyasa Rejimi = YATAY → Sadece Squeeze patlama kırılımlarında
```

### Kural 2 — Skor Eşiği Rejime Göre
```
BULL rejimde:  Skor ≥ 6/10 → İşlem yapılabilir
YATAY rejimde: Skor ≥ 7/10 → İşlem yapılabilir
BEAR rejimde:  Skor ≥ 8/10 → YINE DE ÇOK DİKKATLİ
```

### Kural 3 — R:R Kuralı (KIRILMAz)
```
R:R < 1:2 → GİRİLMEZ. Başka setup ara.
```

### Kural 4 — Portföy Risk Limiti
```
Tek trade: Portföyün max %1-2'si risk
Aynı anda açık pozisyon: Max 3-4
Toplam risk: Portföyün max %5'i
```

### Kural 5 — Alert → Grafik, Grafik → Karar
```
Alert gelir → Grafiği aç → Kuralları kontrol et → Karar ver
Grafik sürekli açık kalmasın → Bakınca işlem yapma baskısı hissedilir
```

---

## Haftalık Rutin

### Pazar Akşamı (30 dakika) — Hafta Planı
1. BIST100/S&P Haftalık grafik → piyasa-rejimi kontrol
2. İzleme listesini tara (10-15 hisse/kripto/kur)
3. Bu hafta yakın setup var mı? Al not
4. Alert kurulumlarını güncelle

### Her Sabah (10 dakika)
1. DXY, Emtia (Altın, Petrol) yönü
2. BIST100 ilk 1 saatteki yönü
3. Alert var mı? Değerlendir

### Trade Sonrası (5 dakika)
1. Trade defterine ekle (template: KULLANIM-REHBERI'nde)
2. Neden girdin, ne oldu, öğrenilen nedir?

---

## Ne Zaman Hiç İşlem Yapılmaz?

```
□ Piyasa Rejimi BEAR ve belirsiz
□ Önemli bir ekonomik veri açıklanmadan 1 saat önce/sonra
□ "Piyasa açılışında" ilk 30 dakika (BIST: 10:00-10:30)
□ Grafik 30+ dakikadır açık, hâlâ karar veremedinse
□ R:R < 1:2 olan her durumda
□ Stop-Loss nereye koyacağını bilmiyorsan
```

---

## Gerçekçi Beklentiler

Bu sistem ne yapar:
- Sistematik karar verme sağlar
- Çelişen sinyaller filtreler
- Risk yönetimi disiplinini zorlar
- Emotion-free analiz çerçevesi sunar

Bu sistem ne yapmaz:
- Garantili karlı sinyal vermez (böyle bir sistem yoktur)
- Backtest doğrulaması yapmaz
- Seni disiplinli yapmaz (sadece sen yaparsın)
- Geçmişte çalışanın gelecekte çalışacağını garantilemez

---

## Sistemi Değerlendirme Süreci (2-4 Hafta Paper Trading)

**Canlı para koymadan önce** paper trading yap:
1. Her sinyali not al: Tarih, sembol, skor, rejim, SL, TP
2. Sonucu takip et: Kazandı mı, kaybetti mi?
3. 20+ trade sonrasında istatistik çıkar:
   - Win rate kaç? (Hedef: >50%)
   - Ortalama R:R kaç? (Hedef: >1.5)
   - Beklenen değer = Win rate × Ort. kazanç - Loss rate × Ort. kayıp

**Beklenen değer pozitifse** → Sistemi canlıya al.
**Negatifse** → Hangi faktörler işe yaramıyor, düzelt.

---

*Bu rehber araçları değil, kullanım disiplinini anlatır.*
*En iyi araç + en kötü disiplin = Para kaybı.*
*Vasat araç + mükemmel disiplin = Tutarlı kazanç.*
