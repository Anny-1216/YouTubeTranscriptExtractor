Here is the complete `README.md` file you can use for your GitHub project:

````markdown
# 🎬 YouTube Playlist Transcript Downloader

A Python-based tool to **extract transcripts** (subtitles) from individual YouTube videos or entire **YouTube playlists**, and save them as `.txt` files.  
⚡ **No YouTube Data API required.**

---

## 🔧 Technologies Used

- **Python 3**
- `requests` – to fetch video and playlist pages
- `re` – for regex-based extraction
- `bs4 (BeautifulSoup)` – to parse playlist HTML
- `youtube-transcript-api` – to get transcripts from videos

---

## 📥 Features

- Input a **single YouTube video** URL or a **playlist URL**
- Extracts video IDs and titles automatically
- Downloads **available transcripts**
- Saves each transcript in a separate `.txt` file with the video title as the filename
- Automatically removes **duplicate links** from playlists

---

## 🚀 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/Anny-1216/youtube-transcript-downloader.git
cd youtube-transcript-downloader
````

### 2. Install Dependencies

Make sure you have Python 3 installed. Then install the required packages:

```bash
pip install -r requirements.txt
```

You can also install manually:

```bash
pip install requests beautifulsoup4 youtube-transcript-api
```

### 3. Run the Script

```bash
python transcript_downloader.py
```

Enter either:

* A YouTube **video URL**
  *Example:* `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
* Or a YouTube **playlist URL**
  *Example:* `https://www.youtube.com/playlist?list=PLxxxx...`

Transcripts (if available) will be saved in the current directory.

---

## ⚠️ Notes

* This tool **only works for YouTube videos that have transcripts (subtitles)**.

  * If a video has no transcript (e.g., private videos, music videos), a message will be shown.
* Works with **public playlists** only.
* YouTube may limit how many videos load per playlist page. This tool parses the raw HTML, so very long playlists may have missing entries.
* Duplicate video links from playlists are automatically removed.

---

## 📂 Output Example

For a video titled `Intro to Python`, the transcript will be saved as:

```
Intro to Python.txt
```

---

## 👤 Author

**GitHub:** [Anny-1216](https://github.com/Anny-1216)

---

## 📝 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

```.
```
