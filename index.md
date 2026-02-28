---
layout: default
title: TalulaT - a biking blog
---

<section class="topics-grid">
  {% for t in site.topics %}
    {% assign cat = t.category %}
    {% assign posts_in_cat = site.categories[cat] %}
    {% assign last_updated = nil %}
    {% if posts_in_cat and posts_in_cat.size > 0 %}
      {% comment %}
      site.categories arrays are reverse chronological by default,
      so the first element is the most recent post.
      {% endcomment %}
      {% assign last_post = posts_in_cat | first %}
      {% assign last_updated = last_post.date %}
    {% endif %}

    <div class="topic-card">
      <h2 class="topic-title">
        {{ site.baseurl }}{{ t.url }}{{ t.title }}</a>
      </h2>

      {% if posts_in_cat %}
        <p class="topic-meta">
          {{ posts_in_cat.size }} posts
          {% if last_updated %} • Last updated {{ last_updated | date: "%b %-d, %Y" }}{% endif %}
        </p>
      {% else %}
        <p class="topic-meta">No posts yet</p>
      {% endif %}
    </div>
  {% endfor %}
</section>