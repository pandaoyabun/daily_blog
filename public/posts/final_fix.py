import os
import re
from pathlib import Path

def final_cleanup(directory):
    path_obj = Path(directory)
    for file_path in path_obj.glob("*.md"):
        # 1. 拡張子を除いた名前を取得
        name = file_path.stem
        
        # 2. 末尾のドットを完全に削除 (Windowsの最優先エラー原因)
        name = name.rstrip('.')
        
        # 3. Windows禁止文字 \ / : * ? " < > | とスペースをハイフンに
        name = re.sub(r'[\\/:*?"<>| ]', '-', name)
        
        # 4. 長すぎるパス対策：ファイル名を先頭30文字に切り詰める
        # (日付 10文字 + 内容少し で十分ユニークになります)
        if len(name) > 30:
            name = name[:30]
            
        new_file_name = f"{name.rstrip('-')}.md"
        new_path = file_path.parent / new_file_name
        
        if file_path != new_path:
            try:
                # すでに同名ファイルがある場合の衝突回避
                if new_path.exists():
                    new_path = file_path.parent / f"{name[:25]}-{os.urandom(2).hex()}.md"
                
                os.rename(file_path, new_path)
                print(f"Safe: {file_path.name} -> {new_path.name}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    # 記事があるフォルダを直接指定
    target_dir = r"E:\daily_blog\content\posts"
    final_cleanup(target_dir)
