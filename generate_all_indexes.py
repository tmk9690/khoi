import os

# The directories you want to scan (add or remove as needed)
target_dirs = ['.', 'Apks', 'Kodi', 'Kodi/Plugin Phim']

def generate_index(directory):
    if not os.path.exists(directory):
        return

    # Get all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Filter for zip and apk files (case insensitive)
    valid_extensions = ('.zip', '.apk')
    download_files = [f for f in files if f.lower().endswith(valid_extensions)]
    
    if not download_files:
        return

    # Create HTML content
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Index of {directory}</title>
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
    <h1>Files in /{directory}</h1>
    <ul>
"""
    for file in sorted(download_files):
        html_content += f'        <li><a href="./{file}">{file}</a></li>\n'
        
    html_content += """    </ul>
</body>
</html>"""

    # Write the HTML file
    index_path = os.path.join(directory, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated index for {directory}")

if __name__ == "__main__":
    for d in target_dirs:
        generate_index(d)
