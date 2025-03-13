---
layout: home
title: ホーム
---

<div class="home-header">
  <div class="container">
    <h1>Claude実践ラボ</h1>
    <p class="lead mb-3">ビジネスと開発のプロフェッショナルのための<br>戦略的AI活用プラットフォーム</p>
    <p class="mb-4">効率化と価値創出を実現する実践メソッドとプロンプト設計</p>
    <div class="cta-buttons">
      <a href="{{ site.baseurl }}/categories/" class="btn btn-primary">ソリューション一覧</a>
      <a href="{{ site.baseurl }}/about/" class="btn btn-outline">詳細を確認</a>
    </div>
  </div>
</div>

<div class="container">
  <section class="site-features mb-5">
    <div class="section-header text-center mb-5">
      <span class="section-tag">CORE VALUES</span>
      <h2>ビジネス価値を創出する4つの強み</h2>
      <p class="section-subtitle">企業の競争力を高めるClaudeの戦略的活用アプローチ</p>
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
    <div class="section-header text-center mb-5">
      <span class="section-tag">INSIGHTS & RESOURCES</span>
      <h2>最新の実践知見</h2>
      <p class="section-subtitle">ビジネス成果を生み出すためのAI活用事例と戦略</p>
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
          <p class="mb-0">このサイトでは、ビジネスと開発のプロフェッショナルのためのClaudeの戦略的活用法を紹介しています。まずは、あなたの業務課題に最適なソリューションを探してみてください。</p>
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
  padding: 90px 0 70px;
  margin-bottom: 70px;
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.08), rgba(59, 130, 246, 0.12));
  border-radius: 0 0 60px 60px;
}

.home-header h1 {
  font-size: 2.7rem;
  font-weight: 800;
  margin-bottom: 1.2rem;
  letter-spacing: -0.03em;
  color: var(--dark-text);
}

.home-header .lead {
  font-size: 1.35rem;
  max-width: 700px;
  margin: 0 auto 1rem;
  color: var(--medium-text);
  font-weight: 400;
  line-height: 1.5;
}

.cta-buttons {
  display: flex;
  gap: 15px;
  justify-content: center;
  margin-top: 2rem;
}

.cta-buttons .btn {
  min-width: 180px;
  padding: 12px 24px;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 8px;
}

.section-header {
  margin-bottom: 3rem;
}

.section-tag {
  display: inline-block;
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--primary-color);
  margin-bottom: 10px;
  letter-spacing: 1.5px;
}

.section-header h2 {
  font-size: 2.2rem;
  margin-top: 0;
  margin-bottom: 0.8rem;
  padding-bottom: 0;
  border-bottom: none;
  letter-spacing: -0.02em;
  line-height: 1.2;
}

.section-subtitle {
  color: var(--medium-text);
  font-size: 1.15rem;
  max-width: 800px;
  margin: 0 auto 1rem;
  line-height: 1.5;
}

/* 特徴セクションの強化 */
.site-features {
  padding: 30px 0 60px;
}

.feature-card {
  padding: 35px 28px;
  border-radius: 16px;
  transition: all 0.3s ease;
  border: 1px solid rgba(226, 232, 240, 0.8);
  height: 100%;
}

.feature-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-lg);
  border-color: rgba(226, 232, 240, 0.2);
}

.feature-card .feature-icon {
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.08), rgba(59, 130, 246, 0.18));
  width: 76px;
  height: 76px;
  border-radius: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
  font-size: 1.9rem;
  color: var(--primary-color);
}

.feature-card h3 {
  font-size: 1.35rem;
  font-weight: 700;
  margin-bottom: 15px;
  color: var(--dark-text);
  letter-spacing: -0.01em;
}

.feature-card p {
  color: var(--medium-text);
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 0;
}

/* 専門分野別ソリューションの強化 */
.category-section {
  padding: 30px 0 60px;
  background-color: var(--light-bg);
  border-radius: 30px;
  margin: 70px 0;
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
  padding: 28px 28px 8px;
  position: relative;
}

.expertise-icon {
  width: 65px;
  height: 65px;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.12), rgba(59, 130, 246, 0.2));
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 18px;
  font-size: 1.5rem;
  color: var(--primary-color);
  box-shadow: 0 6px 12px rgba(37, 99, 235, 0.12);
}

.expertise-label {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 1.5px;
  color: var(--light-text);
  margin-bottom: 0;
  display: block;
  position: absolute;
  right: 28px;
  top: 28px;
  background-color: rgba(226, 232, 240, 0.5);
  padding: 5px 10px;
  border-radius: 12px;
}

.expertise-card h3 {
  padding: 0 28px;
  margin: 8px 0 15px;
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: var(--dark-text);
}

.expertise-divider {
  width: 45px;
  height: 3px;
  background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
  margin: 0 28px 18px;
  border-radius: 3px;
}

.expertise-card p {
  padding: 0 28px;
  color: var(--medium-text);
  font-size: 0.98rem;
  line-height: 1.6;
  margin-bottom: 20px;
}

.expertise-points {
  list-style: none;
  padding: 0 28px;
  margin: 0 0 28px;
}

.expertise-points li {
  position: relative;
  padding-left: 24px;
  margin-bottom: 12px;
  font-size: 0.95rem;
  color: var(--medium-text);
}

.expertise-points li:before {
  content: "";
  position: absolute;
  left: 0;
  top: 8px;
  width: 10px;
  height: 10px;
  background-color: var(--primary-color);
  border-radius: 50%;
  opacity: 0.7;
}

.expertise-card .read-more {
  margin: auto 28px 28px;
  align-self: flex-start;
  font-weight: 600;
}

/* 最新記事セクションの強化 */
.latest-posts {
  padding: 30px 0 60px;
}

.post-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 30px;
  margin: 0 auto;
  max-width: 1140px;
}

.post-card {
  background-color: #fff;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: var(--shadow-md);
  border: 1px solid var(--border-color);
  transition: all 0.3s ease;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.post-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-lg);
}

.post-card .post-thumbnail {
  height: 200px;
  margin-bottom: 0;
  border-radius: 0;
  box-shadow: none;
}

.post-card-content {
  padding: 25px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.post-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.post-meta .post-date {
  font-size: 0.85rem;
  color: var(--light-text);
  font-weight: 500;
}

.post-meta .post-category {
  font-size: 0.8rem;
  padding: 4px 12px;
  border-radius: 20px;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.post-card h3 {
  font-size: 1.25rem;
  line-height: 1.4;
  margin-top: 0;
  margin-bottom: 15px;
  font-weight: 700;
  letter-spacing: -0.01em;
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
  font-size: 0.95rem;
  color: var(--medium-text);
  line-height: 1.6;
  margin-bottom: 20px;
  flex-grow: 1;
}

/* CTAセクションの強化 */
.cta-section {
  margin: 70px 0;
}

.cta-card {
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.05), rgba(59, 130, 246, 0.08));
  padding: 50px;
  border-radius: 20px;
  border: 1px solid rgba(37, 99, 235, 0.08);
  box-shadow: var(--shadow-sm);
}

.cta-card h2 {
  font-size: 1.8rem;
  margin-top: 0;
  padding-bottom: 0;
  border-bottom: none;
  letter-spacing: -0.02em;
  line-height: 1.3;
  color: var(--dark-text);
}

.cta-card p {
  font-size: 1.1rem;
  line-height: 1.6;
  color: var(--medium-text);
}

.cta-card .btn {
  padding: 12px 28px;
  font-weight: 600;
  font-size: 1rem;
  border-radius: 8px;
  min-width: 200px;
}

/* レスポンシブ調整 */
@media (max-width: 992px) {
  .home-header {
    padding: 70px 0 50px;
    margin-bottom: 50px;
  }
  
  .home-header h1 {
    font-size: 2.3rem;
  }
  
  .home-header .lead {
    font-size: 1.2rem;
  }
  
  .section-header h2 {
    font-size: 1.9rem;
  }
  
  .section-subtitle {
    font-size: 1.05rem;
  }
  
  .post-grid {
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  }
  
  .cta-card {
    padding: 40px 30px;
  }
}

@media (max-width: 768px) {
  .home-header {
    padding: 60px 0 40px;
    margin-bottom: 40px;
    border-radius: 0 0 40px 40px;
  }
  
  .home-header h1 {
    font-size: 2rem;
  }
  
  .home-header .lead {
    font-size: 1.1rem;
  }
  
  .feature-card .feature-icon {
    width: 65px;
    height: 65px;
    font-size: 1.6rem;
  }
  
  .feature-card h3 {
    font-size: 1.2rem;
  }
  
  .feature-card p {
    font-size: 0.9rem;
  }
  
  .expertise-card {
    margin-bottom: 25px;
  }
  
  .expertise-icon {
    width: 55px;
    height: 55px;
    font-size: 1.3rem;
  }
  
  .expertise-card h3 {
    font-size: 1.3rem;
  }
  
  .expertise-points li {
    font-size: 0.9rem;
  }
  
  .post-grid {
    grid-template-columns: 1fr;
    max-width: 500px;
  }
  
  .cta-card h2 {
    font-size: 1.6rem;
  }
  
  .cta-card p {
    font-size: 1rem;
  }
  
  .section-header {
    margin-bottom: 2rem;
  }
  
  .category-section {
    margin: 40px 0;
    padding: 30px 0 40px;
    border-radius: 20px;
  }
}

@media (max-width: 576px) {
  .home-header {
    padding: 50px 0 40px;
    margin-bottom: 30px;
    border-radius: 0 0 30px 30px;
  }
  
  .home-header h1 {
    font-size: 1.8rem;
  }
  
  .home-header .lead {
    font-size: 1rem;
  }
  
  .cta-buttons {
    flex-direction: column;
    gap: 12px;
  }
  
  .cta-buttons .btn {
    width: 100%;
    min-width: 0;
  }
  
  .section-header h2 {
    font-size: 1.6rem;
  }
  
  .section-subtitle {
    font-size: 0.95rem;
  }
  
  .feature-card, .expertise-card {
    padding: 25px 20px;
  }
  
  .expertise-header {
    padding: 25px 20px 5px;
  }
  
  .expertise-label {
    right: 20px;
    top: 20px;
    font-size: 0.7rem;
  }
  
  .expertise-card h3 {
    padding: 0 20px;
    font-size: 1.2rem;
  }
  
  .expertise-divider {
    margin: 0 20px 15px;
  }
  
  .expertise-card p {
    padding: 0 20px;
    font-size: 0.9rem;
  }
  
  .expertise-points {
    padding: 0 20px;
  }
  
  .expertise-card .read-more {
    margin: auto 20px 20px;
  }
  
  .cta-card {
    padding: 30px 20px;
  }
  
  .cta-card h2 {
    font-size: 1.4rem;
  }
  
  .cta-card p {
    font-size: 0.95rem;
  }
}
</style>
