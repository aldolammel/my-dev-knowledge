


FRONT-END: USER PROFILE FORM


    
    1) In a template (e.g. profile.html) customize this:

        {% extends "base.html" %}

        {% block title %}{{ page_title }}{% endblock %}

        {% block description %}{% endblock %}

        {% block content %}

            <!-- feedback messages - start -->
            {% if messages %}
                <ul class="messages">
                    {% for msg in messages %}
                        <li{% if msg.tags %} class="{{ msg.tags }}"{% endif %}>{{ msg }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
            <!-- feedback messages - end -->
            
            <h1>{{ page_title }}</h1>

            <!-- PROFILE FORM - START -->
            <form method="post">

                {% csrf_token %}

                <div class="">

                    {{ form.as_p }}

                </div>
                <button type="submit" name="action" value="update_account">{{ bt_submit }}</button>
                <button type="submit" name="action" value="delete_account">{{ bt_del }}</button>

            </form>
            <!-- PROFILE FORM - END -->
            
        {% endblock %}

        {% block scripts %}{% endblock %}

