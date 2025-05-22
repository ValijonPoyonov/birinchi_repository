from django.shortcuts import render, get_object_or_404

from .forms import CommentForm
from .models import Post
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Countries, Employees, Dependents

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = "blog/post/list.html"


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug,
                             status="published",
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active = True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
            comment_form = CommentForm()


    return render(request, 'blog/post/detail.html', {'post': post,
                                                     'comments':comments,
                                                     'new_comment':new_comment,
                                                     'comment_form':comment_form,
                                                     })



def index_page(request):
     return render(request, "index.html")

def get_max_salary_employees(request, top):
     queryset = Employees.objects.all().order_by('-salary')[:top]
     return render(request,"max_salary.html",{"max_salary":queryset})

def get_dependents(request, employee_id):
     queryset=Dependents.objects.all().filter(employee=employee_id)
     employee=Employees.objects.get(employee_id=employee_id)
     contex = {'deps':queryset, 'employee':employee}
     return render(request, "dependents.html", contex)

# def list1(request):
#      countries = Employees.objects.order_by('-salary')
#      country_list = ""
#
#      for i in countries:
#           country_list = country_list + f"<li>{i.first_name} {i.salary}</li>"
#      return HttpResponse(f"<ol>{country_list}</ol>")