import os

# Đường dẫn tới thư mục cần tạo index
folder_path = 'Kodi/Plugin Phim'
html_file = os.path.join(folder_path, 'index.html')

# Mẫu HTML với CSS mô phỏng giao diện hiện tại của bạn
html_template = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plugin Phim</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #f6f8fa; padding: 20px; color: #24292f; }
        h1 { font-size: 24px; font-weight: 600; line-height: 1.25; margin-bottom: 24px; }
        .file-list { background: #ffffff; border: 1px solid #d0d7de; border-radius: 6px; overflow: hidden; }
        .file-item { display: flex; align-items: center; padding: 12px 16px; border-bottom: 1px solid #d0d7de; text-decoration: none; color: #0969da; font-size: 16px; }
        .file-item:last-child { border-bottom: none; }
        .file-item:hover { background-color: #f6f8fa; }
        .icon { margin-right: 10px; }
        .back-link { display: inline-block; margin-top: 24px; color: #0969da; text-decoration: none; font-size: 16px; }
        .back-link:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>📁 Plugin Phim<br>(VNMedia & Kkphim)</h1>
    <div class="file-list">
"""

# Quét các file trong thư mục
if os.path.exists(folder_path):
    # Lấy danh sách file, sắp xếp theo tên
    files = sorted(os.listdir(folder_path))
    for filename in files:
        # Chỉ lấy các file .zip hoặc .ZIP
        if filename.lower().endswith('.zip'):
            html_template += f'        <a href="{filename}" class="file-item"><span class="icon">📦</span>{filename}</a>\n'

# Đóng thẻ HTML và thêm nút quay lại
html_template += """    </div>
    <a href="../" class="back-link">← Về thư mục Kodi</a>
</body>
</html>"""

# Ghi nội dung vào file index.html
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Đã cập nhật {html_file} thành công!")
