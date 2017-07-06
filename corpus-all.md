---
title: Corpus-all

---

{% for item in site.data.dataset %}
  <div id="{{ item.item-id }}">
    <h2>Content</h2>
    <p>{{ item.content }}</p>
    <h2>Learner</h2>
  </div>
  <hr>
{% endfor %}
