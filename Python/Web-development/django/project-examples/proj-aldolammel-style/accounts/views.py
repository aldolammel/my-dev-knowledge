from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
)
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone, translation
from .models import User, UserProfileOne
from .forms import (
    CustomUserCreationForm,
    CustomLoginForm,
    CustomPasswordResetConfirmForm,
    CustomPasswordChangeForm,
    CustomPasswordResetForm,
    UserProfileOneForm,
)
from core import language as lng
from core.constants import (
    NAMESPACE_1,
    NAMESPACE_2,
    NAMESPACE_3,
    PATTERN_1_1,
    PATTERN_1_2,
    PATTERN_2_1,
    PATTERN_3_2,
    PATTERN_3_6,
    PATTERN_3_8,
)


def register(request):
    # Escape if logged-in:
    if request.user.is_authenticated:
        # There the user will be filtered in Personal or Business:
        return redirect(NAMESPACE_2 + ":" + PATTERN_2_1)
    # Otherwise:
    else:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                # Automatic log-in after registration:
                login(request, new_user)
                return redirect(NAMESPACE_2 + ":" + PATTERN_2_1)
        else:
            form = CustomUserCreationForm()
        # Defining what send to the template:
        context = {
            "page_title": lng.S_G_REG_TTL,
            "form": form,
            "bt_have_account": lng.BT_LOGIN_HAVE_ACCOUNT,
            "bt_submit": lng.BT_REG_SUBMIT,
            "bt_back": lng.BT_BACK,
        }
        # Load template:
        return render(request, "registration/register.html", context)


class CustomLoginView(LoginView):
    template_name = NAMESPACE_3 + "/login.html"
    form_class = CustomLoginForm
    redirect_authenticated_user = True
    extra_context = {
        "page_title": lng.S_G_LOGIN_TTL,
        "bt_submit": lng.BT_LOGIN,
        # 'bt_back': lng.BT_BACK,
        "bt_pwd_forgot": lng.BT_LOGIN_RESET,
        "bt_new_account": lng.BT_REG_NEW_ACCOUNT,
    }
    success_url = NAMESPACE_2 + ":" + PATTERN_2_1


# It sends the mail:
class CustomPasswordResetView(PasswordResetView):
    template_name = "registration/password_reset.html"
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy(NAMESPACE_3 + ":" + PATTERN_3_6)
    email_template_name = "registration/password_reset_email_custom.html"
    extra_context = {
        "page_title": lng.S_G_LOGIN_RESET_TTL,
        "bt_submit": lng.BT_LOGIN_RESET_SUBMIT,
        "bt_back": lng.BT_BACK,
    }

    def form_valid(self, form):
        """Override form_valid to add custom messages or actions on successful form submission."""
        messages.info(self.request, lng.TX_FDBK_LOGIN_RESET)
        return super().form_valid(form)


# It shows a success message about the email sent with the link to reset the password:
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/password_reset_done_custom.html"
    extra_context = {
        "page_title": lng.S_G_LOGIN_RESET_TTL,
    }


# It checks the link the user clicked and prompts for a new password:
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "registration/password_reset_confirm_custom.html"
    form_class = CustomPasswordResetConfirmForm
    success_url = reverse_lazy(NAMESPACE_3 + ":" + PATTERN_3_8)
    extra_context = {
        "page_title": lng.S_G_LOGIN_RESET_TTL,
        "header": lng.S_I_PROFILE_PWD_TTL,
        "bt_submit": lng.BT_PROFILE_PWD_SUBMIT,
    }


# It shows a success message when the new password is defined in reset proccess:
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "registration/password_reset_complete_custom.html"
    extra_context = {
        "page_title": lng.S_G_LOGIN_RESET_COMPLETE_TTL,
        #'bt_submit': lng.S_G_LOGIN_NAME,
    }


class CustomPasswordChangeView(PasswordChangeView):
    template_name = "registration/password_change.html"
    form_class = CustomPasswordChangeForm

    def form_valid(self, form):
        """Override form_valid to add custom messages or actions on successful form submission."""
        user = self.request.user
        # Check if the old password is correct:
        if user.check_password(form.cleaned_data["old_password"]):
            # Check if the new password is different from the old password:
            if form.cleaned_data["new_password1"] != form.cleaned_data["old_password"]:
                # Set the new password:
                user.set_password(form.cleaned_data["new_password1"])
                user.save()  # save the user instance to the db.
                messages.success(self.request, lng.TX_FDBK_PROFILE_PWD_UPDATED)
                return redirect(NAMESPACE_3 + ":" + PATTERN_3_2, username=user.username)
            else:
                form.add_error("new_password1", lng.TX_FDBK_PROFILE_PWD_EQUAL_OLD)
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        # Definitions:
        user = self.request.user
        profile_type = (
            lng.TX_PROFILE_1
            #lng.TX_PROFILE_1 if user.profile_type == "1" else lng.TX_PROFILE_2
        )
        context = super().get_context_data(**kwargs)
        # Building context:
        context["page_title"] = (
            f"{lng.S_I_PROFILE_PWD_TTL}: {user.username} ({profile_type})"
        )
        context["header"] = lng.S_I_PROFILE_PWD_TTL
        context["bt_back"] = lng.BT_BACK
        context["bt_submit"] = lng.BT_PROFILE_PWD_SUBMIT
        return context


def custom_logout_view(request):
    """Select a more appropriated home to the user after logout"""
    if request.user.is_authenticated:
        # profile_type = request.user.profile_type
        logout(request)
        # if profile_type == "2":
        #     return redirect(NAMESPACE_1 + ":" + PATTERN_1_2)
    return redirect(NAMESPACE_1 + ":" + PATTERN_1_1)


@login_required
def profile_view(request, username):
    # Identifying the current authenticated user and the profile owner:
    user = request.user
    profile_user = get_object_or_404(User, username=username)
    # Privacy control:
    if user != profile_user:
        return render(request, "401.html", status=401)

    # Take the right profile type:
    is_profile_1 = profile_user.profile_type == "1"
    if is_profile_1:
        instance = get_object_or_404(UserProfileOne, user=profile_user)
        form = UserProfileOneForm(instance=instance, user=user)
        profile_type = lng.TX_PROFILE_1
    # else:
    #     instance = get_object_or_404(UserProfileTwo, user=profile_user)
    #     form = UserProfileTwoForm(instance=instance, user=user)
    #     profile_type = lng.TX_PROFILE_2

    # If something's submitted:
    if request.method == "POST":
        if "delete_account" in request.POST:
            # TODO FIX: DELETION OPTIONS IS NEEDED IN FRONT-END TOO!
            # instance.delete_instance()
            logout(request)
            if is_profile_1:
                messages.success(request, lng.TX_FDBK_PROFILE_1_DEL)
                return redirect(NAMESPACE_1 + ":" + PATTERN_1_1)
            # messages.success(request, TX_FDBK_PROFILE_2_DEL)
            return redirect(NAMESPACE_1 + ":" + PATTERN_1_2)
        # Defining the object of the current form, passing also the user object:
        if is_profile_1:
            form = UserProfileOneForm(request.POST, instance=instance, user=user)
        # else:
        #     form = UserProfileTwoForm(request.POST, instance=instance, user=user)
        if form.is_valid():
            profile_user.email = form.cleaned_data["email"]
            profile_user.is_notified_by_email = form.cleaned_data["is_notified_by_email"]
            profile_user.language = form.cleaned_data["language"]
            # Automatically set `updated_by` to the current user if different:
            if profile_user.updated_by != user:
                profile_user.updated_by = user
            profile_user.updated_at = timezone.now()
            # Save the user object and passing the current user to update UserProfile:
            profile_user.save()
            form.save(user=user)
            # Update the session language to match the new preference:
            # Important: keep it before the messages.success() to translate the message according to
            # the new language if the user has changed it.
            if 'language' in form.cleaned_data and form.cleaned_data['language']:
                # Get the ISO code from the Language model instance:
                language_code = form.cleaned_data['language'].iso_code
                # Set the new language in the session:
                translation.activate(language_code)
                request.session['_language'] = language_code
            # Feedback message:
            messages.success(request, lng.TX_FDBK_PROFILE_SUCC_UPDATED)
            # Refresh the profile page:
            return redirect(NAMESPACE_3 + ":" + PATTERN_3_2, username=username)

    # Defining what send to the template:
    context = {
        "page_title": f"{lng.S_I_PROFILE_TTL}: {username} ({profile_type})",
        "form": form,
        "profile_type": profile_type,
        "ttl": lng.S_I_PROFILE_TTL,
        "bt_submit": lng.BT_PROFILE_SUBMIT,
        "bt_cancel": lng.BT_CANCEL,
        "bt_change_pwd": lng.BT_PROFILE_PWD_CHANGE,
        "bt_del": lng.BT_PROFILE_DEL,
    }
    # Load template:
    # if is_profile_2:
    #     return render(request, NAMESPACE_3 + "/profile_2.html", context)
    return render(request, NAMESPACE_3 + "/profile_1.html", context)
    
