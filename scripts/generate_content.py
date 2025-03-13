import os
import json
import requests
import time
import re
from datetime import datetime

def slugify(text):
    """URLフレンドリーなスラグを作成"""
    # 英数字以外を'-'に置換し、連続した'-'を単一の'-'にする
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', text.lower())
    # 先頭と末尾の'-'を削除
    slug = slug.strip('-')
    return slug

def generate_content():
    # 環境変数からAPIキーを取得
    api_key = os.environ.get('CLAUDE_API_KEY')
    if not api_key:
        print("エラー: CLAUDE_API_KEYが設定されていません")
        return

    # Claude APIの設定
    headers = {
        'x-api-key': api_key,
        'content-type': 'application/json',
        'anthropic-version': '2023-06-01'
    }

    # データ読み込み
    try:
        print("収集したデータを読み込んでいます...")
        if os.path.exists('_data/collected_examples.json'):
            with open('_data/collected_examples.json', 'r', encoding='utf-8') as f:
                examples = json.load(f)
            print(f"{len(examples)}件のデータを読み込みました")
        else:
            print("警告: データファイルが見つかりません。空のリストで始めます。")
            examples = []
    except json.JSONDecodeError as e:
        print(f"警告: データファイルの形式が正しくありません: {e}")
        print("空のリストで始めます。")
        examples = []

    processed_count = 0
    max_to_process = 2  # 1回のワークフローで生成する記事数の上限

    # _postsディレクトリがなければ作成
    os.makedirs("_posts", exist_ok=True)

    # 各エクサンプルを処理
    for example in examples:
        # 処理済みまたは上限に達している場合はスキップ
        if example.get('processed', False) or processed_count >= max_to_process:
            continue

        # カテゴリに応じてプロンプトをカスタマイズ
        category = example.get('category', '')
        if category == "プログラミング":
            category_prompt = "特にプログラミングと開発の視点から、コード例やベストプラクティスを含めて"
        elif category == "資料作成":
            category_prompt = "特にビジネス文書作成の視点から、実践的なプロンプト例と構成テクニックを含めて"
        elif category == "サービス開発":
            category_prompt = "特にサービス開発とAPI連携の視点から、実装例とユースケースを含めて"
        else:
            category_prompt = ""

        # プロンプト生成
        prompt = f"""
以下のClaude AI活用事例を、日本語で分かりやすく解説する実践的な記事を書いてください。
{category_prompt}、以下の構成で記事を書いてください:
1. 導入（100単語程度）: この活用法の主な価値と用途
2. 活用シーン（200単語程度）: どのような場面で役立つか、具体的なユースケース
3. 実践ステップ（箇条書き5-7項目）: 段階的な実装手順
4. プロンプト例（2-3例）: 実際に使えるプロンプトテンプレート
5. 応用テクニック（150単語程度）: さらに効果を高めるための工夫
6. まとめと次のステップ（100単語程度）: 要点の整理と発展的な活用法
情報:
タイトル: {example['title']}
説明: {example['description']}
使用方法: {example['usage']}
URL: {example.get('source_url', 'なし')}
実践的で具体的な内容にし、読者が即実践できるようにしてください。必要に応じて図表や具体例を含め、技術的に正確な内容にしてください。
また、Markdownフォーマットで作成し、適切な見出し（##, ###）を使用してください。
"""

        try:
            print(f"Claude APIにリクエストを送信中... タイトル: {example['title']}")
            
            # 最大3回まで再試行
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    response = requests.post(
                        'https://api.anthropic.com/v1/messages',
                        headers=headers,
                        json={
                            'model': 'claude-3-haiku-20240307',  # 最新の低コストモデル
                            'max_tokens': 1500,  # 出力を制限してコスト削減
                            'messages': [{'role': 'user', 'content': prompt}]
                        },
                        timeout=60  # タイムアウト設定
                    )
                    response.raise_for_status()  # HTTPエラーを例外として発生
                    break  # 成功したらループ終了
                except (requests.exceptions.RequestException, requests.exceptions.HTTPError) as e:
                    if attempt < max_retries - 1:
                        wait_time = (attempt + 1) * 10  # バックオフ戦略
                        print(f"APIリクエスト失敗 ({e}). {wait_time}秒後に再試行します ({attempt+1}/{max_retries})")
                        time.sleep(wait_time)
                    else:
                        print(f"最大再試行回数に達しました。このアイテムをスキップします: {example['title']}")
                        raise
            
            # レスポンス解析
            response_data = response.json()
            content = response_data['content'][0]['text']
            
            # Jekyllの記事として保存
            current_date = datetime.now()
            date_str = current_date.strftime('%Y-%m-%d')
            
            # ファイル名に使用できるスラグを作成
            slug = slugify(example['id'])
            
            # ファイル名作成とカテゴリのスラグ化
            filename = f"_posts/{date_str}-{slug}.md"
            
            # タグを適切な形式に変換
            tags_formatted = ', '.join([f'"{tag}"' for tag in example['tags']])
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"""---
layout: post
title: "{example['title']}"
date: {current_date.strftime('%Y-%m-%d %H:%M:%S +0900')}
categories: {example['category']}
tags: [{tags_formatted}]
---

{content}
""")
            
            print(f"記事を生成しました: {filename}")
            
            # 処理済みとしてマーク
            example['processed'] = True
            processed_count += 1
        
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            continue

    # 更新したデータを保存
    try:
        with open('_data/collected_examples.json', 'w', encoding='utf-8') as f:
            json.dump(examples, f, ensure_ascii=False, indent=2)
        print("データファイルを更新しました。")
    except Exception as e:
        print(f"データファイルの更新中にエラーが発生しました: {e}")

if __name__ == "__main__":
    generate_content()
# 既存のスクリプトに以下のコードを追加

# カテゴリごとのデフォルトサムネイル
category_thumbnails = {
    "資料作成": "/assets/images/thumbnails/document/default.jpg",
    "サービス開発": "/assets/images/thumbnails/service/default.jpg",
    "プログラミング": "/assets/images/thumbnails/programming/default.jpg"
}

# 以下の部分を修正（ファイル生成部分）
# thumbnail_path を取得
thumbnail_path = category_thumbnails.get(example['category'], "/assets/images/thumbnails/default-thumb.jpg")

# 記事生成部分
with open(filename, 'w', encoding='utf-8') as f:
    f.write(f"""---
layout: post
title: "{example['title']}"
date: {current_date.strftime('%Y-%m-%d %H:%M:%S +0900')}
categories: {example['category']}
tags: [{tags_formatted}]
thumbnail: {thumbnail_path}
---

{content}
""")
