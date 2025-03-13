---
layout: home
title: ホーム
---

<div class="home-header">
  <div class="container">
    <h1 class="mb-3">Claude実践ラボ</h1>
    <p class="lead mb-4">プログラミング・資料作成・サービス開発における<br>Claude AIの実践的活用術</p>
    <p class="mb-0">即使える事例とプロンプトで、開発・制作を加速</p>
  </div>
</div>

<div class="container">
  <section class="site-features mb-5">
    <h2 class="text-center mb-4">サイトの特徴</h2>
    <div class="row">
      <div class="col col-md-3 col-6 mb-4">
        <div class="feature-card content-card">
          <div class="feature-icon">📊</div>
          <h3>実践重視</h3>
          <p>現場で即活用できる具体的なプロンプトとテクニック</p>
        </div>
      </div>
      <div class="col col-md-3 col-6 mb-4">
        <div class="feature-card content-card">
          <div class="feature-icon">💻</div>
          <h3>開発者視点</h3>
          <p>エンジニア目線での実装例とアプローチ</p>
        </div>
      </div>
      <div class="col col-md-3 col-6 mb-4">
        <div class="feature-card content-card">
          <div class="feature-icon">✅</div>
          <h3>実績ベース</h3>
          <p>実際の使用例と効果測定に基づく信頼性</p>
        </div>
      </div>
      <div class="col col-md-3 col-6 mb-4">
        <div class="feature-card content-card">
          <div class="feature-icon">🔄</div>
          <h3>定期更新</h3>
          <p>最新のClaude機能と活用法を継続的に提供</p>
        </div>
      </div>
    </div>
  </section>

  <section class="category-section mb-5">
    <h2 class="text-center mb-4">カテゴリ別コンテンツ</h2>
    <div class="row">
      <div class="col col-md-4 mb-4">
        <div class="category-card content-card">
          <div class="category-icon">🧩</div>
          <h3>プログラミング</h3>
          <p>コード生成・デバッグ・リファクタリングのAI活用法</p>
          <a href="{{ site.baseurl }}/categories/#プログラミング" class="read-more">記事一覧</a>
        </div>
      </div>
      
      <div class="col col-md-4 mb-4">
        <div class="category-card content-card">
          <div class="category-icon">📝</div>
          <h3>資料作成</h3>
          <p>企画書・プレゼン資料・マニュアルの効率化</p>
          <a href="{{ site.baseurl }}/categories/#資料作成" class="read-more">記事一覧</a>
        </div>
      </div>
      
      <div class="col col-md-4 mb-4">
        <div class="category-card content-card">
          <div class="category-icon">🚀</div>
          <h3>サービス開発</h3>
          <p>API連携・自動化ソリューションの構築方法</p>
          <a href="{{ site.baseurl }}/categories/#サービス開発" class="read-more">記事一覧</a>
        </div>
      </div>
    </div>
  </section>

  <section class="latest-posts mb-5">
    <h2 class="mb-4">最新記事</h2>
    <div class="post-list">
      {% for post in site.posts limit:5 %}
        <div class="post-item">
          <h3 class="mb-2"><a href="{{ post.url | relative_url }}" class="post-link">{{ post.title }}</a></h3>
          <div class="post-meta mb-3">
            <span class="post-date">{{ post.date | date: "%Y年%m月%d日" }}</span>
            <span class="post-category">{{ post.categories }}</span>
          </div>
          <div class="post-excerpt">
            {{ post.excerpt | strip_html | truncatewords: 20 }}
          </div>
          <a href="{{ post.url | relative_url }}" class="read-more">続きを読む</a>
        </div>
      {% endfor %}
    </div>
    <div class="text-center mt-4">
      <a href="{{ site.baseurl }}/categories/" class="btn btn-outline">すべての記事を見る</a>
    </div>
  </section>
</div>

<style>
.feature-icon, .category-icon {
  font-size: 2rem;
  margin-bottom: 0.8rem;
  display: inline-block;
}

.feature-card, .category-card {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: 15px;
}

.category-card h3 {
  margin-top: 0;
  font-size: 1.2rem;
}

.category-card p {
  flex-grow: 1;
  font-size: 0.95rem;
  margin-bottom: 10px;
}

.home-header {
  position: relative;
  text-align: center;
  padding: 60px 0;
  margin-bottom: 40px;
  background: linear-gradient(135deg, rgba(67, 97, 238, 0.1) 0%, rgba(72, 149, 239, 0.15) 100%);
  border-radius: 0 0 30px 30px;
}

.home-header h1 {
  font-size: 2.5rem;
  font-weight: 800;
  color: var(--dark-text);
  margin-top: 0;
}

.home-header .lead {
  font-size: 1.2rem;
  max-width: 800px;
  margin: 0 auto;
  color: var(--medium-text);
}

@media (max-width: 768px) {
  .home-header {
    padding: 40px 15px;
    margin-bottom: 30px;
  }
  
  .home-header h1 {
    font-size: 2rem;
  }
  
  .home-header .lead {
    font-size: 1rem;
  }
  
  .feature-card, .category-card {
    padding: 12px;
  }
  
  .feature-icon, .category-icon {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
  }
  
  .feature-card h3, .category-card h3 {
    font-size: 1rem;
    margin-bottom: 5px;
  }
  
  .feature-card p, .category-card p {
    font-size: 0.9rem;
    margin-bottom: 5px;
  }
}

@media (max-width: 576px) {
  .home-header h1 {
    font-size: 1.8rem;
  }
  
  .read-more {
    font-size: 0.9rem;
  }
}
</style>
