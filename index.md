---
layout: default
title: 首页
description: wind989 的学习记录，分享 Python 后端、AI 应用与项目实践中的问题和思考。
---

<section class="home-intro" aria-labelledby="intro-title">
  <p class="section-kicker"><span aria-hidden="true">✦</span> WIND989 · 学习与实践</p>
  <h1 id="intro-title">Python 后端与<br class="intro-break"> AI 应用实践</h1>
  <p class="intro-copy">你好，我是 wind989。这里记录我在后端开发、数据处理与 AI 应用中的学习过程，也整理项目中的问题和阅读之后的思考。</p>
  <div class="intro-links"><a class="text-link" href="{{ '/about/' | relative_url }}">认识我 <span aria-hidden="true">↗</span></a><span aria-hidden="true">·</span><a class="text-link" href="{{ '/feed.xml' | relative_url }}">RSS 订阅</a></div>
</section>

<section class="home-section articles" id="articles" aria-labelledby="articles-title">
  <div class="section-title-row"><div><p class="section-kicker">WRITING</p><h2 id="articles-title">最新文章</h2></div><a class="section-more" href="{{ '/archive/' | relative_url }}">全部 {{ site.posts.size }} 篇 <span aria-hidden="true">→</span></a></div>
  <div class="post-grid">
    {% for post in site.posts limit: 4 %}
    <article class="post-card">
      <div class="card-meta"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%Y.%m.%d' }}</time>{% if post.categories.size > 0 %}<span>{{ post.categories | first | escape }}</span>{% endif %}</div>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
      <p>{{ post.excerpt | strip_html | normalize_whitespace | truncate: 100 }}</p>
      <a class="card-link" href="{{ post.url | relative_url }}" aria-label="阅读：{{ post.title | escape }}">阅读全文 <span aria-hidden="true">→</span></a>
    </article>
    {% else %}
    <p class="empty-state">文章正在整理中。</p>
    {% endfor %}
  </div>
</section>

<section class="home-section projects" id="projects" aria-labelledby="projects-title">
  <div class="section-title-row"><div><p class="section-kicker">BUILDING</p><h2 id="projects-title">项目实践</h2></div><a class="section-more" href="https://github.com/wind989" target="_blank" rel="noopener noreferrer">GitHub <span aria-hidden="true">↗</span></a></div>
  <div class="project-grid">
    {% for project in site.data.projects %}
    <article class="project-card">
      <div class="card-meta"><span>学习项目</span><span>{{ project.repo }}</span></div>
      <h3>{{ project.name | escape }}</h3>
      <p class="project-description">{{ project.description | escape }}</p>
      <p class="project-evidence">{% if project.name == 'RepoMind' %}文档中包含架构说明、检索评测与验证边界。{% else %}文档中区分了已验证的流程与尚待完成的验证。{% endif %}</p>
      <div class="project-links"><a class="card-link" href="{{ project.url }}" target="_blank" rel="noopener noreferrer">代码与文档 <span aria-hidden="true">↗</span></a><a href="{{ project.url }}/releases" target="_blank" rel="noopener noreferrer">版本记录</a></div>
    </article>
    {% endfor %}
  </div>
</section>

<aside class="home-note"><span aria-hidden="true">✧</span><p>学习记录、项目实践、阅读思考，都可以在<a href="{{ '/archive/' | relative_url }}">文章归档</a>里找到。</p></aside>
