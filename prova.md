---
title: sample post
type: Email
---

<ul>
{% assign item.Type = site.data.table[page.type] %}
{% for item in site.data.table %}
  <li>
      {{ item.Learner }}
      {{ item.Type }}
      {{ item.Text }}
  </li>
{% endfor %}
</ul>
