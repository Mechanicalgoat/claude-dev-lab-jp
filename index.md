---
layout: home
title: ホーム
---

<div class="home-header">
  <div class="container">
    <h1>Claude実践ラボ</h1>
    <p class="lead mb-3">ビジネスと開発のプロフェッショナルのための<br>AI活用プラットフォーム</p>
    <p class="mb-4">実践的な事例と最先端のプロンプト技術で、作業効率を最大化</p>
    <div class="cta-buttons">
      <a href="{{ site.baseurl }}/categories/" class="btn btn-primary">カテゴリを見る</a>
      <a href="{{ site.baseurl }}/about/" class="btn btn-outline">詳細を確認</a>
    </div>
  </div>
</div>

<div class="container">
  <section class="site-features mb-5">
    <div class="section-header text-center mb-4">
      <span class="section-tag">OUR FEATURES</span>
      <h2>プロフェッショナルをサポートする4つの特徴</h2>
    </div>
    <div class="row">
      <div class="col col-md-3 col-6 mb-4">
        <div class="feature-card">
          <div class="feature-icon">📊</div>
          <h3>実践重視</h3>
          <p>理論より実践。すぐに業務に適用できるテクニックを厳選</p>
        </div>
      </div>
      <div class="col col-md-3 col-6 mb-4">
        <div class="feature-card">
          <div class="feature-icon">💻</div>
          <h3>開発者視点</h3>
          <p>エンジニアの思考プロセスに沿った実装アプローチ</p>
        </div>
      </div>
      <div class="col col-md-3 col-6 mb-4">
        <div class="feature-card">
          <div class="feature-icon">✅</div>
          <h3>検証済み</h3>
          <p>実績と効果測定に基づく信頼性の高い手法を提供</p>
        </div>
      </div>
      <div class="col col-md-3 col-6 mb-4">
        <div class="feature-card">
          <div class="feature-icon">🔄</div>
          <h3>常時更新</h3>
          <p>最新のAI技術を取り入れ、継続的に価値を提供</p>
        </div>
      </div>
    </div>
  </section>

  <section class="category-section mb-5">
    <div class="section-header text-center mb-4">
      <span class="section-tag">CATEGORIES</span>
      <h2>専門分野別の活用ガイド</h2>
    </div>
    <div class="row">
      <div class="col col-md-4 mb-4">
        <div class="category-card">
          <div class="category-icon">🧩</div>
          <h3>プログラミング</h3>
          <p>開発効率を最大化するコード生成・デバッグ・リファクタリング手法</p>
          <a href="{{ site.baseurl }}/categories/#プログラミング" class="read-more">カテゴリを見る</a>
        </div>
      </div>
      
      <div class="col col-md-4 mb-4">
        <div class="category-card">
          <div class="category-icon">📝</div>
          <h3>資料作成</h3>
          <p>企画書・プレゼン・技術文書の質と作成速度を向上させる方法</p>
          <a href="{{ site.baseurl }}/categories/#資料作成" class="read-more">カテゴリを見る</a>
        </div>
      </div>
      
      <div class="col col-md-4 mb-4">
        <div class="category-card">
          <div class="category-icon">🚀</div>
          <h3>サービス開発</h3>
          <p>APIとの連携・自動化による革新的なサービス構築のガイド</p>
          <a href="{{ site.baseurl }}/categories/#サービス開発" class="read-more">カテゴリを見る</a>
        </div>
      </div>
    </div>
  </section>

  <section class="latest-posts mb-5">
    <div class="section-header mb-4">
      <div class="d-flex justify-content-between align-items-center">
        <div>
          <span class="section-tag">LATEST ARTICLES</span>
          <h2 class="mb-0">最新記事</h2>
        </div>
        <a href="{{ site.baseurl }}/categories/" class="btn btn-outline btn-sm">すべての記事</a>
      </div>
    </div>
    
    <div class="post-grid">
      {% for post in site.posts limit:3 %}
        <div class="post-card">
          {% if post.thumbnail %}
          <div class="post-thumbnail">
            <a href="{{ post.url | relative_url }}">
              <img src="{{ site.baseurl }}{{ post.thumbnail }}" alt="{{ post.title }}" loading="lazy">
            </a>
          </div>
          {% endif %}
          <div class="post-card-content">
            <div class="post-meta">
              <span class="post-category">{{ post.categories }}</span>
              <span class="post-date">{{ post.date | date: "%Y.%m.%d" }}</span>
            </div>
            <h3><a href="{{ post.url | relative_url }}" class="post-title-link">{{ post.title }}</a></h3>
            <div class="post-excerpt">
              {{ post.excerpt | strip_html | truncatewords: 15 }}
            </div>
            <a href="{{ post.url | relative_url }}" class="read-more">記事を読む</a>
          </div>
        </div>
      {% endfor %}
    </div>
  </section>

  <section class="cta-section mb-5">
    <div class="cta-card">
      <div class="row align-items-center">
        <div class="col col-md-8 mb-4 mb-md-0">
          <h2 class="mb-3">Claude AIの力を最大限に活用しませんか？</h2>
          <p class="mb-0">このサイトでは、様々な業務シーンでClaudeを効果的に活用するための実践的な知識を提供しています。まずはカテゴリから、あなたの興味のある分野をチェックしてみてください。</p>
        </div>
        <div class="col col-md-4 text-center text-md-right">
          <a href="{{ site.baseurl }}/categories/" class="btn btn-primary">カテゴリを見る</a>
        </div>
      </div>
    </div>
  </section>
</div>

<style>
/* ホームページ専用スタイル */
.home-header {
  position: relative;
  text-align: center;
  padding: 80px 0 60px;
  margin-bottom: 60px;
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.08), rgba(59, 130, 246, 0.12));
  border-radius: 0 0 30px 30px;
}

.cta-buttons {
  display: flex;
  gap: 12px;
  justify-content: center;
}

.section-tag {
  display: inline-block;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--primary-color);
  margin-bottom: 8px;
  letter-spacing: 1px;
}

.section-header h2 {
  font-size: 1.8rem;
  margin-top: 0;
  margin-bottom: 0.5rem;
  padding-bottom: 0;
  border-bottom: none;
}

.post-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 24px;
}

.post-card {
  background-color: #fff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--shadow-md);
  border: 1px solid var(--border-color);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.post-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.post-card .post-thumbnail {
  height: 180px;
  margin-bottom: 0;
  border-radius: 0;
  box-shadow: none;
}

.post-card-content {
  padding: 20px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.post-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.post-meta .post-date {
  font-size: 0.8rem;
  color: var(--light-text);
}

.post-meta .post-category {
  font-size: 0.75rem;
  padding: 3px 10px;
}

.post-card h3 {
  font-size: 1.15rem;
  line-height: 1.4;
  margin-top: 0;
  margin-bottom: 12px;
}

.post-title-link {
  color: var(--dark-text);
  text-decoration: none;
  transition: color 0.2s ease;
}

.post-title-link:hover {
  color: var(--primary-color);
  text-decoration: none;
}

.post-excerpt {
  font-size: 0.9rem;
  color: var(--medium-text);
  line-height: 1.6;
  margin-bottom: 16px;
  flex-grow: 1;
}

.btn-sm {
  padding: 5px 12px;
  font-size: 0.85rem;
}

.cta-card {
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.05), rgba(59, 130, 246, 0.1));
  padding: 40px;
  border-radius: 16px;
  border: 1px solid rgba(37, 99, 235, 0.08);
}

.cta-card h2 {
  font-size: 1.6rem;
  margin-top: 0;
  padding-bottom: 0;
  border-bottom: none;
}

.d-flex {
  display: flex;
}

.justify-content-between {
  justify-content: space-between;
}

.align-items-center {
  align-items: center;
}

.text-center {
  text-align: center;
}

.text-md-right {
  text-align: right;
}

@media (max-width: 768px) {
  .home-header {
    padding: 60px 0 40px;
  }
  
  .cta-card {
    padding: 30px 20px;
  }
  
  .post-grid {
    grid-template-columns: 1fr;
  }
  
  .text-md-right {
    text-align: center;
  }
}

@media (max-width: 576px) {
  .home-header {
    padding: 40px 0 30px;
  }
  
  .cta-buttons {
    flex-direction: column;
    gap: 10px;
  }
  
  .cta-card {
    padding: 25px 15px;
  }
  
  .cta-card h2 {
    font-size: 1.4rem;
  }
  
  .section-header h2 {
    font-size: 1.5rem;
  }
}
</style>
