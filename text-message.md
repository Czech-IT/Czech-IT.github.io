---
title: Text messages
description: Subcorpus Text messages
type: text-message
---


<h1> {{ page.title }} </h1>
<h2> {{ page.description }} </h2>
<table>
  <thead>
    <tr>
      <th>Learner</th>
      <th>Text</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.table %}
      {% if item.type == page.type %}
        <tr>
          <td> {{ item.learner }} </td>
          <td> {{ item. text }} </td>
        </tr>
      {% endif %}
    {% endfor %}
  </tbody>
</table>


