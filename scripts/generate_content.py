import os
import json
import requests
from datetime import datetime

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

    # 各エクサンプルを処理
    for example in examples:
        # カテゴリに応じてプロンプトをカスタマイズ
        category = example.get('category', '')
        if category == "プログラミング":
            category_prompt = "特にプログラミングと開発の視点から、コード例やベストプラクティスを含めて"
        elif category == "資料作成":
            category_prompt = "特にビジネス文書作成の視点から、実践的なプロンプト例と構成テクニックを含めて"
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
"""
        
        # 処理済みまたは上限に達している場合はスキップ
        if example.get('processed', False) or processed_count >= 2:
            continue

        try:
            print("Claude APIにリクエストを送信中...")
            response = requests.post(
                'https://api.anthropic.com/v1/messages',
                headers=headers,
                json={
                    'model': 'claude-3-5-sonnet-20240620',  # コスパの良いモデル
                    'max_tokens': 1500,  # 出力を制限してコスト削減
                    'messages': [{'role': 'user', 'content': prompt}]
                }
            )
            
            # エラー処理とレスポンス解析
            if response.status_code != 200:
                print(f"API呼び出しエラー: ステータスコード {response.status_code}")
                print(f"レスポンス: {response.text}")
                continue
            
            response_data = response.json()
            content = response_data['content'][0]['text']
            
            # Jekyllの記事として保存
            date_str = datetime.now().strftime('%Y-%m-%d')
            slug = example['id'].lower().replace(' ', '-')
            filename = f"_posts/{date_str}-{slug}.md"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"""---
layout: post
title: "{example['title']}"
date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S +0900')}
categories: {example['category']}
tags: {json.dumps(example['tags'], ensure_ascii=False)}
source_url: "{example.get('source_url', '')}"
---
{content}
""")
            
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
