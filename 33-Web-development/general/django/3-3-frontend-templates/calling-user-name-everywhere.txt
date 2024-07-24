

If you want to print the user (username or first_name or last_name) on the template,
you DONT need bring some in your views.py CONTEXT. Just call 'user.username' on the
template:

    e.g

        {{ user.username }}