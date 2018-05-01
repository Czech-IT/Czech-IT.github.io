---
title: Learners
layout: table
headers:
	- Learner-id
	- Age
	- Education
	- Native Language
	- Other Languages
	- Italian Level

---

{% for item in site.data.learners %}

<tr id="{{ item.learner-id }}">

<td> {{ item.learner-id }}</td>
<td> {{ item.age }}</td>
<td> {{ item.education }}</td>
<td> {{ item.lang-native }}</td>
<td> {{ item.lang-other }}</td>
<td> {{ item.it-level }}</td>
</tr>
{% endfor %}
