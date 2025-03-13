---
layout: home
title: ホーム
---

<div class="home-header">
  <div class="container">
    <h1>Claude実践ラボ</h1>
    <p class="lead mb-4">ビジネスと開発のプロフェッショナルのためのAI活用プラットフォーム</p>
    <div class="cta-buttons">
      <a href="{{ site.baseurl }}/categories/" class="btn btn-primary">ソリューション一覧</a>
      <a href="{{ site.baseurl }}/about/" class="btn btn-outline">詳細を確認</a>
    </div>
  </div>
</div>

<div class="container">
  <section class="core-strengths mb-5">
    <div class="section-header text-center mb-4">
      <h2>戦略的AI活用の4つの強み</h2>
    </div>
    <div class="strengths-container">
      <div class="strength-item">
        <div class="strength-icon">
          <i class="fas fa-bullseye"></i>
        </div>
        <h3>実践志向</h3>
        <p>ビジネスに直結する実装手法</p>
      </div>
      <div class="strength-item">
        <div class="strength-icon">
          <i class="fas fa-code-branch"></i>
        </div>
        <h3>開発者視点</h3>
        <p>拡張性を重視した設計</p>
      </div>
      <div class="strength-item">
        <div class="strength-icon">
          <i class="fas fa-chart-line"></i>
        </div>
        <h3>検証主導</h3>
        <p>定量的な効果測定と最適化</p>
      </div>
      <div class="strength-item">
        <div class="strength-icon">
          <i class="fas fa-sync-alt"></i>
        </div>
        <h3>革新継続</h3>
        <p>最新技術による価値創出</p>
      </div>
    </div>
  </section>

  <section class="category-section mb-5">
    <div class="section-header text-center mb-5">
      <span class="section-tag">EXPERTISE DOMAINS</span>
      <h2>専門分野別ソリューション</h2>
    </div>
    <div class="row expertise-row">
      <div class="col col-md-4 mb-4">
        <div class="expertise-card">
          <div class="expertise-header">
            <div class="expertise-icon">
              <i class="fas fa-code"></i>
            </div>
            <span class="expertise-label">DEVELOPMENT</span>
          </div>
          <h3>エンジニアリング最適化</h3>
          <div class="expertise-divider"></div>
          <p>コード生成・リファクタリング・デバッグの効率を飛躍的に高める先進的手法と統合アプローチ</p>
          <ul class="expertise-points">
            <li>インテリジェントなプロトタイピング</li>
            <li>コードレビュー自動化</li>
            <li>テスト生成プラットフォーム</li>
          </ul>
          <a href="{{ site.baseurl }}/categories/#プログラミング" class="read-more">専門知識を探る</a>
        </div>
      </div>
      
      <div class="col col-md-4 mb-4">
        <div class="expertise-card">
          <div class="expertise-header">
            <div class="expertise-icon">
              <i class="fas fa-file-alt"></i>
            </div>
            <span class="expertise-label">DOCUMENTATION</span>
          </div>
          <h3>ドキュメント戦略</h3>
          <div class="expertise-divider"></div>
          <p>企画書・報告書・技術文書の質と作成効率を両立させる体系的フレームワークと最適化手法</p>
          <ul class="expertise-points">
            <li>説得力のある提案構造設計</li>
            <li>データドリブンなレポート</li>
            <li>技術情報の効果的伝達</li>
          </ul>
          <a href="{{ site.baseurl }}/categories/#資料作成" class="read-more">専門知識を探る</a>
        </div>
      </div>
      
      <div class="col col-md-4 mb-4">
        <div class="expertise-card">
          <div class="expertise-header">
            <div class="expertise-icon">
              <i class="fas fa-cogs"></i>
            </div>
            <span class="expertise-label">INNOVATION</span>
          </div>
          <h3>サービス変革</h3>
          <div class="expertise-divider"></div>
          <p>APIとの戦略的統合による革新的サービス構築と自動化で実現するビジネスモデルの進化</p>
          <ul class="expertise-points">
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
    <div class="section-header text-center mb-4">
      <span class="section-tag">INSIGHTS & RESOURCES</span>
      <h2>最新の実践知見</h2>
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
            <a href="{{ post.url | relative_url }}" class="read-more">詳細を見る</a>
          </div>
        </div>
      {% endfor %}
    </div>
    
    <div class="text-center mt-4">
      <a href="{{ site.baseurl }}/categories/" class="btn btn-outline">すべての記事を見る</a>
    </div>
  </section>

  <section class="cta-section mb-5">
    <div class="cta-card">
      <div class="row align-items-center">
        <div class="col col-md-8 mb-4 mb-md-0">
          <h2 class="mb-3">Claude AIの力で業務効率を革新しませんか？</h2>
          <p class="mb-0">様々な業務シーンでClaudeを効果的に活用するための実践的な知識を提供しています。</p>
        </div>
        <div class="col col-md-4 text-center text-md-right">
          <a href="{{ site.baseurl }}/categories/" class="btn btn-primary">ソリューションを探す</a>
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
  padding: 70px 0 50px;
  margin-bottom: 50px;
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.08), rgba(59, 130, 246, 0.12));
  border-radius: 0 0 40px 40px;
}

.home-header h1 {
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 1rem;
  letter-spacing: -0.03em;
  color: var(--dark-text);
}

.home-header .lead {
  font-size: 1.25rem;
  max-width: 700px;
  margin: 0 auto 1.5rem;
  color: var(--medium-text);
  font-weight: 400;
  line-height: 1.5;
}

.cta-buttons {
  display: flex;
  gap: 15px;
  justify-content: center;
}

.cta-buttons .btn {
  min-width: 180px;
  padding: 10px 20px;
  font-weight: 600;
  border-radius: 8px;
}

.section-header {
  margin-bottom: 2.5rem;
}

.section-tag {
  display: inline-block;
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--primary-color);
  margin-bottom: 8px;
  letter-spacing: 1.5px;
}

.section-header h2 {
  font-size: 2rem;
  margin-top: 0;
  margin-bottom: 0.5rem;
  padding-bottom: 0;
  border-bottom: none;
  letter-spacing: -0.02em;
  line-height: 1.2;
}

/* 4つの強みセクションのコンパクト化 */
.core-strengths {
  padding: 20px 0 40px;
}

.strengths-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  margin: 0 auto;
  max-width: 1000px;
}

.strength-item {
  flex: 1;
  min-width: 220px;
  max-width: 240px;
  padding: 25px 15px;
  text-align: center;
  background-color: #fff;
  border-radius: 12px;
  box-shadow: var(--shadow-sm);
  border: 1px solid var(--border-color);
  transition: all 0.3s ease;
}

.strength-item:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-md);
}

.strength-icon {
  width: 60px;
  height: 60px;
  border-radius: 12px;
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.08), rgba(59, 130, 246, 0.15));
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 15px;
  font-size: 1.6rem;
  color: var(--primary-color);
}

.strength-item h3 {
  font-size: 1.15rem;
  font-weight: 700;
  margin-bottom: 8px;
  color: var(--dark-text);
}

.strength-item p {
  color: var(--medium-text);
  font-size: 0.9rem;
  line-height: 1.4;
  margin-bottom: 0;
}

/* 専門分野別ソリューションの強化 */
.category-section {
  padding: 30px 0 50px;
  background-color: var(--light-bg);
  border-radius: 30px;
  margin: 50px 0;
}

.expertise-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.expertise-card {
  padding: 0;
  border-radius: 16px;
  overflow: hidden;
  background-color: #fff;
  transition: all 0.3s ease;
  height: 100%;
  display: flex;
  flex-direction: column;
  box-shadow: var(--shadow-md);
  border: 1px solid var(--border-color);
}

.expertise-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-lg);
}

.expertise-header {
  display: flex;
  align-items: center;
  padding: 25px 25px 5px;
  position: relative;
}

.expertise-icon {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.12), rgba(59, 130, 246, 0.2));
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 15px;
  font-size: 1.4rem;
  color: var(--primary-color);
  box-shadow: 0 5px 10px rgba(37, 99, 235, 0.1);
}

.expertise-label {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 1.5px;
  color: var(--light-text);
  margin-bottom: 0;
  display: block;
  position: absolute;
  right: 25px;
  top: 25px;
  background-color: rgba(226, 232, 240, 0.5);
  padding: 4px 8px;
  border-radius: 10px;
}

.expertise-card h3 {
  padding: 0 25px;
  margin: 5px 0 12px;
  font-size: 1.4rem;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: var(--dark-text);
}

.expertise-divider {
  width: 40px;
  height: 3px;
  background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
  margin: 0 25px 15px;
  border-radius: 3px;
}

.expertise-card p {
  padding: 0 25px;
  color: var(--medium-text);
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 15px;
}

.expertise-points {
  list-style: none;
  padding: 0 25px;
  margin: 0 0 20px;
}

.expertise-points li {
  position: relative;
  padding-left: 20px;
  margin-bottom: 10px;
  font-size: 0.9rem;
  color: var(--medium-text);
}

.expertise-points li:before {
  content: "";
  position: absolute;
  left: 0;
  top: 8px;
  width: 8px;
  height: 8px;
  background-color: var(--primary-color);
  border-radius: 50%;
  opacity: 0.7;
}

.expertise-card .read-more {
  margin: auto 25px 25px;
  align-self: flex-start;
  font-weight: 600;
}

/* 最新記事セクションの強化 */
.latest-posts {
  padding: 30px 0 50px;
}

.post-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 25px;
  margin: 0 auto;
}

.post-card {
  background-color: #fff;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: var(--shadow-md);
  border: 1px solid var(--border-color);
  transition: all 0.3s ease;
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
  border-radius: 15px;
}

.post-card h3 {
  font-size: 1.15rem;
  line-height: 1.4;
  margin-top: 0;
  margin-bottom: 10px;
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
  margin-bottom: 15px;
  flex-grow: 1;
}

/* CTAセクションの強化 */
.cta-section {
  margin: 50px 0;
}

.cta-card {
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.05), rgba(59, 130, 246, 0.08));
  padding: 40px;
  border-radius: 16px;
  border: 1px solid rgba(37, 99, 235, 0.08);
  box-shadow: var(--shadow-sm);
}

.cta-card h2 {
  font-size: 1.6rem;
  margin-top: 0;
  padding-bottom: 0;
  border-bottom: none;
  line-height: 1.3;
}

.cta-card p {
  font-size: 1rem;
  line-height: 1.6;
  color: var(--medium-text);
}

.cta-card .btn {
  padding: 10px 25px;
  font-weight: 600;
  min-width: 180px;
}

/* レスポンシブ調整 */
@media (max-width: 992px) {
  .home-header h1 {
    font-size: 2.2rem;
  }
  
  .home-header .lead {
    font-size: 1.15rem;
  }
  
  .section-header h2 {
    font-size: 1.8rem;
  }
  
  .strength-item {
    min-width: 200px;
  }
}

@media (max-width: 768px) {
  .home-header {
    padding: 50px 0 35px;
    margin-bottom: 35px;
  }
  
  .home-header h1 {
    font-size: 2rem;
  }
  
  .home-header .lead {
    font-size: 1.1rem;
    margin-bottom: 1.2rem;
  }
  
  .strengths-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
  }
  
  .strength-item {
    min-width: 0;
    max-width: none;
    width: 100%;
    padding: 20px 15px;
  }
  
  .strength-icon {
    width: 50px;
    height: 50px;
    font-size: 1.4rem;
    margin-bottom: 10px;
  }
  
  .strength-item h3 {
    font-size: 1.05rem;
    margin-bottom: 5px;
  }
  
  .strength-item p {
    font-size: 0.85rem;
  }
  
  .section-header h2 {
    font-size: 1.6rem;
  }
  
  .cta-card {
    padding: 30px 25px;
  }
  
  .cta-card h2 {
    font-size: 1.4rem;
  }
}

@media (max-width: 576px) {
  .home-header {
    padding: 40px 0 30px;
    margin-bottom: 30px;
    border-radius: 0 0 25px 25px;
  }
  
  .home-header h1 {
    font-size: 1.8rem;
  }
  
  .home-header .lead {
    font-size: 1rem;
  }
  
  .cta-buttons {
    flex-direction: column;
    gap: 10px;
    max-width: 220px;
    margin: 0 auto;
  }
  
  .cta-buttons .btn {
    width: 100%;
  }
  
  .section-header h2 {
    font-size: 1.5rem;
  }
  
  .strengths-container {
    grid-template-columns: 1fr;
    max-width: 260px;
    margin: 0 auto;
  }
  
  .strength-item {
    max-width: none;
    padding: 18px 15px;
  }
  
  .cta-card {
    padding: 25px 20px;
  }
  
  .cta-card h2 {
    font-size: 1.3rem;
  }
  
  .cta-card p {
    font-size: 0.9rem;
  }
  
  .category-section {
    padding: 25px 0 35px;
    margin: 30px 0;
    border-radius: 20px;
  }
}
</style>
