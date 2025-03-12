---
layout: page
title: タグ一覧
permalink: /tags/
---

<div class="tags-page">
  <p class="lead text-center mb-4">Claude実践ラボの記事は以下のタグで分類されています。<br>興味のあるタグをクリックして関連記事を閲覧できます。</p>

  {% assign tags = site.tags | sort %}
  <div class="tag-cloud mb-5">
    {% for tag in tags %}
      <a href="#{{ tag[0] | slugify }}" class="tag-cloud-item" style="font-size: {{ tag[1].size | times: 4 | plus: 80 }}%">
        {{ tag[0] }} <span class="tag-count">{{ tag[1].size }}</span>
      </a>
    {% endfor %}
  </div>

  <div class="tag-details">
    {% for tag in tags %}
      <div class="tag-section mb-5" id="{{ tag[0] | slugify }}">
        <div class="tag-header">
          <h2 class="mb-4">{{ tag[0] }}</h2>
          <span class="tag-pill">{{ tag[1].size }} 記事</span>
        </div>
        
        <div class="post-list">
          {% for post in tag[1] %}
            <div class="post-item">
              <div class="post-meta mb-1">
                <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
                <span class="post-category">{{ post.categories }}</span>
              </div>
              <h3 class="post-title mb-0">
                <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
              </h3>
            </div>
          {% endfor %}
        </div>
        
        <div class="text-right mt-3">
          <a href="#" class="back-to-top">トップへ戻る ↑</a>
        </div>
      </div>
    {% endfor %}
  </div>
</div>

<style>
  .tags-page .lead {
    color: var(--medium-text);
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
  }
  
  .tag-cloud {
    text-align: center;
    padding: 30px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  }
  
  .tag-cloud-item {
    display: inline-block;
    margin: 8px;
    padding: 5px 15px;
    background-color: rgba(67, 97, 238, 0.08);
    border-radius: 25px;
    text-decoration: none;
    color: var(--primary-color);
    font-weight: 500;
    transition: all 0.2s ease;
    line-height: 1.8;
  }
  
  .tag-cloud-item:hover {
    background-color: var(--primary-color);
    color: #fff;
    text-decoration: none;
    transform: translateY(-3px);
  }
  
  .tag-count {
    display: inline-block;
    background-color: rgba(255, 255, 255, 0.3);
    color: inherit;
    width: 24px;
    height: 24px;
    line-height: 24px;
    text-align: center;
    border-radius: 50%;
    font-size: 0.75em;
    margin-left: 5px;
  }
  
  .tag-header {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid var(--primary-color);
  }
  
  .tag-header h2 {
    margin: 0;
    padding: 0;
    border: none;
    flex-grow: 1;
  }
  
  .tag-pill {
    background-color: var(--primary-color);
    color: white;
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 0.9em;
    font-weight: 600;
  }
  
  .post-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
  }
  
  .post-item {
    background-color: #fff;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  
  .post-item:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
  }
  
  .post-title {
    font-size: 1.1em;
    line-height: 1.4;
  }
  
  .post-title a {
    color: var(--dark-text);
    text-decoration: none;
  }
  
  .post-title a:hover {
    color: var(--primary-color);
  }
  
  .post-date {
    color: var(--light-text);
    font-size: 0.9em;
    margin-right: 10px;
  }
  
  .post-category {
    background-color: rgba(67, 97, 238, 0.1);
    color: var(--primary-color);
    padding: 3px 10px;
    border-radius: 15px;
    font-size: 0.85em;
    font-weight: 500;
  }
  
  .back-to-top {
    display: inline-block;
    padding: 5px 15px;
    border-radius: 20px;
    background-color: var(--light-bg);
    color: var(--medium-text);
    font-size: 0.9em;
    transition: all 0.2s ease;
  }
  
  .back-to-top:hover {
    background-color: var(--border-color);
    text-decoration: none;
  }
  
  @media (max-width: 768px) {
    .post-list {
      grid-template-columns: 1fr;
    }
    
    .tag-header {
      flex-direction: column;
      align-items: flex-start;
    }
    
    .tag-pill {
      margin-top: 10px;
    }
  }
</style>
