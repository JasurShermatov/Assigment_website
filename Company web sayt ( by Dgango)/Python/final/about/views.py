from django.shortcuts import render
from .models import AboutWorker, Company, Feedback
from django.shortcuts import render, redirect


# Create your views here.
def news(request):
    info = Company.objects.all().order_by('-date')
    context = {
        'info':info,
        'html_name': 'about',
        'title': 'Web Project'
    }
    return render(request, 'about/index.html', context=context)


def workers_info(request):
    info = AboutWorker.objects.all().order_by('-place')
    context = {
        'info': info,
        'html_name': 'workers_info',
        'title': "Worker's info"
    }
    return render(request, 'about/index.html', context=context)

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        f = Feedback(name=name, email=email, message=message)
        if name.strip() == '' and email.strip() == '':
            return redirect('feedback')
        else:
            f.save()
            return redirect('news')
    else:
        return render (request, 'about/index.html', context={
            'html_name': 'feedback', 'title': 'Feedback'
        })
            
    


