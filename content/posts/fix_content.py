import os
from pathlib import Path

def fix_markdown_body(directory):
    path_obj = Path(directory)
    for file_path in path_obj.glob("*.md"):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # フロントマターの区切り '---' が2つあるか確認
        parts = content.split('---')
        
        if len(parts) >= 3:
            # すでに区切りがある場合、本文の前に改行が足りない可能性を修正
            header = parts[1]
            body = "---".join(parts[2:]).strip()
            new_content = f"---\n{header.strip()}\n---\n\n{body}"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                print(f"Fixed body for: {file_path.name}")
        else:
            # 区切りが足りない場合（本文が宙に浮いている）
            print(f"Skipped (No separators found): {file_path.name}")

if __name__ == "__main__":
    target_dir = r"E:\daily_blog\content\posts"
    fix_markdown_body(target_dir)