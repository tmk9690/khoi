import os

# Đường dẫn gốc của toàn bộ Repository
base_dir = '.'

# Các thư mục KHÔNG CẦN tạo index (ví dụ thư mục hệ thống)
ignore_dirs = {'.git', '.github'}

# Tùy chỉnh tiêu đề cho từng thư mục (Nếu thư mục không có trong danh sách này, nó sẽ lấy tên thư mục làm tiêu đề)
custom_titles = {
    'Plugin Phim': '📁 Plugin Phim<br>(VNMedia & Kkphim)',
    'Kodi': '📁 Kodi',
    'Apks': '📁 Kho Ứng Dụng (APKs)'
}

html_template = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #f6f8fa; padding: 20px; color: #24292f; }}
        h1 {{ font-size: 24px; font-weight: 600; line-height: 1.25; margin-bottom: 24px; }}
        .file-list {{ background: #ffffff; border: 1px solid #d0d7de; border-radius: 6px; overflow: hidden; }}
        .file-item {{ display: flex; align-items: center; padding: 12px 16px; border-bottom: 1px solid #d0d7de; text-decoration: none; color: #0969da; font-size: 16px; }}
        .file-item:last-child {{ border-bottom: none; }}
        .file-item:hover {{ background-color: #f6f8fa; }}
        .icon {{ margin-right: 10px; }}
        .back-link {{ display: inline-block; margin-top: 24px; color: #0969da; text-decoration: none; font-size: 16px; }}
        .back-link:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <div class="file-list">
"""

# Quét toàn bộ thư mục
for dirpath, dirnames, filenames in os.walk(base_dir):
    # Bỏ qua các thư mục trong danh sách ignore
    dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
    
    # Bỏ qua thư mục gốc (không tạo index cho thư mục chính)
    if dirpath == base_dir:
        continue

    folder_name = os.path.basename(dirpath)
    if not folder_name: continue

    # Chỉ lấy các file (bỏ qua file index.html và các file ẩn)
    files_to_list = sorted([f for f in filenames if f != 'index.html' and not f.startswith('.')])
    
    # Nếu thư mục trống thì bỏ qua
    if not files_to_list:
        continue

    # Lấy tiêu đề (nếu có custom thì dùng, không thì lấy tên thư mục)
    title = custom_titles.get(folder_name, f"📁 {folder_name}")
    
    # Bắt đầu tạo HTML
    content = html_template.format(title=title)
    
    # Thêm danh sách file
    for f in files_to_list:
        # Gắn icon: File zip thì dùng hộp, file khác dùng tờ giấy
        icon = "📦" if f.lower().endswith('.zip') else "📄"
        content += f'        <a href="{f}" class="file-item"><span class="icon">{icon}</span>{f}</a>\n'

    # Thêm nút quay lại
    content += """    </div>\n"""
    if dirpath != base_dir:
        content += '    <a href="../" class="back-link">← Về thư mục trước</a>\n'
    
    content += """</body>\n</html>"""

    # Ghi đè file index.html vào thư mục tương ứng
    index_path = os.path.join(dirpath, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Đã cập nhật: {index_path}")
