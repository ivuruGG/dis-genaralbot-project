{% extends 'base.html' %}

{% block title %}Login{% endblock %}

{% block content %}
<header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">My Dashboard</a>
    </nav>
</header>

<div class="container mt-5">
    <div class="card mx-auto" style="max-width: 400px;">
        <div class="card-header">
            Login
        </div>
        <div class="card-body">
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
    </div>
</div>

<footer>
    <div class="bg-light py-3">
        <div class="container">
            <div class="row">
                <div class="col-md-12 text-center">
                    <p class="text-muted mb-0">My Dashboard &copy; 2023</p>
                </div>
            </div>
        </div>
    </div>
</footer>
{% endblock %}