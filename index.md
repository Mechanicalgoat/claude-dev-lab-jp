---
layout: home
title: ホーム
---

<div class="home-header">
  <h1>Claude実践ラボ</h1>
  <p class="lead">プログラミング・資料作成・サービス開発におけるClaude AIの実践的活用術を紹介します。即使える事例とプロンプトで、あなたの開発・制作を加速させましょう。</p>
</div>

## サイトの特徴

- **実践重視**: 即現場で使える具体的なプロンプトとテクニック
- **開発者視点**: プログラミングとサービス開発に特化した活用法
- **実績ベース**: 実際の使用例と効果測定に基づく信頼できる情報
- **常時更新**: 最新のClaude機能と活用法を定期的に更新

## カテゴリ別コンテンツ

<div class="category-section">
  <div class="category-card">
    <h3>プログラミング</h3>
    <p>コード生成、デバッグ支援、リファクタリングなど、開発者のためのClaude活用法</p>
    <a href="{{ site.baseurl }}/categories/#プログラミング" class="category-link">記事一覧を見る →</a>
  </div>
  
  <div class="category-card">
    <h3>資料作成</h3>
    <p>企画書、プレゼン資料、マニュアルなど、ビジネス文書作成の効率化テクニック</p>
    <a href="{{ site.baseurl }}/categories/#資料作成" class="category-link">記事一覧を見る →</a>
  </div>
  
  <div class="category-card">
    <h3>サービス開発</h3>
    <p>Claude APIの実装例、サービス連携、自動化ソリューションの構築方法</p>
    <a href="{{ site.baseurl }}/categories/#サービス開発" class="category-link">記事一覧を見る →</a>
  </div>
</div>

## 最新記事

<div class="latest-posts">
  {% for post in site.posts limit:5 %}
    <div class="post-item">
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <div class="post-meta">
        <span class="post-date">{{ post.date | date: "%Y年%m月%d日" }}</span>
        <span class="post-category">{{ post.categories }}</span>
      </div>
      <p>{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
      <a href="{{ post.url | relative_url }}" class="read-more">続きを読む →</a>
    </div>
  {% endfor %}
</div>

<style>
.home-header {
  text-align: center;
  margin-bottom: 40px;
  padding: 30px 0;
  background-color: #f5f5ff;
  border-radius: 5px;
}

.lead {
  font-size: 1.2em;
  max-width: 800px;
  margin: 0 auto;
}

.category-section {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin: 30px 0;
}

.category-card {
  flex: 1;
  min-width: 250px;
  padding: 20px;
  background-color: #fff;
  border: 1px solid #eee;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

.category-link {
  display: inline-block;
  margin-top: 10px;
  font-weight: bold;
}

.latest-posts {
  margin-top: 40px;
}

.post-item {
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 1px solid #eee;
}

.post-meta {
  font-size: 0.9em;
  color: #666;
  margin-bottom: 10px;
}

.post-date {
  margin-right: 15px;
}

.post-category {
  background-color: #f0f0f0;
  padding: 3px 8px;
  border-radius: 12px;
}

.read-more {
  display: inline-block;
  margin-top: 10px;
  font-weight: bold;
}
</style>
