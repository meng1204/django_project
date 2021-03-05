from django.shortcuts import render


posts = [
    {
        'author': 'John',
        'title': 'Blog Post 1', 
        'content': "First post content",
        "date_posted": 'August 27 2021'
    },
    {
        'author': 'Apple',
        'title': 'Blog Post 2', 
        'content': "Second post content",
        "date_posted": 'August 25 2021'
    },
    {
        'author': 'Ben',
        'title': 'Blog Post 3', 
        'content': "Third post content",
        "date_posted": 'August 24 2021'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': "About"})