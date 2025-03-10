def collect_from_github():
    print("GitHubからデータを収集中...")
    try:
        # 開発・プログラミング関連のリポジトリを検索
        query = "claude anthropic programming development"
        response = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": query, "sort": "stars", "per_page": 5}
        )
        
        # エラーチェックとデータ処理
        if response.status_code != 200:
            print(f"GitHub APIエラー: ステータスコード {response.status_code}")
            return
            
        repos = response.json().get("items", [])
        
        if not repos:
            print("リポジトリが見つかりませんでした")
            return
            
        print(f"{len(repos)}個のリポジトリを見つけました")
        
        # リポジトリ情報を構造化してリストに追加
        for repo in repos:
            examples.append({
                "id": f"github-{repo['id']}",
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
    examples.append({
        "id": "manual-doc-1",
        "title": "企画書・提案書作成を効率化するClaude活用法",
        "description": "ビジネス文書作成をClaudeで加速する実践テクニック",
        "usage": "企画書・提案書・報告書などの効率的な作成方法",
        "source_url": "",
        "category": "資料作成",
        "tags": ["企画書", "ビジネス文書", "効率化"],
        "processed": False
    })
    
    # 2つ目の手動エントリ...（省略）
def save_data():
    # _dataディレクトリがなければ作成
    os.makedirs("_data", exist_ok=True)
    
    try:
        with open("_data/collected_examples.json", "w", encoding="utf-8") as f:
            json.dump(examples, f, indent=2, ensure_ascii=False)
        print(f"データを保存しました: _data/collected_examples.json")
    except Exception as e:
        print(f"データ保存中にエラーが発生しました: {e}")
if __name__ == "__main__":
    collect_from_github()
    add_document_examples()
    add_service_examples()
    save_data()
    print(f"{len(examples)}件の事例を収集しました")
query = "claude anthropic YOUR_NICHE_KEYWORD"
params={"q": query, "sort": "stars", "per_page": 5}  # 5を調整
"category": "あなたのカテゴリー名",
"tags": ["タグ1", "タグ2", "タグ3"],
