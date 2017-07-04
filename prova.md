---
title: sample post
type: Email
---

<ul>
{% for item in site.data.table %}
  {% if item.Type == page.type %}
    <li>
        {{ item.Learner }}
        {{ item.Type }}
        {{ item.Text }}
    </li>
  {% endif %}
{% endfor %}
</ul>
