from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect

# from django.utils.translation import gettext_lazy as _
from core.constants import (
    NAMESPACE_2,
    NAMESPACE_3,
    PATTERN_2_2,
    PATTERN_2_3,
    PATTERN_3_3,
)
from core.language import (
    S_I_HOME_1_TTL,
    LB_PROFILE_TYPE,
    TX_PROFILE_1,
)


def home_selector_view(request):
    # Identifying the visitor:
    user = request.user
    # If logged-in:
    if user.is_authenticated:
        # Go to Personal or Business home page:
        if user.profile_type == "1":
            return redirect(reverse(NAMESPACE_2 + ":" + PATTERN_2_2))
        # else:
        #     return redirect(reverse(NAMESPACE_2 + ":" + PATTERN_2_3))
    # Send the visitor to login form:
    return redirect(reverse(NAMESPACE_3 + ":" + PATTERN_3_3))


@login_required
def home_profile_one_view(request):
    # If you wanna pass variables to the template, you need this always as dictionary:
    context = {
        "page_title": S_I_HOME_1_TTL,
        "profile_type": f"{LB_PROFILE_TYPE}: {TX_PROFILE_1}",
    }
    # Return the data to be rendered with the template when a key of the context dict is called:
    return render(request, NAMESPACE_2 + "/home_one.html", context)

