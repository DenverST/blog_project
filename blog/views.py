from django.shortcuts import render
from django.http import HttpResponse

posts = [
  {
    'author':'Denver T',
    'title':"Blodding Around1",
    'content':'Hellow wwolrd',
    'date_posted':"December 22, 2019"
  },
    {
    'author': 'Andrew P',
    'title': "Clocking aaaaaRound",
    'content': 'How to get the perfect time',
    'date_posted': "December 52, 2229"
  }
]

def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title':'About'})
