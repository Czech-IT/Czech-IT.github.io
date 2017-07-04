---
title: sample post
type: Email
---

<ul>
{% for item in site.data.table %}
  <li>
      {{ item.Learner }}
      {{ item.Type }}
      {{ item.Text }}
  </li>
{% endfor %}
</ul>
