# TradingView Pine Script Koleksiyonu
### Profesyonel Teknik Analiz Sistemi — v1

---

## Bu Proje Hakkında

Bu depo, TradingView platformunda kullanılmak üzere geliştirilmiş **Pine Script v6** tabanlı teknik analiz indikatörlerini içerir. Sistem; hisse senedi, kripto para, döviz kurları ve emtia piyasaları için ayrı ayrı yapılandırılmış, birbirleriyle uyumlu indikatör paketlerinden oluşur.

Her indikatör dosyası, tek bir gösterge yerine birbiriyle çalışmak üzere tasarlanmış birden fazla analiz aracını bir araya getirir. Dark mode/light mode otomatik uyumu, webhook destekli alert sistemi ve çok zaman dilimli (MTF) analiz bu sistemin temel özellikleri arasındadır.

---

## Klasör Yapısı

```
tradingview/
├── README.md               ← Bu dosya
│
├── v1/                     ← Aktif sistem (Pine Script v6)
│   ├── KULLANIM-REHBERI.md ← Başlangıç için oku
│   ├── MINIMUM-KURULUM.md  ← Hangi dosyaları kullanmalısın?
│   ├── README.md           ← Sistem tanıtımı ve hızlı başlangıç
│   │
│   ├── notlar/             ← Varlık sınıfı bazında detaylı rehberler
│   │   ├── HISSE-NOTLARI.md
│   │   ├── KRIPTO-NOTLARI.md
│   │   ├── KURLAR-NOTLARI.md
│   │   └── EMTIA-NOTLARI.md
│   │
│   ├── evrensel/           ← Tüm varlık sınıflarında çalışan araçlar
│   │   ├── piyasa-rejimi.pine
│   │   ├── piyasa-yapisi-suite.pine
│   │   ├── ichimoku-suite.pine
│   │   ├── risk-odül-hesaplayici.pine
│   │   └── goreceli-guc-suite.pine
│   │
│   ├── hisse/              ← BIST ve global hisse senetleri
│   ├── kripto/             ← BTC, ETH ve altcoinler
│   ├── kurlar/             ← Forex ve döviz çiftleri
│   └── emtia/              ← Altın, petrol, bakır, tarım
│
└── [eski .pine dosyaları]  ← Arşiv — v1 öncesi bireysel denemeler
```

---

## Hızlı Başlangıç

1. `v1/KULLANIM-REHBERI.md` dosyasını oku — sistemin nasıl kullanıldığı, hangi sırayla bakılması gerektiği burada.
2. Hangi piyasayla çalışıyorsan ilgili `notlar/` dosyasını oku.
3. İlgili kategorinin indikatör dosyalarını TradingView Pine Editor'a yapıştır.
4. Minimum kurulum için `v1/MINIMUM-KURULUM.md` dosyasına bak.

---

## Sistem Özellikleri

| Özellik | Detay |
|---------|-------|
| Pine Script Versiyonu | v6 |
| Dark / Light Mode | Otomatik uyum (`chart.bg_color`) |
| Alert Sistemi | `alertcondition` + `alert()` + Webhook JSON |
| Multi-Timeframe | `request.security()` + `barstate.isconfirmed` |
| Piyasa Yapısı | HH/HL/LH/LL + Break of Structure + Order Block |
| Risk Yönetimi | SL/TP/Pozisyon boyutu hesaplayıcı |
| Göreceli Güç | Varlık vs Benchmark karşılaştırması |
| Dil | Türkçe arayüz ve dokümantasyon |

---

## Desteklenen Piyasalar

- **Hisse Senedi:** BIST (XU100, XU030), Global (S&P 500, NASDAQ)
- **Kripto:** BTC, ETH ve tüm major/minor altcoinler
- **Döviz Kurları:** Major Forex çiftleri (EUR/USD, GBP/USD), USD/TRY ve cross çiftler
- **Emtia:** Değerli metaller (XAUUSD, XAGUSD), Enerji (CL, NG), Endüstriyel metaller (HG)

---

## ⚠️ Yasal Uyarı / Disclaimer

> **Bu projede yer alan hiçbir içerik, indikatör, sinyal veya analiz araçları yatırım tavsiyesi niteliği taşımaz.**
>
> Buradaki tüm içerikler yalnızca **eğitim ve bilgilendirme** amacıyla hazırlanmıştır. Teknik analiz araçları geçmiş fiyat verilerine dayalıdır ve gelecekteki fiyat hareketlerini garanti etmez. Her yatırım kararı, yatırımcının kendi araştırması, risk toleransı ve finansal durumu gözetilerek alınmalıdır.
>
> Finansal piyasalarda işlem yapmak sermaye kaybı riski içerir. Kaybetmeyi göze alamayacağın tutarı asla yatırıma koyma.
>
> Gerektiğinde lisanslı bir yatırım danışmanına başvur.

---

## Sürüm Geçmişi

| Sürüm | Durum | Açıklama |
|-------|-------|----------|
| **v1** | ✅ Aktif | Pine Script v6, dark mode, MTF, webhook, 4 piyasa kategorisi |
| v2 | 🔜 Planlanan | — |

---

*Pine Script v6 · TradingView · Türkçe*
