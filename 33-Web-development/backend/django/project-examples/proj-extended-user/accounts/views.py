from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .models import User, UserProfileOne, UserProfileTwo
from .forms import CustomUserCreationForm, UserProfileOneForm, UserProfileTwoForm
from cefalog.language import (
    TX_FDBK_PROFILE_SUCC_UPDATED,
    TX_FDBK_PROFILE_FAIL,
    BT_REG_HAVE_ACCOUNT,
    BT_REG_SUBMIT,
    BT_PROFILE_SUBMIT,
    BT_PROFILE_DEL,
    TX_PROFILE_1,
    TX_PROFILE_2,
    S_G_REG_TTL,
)
from cefalog.constants import (
    PATTERN_1_1,
    PATTERN_1_2,
    PATTERN_2_1,
    PATTERN_3_2,
)


def register(request):
    # If logged-in:
    if request.user.is_authenticated:
        # There the user will be filtered in Personal or Business:
        return redirect('in:' + PATTERN_2_1)
    # Otherwise:
    else:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                # Automatic log-in after registration:
                login(request, new_user)
                return redirect('in:' + PATTERN_2_1)
        else:
            form = CustomUserCreationForm()
        # Defining what send to the template:
        context = {
            'page_title': S_G_REG_TTL,
            'form': form,
            'bt_have_account': BT_REG_HAVE_ACCOUNT,
            'bt_submit': BT_REG_SUBMIT,
        }
        # Load template:
        return render(request, 'registration/register.html', context)


@login_required
def profile_view(request, username):
    # Identifying the current authenticated user and the profile owner:
    user = request.user
    profile_user = get_object_or_404(User, username=username)
    # Privacy control:
    if user != profile_user:
        return render(request, '401.html', status=401)

    # Take the right profile type:
    is_profile_1 = profile_user.profile_type == '1'
    if is_profile_1:
        instance = get_object_or_404(UserProfileOne, user=profile_user)
        form = UserProfileOneForm(instance=instance, user=user)
        profile_type = TX_PROFILE_1
    else:
        instance = get_object_or_404(UserProfileTwo, user=profile_user)
        form = UserProfileTwoForm(instance=instance, user=user)
        profile_type = TX_PROFILE_2

    # If something's submitted:
    if request.method == 'POST':
        if 'del_account' in request.POST:
            # TODO FIX: DELETION OPTIONS IS NEEDED IN FRONT-END TOO!
            # instance.delete_instance()
            if is_profile_1:
                return redirect('general:' + PATTERN_1_1)
            return redirect('general:' + PATTERN_1_2)
        # Defining the object of the current form, passing also the user object:
        if is_profile_1:
            form = UserProfileOneForm(request.POST, instance=instance, user=user)
        else:
            form = UserProfileTwoForm(request.POST, instance=instance, user=user)
        if form.is_valid():
            # form.save()  # It seems duplicated!!!! So I commented it!
            # Update the User model fields:
            # profile_type is NOT available for user edition;
            profile_user.email = form.cleaned_data['email']
            profile_user.is_notified_by_email = form.cleaned_data['is_notified_by_email']
            profile_user.language = form.cleaned_data['language']
            # Automatically set `updated_by` to the current user if different:
            if profile_user.updated_by != user:
                profile_user.updated_by = user
            profile_user.updated_at = timezone.now()
            # Save the user object and passing the current user to update UserProfile:
            profile_user.save()
            form.save(user=user)
            messages.success(request, TX_FDBK_PROFILE_SUCC_UPDATED)
            return redirect('accounts:' + PATTERN_3_2, username=username)
        else:
            messages.error(request, TX_FDBK_PROFILE_FAIL)

    # Defining what send to the template:
    context = {
        'page_title': f'{username} ({profile_type})',
        'form': form,
        'bt_submit': BT_PROFILE_SUBMIT,
        'bt_del': BT_PROFILE_DEL,
    }
    # Load template:
    return render(request, 'accounts/profile.html', context)
