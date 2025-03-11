import os
import json
import requests
import time
from datetime import datetime

# 収集したデータを格納するリスト
examples = []

def collect_from_github():
    print("GitHubからデータを収集中...")
    try:
        # GitHub APIのレート制限を考慮
        headers = {}
        github_token = os.environ.get('GITHUB_TOKEN')
        if github_token:
            headers['Authorization'] = f'token {github_token}'
        
        # 開発・プログラミング関連のリポジトリを検索
        query = "claude anthropic programming development"
        response = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": query, "sort": "stars", "per_page": 5},
            headers=headers
        )
        
        # レート制限に達した場合の処理
        if response.status_code == 403 and 'X-RateLimit-Remaining' in response.headers and int(response.headers['X-RateLimit-Remaining']) == 0:
            reset_time = int(response.headers['X-RateLimit-Reset'])
            wait_time = reset_time - int(time.time()) + 10  # 安全マージンを追加
            print(f"GitHub APIのレート制限に達しました。{wait_time}秒後に再試行します。")
            if wait_time > 0 and wait_time < 3600:  # 1時間以上待つのは現実的でない
                time.sleep(wait_time)
                return collect_from_github()  # 再帰的に再試行
            else:
                print("レート制限リセット待機時間が長すぎるため、GitHubからのデータ収集をスキップします。")
                return
        
        # その他のエラーチェックとデータ処理
        if response.status_code != 200:
            print(f"GitHub APIエラー: ステータスコード {response.status_code}")
            print(f"レスポンス: {response.text}")
            return
            
        repos = response.json().get("items", [])
        
        if not repos:
            print("リポジトリが見つかりませんでした")
            return
            
        print(f"{len(repos)}個のリポジトリを見つけました")
        
        # リポジトリ情報を構造化してリストに追加
        for repo in repos:
            # ファイル名に使用できる形式のIDを作成
            repo_id = f"github-{repo['name'].lower().replace(' ', '-')}-{repo['id']}"
            
            examples.append({
                "id": repo_id,
                "title": f"GitHub: {repo['name']} - Claude活用事例",
                "description": repo['description'] or "説明なし",
                "usage": f"開発者向けのClaude活用例。スター数: {repo['stargazers_count']}",
                "source_url": repo['html_url'],
                "category": "プログラミング",
                "tags": ["github", "オープンソース", "開発事例"],
                "processed": False
            })
    except Exception as e:
        print(f"データ収集中にエラーが発生しました: {e}")

def add_document_examples():
    print("資料作成の例を追加中...")
    examples.append({
        "id": "document-planning-efficiency",
        "title": "企画書・提案書作成を効率化するClaude活用法",
        "description": "ビジネス文書作成をClaudeで加速する実践テクニック",
        "usage": "企画書・提案書・報告書などの効率的な作成方法",
        "source_url": "",
        "category": "資料作成",
        "tags": ["企画書", "ビジネス文書", "効率化"],
        "processed": False
    })
    
    # 2つ目の手動エントリを追加
    examples.append({
        "id": "academic-report-techniques",
        "title": "レポート・論文作成のためのClaude活用テクニック",
        "description": "学術・研究文書の質を高めるClaude活用法",
        "usage": "学生・研究者向けの文書作成支援",
        "source_url": "",
        "category": "資料作成",
        "tags": ["学術", "論文", "研究"],
        "processed": False
    })

def add_service_examples():
    print("サービス開発の例を追加中...")
    examples.append({
        "id": "content-generation-service",
        "title": "Claudeを活用したコンテンツ自動生成サービス",
        "description": "ブログ・SNS投稿を効率的に作成するWebサービス事例",
        "usage": "マーケティング・コンテンツ制作の効率化",
        "source_url": "",
        "category": "サービス開発",
        "tags": ["コンテンツ作成", "マーケティング", "自動化"],
        "processed": False
    })
    
    # もう一つサービス開発の例を追加
    examples.append({
        "id": "claude-api-integration",
        "title": "既存サービスへのClaude API連携実装ガイド",
        "description": "自社サービスへのClaude APIの組み込み方と実装例",
        "usage": "API連携によるサービス機能の強化",
        "source_url": "",
        "category": "サービス開発",
        "tags": ["API連携", "システム開発", "実装例"],
        "processed": False
    })

def save_data():
    # _dataディレクトリがなければ作成
    os.makedirs("_data", exist_ok=True)
    
    # データファイルが既に存在する場合、マージする
    existing_examples = []
    if os.path.exists("_data/collected_examples.json"):
        try:
            with open("_data/collected_examples.json", "r", encoding="utf-8") as f:
                existing_examples = json.load(f)
            print(f"既存のデータを読み込みました: {len(existing_examples)}件")
            
            # 既存データからIDのリストを作成
            existing_ids = [ex["id"] for ex in existing_examples]
            
            # 新しいデータからまだ存在しないものだけを追加
            for example in examples:
                if example["id"] not in existing_ids:
                    existing_examples.append(example)
                    print(f"新しいデータを追加: {example['title']}")
                
            # 更新されたデータを保存
            with open("_data/collected_examples.json", "w", encoding="utf-8") as f:
                json.dump(existing_examples, f, indent=2, ensure_ascii=False)
            print(f"マージされたデータを保存しました: {len(existing_examples)}件")
            return
        except Exception as e:
            print(f"既存データの読み込み中にエラーが発生: {e}")
            print("新しいデータファイルを作成します")
    
    # 新規作成の場合
    try:
        with open("_data/collected_examples.json", "w", encoding="utf-8") as f:
            json.dump(examples, f, indent=2, ensure_ascii=False)
        print(f"データを保存しました: _data/collected_examples.json ({len(examples)}件)")
    except Exception as e:
        print(f"データ保存中にエラーが発生しました: {e}")

if __name__ == "__main__":
    collect_from_github()
    add_document_examples()
    add_service_examples()
    save_data()
    print(f"{len(examples)}件の事例を収集しました")
