import os

# Danh sách các thư mục bạn muốn quét để tạo index
target_dirs = ['.', 'Apks', 'Kodi', 'Kodi/Plugin Phim']

def generate_index(directory):
    if not os.path.exists(directory):
        return

    # Lấy tất cả các file trong thư mục
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Lọc lấy file .zip và .apk (không phân biệt chữ hoa chữ thường)
    valid_extensions = ('.zip', '.apk')
    download_files = [f for f in files if f.lower().endswith(valid_extensions)]
    
    if not download_files:
        return

    # Tạo nội dung HTML
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Danh sách file - {directory}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 10px 0; }}
        a {{ text-decoration: none; color: #0366d6; font-size: 18px; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h2>Các file trong thư mục /{directory}</h2>
    <ul>
"""
    for file in sorted(download_files):
        html_content += f'        <li><a href="./{file}">{file}</a></li>\n'
        
    html_content += """    </ul>
</body>
</html>"""

    # Ghi file index.html
    index_path = os.path.join(directory, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Đã tạo xong index cho thư mục: {directory}")

if __name__ == "__main__":
    for d in target_dirs:
        generate_index(d)
