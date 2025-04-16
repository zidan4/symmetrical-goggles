import threading
import requests
import os

urls = [
    'https://example.com/file1.txt',
    'https://example.com/file2.txt',
    # Add more URLs
]

def download_file(url):
    local_filename = url.split('/')[-1]
    try:
        response = requests.get(url)
        with open(local_filename, 'wb') as f:
            f.write(response.content)
        print(f"✅ Downloaded {local_filename}")
    except Exception as e:
        print(f"⚠️ Failed to download {url}: {e}")

threads = []
for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
