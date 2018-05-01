---
title: Learners
layout: table

---

{% for item in site.data.learners %}

<tr>

<td> {{ item.learner-id }}</td>
<td> {{ item.age }}</td>
<td> {{ item.education }}</td>
<td> {{ item.lang-native }}</td>
<td> {{ item.lang-other }}</td>
<td> {{ item.it-level }}</td>
</tr>
{% endfor %}
