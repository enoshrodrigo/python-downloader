# 🎵 Media Downloader with Web Scraping and Progress Bar 🚀

This Python project allows you to scrape media file links from a given website and download them efficiently with a progress bar, providing an organized and automated way to handle bulk media downloads.

## ✨ Features

- 🔍 **Web Scraping:** Extracts media file URLs from a specified website using BeautifulSoup.
- 🎥 **File Type Filtering:** Downloads only specified file types (e.g., `.mp4`, `.avi`, `.mkv`).
- 📊 **Progress Bar:** Displays real-time download progress using `tqdm`.
- 📁 **Directory Management:** Automatically creates a `music_files` directory to store the downloaded files.

## 📋 Requirements

Ensure you have Python installed, then install the required packages by running:

```bash
pip install -r requirements.txt
```

### 📦 `requirements.txt`
```
requests
beautifulsoup4
tqdm
```

## 🚀 Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/enoshrodrigo/python-downloader.git
   cd media-downloader
   ```

2. **Update the `url` variable in the script with the target website URL:**
   ```python
   url = "http://188.165.227.112/portail/series/Game_of_thrones_S3/"
   ```

3. **Run the script:**
   ```bash
   python media_downloader.py
   ```

4. **View Downloads:** The media files will be downloaded to the `music_files` directory.

## 🛠️ How It Works

1. **Scrape the Website:** The script sends a GET request to the specified URL and parses the HTML content.
2. **Extract Media Links:** Identifies all anchor tags (`<a>`) containing media file extensions.
3. **Download Files:** Downloads each media file with a real-time progress bar.
4. **Save Files:** Stores the downloaded files in the `music_files` directory.

## 🧑‍💻 Code Example

```python
import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm  # Import tqdm for progress bar

url = "http://188.165.227.112/portail/series/Game_of_thrones_S3/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Create a directory to save files
os.makedirs("music_files", exist_ok=True)

for link in soup.find_all('a', href=True):
    file_url = url + link['href']
    if file_url.endswith(('.mp4', '.avi', '.mkv')):  # Filter by file type
        print(f"Downloading {file_url}...")

        # Get the file size
        file_response = requests.head(file_url)
        file_size = int(file_response.headers.get('Content-Length', 0))

        # Download the file with progress
        with requests.get(file_url, stream=True) as r:
            r.raise_for_status()  # Check for successful download
            file_path = os.path.join("music_files", link['href'])

            # Open the file and write the content
            with open(file_path, 'wb') as f:
                # Use tqdm for progress bar
                with tqdm(total=file_size, unit='B', unit_scale=True) as pbar:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            pbar.update(len(chunk))  # Update progress bar

        print(f"Downloaded {file_url} successfully!")
```

## 📝 Notes

- ⚠️ Ensure the target website allows scraping before running this script.
- 🔧 You can customize the file types by modifying the `if file_url.endswith(...)` condition.
- ⚡ Handle large files with caution, as the script may consume significant bandwidth and disk space.

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## 📜 License

This project is licensed under the MIT License.

