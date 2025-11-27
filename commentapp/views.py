from django.shortcuts import render

from django.views.generic import TemplateView,ListView,CreateView

from .models import UserComments

from .forms import CommentForm
# Create your views here.
from django.urls import reverse_lazy

class CommentView(CreateView):

    form_class = CommentForm


    template_name = 'comment.html'

    success_url = reverse_lazy('comment:comeiti')

    def form_valid(self, form):
        postdata = form.save(commit=False)


        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

class ComeitiView(ListView):
    context_object_name = 'comment'
    template_name = 'comeiti.html'
    paginate_by = 8

    def get_queryset(self):
        return UserComments.objects.all().order_by('-id')
    
    