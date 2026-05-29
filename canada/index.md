---
layout: page
title: Canada Trip
permalink: /canada/
---

# Canada 2023 🇨🇦

Biking across Canada - Summer 2023

{% assign canada_posts = site.categories.canada | sort: "date" %}
{% for post in canada_posts %}
- {{ post.date | date: "%Y-%m-%d" }} — [{{ post.title }}]({{ post.url }})
{% endfor %}
