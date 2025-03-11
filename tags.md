---
layout: page
title: タグ一覧
permalink: /tags/
---

<div class="tags-page">
  <p>Claude実践ラボの記事は以下のタグで分類されています。興味のあるタグをクリックして関連記事を閲覧できます。</p>

  {% assign tags = site.tags | sort %}
  <div class="tag-cloud">
    {% for tag in tags %}
      <a href="#{{ tag[0] | slugify }}" class="tag-link" style="font-size: {{ tag[1].size | times: 4 | plus: 80 }}%">
        {{ tag[0] }} <span>({{ tag[1].size }})</span>
      </a>
    {% endfor %}
  </div>

  <div class="tag-list">
    {% for tag in tags %}
      <h2 id="{{ tag[0] | slugify }}">{{ tag[0] }}</h2>
      <ul>
        {% for post in tag[1] %}
          <li>
            <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
            <small>{{ post.date | date: "%Y-%m-%d" }}</small>
          </li>
        {% endfor %}
      </ul>
    {% endfor %}
  </div>
</div>

<style>
  .tag-cloud {
    margin: 30px 0;
    text-align: center;
  }
  .tag-link {
    display: inline-block;
    margin: 5px;
    padding: 5px 10px;
    background-color: #f5f5f5;
    border-radius: 15px;
    text-decoration: none;
  }
  .tag-link:hover {
    background-color: #e0e0e0;
    text-decoration: none;
  }
  .tag-link span {
    color: #666;
    font-size: 80%;
  }
  .tag-list ul {
    margin-bottom: 30px;
  }
  .tag-list small {
    color: #666;
    margin-left: 8px;
  }
</style>
