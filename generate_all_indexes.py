import os

base_dir = '.'
ignore_dirs = {'.git', '.github'}

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

for dirpath, dirnames, filenames in os.walk(base_dir):
    dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
    
    if dirpath == base_dir:
        continue

    folder_name = os.path.basename(dirpath)
    if not folder_name: continue

    subdirs = sorted([d for d in dirnames if d not in ignore_dirs])
    files_to_list = sorted([f for f in filenames if f != 'index.html' and not f.startswith('.')])
    
    if not subdirs and not files_to_list:
        continue

    print(f"Đang xử lý thư mục: {folder_name} - Có {len(subdirs)} thư mục con, {len(files_to_list)} file.")
    
    title = custom_titles.get(folder_name, f"📁 {folder_name}")
    content = html_template.format(title=title)
    
    for d in subdirs:
        content += f'        <a href="{d}/" class="file-item"><span class="icon">📁</span>{d}</a>\n'
        
    for f in files_to_list:
        icon = "📦" if f.lower().endswith('.zip') else "📄"
        content += f'        <a href="{f}" class="file-item"><span class="icon">{icon}</span>{f}</a>\n'

    content += """    </div>\n"""
    if dirpath != base_dir:
        content += '    <a href="../" class="back-link">← Về thư mục trước</a>\n'
    
    content += """</body>\n</html>"""

    index_path = os.path.join(dirpath, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
