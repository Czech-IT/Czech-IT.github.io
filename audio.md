---
title: Audio
description: Subcorpus Audio messages
type: audio
---


<h1> {{ page.title }} </h1>
<h2> {{ page.description }} </h2>
<table>
  <thead>
    <tr>
      <th>Learner</th>
      <th>Audio</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.table %}
      {% if item.type == page.type %}
        <tr>
          <td> {{ item.learner }} </td>
          <td>  
            <audio controls>
              <source src="{{ item.text }}" type="audio/mp3">
              Your browser does not support the audio element.
            </audio>
          </td>
        </tr>
      {% endif %}
    {% endfor %}
  </tbody>
</table>


