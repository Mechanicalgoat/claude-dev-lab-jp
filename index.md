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
      <span class="section-tag">CORE VALUES</span>
      <h2>戦略的AI活用を実現する4つの強み</h2>
      <p class="section-subtitle">Claude実践ラボが提供する差別化されたアプローチ</p>
    </div>
    <div class="row">
      <div class="col col-md-3 col-6 mb-4">
        <div class="feature-card">
          <div class="feature-icon">
            <i class="fas fa-bullseye"></i>
          </div>
          <h3>実践志向</h3>
          <p>理論だけでなく、即ビジネスに応用可能な戦略的プロンプト設計と実装手法</p>
        </div>
      </div>
      <div class="col col-md-3 col-6 mb-4">
        <div class="feature-card">
          <div class="feature-icon">
            <i class="fas fa-code-branch"></i>
          </div>
          <h3>開発者視点</h3>
          <p>エンタープライズ開発の要件を満たすアーキテクチャと拡張性を重視した設計</p>
        </div>
      </div>
      <div class="col col-md-3 col-6 mb-4">
        <div class="feature-card">
          <div class="feature-icon">
            <i class="fas fa-chart-line"></i>
          </div>
          <h3>検証主導</h3>
          <p>定量的な効果測定と品質評価に基づく、信頼性の高い最適化アプローチ</p>
        </div>
      </div>
      <div class="col col-md-3 col-6 mb-4">
        <div class="feature-card">
          <div class="feature-icon">
            <i class="fas fa-sync-alt"></i>
          </div>
          <h3>革新継続</h3>
          <p>最新のAI技術動向と統合された、持続的な価値創出フレームワーク</p>
        </div>
      </div>
    </div>
  </section>

  <section class="category-section mb-5">
    <div class="section-header text-center mb-5">
      <span class="section-tag">EXPERTISE DOMAINS</span>
      <h2>専門分野別ソリューション</h2>
      <p class="section-subtitle">業界とビジネス課題に特化した戦略的アプローチ</p>
    </div>
    <div class="row">
      <div class="col col-md-4 mb-4">
        <div class="category-card">
          <div class="category-header">
            <div class="category-icon">
              <i class="fas fa-code"></i>
            </div>
            <span class="category-label">DEVELOPMENT</span>
          </div>
          <h3>エンジニアリング最適化</h3>
          <div class="category-divider"></div>
          <p>コード生成・リファクタリング・デバッグの効率を飛躍的に高める先進的手法と統合アプローチ</p>
          <ul class="category-points">
            <li>インテリジェントなプロトタイピング</li>
            <li>コードレビュー自動化</li>
            <li>テスト生成プラットフォーム</li>
          </ul>
          <a href="{{ site.baseurl }}/categories/#プログラミング" class="read-more">専門知識を探る</a>
        </div>
      </div>
      
      <div class="col col-md-4 mb-4">
        <div class="category-card">
          <div class="category-header">
            <div class="category-icon">
              <i class="fas fa-file-alt"></i>
            </div>
            <span class="category-label">DOCUMENTATION</span>
          </div>
          <h3>ドキュメント戦略</h3>
          <div class="category-divider"></div>
          <p>企画書・報告書・技術文書の質と作成効率を両立させる体系的フレームワークと最適化手法</p>
          <ul class="category-points">
            <li>説得力のある提案構造設計</li>
            <li>データドリブンなレポート</li>
            <li>技術情報の効果的伝達</li>
          </ul>
          <a href="{{ site.baseurl }}/categories/#資料作成" class="read-more">専門知識を探る</a>
        </div>
      </div>
      
      <div class="col col-md-4 mb-4">
        <div class="category-card">
          <div class="category-header">
            <div class="category-icon">
              <i class="fas fa-cogs"></i>
            </div>
            <span class="category-label">INNOVATION</span>
          </div>
          <h3>サービス変革</h3>
          <div class="category-divider"></div>
          <p>APIとの戦略的統合による革新的サービス構築と自動化で実現するビジネスモデルの進化</p>
          <ul class="category-points">
            <li>スケーラブルなAI統合</li>
            <li>カスタムソリューション設計</li>
            <li>プロセス最適化アーキテクチャ</li>
          </ul>
          <a href="{{ site.baseurl }}/categories/#サービス開発" class="read-more">専門知識を探る</a>
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

/* 特徴セクションのスタイル強化 */
.section-subtitle {
  color: var(--medium-text);
  font-size: 1.1rem;
  max-width: 700px;
  margin: 0 auto 1rem;
}

.feature-card {
  padding: 30px 24px;
  border-radius: 12px;
  transition: all 0.3s ease;
}

.feature-card .feature-icon {
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.1), rgba(59, 130, 246, 0.2));
  width: 70px;
  height: 70px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.2rem;
  font-size: 1.8rem;
  color: var(--primary-color);
}

.feature-card h3 {
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 12px;
  position: relative;
}

/* カテゴリーカードのスタイル強化 */
.category-card {
  padding: 0;
  border-radius: 12px;
  overflow: hidden;
  background-color: #fff;
  transition: all 0.3s ease;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.category-header {
  display: flex;
  align-items: center;
  padding: 20px 24px 5px;
}

.category-icon {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.15), rgba(59, 130, 246, 0.25));
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 15px;
  font-size: 1.5rem;
  color: var(--primary-color);
}

.category-label {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 1px;
  color: var(--light-text);
  margin-bottom: 0;
  display: block;
  position: absolute;
  right: 24px;
  top: 24px;
}

.category-card h3 {
  padding: 0 24px;
  margin: 0 0 15px;
  font-size: 1.4rem;
  font-weight: 700;
}

.category-divider {
  width: 40px;
  height: 3px;
  background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
  margin: 0 24px 15px;
}

.category-card p {
  padding: 0 24px;
  color: var(--medium-text);
  font-size: 0.95rem;
  line-height: 1.5;
  margin-bottom: 20px;
}

.category-points {
  list-style: none;
  padding: 0 24px;
  margin: 0 0 20px;
}

.category-points li {
  position: relative;
  padding-left: 20px;
  margin-bottom: 8px;
  font-size: 0.9rem;
  color: var(--medium-text);
}

.category-points li:before {
  content: "";
  position: absolute;
  left: 0;
  top: 8px;
  width: 8px;
  height: 8px;
  background-color: var(--primary-color);
  border-radius: 50%;
}

.category-card .read-more {
  margin: auto 24px 24px;
  align-self: flex-start;
}

@media (max-width: 768px) {
  .home-header {
    padding: 60px 0 40px;
  }
  
  .home-header h1 {
    font-size: 2rem;
  }
  
  .home-header .lead {
    font-size: 1.1rem;
  }
  
  .feature-icon, .category-icon {
    width: 50px;
    height: 50px;
    font-size: 1.3rem;
  }
  
  .feature-card, .category-card {
    padding: 20px;
  }
  
  .post-title {
    font-size: 1.75em;
  }
  
  .category-card {
    margin-bottom: 20px;
  }
  
  .category-card h3 {
    font-size: 1.2rem;
  }
  
  .category-points li {
    font-size: 0.85rem;
  }
  
  .post-grid {
    grid-template-columns: 1fr;
  }
  
  .text-md-right {
    text-align: center;
  }
  
  .cta-card {
    padding: 30px 20px;
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
