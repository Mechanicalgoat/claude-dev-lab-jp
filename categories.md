---
layout: page
title: カテゴリ一覧
permalink: /categories/
---

<div class="categories-page">
  <p>Claude実践ラボの記事は以下のカテゴリに分類されています。各カテゴリをクリックして、関連記事を閲覧できます。</p>

  {% for category in site.categories %}
    <h2 id="{{ category[0] | slugify }}">{{ category[0] }}</h2>
    <ul>
      {% for post in category[1] %}
        <li>
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
          <small>{{ post.date | date: "%Y-%m-%d" }}</small>
        </li>
      {% endfor %}
    </ul>
  {% endfor %}
</div>

<style>
  .categories-page ul {
    margin-bottom: 30px;
  }
  .categories-page small {
    color: #666;
    margin-left: 8px;
  }
</style>
