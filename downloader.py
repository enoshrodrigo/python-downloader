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

