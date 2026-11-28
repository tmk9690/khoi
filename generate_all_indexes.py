import os

# Danh sách các thư mục cần tạo index (Bạn có thể thêm/bớt tùy ý)
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

    # Tạo nội dung HTML với CSS cơ bản cho đẹp
    html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Danh sách file - {directory}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; padding: 20px; background-color: #f6f8fa; color: #24292f; }}
        .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
        h2 {{ border-bottom: 1px solid #d0d7de; padding-bottom: 10px; margin-top: 0; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 12px 0; padding: 10px; background: #f6f8fa; border-radius: 6px; border: 1px solid #d0d7de; }}
        a {{ text-decoration: none; color: #0969da; font-weight: 500; display: block; word-break: break-all; }}
        a:hover {{ text-decoration: underline; }}
        .icon {{ margin-right: 8px; }}
    </style>
</head>
<body>
    <div class="container">
        <h2>📁 Thư mục: /{directory}</h2>
        <ul>
"""
    for file in sorted(download_files):
        # Xác định icon dựa vào đuôi file
        icon = "📦" if file.lower().endswith('.zip') else "📱"
        html_content += f'        <li><a href="./{file}"><span class="icon">{icon}</span>{file}</a></li>\n'
        
    html_content += """    </ul>
    </div>
</body>
</html>"""

    # Ghi file index.html
    index_path = os.path.join(directory, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Đã tạo xong index cho thư mục: {directory}")

if __name__ == "__main__":
    print("Bắt đầu quét và tạo index...")
    for d in target_dirs:
        generate_index(d)
    print("Hoàn tất!")
