---
title: Corpus
layout: table

---


<div class="container">
  <div class="dataTables_wrapper container-fluid dt-bootstrap4 no-footer">
    <div class="row">
      <div class="col-sm-12">
        <input onchange="filterme()" type="checkbox" name="type" value="text-message|email|survey-message|audio">All
        <input onchange="filterme()" type="checkbox" name="type" value="text-message">Text-message
        <input onchange="filterme()" type="checkbox" name="type" value="email">Email
        <input onchange="filterme()" type="checkbox" name="type" value="survey-message">Surveys
        <input onchange="filterme()" type="checkbox" name="type" value="audio">Audio
      </div>
    </div>
  </div>
</div>



{% for item in site.data.dataset %}

<tr>

<td> {{ item.item-id }}</td>
<td> {{ item.learner-id }}</td>
<td> {{ item.content }}</td>
<td> {{ item.type }}</td>
</tr>
{% endfor %}
