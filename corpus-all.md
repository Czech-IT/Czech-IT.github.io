---
title: Corpus-all

---

{% for item in site.data.dataset %}
  <div id="{{ item.item-id }}">
    <h2>Item ID: {{ item.item-id }}</h2>
    <h3>Content</h3>
    <p>{{ item.content }}</p>
    <h3>Learner</h3>
    {% for learner in site.data.learners %}
    {% if learner.learner-id == item.learner-id %}
      <p>ID: {{ learner.learner-id }}</p>
      <p>Age: {{ learner.age }}</p>
      <p>Level (IT):  	{{ learner.it-level }} </p>
      <p>Education: {{ learner.education }} </p>
      <p>Languages: {{ learner.languages }} </p>
    {% endif %}
    {% endfor %}
    <h3>Annotations</h3>
    {% for annotated in site.data.annotations-dataset %}
    {% if annotated.item-id == item.item-id %}
      <p>Manual phenomena: {{ annotated.manual-phenomena }}</p>
      <p>Auto tokenize: {{ annotated.auto-tokenize }}</p>
      <p>Auto POS: {{ annotated.auto-pos }}</p>
      <p>Notes: {{ annotated.notes }}</p>
    {% endif %}
    {% endfor %}
  </div>
{% endfor %}
