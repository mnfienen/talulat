---
layout: page
title: Japan Trip
permalink: /japan/
---

# Japan 2026 🇯🇵

Biking across Japan - Spring 2026

{% assign japan_posts = site.categories.japan | sort: "date" %}
{% for post in japan_posts %}
- {{ post.date | date: "%Y-%m-%d" }} — [{{ post.title }}]({{ site.baseurl }}{{ post.url }})
{% endfor %}
