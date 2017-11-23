---
title: Corpus
layout: table

---

{% for item in site.data.dataset %}

<tr>

<td> {{ item.item-id }}</td>
<td> {{ item.learner-id }}</td>
<td> {{ item.content }}</td>
<td> {{ item.type }}</td>
</tr>
{% endfor %}
