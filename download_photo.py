import requests
import time
import os

def download_image(url, save_folder, interval=5):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    image_count = 1
    while True:
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                file_name = f"image_{image_count}.jpg"
                file_path = os.path.join(save_folder, file_name)
                
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                
                print(f"Đã tải xuống: {file_name}")
                image_count += 1
            else:
                print(f"Không thể tải hình ảnh")
            
        except Exception as e:
            print(f"Lỗi khi tải hình ảnh: {e}")
        
        time.sleep(interval)

stream_url = "http://192.168.1.87/"
save_directory = "./"

download_image(stream_url, save_directory, interval=5)
