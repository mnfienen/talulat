---
layout: page
title: Japan Trip
permalink: /japan/
---

# Japan 2026 🇯🇵

Back to Japan! 日本に帰ります！

<img src="../assets/images/mc-8.jpg" width=400>


It's time for a return to Japan. Connecting Kunitachi to Obihiro - through the northeast exploring some places new to us. Enjoy the ride with us!

If you want to reach out, you can find us on Instagram @taikomike.

<img src="../assets/images/日本-map.png" width=400>

{% assign japan_posts = site.categories.japan | sort: "date" %}
{% for post in japan_posts %}
- {{ post.date | date: "%Y-%m-%d" }} — [{{ post.title }}]({{ site.baseurl }}{{ post.url }})
{% endfor %}
