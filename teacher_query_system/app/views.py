from django.shortcuts import render
from .models import Teacher


def query_view(request):
    if request.method == "POST":
        search_type = request.POST.get('search_type')

        if search_type == 'name':
            name = request.POST.get('name')
            teachers = Teacher.objects.filter(name=name)
        elif search_type == 'department':
            departments = request.POST.getlist('department')
            teachers = Teacher.objects.filter(department__in=departments)
            
        return render(request, 'results.html', {'teachers': teachers})

    departments = Teacher.objects.values_list('department', flat=True).distinct()
    return render(request, 'query.html', {'departments': departments})

