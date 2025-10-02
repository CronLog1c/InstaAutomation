# InstaAutomation

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  

**InstaAutomation** is a lightweight Python tool that allows you to **download Instagram videos** and **automatically re-upload them to any account**. Simply provide the URL of a post, and the script takes care of the rest.

---

## Features

- Download Instagram videos using a single URL.  
- Automatically upload videos to any Instagram account.  
- Built with reliable Python libraries: [Instagrapi](https://github.com/adw0rd/instagrapi) and [Instaloader](https://instaloader.github.io/).  
- Easy setup and minimal dependencies.  

---

## Requirements

- **Python 3.8+**  
- **FFmpeg** installed and available in your system PATH (required for video processing).  
- Python libraries:  
```bash
pip install instagrapi instaloader imageio imageio-ffmpeg
```

---

## Installation

1. Clone the repository:  
```bash
git clone https://github.com/CronLog1c/IntaAutomation.git
```
2. Navigate to the project folder:  
```bash
cd IntaAutomation
```

---

## Usage

Run the script:  
```bash
python insta_automation.py
```

**Steps:**

1. Enter the URL of the Instagram post you want to download.  
2. The video will be downloaded and saved locally.  
3. Provide your Instagram login credentials to upload the video automatically.  

---

## Notes

- Keep your Instagram credentials secure.  
- Ensure FFmpeg is installed and accessible via your system PATH for proper video handling.  

---

## References

- [Instagrapi GitHub](https://github.com/adw0rd/instagrapi)  
- [Instaloader Official Site](https://instaloader.github.io/)  
