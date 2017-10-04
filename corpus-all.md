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
    <ul>
      <li>ID: <span class="mono"> {{ item.learner-id }}</span></li>
      <!--<li>Age: <span class="mono">{{ learner.age }}</span></li>
      <li>Level (IT):   <span class="mono"> {{ learner.it-level }} </span></li>
      <li>Education:  <span class="mono"> {{ learner.education }} </span></li>
      <li>Languages:  <span class="mono"> {{ learner.languages }}</span> </li>-->
    </ul>
    <h3>Annotations</h3>
    <ul>
      <li>Manual phenomena:  <span class="mono"> {{ item.manual-phenomena }}</span></li>
      <li>Auto tokenize:  <span class="mono"> {{ item.auto-tokenize }}</span></li>
      <li>Auto word count:  <span class="mono"> {{ item.auto-count-words }}</span></li>
      <li>Auto POS:  <span class="mono"> {{ item.auto-pos }}</span></li>
      <li>Notes: <span class="mono">  {{ item.notes }}</span></li>
    </ul>
  </div>
{% endfor %}
