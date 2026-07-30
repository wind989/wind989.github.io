---
layout: default
title: 首页
---

<section class="entry-overlay" id="entry-overlay" aria-hidden="true" aria-labelledby="entry-title">
  <div class="entry-overlay__stars" aria-hidden="true"></div>
  <div class="entry-overlay__content">
    <p class="entry-overlay__eyebrow">WIND989 · PERSONAL BLOG</p>
    <h1 class="entry-overlay__title" id="entry-title"><span>欢迎来到</span><strong>我的个人博客</strong></h1>
    <p class="entry-overlay__subtitle">记录每一次探索，也连接下一次成长。</p>
    <button class="entry-overlay__enter" id="enter-site" type="button">
      <span>进入网站</span><i aria-hidden="true">↓</i>
    </button>
    <p class="entry-overlay__hint">点击开启探索</p>
  </div>
</section>

<section class="hero" aria-labelledby="hero-title">
  <div class="hero__content">
    <p class="eyebrow">STUDENT · BACKEND · AI</p>
    <h1 id="hero-title">你好，我是 <span>wind989</span>。</h1>
    <p class="hero__lead">一名正在成长的开发者，专注记录 Python 后端、数据持久化与 AI 应用开发的学习过程。</p>
    <div class="hero__actions">
      <a class="button button--primary" href="#articles">阅读文章 <span aria-hidden="true">↓</span></a>
      <a class="button button--ghost" href="#about">认识我</a>
    </div>
  </div>
  <div class="hero__code" aria-label="我的学习技术栈">
    <div class="code-dots" aria-hidden="true"><i></i><i></i><i></i></div>
    <pre><code><span class="code-comment"># 我的技术成长路线</span>
stack = [
  <span class="code-string">"Python"</span>, <span class="code-string">"FastAPI"</span>,
  <span class="code-string">"MySQL"</span>, <span class="code-string">"AI Agent"</span>
]

<span class="code-keyword">while</span> learning:
    build()
    share()</code></pre>
  </div>
</section>

<section class="intro" id="about" aria-labelledby="about-title">
  <p class="section-kicker">ABOUT THIS BLOG</p>
  <div class="section-heading">
    <h2 id="about-title">把每一次学习，变成看得见的积累。</h2>
    <p>这里没有复杂的术语堆砌，只有真实的学习笔记、项目实践和问题复盘。希望未来回看时，能看到自己一步一步走来的痕迹。</p>
  </div>
</section>

<section class="focus" aria-labelledby="focus-title">
  <div class="section-title-row">
    <div>
      <p class="section-kicker">CURRENT FOCUS</p>
      <h2 id="focus-title">正在学习与探索</h2>
    </div>
    <span class="focus-status"><i></i> 持续更新中</span>
  </div>

  <div class="focus-grid">
    <article class="focus-card focus-card--python">
      <span class="focus-card__number">01</span>
      <div class="focus-card__icon">Py</div>
      <h3>Python 后端</h3>
      <p>夯实语言基础，学习用清晰的代码解决实际问题。</p>
    </article>
    <article class="focus-card focus-card--fastapi">
      <span class="focus-card__number">02</span>
      <div class="focus-card__icon">⚡</div>
      <h3>FastAPI</h3>
      <p>理解路由、依赖注入和接口设计，构建可靠的服务。</p>
    </article>
    <article class="focus-card focus-card--data">
      <span class="focus-card__number">03</span>
      <div class="focus-card__icon">DB</div>
      <h3>MySQL · SQLAlchemy</h3>
      <p>探索数据表、ORM 和事务，让数据处理更扎实。</p>
    </article>
    <article class="focus-card focus-card--agent">
      <span class="focus-card__number">04</span>
      <div class="focus-card__icon">AI</div>
      <h3>AI Agent</h3>
      <p>把大模型能力连接到真实场景，做出有用的小应用。</p>
    </article>
  </div>
</section>

<section class="articles" id="articles" aria-labelledby="articles-title">
  <div class="section-title-row">
    <div>
      <p class="section-kicker">LATEST NOTES</p>
      <h2 id="articles-title">最新文章</h2>
    </div>
    <span class="article-count">{{ site.posts.size }} 篇记录</span>
  </div>

  {% if site.posts.size > 0 %}
  <div class="post-grid">
    {% for post in site.posts limit: 6 %}
    <article class="post-card">
      <div class="post-card__meta">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y.%m.%d" }}</time>
        {% if post.categories.size > 0 %}<span>{{ post.categories | first }}</span>{% endif %}
      </div>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
      <p>{{ post.excerpt | strip_html | normalize_whitespace | truncate: 88 }}</p>
      <a class="post-card__link" href="{{ post.url | relative_url }}">继续阅读 <span aria-hidden="true">→</span></a>
    </article>
    {% endfor %}
  </div>
  {% else %}
  <div class="empty-posts">
    <p>第一篇学习笔记正在路上。</p>
  </div>
  {% endif %}
</section>

<section class="closing-note">
  <p>Learning in public</p>
  <h2>代码、笔记和思考，都会成为下一步的底气。</h2>
</section>

<script src="{{ '/assets/js/entry.js' | relative_url }}" defer></script>
