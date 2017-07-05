---
title: Survey messages
description: Subcorpus Survey messages
type: survey-message
---


<h2> {{ page.title }} </h2>
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
