from django.views.generic.base import TemplateView
from core.consts import (
    NAMEAPP_1,
)
from core.language import (
    S_G_HOME_1_TTL,
    S_G_HELP_TTL,
    S_G_ABOUT_TTL,
    S_G_PRIVACY_TTL,
    TX_PROFILE_1_CTA,
)

# Sections - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class HomeProfileOneView(TemplateView):
    template_name = NAMEAPP_1 + "/home_one.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = S_G_HOME_1_TTL
        context["cta"] = TX_PROFILE_1_CTA
        return context


# class HomeProfileTwoView(TemplateView):
#     template_name = NAMEAPP_1 + "/home_two.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["page_title"] = S_G_HOME_2_TTL
#         context["cta"] = TX_PROFILE_2_CTA
#         return context


class HelpView(TemplateView):
    template_name = NAMEAPP_1 + "/help.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = S_G_HELP_TTL
        return context


class AboutView(TemplateView):
    template_name = NAMEAPP_1 + "/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = S_G_ABOUT_TTL
        return context


class PrivacyPolicyView(TemplateView):
    template_name = NAMEAPP_1 + "/privacy_policy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = S_G_PRIVACY_TTL
        return context
