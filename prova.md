---
title: sample post
type: Email
---

<ul>
{% for example in site.data.table %}
  <li>
      {{ example.type }} {{ example.text }}
  </li>
{% endfor %}
</ul>
