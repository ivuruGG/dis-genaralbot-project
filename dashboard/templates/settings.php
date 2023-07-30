{% extends 'base.html' %}

{% block content %}
  <h1>Settings</h1>
  <form method="POST" action="{{ url_for('settings') }}">
    <label for="username">Username:</label>
    <input type="text" name="username" value="{{ current_user.username }}" required><br>
    <label for="email">Email:</label>
    <input type="email" name="email" value="{{ current_user.email }}" required><br>
    <label for="new_password">New Password:</label>
    <input type="password" name="new_password"><br>
    <label for="confirm_password">Confirm New Password:</label>
    <input type="password" name="confirm_password"><br>
    <input type="submit" value="Save">
  </form>
{% endblock %}
