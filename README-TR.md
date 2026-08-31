# VOD & Canlı Yayın İndirici

Twitch, Kick ve diğer yayın platformlarından VOD (geçmiş yayın) ve canlı yayın içeriklerini kolayca indırmenizi sağlayan modern bir masaüstü uygulamasıdır. `customtkinter` ile şık bir arayüze ve `yt-dlp` altyapısına sahiptir.

---

## Özellikler

- **Çoklu Platform Desteği:** Twitch, Kick ve yt-dlp tarafından desteklenen tüm video/yayın platformları.
- **Çözünürlük Seçimi:** En yüksek kaliteden (Best) 1080p, 720p, 480p ve 360p seçeneklerine kadar esnek çözünürlük ayarı.
- **Çoklu Dil Desteği:** Tek tıkla Türkçe ve İngilizce arayüz geçişi.
- **Anlık İlerleme Takibi:** İndirme hızı, kalan süre (ETA) ve yüzde bazlı ilerleme çubuğu.
- **Akıcı Arayüz (Multithreading):** İndirmeler arka planda çalışır, arayüzde donma veya kilitlenme yaşanmaz.

---

## Ön Gereksinimler

Uygulamanın sorunsuz çalışabilmesi için sisteminizde aşağıdaki bileşenlerin bulunması gerekir:

1. **Python 3.8 veya üzeri:** [python.org](https://www.python.org/) adresinden indirip kurabilirsiniz. (Kurulum sırasında *"Add Python to PATH"* seçeneğini işaretlemeyi unutmayın).
2. **FFmpeg:** Video ve ses akışlarını birleştirmek için gereklidir.
   - **Windows:** `winget install ffmpeg` veya `choco install ffmpeg` komutlarıyla yükleyebilirsiniz.
   - **Linux (Ubuntu/Debian):** `sudo apt install ffmpeg`
   - **macOS:** `brew install ffmpeg`

---

## Kurulum ve Çalıştırma

### 1. Depoyu Klonlayın veya İndirin
Kodları bilgisayarınıza indirin veya terminal üzerinden klonlayın:
```bash
git clone [https://github.com/endfreezy/vod-downloader.git](https://github.com/endfreezy/vod-downloader.git)
cd vod-downloader

