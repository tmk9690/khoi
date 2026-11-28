"""Chép toàn bộ repo sang _site/ và tạo index.html cho MỌI thư mục."""
import html
import shutil
from pathlib import Path
from urllib.parse import quote

SOURCE = Path(".")
OUTPUT = Path("_site")
ROOT_TITLE = "Kho Lưu Trữ"

# Những mục không đưa lên trang (ngoài các file/thư mục bắt đầu bằng dấu chấm)
SKIP_ROOT = {"_site", "generate_all_indexes.py", "README.md"}

ICONS = {".apk": "📱", ".zip": "📦"}

PAGE = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background: #f6f8fa; color: #24292f; }}
h1 {{ font-size: 26px; border-bottom: 1px solid #d0d7de; padding-bottom: 12px; overflow-wrap: anywhere; }}
ul {{ list-style: none; padding: 0; background: #fff; border: 1px solid #d0d7de; border-radius: 6px; }}
li {{ display: flex; align-items: center; border-bottom: 1px solid #d0d7de; padding-left: 16px; }}
li:last-child {{ border-bottom: none; }}
li::before {{ content: attr(data-icon); margin-right: 10px; }}
li a {{ flex: 1; padding: 14px 16px 14px 0; overflow-wrap: anywhere; }}
a {{ color: #0969da; text-decoration: none; font-weight: 500; }}
a:hover, a:focus {{ text-decoration: underline; }}
</style>
</head>
<body>
<h1>{title}</h1>
{body}
{back}
</body>
</html>
"""


def visible_entries(folder, is_root):
    """Trả về (danh sách thư mục con, danh sách file) cần hiển thị."""
    dirs, files = [], []
    for item in folder.iterdir():
        name = item.name
        if name.startswith(".") or item.is_symlink():
            continue
        if is_root and name in SKIP_ROOT:
            continue
        if item.is_dir():
            dirs.append(item)
        elif name.lower() != "index.html":
            files.append(item)
    key = lambda p: p.name.casefold()
    return sorted(dirs, key=key), sorted(files, key=key)


def has_content(folder):
    """Thư mục chỉ còn index.html cũ (hoặc rỗng) thì bỏ qua."""
    dirs, files = visible_entries(folder, False)
    return bool(files) or any(has_content(d) for d in dirs)


def row(icon, name, is_dir):
    slash = "/" if is_dir else ""
    href = quote(name, safe="") + slash
    # Chữ trong thẻ <a> phải đúng bằng tên file thì Kodi mới đọc được
    text = html.escape(name, quote=False) + slash
    return f'<li data-icon="{icon}"><a href="{href}">{text}</a></li>'


def build(folder, target, is_root=True):
    target.mkdir(parents=True, exist_ok=True)
    dirs, files = visible_entries(folder, is_root)
    rows = []

    for d in dirs:
        if has_content(d):
            rows.append(row("📁", d.name, True))
            build(d, target / d.name, False)

    for f in files:
        shutil.copy2(f, target / f.name)
        rows.append(row(ICONS.get(f.suffix.lower(), "📄"), f.name, False))

    title = ROOT_TITLE if is_root else "📁 " + html.escape(folder.name)
    body = "<ul>\n" + "\n".join(rows) + "\n</ul>" if rows else "<p>Chưa có file.</p>"
    back = "" if is_root else '<p><a href="../">← Về thư mục trước</a></p>'
    page = PAGE.format(title=title, body=body, back=back)
    (target / "index.html").write_text(page, encoding="utf-8")
    print(f"Đã tạo: {target / 'index.html'} ({len(rows)} mục)")


if __name__ == "__main__":
    shutil.rmtree(OUTPUT, ignore_errors=True)
    build(SOURCE, OUTPUT)
    print("Hoàn tất!")
