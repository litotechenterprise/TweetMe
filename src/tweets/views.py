from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Tweet
from .forms import TweetModelForm
from django.urls import reverse_lazy
from django import forms
from .mixin import FormUserNeededMixin, UserOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Create your views here.

# Create
class TweetCreateView(FormUserNeededMixin, CreateView):
    template_name = "tweets/create_view.html"
    #success_url = reverse_lazy("tweets:list")
    #login_url = "/admin/"
    queryset = Tweet.objects.all()
    form = TweetModelForm
    fields = ['content']


'''
def tweet_create_view(request):
    form = TweetModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
    context = {
        "form" : form
    }
    return render(request, "tweets/create_view.html", context)
'''


# Upate

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    form = TweetModelForm
    template_name = "tweets/update_view.html"
    success_url = reverse_lazy("tweets:list")
    queryset = Tweet.objects.all()
    fields = ['content']

# Delete

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = "tweets/delete_confirm.html"
    success_url = reverse_lazy("tweets:list")

# Retrieve

class TweetDetailView(DetailView):
    template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

'''
    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        print(pk)
        return Tweet.objects.get(id=pk) '''

# List / Search 
class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()


# with the  Q search makesure that you double underscore between each word!

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(

                Q(content__icontains=query) |
                Q(user__username__icontains=query)

            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
       # print(context)
        return context

'''
def tweet_Detail_View(request, id=1):
    obj = Tweet.objects.get(id=id) #Getting from database
    print(obj)
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)


def tweet_List_View(request):
    queryset = Tweet.objects.all() # Getting from the database
    print(queryset)

    # Printing out each item in the QuerySet
    for obj in queryset:
        print(obj.content)

    context = {
        "object_list": queryset
    }
    return render(request, "tweets/list_view.html", context)
'''