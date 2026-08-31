import os
import sys
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
from PIL import Image
import yt_dlp

# CustomTkinter Teması
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class VODDownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("VOD & Stream Downloader")
        self.geometry("650x520")
        self.resizable(False, False)

        self.download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        self.lang_code = "TR"

        self.texts = {
            "TR": {
                "title": "VOD & Canlı Yayın İndirici",
                "url_label": "Yayın / VOD Linki (Twitch, Kick vb.):",
                "browse": "Gözat",
                "folder_label": "Kaydedilecek Klasör:",
                "quality_label": "Video Kalitesi:",
                "start_download": "İndirmeyi Başlat",
                "status_idle": "Durum: Hazır",
                "status_fetching": "Durum: Video bilgileri alınıyor...",
                "status_downloading": "Durum: İndiriliyor...",
                "status_done": "Durum: İndirme Tamamlandı!",
                "status_error": "Durum: Hata Oluştu!",
                "best": "En Yüksek (Best)",
                "err_url": "Lütfen geçerli bir URL girin!",
                "err_title": "Hata"
            },
            "EN": {
                "title": "VOD & Stream Downloader",
                "url_label": "Stream / VOD Link (Twitch, Kick etc.):",
                "browse": "Browse",
                "folder_label": "Save Directory:",
                "quality_label": "Video Quality:",
                "start_download": "Start Download",
                "status_idle": "Status: Ready",
                "status_fetching": "Status: Fetching video info...",
                "status_downloading": "Status: Downloading...",
                "status_done": "Status: Download Complete!",
                "status_error": "Status: Error Occurred!",
                "best": "Best Quality",
                "err_url": "Please enter a valid URL!",
                "err_title": "Error"
            }
        }

        self.setup_ui()

    def setup_ui(self):
        t = self.texts[self.lang_code]

        # Başlık ve Dil Değiştirici
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(fill="x", px=20, py=(15, 5))

        self.title_label = ctk.CTkLabel(self.header_frame, text=t["title"], font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(side="left")

        self.lang_btn = ctk.CTkSegmentedButton(self.header_frame, values=["TR", "EN"], command=self.change_language)
        self.lang_btn.set(self.lang_code)
        self.lang_btn.pack(side="right")

        # URL Girişi
        self.url_frame = ctk.CTkFrame(self)
        self.url_frame.pack(fill="x", px=20, py=10)

        self.url_label = ctk.CTkLabel(self.url_frame, text=t["url_label"])
        self.url_label.pack(anchor="w", px=10, py=(5, 0))

        self.url_entry = ctk.CTkEntry(self.url_frame, placeholder_text="https://...")
        self.url_entry.pack(fill="x", px=10, py=(0, 10))

        # Dizin Seçimi
        self.folder_frame = ctk.CTkFrame(self)
        self.folder_frame.pack(fill="x", px=20, py=10)

        self.folder_label = ctk.CTkLabel(self.folder_frame, text=t["folder_label"])
        self.folder_label.pack(anchor="w", px=10, py=(5, 0))

        self.folder_inner_frame = ctk.CTkFrame(self.folder_frame, fg_color="transparent")
        self.folder_inner_frame.pack(fill="x", px=10, py=(0, 10))

        self.folder_entry = ctk.CTkEntry(self.folder_inner_frame)
        self.folder_entry.insert(0, self.download_folder)
        self.folder_entry.pack(side="left", fill="x", expand=True, rx=5)

        self.browse_btn = ctk.CTkButton(self.folder_inner_frame, text=t["browse"], width=80, command=self.browse_folder)
        self.browse_btn.pack(side="right")

        # Kalite Seçeneği
        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.pack(fill="x", px=20, py=10)

        self.quality_label = ctk.CTkLabel(self.options_frame, text=t["quality_label"])
        self.quality_label.pack(side="left", px=10, py=10)

        self.quality_option = ctk.CTkOptionMenu(self.options_frame, values=[t["best"], "1080p", "720p", "480p", "360p"])
        self.quality_option.pack(side="left", px=10, py=10)

        # İlerleme Çubuğu ve Durum Metni
        self.progress_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.progress_frame.pack(fill="x", px=20, py=10)

        self.status_label = ctk.CTkLabel(self.progress_frame, text=t["status_idle"], font=ctk.CTkFont(size=12))
        self.status_label.pack(anchor="w")

        self.progress_bar = ctk.CTkProgressBar(self.progress_frame)
        self.progress_bar.set(0)
        self.progress_bar.pack(fill="x", py=5)

        # İndir Butonu
        self.download_btn = ctk.CTkButton(self, text=t["start_download"], font=ctk.CTkFont(size=14, weight="bold"), command=self.start_download_thread)
        self.download_btn.pack(fill="x", px=20, py=15)

    def change_language(self, choice):
        self.lang_code = choice
        t = self.texts[self.lang_code]

        self.title_label.configure(text=t["title"])
        self.url_label.configure(text=t["url_label"])
        self.folder_label.configure(text=t["folder_label"])
        self.browse_btn.configure(text=t["browse"])
        self.quality_label.configure(text=t["quality_label"])
        self.download_btn.configure(text=t["start_download"])
        self.status_label.configure(text=t["status_idle"])
        self.quality_option.configure(values=[t["best"], "1080p", "720p", "480p", "360p"])
        self.quality_option.set(t["best"])

    def browse_folder(self):
        selected = filedialog.askdirectory(initialdir=self.download_folder)
        if selected:
            self.download_folder = selected
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, self.download_folder)

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            downloaded_bytes = d.get('downloaded_bytes', 0)
            if total_bytes > 0:
                progress = downloaded_bytes / total_bytes
                self.progress_bar.set(progress)
                speed = d.get('_speed_str', 'N/A')
                eta = d.get('_eta_str', 'N/A')
                self.status_label.configure(text=f"{self.texts[self.lang_code]['status_downloading']} ({int(progress * 100)}%) - {speed} - ETA: {eta}")

        elif d['status'] == 'finished':
            self.progress_bar.set(1.0)
            self.status_label.configure(text=self.texts[self.lang_code]['status_done'])

    def start_download_thread(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning(self.texts[self.lang_code]["err_title"], self.texts[self.lang_code]["err_url"])
            return

        self.download_btn.configure(state="disabled")
        threading.Thread(target=self.download_video, args=(url,), daemon=True).start()

    def download_video(self, url):
        t = self.texts[self.lang_code]
        self.status_label.configure(text=t["status_fetching"])
        self.progress_bar.set(0)

        quality_choice = self.quality_option.get()
        if "1080" in quality_choice:
            fmt = "bestvideo[height<=1080]+bestaudio/best[height<=1080]"
        elif "720" in quality_choice:
            fmt = "bestvideo[height<=720]+bestaudio/best[height<=720]"
        elif "480" in quality_choice:
            fmt = "bestvideo[height<=480]+bestaudio/best[height<=480]"
        elif "360" in quality_choice:
            fmt = "bestvideo[height<=360]+bestaudio/best[height<=360]"
        else:
            fmt = "bestvideo+bestaudio/best"

        ydl_opts = {
            'format': fmt,
            'outtmpl': os.path.join(self.folder_entry.get(), '%(title)s.%(ext)s'),
            'progress_hooks': [self.progress_hook],
            'quiet': True,
            'no_warnings': True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            self.status_label.configure(text=t["status_error"])
            messagebox.showerror(t["err_title"], str(e))
        finally:
            self.download_btn.configure(state="normal")

if __name__ == "__main__":
    app = VODDownloaderApp()
    app.mainloop()
