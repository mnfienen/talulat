---
layout: page
title: Canada Trip
permalink: /canada/
---

# Canada 2023 🇨🇦

Biking across Canada - Summer 2023

Out the St. Lawrence through the Great Lakes.

<img src="../assets/images/Canada-map.png" width=400>

{% assign canada_posts = site.categories.canada | sort: "date" %}
{% for post in canada_posts %}
- {{ post.date | date: "%Y-%m-%d" }} — [{{ post.title }}]({{ site.baseurl }}{{ post.url }})
{% endfor %}
