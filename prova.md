---
title: sample post
type: Email
---

<ul>
{% assign item.Type = site.data.table[page.type] %}
  <li>
      {{ item.Learner }}
      {{ item.Type }}
      {{ item.Text }}
  </li>
</ul>
