# VOD & Stream Downloader

A modern desktop application built to download VODs and video content from live-streaming platforms such as Twitch, Kick, and more. Powered by `customtkinter` for UI and `yt-dlp` for downloading capabilities.

## Features

- **Multi-Platform Support:** Twitch, Kick, and all other platforms supported by yt-dlp.
- **Resolution Control:** Select preferred video quality ranging from Best Quality down to 360p.
- **Bilingual Interface:** Real-time UI toggle between English and Turkish.
- **Live Tracking:** Real-time download speed, percentage, and estimated time remaining (ETA).
- **Non-blocking UI:** Multithreaded architecture ensures smooth UI execution during heavy downloads.

## Prerequisites

- Python 3.8+
- FFmpeg installed on your system (Required for merging video and audio streams)

## Installation

1. Clone the repository or download the source code:
   ```bash
   git clone [https://github.com/endfreezy/vod-downloader.git](https://github.com/endfreezy/vod-downloader.git)
   cd vod-downloader
