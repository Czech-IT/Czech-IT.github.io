---
title: Corpus-all

---

{% for item in site.data.dataset %}
  <div id="{{ item.item-id }}">
    <p>Item ID: {{ item.item-id }}</p>
    <h2>Content</h2>
    <p>{{ item.content }}</p>
    <h2>Learner</h2>
    {% for learner in site.data.learners %}
    {% if learner.learner-id == item.learner-id %}
      <p>Name: {{ learner.name }}
    {% endif %}
    {% endfor %}
  </div>
  <hr>
{% endfor %}
