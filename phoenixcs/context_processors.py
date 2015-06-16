def include_login_form(request):
    from django.contrib.auth.forms import AuthenticationForm
    from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
    from django.views.generic import TemplateView
    from django.contrib import messages
    from django.utils.translation import ugettext as _
    from userena.forms import (SignupForm, SignupFormOnlyEmail, AuthenticationForm,
                               ChangeEmailForm, EditProfileForm)
    from userena.utils import (signin_redirect, get_profile_model, get_user_model,
                               get_user_profile)
    from userena import signals as userena_signals
    from userena import settings as userena_settings
    from django.http import Http404, HttpResponseRedirect
    auth_form=AuthenticationForm
    template_name='userena/signin_form.html'
    redirect_field_name=REDIRECT_FIELD_NAME
    redirect_signin_function=signin_redirect
    extra_context=None

    form = auth_form()
    if request.method == 'POST':
        form = auth_form(request.POST, request.FILES)
        if form.is_valid():
            identification, password, remember_me = (form.cleaned_data['identification'],
                                                     form.cleaned_data['password'],
                                                     form.cleaned_data['remember_me'])
            user = authenticate(identification=identification,
                                password=password)
            if user.is_active:
                login(request, user)
                if remember_me:
                    request.session.set_expiry(userena_settings.USERENA_REMEMBER_ME_DAYS[1] * 86400)
                else: request.session.set_expiry(0)

                if userena_settings.USERENA_USE_MESSAGES:
                    messages.success(request, _('You have been signed in.'),
                                     fail_silently=True)

                #send a signal that a user has signed in
                userena_signals.account_signin.send(sender=None, user=user)
                # Whereto now?
                redirect_to = redirect_signin_function(
                    request.REQUEST.get(redirect_field_name), user)
                return HttpResponseRedirect(redirect_to)
            else:
                return redirect(reverse('userena_disabled',
                                        kwargs={'username': user.username}))

    if not extra_context: extra_context = dict()
    return {
        'form': form,
        'next': request.REQUEST.get(redirect_field_name),
    }
    # return ExtraContextTemplateView.as_view(template_name=template_name,
    #                                         extra_context=extra_context)(request)

