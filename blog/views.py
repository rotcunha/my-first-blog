from django.shortcuts import render

def post_list(resquest):
    return render(request, 'blog/post_list.html', {})
