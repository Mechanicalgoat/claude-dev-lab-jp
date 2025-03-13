---
layout: default
title: カテゴリ一覧
permalink: /categories/
---

<div class="categories-hero">
  <div class="container">
    <div class="categories-hero-content">
      <span class="categories-badge">CATEGORIES</span>
      <h1 class="categories-title">専門分野別コンテンツ</h1>
      <p class="categories-description">Claude実践ラボの記事は、各専門分野に最適化された実践ノウハウを提供します。<br>ビジネスと開発のニーズに合わせて分類されたコンテンツをご覧ください。</p>
    </div>
  </div>
  <div class="categories-hero-shape"></div>
</div>

<div class="container categories-container">
  <div class="categories-grid">
    {% assign categories = site.categories | sort %}
    {% for category in categories %}
      <div class="category-card" data-category="{{ category[0] | slugify }}">
        <div class="category-card-inner">
          <div class="category-icon">
            {% case category[0] %}
              {% when "サービス開発" %}
                <svg viewBox="0 0 24 24" width="24" height="24">
                  <path d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11L21.54,9.37C21.73,9.22 21.78,8.95 21.66,8.73L19.66,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.87,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.13,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.73C2.21,8.95 2.27,9.22 2.46,9.37L4.57,11C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.21,15.05 2.34,15.27L4.34,18.73C4.46,18.95 4.73,19.03 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.13,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.87,18.93C15.5,18.67 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.03 19.54,18.95 19.66,18.73L21.66,15.27C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z" />
                </svg>
              {% when "資料作成" %}
                <svg viewBox="0 0 24 24" width="24" height="24">
                  <path d="M13,9H18.5L13,3.5V9M6,2H14L20,8V20A2,2 0 0,1 18,22H6C4.89,22 4,21.1 4,20V4C4,2.89 4.89,2 6,2M15,18V16H6V18H15M18,14V12H6V14H18Z" />
                </svg>
              {% when "プログラミング" %}
                <svg viewBox="0 0 24 24" width="24" height="24">
                  <path d="M8,3A2,2 0 0,0 6,5V9A2,2 0 0,1 4,11H3V13H4A2,2 0 0,1 6,15V19A2,2 0 0,0 8,21H10V19H8V14A2,2 0 0,0 6,12A2,2 0 0,0 8,10V5H10V3M16,3A2,2 0 0,1 18,5V9A2,2 0 0,0 20,11H21V13H20A2,2 0 0,0 18,15V19A2,2 0 0,1 16,21H14V19H16V14A2,2 0 0,1 18,12A2,2 0 0,1 16,10V5H14V3H16Z" />
                </svg>
              {% else %}
                <svg viewBox="0 0 24 24" width="24" height="24">
                  <path d="M20,11H4V8H20M20,15H13V13H20M20,19H13V17H20M11,19H4V13H11M20.33,4.67L18.67,3L17,4.67L15.33,3L13.67,4.67L12,3L10.33,4.67L8.67,3L7,4.67L5.33,3L3.67,4.67L2,3V19A2,2 0 0,0 4,21H20A2,2 0 0,0 22,19V3L20.33,4.67Z" />
                </svg>
            {% endcase %}
          </div>
          <div class="category-content">
            <div class="category-meta">
              <h2 class="category-name">{{ category[0] }}</h2>
              <span class="category-count">{{ category[1].size }}記事</span>
            </div>
            <div class="category-divider"></div>
            <p class="category-desc">
              {% case category[0] %}
                {% when "サービス開発" %}
                  API連携や自動化による革新的なサービス構築と拡張性を重視した実装アプローチ
                {% when "資料作成" %}
                  企画書・報告書・技術文書の品質と作成効率を向上させる体系的フレームワーク
                {% when "プログラミング" %}
                  コード生成・デバッグ・最適化を効率化するClaudeの活用術とベストプラクティス
                {% else %}
                  {{ category[0] }}に関連する実践的なノウハウと活用事例
              {% endcase %}
            </p>
          </div>
          <button class="category-expand-btn" aria-label="カテゴリ展開">
            <svg viewBox="0 0 24 24" width="24" height="24">
              <path d="M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z" />
            </svg>
          </button>
        </div>
        
        <div class="category-posts">
          <h3>記事一覧</h3>
          <ul class="post-list">
            {% for post in category[1] %}
              <li class="post-item">
                <a href="{{ post.url | relative_url }}" class="post-link">
                  <div class="post-meta">
                    <span class="post-date">{{ post.date | date: "%Y.%m.%d" }}</span>
                    {% if post.tags.size > 0 %}
                      <div class="post-tags">
                        {% for tag in post.tags limit:2 %}
                          <span class="post-tag">{{ tag }}</span>
                        {% endfor %}
                      </div>
                    {% endif %}
                  </div>
                  <h4 class="post-title">{{ post.title }}</h4>
                </a>
              </li>
            {% endfor %}
          </ul>
        </div>
      </div>
    {% endfor %}
  </div>
</div>

<style>
/* カテゴリページのスタイル */
.categories-hero {
  position: relative;
  padding: 70px 0 50px;
  background: linear-gradient(135deg, rgba(67, 97, 238, 0.08), rgba(59, 130, 246, 0.12));
  margin-bottom: 60px;
  overflow: hidden;
}

.categories-hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
}

.categories-badge {
  display: inline-block;
  background-color: rgba(67, 97, 238, 0.1);
  color: #4361ee;
  font-size: 0.85rem;
  font-weight: 700;
  padding: 5px 12px;
  border-radius: 20px;
  margin-bottom: 15px;
  letter-spacing: 1px;
}

.categories-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: var(--dark-text);
  margin-bottom: 20px;
  letter-spacing: -0.02em;
}

.categories-description {
  font-size: 1.1rem;
  color: var(--medium-text);
  max-width: 700px;
  margin: 0 auto;
  line-height: 1.6;
}

.categories-hero-shape {
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 100%;
  height: 70px;
  background-color: #fff;
  border-radius: 50% 50% 0 0 / 100% 100% 0 0;
  z-index: 1;
}

.categories-container {
  padding-bottom: 80px;
}

.categories-grid {
  display: flex;
  flex-direction: column;
  gap: 25px;
  max-width: 900px;
  margin: 0 auto;
}

.category-card {
  background-color: #fff;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
  border: 1px solid var(--border-color);
  transition: all 0.3s ease;
}

.category-card:hover {
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
  transform: translateY(-3px);
}

.category-card.expanded {
  margin-bottom: 40px;
}

.category-card-inner {
  display: flex;
  align-items: center;
  padding: 25px 30px;
  cursor: pointer;
  position: relative;
}

.category-icon {
  width: 60px;
  height: 60px;
  border-radius: 15px;
  background: linear-gradient(135deg, rgba(67, 97, 238, 0.08), rgba(59, 130, 246, 0.15));
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 25px;
  flex-shrink: 0;
}

.category-icon svg {
  width: 28px;
  height: 28px;
  fill: #4361ee;
}

.category-content {
  flex-grow: 1;
}

.category-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.category-name {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--dark-text);
  margin: 0;
}

.category-count {
  background-color: rgba(67, 97, 238, 0.1);
  color: #4361ee;
  font-size: 0.85rem;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 20px;
}

.category-divider {
  width: 40px;
  height: 3px;
  background: linear-gradient(to right, #4361ee, #3b82f6);
  margin-bottom: 12px;
  border-radius: 3px;
}

.category-desc {
  color: var(--medium-text);
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.6;
}

.category-expand-btn {
  background: none;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  background-color: rgba(67, 97, 238, 0.05);
  margin-left: 15px;
}

.category-expand-btn svg {
  width: 24px;
  height: 24px;
  fill: #4361ee;
  transition: transform 0.3s ease;
}

.category-expand-btn:hover {
  background-color: rgba(67, 97, 238, 0.1);
}

.category-card.expanded .category-expand-btn svg {
  transform: rotate(180deg);
}

.category-posts {
  padding: 0 30px 30px;
  display: none;
  border-top: 1px solid var(--border-color);
}

.category-card.expanded .category-posts {
  display: block;
  animation: fadeDown 0.5s ease forwards;
}

@keyframes fadeDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.category-posts h3 {
  font-size: 1.2rem;
  margin: 25px 0 20px;
  color: var(--dark-text);
  font-weight: 700;
}

.post-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: 1fr;
  gap: 15px;
}

.post-item {
  background-color: rgba(67, 97, 238, 0.03);
  border-radius: 12px;
  transition: all 0.3s ease;
}

.post-item:hover {
  background-color: rgba(67, 97, 238, 0.07);
}

.post-link {
  display: block;
  padding: 20px;
  text-decoration: none;
  color: inherit;
}

.post-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.post-date {
  font-size: 0.85rem;
  color: var(--light-text);
}

.post-tags {
  display: flex;
  gap: 5px;
}

.post-tag {
  font-size: 0.75rem;
  color: #4361ee;
  background-color: rgba(67, 97, 238, 0.08);
  padding: 2px 8px;
  border-radius: 15px;
}

.post-title {
  font-size: 1.05rem;
  margin: 0;
  color: var(--dark-text);
  line-height: 1.5;
  transition: color 0.2s ease;
}

.post-link:hover .post-title {
  color: #4361ee;
}

/* レスポンシブ対応 */
@media (max-width: 768px) {
  .categories-hero {
    padding: 50px 0 30px;
  }
  
  .categories-title {
    font-size: 2rem;
  }
  
  .categories-description {
    font-size: 1rem;
    padding: 0 15px;
  }
  
  .category-card-inner {
    padding: 20px;
  }
  
  .category-icon {
    width: 50px;
    height: 50px;
    margin-right: 15px;
  }
  
  .category-icon svg {
    width: 24px;
    height: 24px;
  }
  
  .category-name {
    font-size: 1.2rem;
  }
  
  .category-count {
    font-size: 0.8rem;
    padding: 3px 10px;
  }
  
  .category-desc {
    font-size: 0.9rem;
  }
  
  .category-posts {
    padding: 0 20px 20px;
  }
}

@media (max-width: 576px) {
  .categories-hero {
    padding: 40px 0 25px;
  }
  
  .categories-title {
    font-size: 1.8rem;
  }
  
  .category-card-inner {
    flex-direction: column;
    align-items: flex-start;
    text-align: center;
  }
  
  .category-icon {
    margin-right: 0;
    margin-bottom: 15px;
  }
  
  .category-meta {
    flex-direction: column;
    gap: 8px;
  }
  
  .category-divider {
    margin: 8px auto 12px;
  }
  
  .category-expand-btn {
    position: absolute;
    top: 15px;
    right: 15px;
    margin-left: 0;
  }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // カテゴリカードの展開/折りたたみ機能
  const categoryCards = document.querySelectorAll('.category-card');
  
  categoryCards.forEach(card => {
    const cardInner = card.querySelector('.category-card-inner');
    
    cardInner.addEventListener('click', function() {
      // 他のカードを閉じる
      categoryCards.forEach(otherCard => {
        if (otherCard !== card && otherCard.classList.contains('expanded')) {
          otherCard.classList.remove('expanded');
        }
      });
      
      // このカードの状態を切り替え
      card.classList.toggle('expanded');
      
      // 展開時にスクロール
      if (card.classList.contains('expanded')) {
        setTimeout(() => {
          const rect = card.getBoundingClientRect();
          const isVisible = (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= window.innerHeight &&
            rect.right <= window.innerWidth
          );
          
          if (!isVisible) {
            card.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        }, 300);
      }
    });
  });
  
  // URLハッシュからカテゴリを開く
  if (window.location.hash) {
    const categoryId = window.location.hash.substring(1);
    const targetCard = document.querySelector(`.category-card[data-category="${categoryId}"]`);
    
    if (targetCard) {
      setTimeout(() => {
        targetCard.classList.add('expanded');
        targetCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 500);
    }
  }
});
</script>
