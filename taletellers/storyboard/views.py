from django.core.mail import send_mail
from django.views import generic
from django.shortcuts import render

from storyboard.forms import *
from storyboard.models import Post


class HomeView(generic.ListView):
    def get_queryset(self):
        return Post.objects.filter(parent__isnull=True)


class StoryView(generic.CreateView):
    form_class = ContactForm
    template_name = "storyboard/post_detail.html"
    success_url = "."

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method in ["POST", "PUT"]:
            post_data = kwargs["data"].copy()
            post_data["title"] = [self.get_context_data()["story_list"][0]]
            kwargs["data"] = post_data
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        story = context["object"]
        story_list = []
        while story.parent is not None:
            story_list.append(story)
            story = story.parent
        else:
            story_list.append(story)
        story_list.reverse()
        context["story_list"] = story_list
        return context


class SSSView(generic.TemplateView):
    template_name = "storyboard/sss.html"


class ContactFormView(generic.FormView):
    form_class = ContactForm
    template_name = "storyboard/contact.html"
    success_url = "/"

    def form_valid(self, form):
        data = form.cleaned_data
        from django.conf import settings
        send_mail(
            "HikayeKitabi ContactForm: {}".format(data["title"]),
            ("Sistemimizde harika\n"
             "---\n"
             "{}\n"
             "---\n"
             "eposta={}\n"
             "ip={}").format(data["body"], data["email"], self.request.META["REMOTE_ADDR"]),
            settings.DEFAULT_FROM_EMAIL,
            ["bilal@taletellers.com"]
        )
        return super().form_valid(form)

"""
class KategoriView(generic.DetailView):
    def get_queryset(self):
        return Category.objects.all()
        

class DetayView(generic.DetayView):
    def get_queryset(self):
        return Category.objects.filter(report_count=0)
        
"""

