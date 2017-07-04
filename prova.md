---
title: sample post
type: Email
---

<ul>
{% for example in site.data.table %}
  <li>
    {% if example.type %}
      {{ example.type }} {{ example.text }}
    {% else %}
      {{ member.name }}
    {% endif %}
  </li>
{% endfor %}
</ul>
