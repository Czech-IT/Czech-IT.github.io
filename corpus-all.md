---
title: Corpus-all

---

{% for item in site.data.dataset %}
  <div id="{{ item.item-id }}">
    <h2>Item ID:  <span class="mono">{{ item.item-id }}</span></h2>
    <h3>Content</h3>
    <p>{{ item.content }}</p>
    <h3>Informations</h3>
    <ul>
      <li>Type: {{ item.type }} </li>
      <li>Date: <span class="mono"> {{ item.date }} </span></li> 
    </ul>
    <h3>Learner</h3>
    {% for learner in site.data.learners %}
    {% if learner.learner-id == item.learner-id %}
    <ul>
      <li>ID: <span class="mono"> {{ learner.learner-id }}</span></li>
      <li>Age: <span class="mono">{{ learner.age }}</span></li>
      <li>Level (IT):  {{ learner.it-level }} </li>
      <li>Education: {{ learner.education }} </li>
      <li>Languages: {{ learner.languages }} </li>
    </ul>
    {% endif %}
    {% endfor %}
    <h3>Annotations</h3>
    {% for annotated in site.data.annotations-dataset %}
    {% if annotated.item-id == item.item-id %}
    <ul>
      <li>Manual phenomena: {{ annotated.manual-phenomena }}</li>
      <li>Auto tokenize: {{ annotated.auto-tokenize }}</li>
      <li>Auto POS: {{ annotated.auto-pos }}</li>
      <li>Notes: {{ annotated.notes }}</li>
    </ul>
    {% endif %}
    {% endfor %}
  </div>
{% endfor %}
