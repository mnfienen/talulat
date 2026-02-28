---
layout: page
title: Topics
permalink: /topics/
---

<ul class="topics-list">
  {% assign sorted = site.categories | sort %}
  {% for cat in sorted %}
    {% assign name = cat | first %}
    {% assign posts = cat | last %}
    <li>
      <a href="{{ '/topics/' | append: name | slugosts)
      </a>
    </li>
  {% endfor %}
