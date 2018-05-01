---
title: Corpus
layout: table

---


<div class="dataTables_wrapper container-fluid dt-bootstrap4 no-footer">
    <div class="row">
	    <div class="col-sm-12 col-md-6">
	    <p>Filter by type: 	</p>
	    </div>
<div class="col-sm-12 col-md-6">
			<div class="btn-group" data-toggle="buttons">
			  <label class="btn btn-light active">
			    <input onchange="filterme()" type="checkbox" name="type" value="text-message|email|survey-message|audio">All
			  </label>
			  <label class="btn btn-light">
			    <input onchange="filterme()" type="checkbox" name="type" value="text-message">Text-message
			  </label>
			  <label class="btn btn-light">
			    <input onchange="filterme()" type="checkbox" name="type" value="email">Email
			  </label>
			   <label class="btn btn-light">
			    <input onchange="filterme()" type="checkbox" name="type" value="survey-message">Surveys
			  </label>
			   <label class="btn btn-light">
			    <input  onchange="filterme()" type="checkbox" name="type" value="audio">Audio
			  </label>
			</div>
		</div>
	</div>
</div>



{% for item in site.data.dataset %}

<tr id="{{ item.item-id }}">

<td> {{ item.item-id }}</td>
<td> <a href="../learners/#{{ item.learner-id }}">{{ item.learner-id }}</a></td>
<td> {{ item.content }}</td>
<td> {{ item.type }}</td>
</tr>
{% endfor %}
