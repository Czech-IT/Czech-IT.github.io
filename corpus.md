---
title: Corpus
layout: table

---

<div class="dataTables_wrapper container-fluid dt-bootstrap4 no-footer">
    <div class="row">
	    <div class="col-sm-12">
<div class="form-inline">
    <div class="form-check mr-3">
        <input type="checkbox" onchange="filterme()" class="filled-in form-check-input" id="check-survey" checked="checked"  value="survey-message" name="type">
        <label class="form-check-label" for="check-survey">Survey</label>
    </div>
    <div class="form-check mr-3">
        <input type="checkbox" onchange="filterme()" class="filled-in form-check-input" id="check-text" checked="checked"  value="text-message" name="type">
        <label class="form-check-label" for="check-text">Text Message</label>
    </div>
    <div class="form-check mr-3">
        <input type="checkbox" onchange="filterme()" class="filled-in form-check-input" id="check-email" checked="checked"  value="email" name="type">
        <label class="form-check-label" for="check-email">Email</label>
    </div>
    <div class="form-check mr-3">
        <input type="checkbox" onchange="filterme()" class="filled-in form-check-input" id="check-audio" checked="checked"  value="audio" name="type">
        <label class="form-check-label" for="check-audio">Audio</label>
    </div>
</div>
</div>
</div>
</div>

<br><br>
{% for item in site.data.dataset %}

<tr id="{{ item.item-id }}">

<td> {{ item.item-id }}</td>
<td> <a href="../learners#{{ item.learner-id }}">{{ item.learner-id }}</a></td>
<td> {{ item.content }}</td>
<td> {{ item.type }}</td>
</tr>
{% endfor %}
