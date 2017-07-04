---
title: Email
description: Subcorpus Email
type: email
---


<h1> {{ page.title }} </h1>
<h2> {{ page.description }} </h2>
<ul>
{% for item in site.data.table %}
  {% if item.type == page.type %}
    <li>
        {{ item.text }} <br>
        {{ item.learner }}
    </li>
  {% endif %}
{% endfor %}
</ul>
