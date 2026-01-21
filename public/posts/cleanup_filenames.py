import os
import re
from pathlib import Path

def cleanup_filenames(directory):
    path_obj = Path(directory)
    for file_path in path_obj.glob("*.md"):
        # ファイル名から拡張子を除いた部分を取得
        old_name = file_path.stem
        # 1. 末尾のドットをすべて削除
        # 2. Windowsで禁止されている記号やスペースをハイフンに置換
        new_name = re.sub(r'\.+$', '', old_name)
        new_name = re.sub(r'[\\/:*?"<>| ]', '-', new_name)
        
        # 念のため名前を短く制限（50文字以内）
        new_name = new_name[:50]
        
        new_file_name = f"{new_name}.md"
        new_path = file_path.parent / new_file_name
        
        if file_path != new_path:
            try:
                os.rename(file_path, new_path)
                print(f"Renamed: {file_path.name} -> {new_file_name}")
            except Exception as e:
                print(f"Error renaming {file_path.name}: {e}")

if __name__ == "__main__":
    # 記事があるフォルダを指定
    cleanup_filenames("./content/posts")