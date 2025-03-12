---
layout: page
title: カテゴリ一覧
permalink: /categories/
---

<div class="categories-page">
  <p class="lead text-center mb-4">Claude実践ラボの記事は以下のカテゴリに分類されています。<br>各カテゴリをクリックして、関連記事を閲覧できます。</p>

  <div class="category-overview mb-5">
    <div class="row">
      {% assign categories = site.categories | sort %}
      {% for category in categories %}
        <div class="col col-md-4 mb-4">
          <a href="#{{ category[0] | slugify }}" class="category-block">
            <div class="category-count">{{ category[1].size }}</div>
            <h3>{{ category[0] }}</h3>
          </a>
        </div>
      {% endfor %}
    </div>
  </div>

  <div class="category-details">
    {% for category in site.categories %}
      <div class="category-section mb-5" id="{{ category[0] | slugify }}">
        <div class="category-header">
          <h2 class="mb-4">{{ category[0] }}</h2>
          <span class="category-pill">{{ category[1].size }} 記事</span>
        </div>
        
        <div class="post-list">
          {% for post in category[1] %}
            <div class="post-item">
              <div class="post-meta mb-1">
                <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
              </div>
              <h3 class="post-title mb-0">
                <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
              </h3>
              <div class="post-tags mt-2">
                {% for tag in post.tags %}
                  <a href="{{ site.baseurl }}/tags/#{{ tag | slugify }}" class="post-tag">{{ tag }}</a>
                {% endfor %}
              </div>
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
  .categories-page .lead {
    color: var(--medium-text);
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
  }
  
  .category-block {
    display: block;
    padding: 25px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    text-align: center;
    transition: all 0.3s ease;
    height: 100%;
    text-decoration: none;
    color: var(--dark-text);
  }
  
  .category-block:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
    text-decoration: none;
    color: var(--primary-color);
  }
  
  .category-count {
    display: inline-block;
    background-color: var(--primary-color);
    color: white;
    width: 50px;
    height: 50px;
    line-height: 50px;
    border-radius: 50%;
    font-size: 1.2em;
    font-weight: 700;
    margin-bottom: 15px;
  }
  
  .category-block h3 {
    margin: 0;
    font-size: 1.3em;
  }
  
  .category-header {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid var(--primary-color);
  }
  
  .category-header h2 {
    margin: 0;
    padding: 0;
    border: none;
    flex-grow: 1;
  }
  
  .category-pill {
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
  }
  
  .post-tags {
    display: flex;
    flex-wrap: wrap;
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
    
    .category-header {
      flex-direction: column;
      align-items: flex-start;
    }
    
    .category-pill {
      margin-top: 10px;
    }
  }
</style>
