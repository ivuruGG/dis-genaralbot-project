{% extends 'base.html' %}

{% block title %}Login{% endblock %}

{% block content %}
  <div class="form-container">
    <h1>Login</h1>
    {% if message %}
      <div class="alert alert-danger" role="alert">
        {{ message }}
      </div>
    {% endif %}
    <form method="POST" action="{{ url_for('login') }}">
      <div class="form-group">
        <label for="email">Email address</label>
        <input type="email" class="form-control" id="email" name="email" required>
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" class="form-control" id="password" name="password" required>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
{% endblock %}
