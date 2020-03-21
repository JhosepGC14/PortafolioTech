from django.shortcuts import render, get_object_or_404
from .models import Job
from .form import DocumentForm
# Create your views here.


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'data': jobs})


def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'data': job_detail})


def index(request):
    return render(request, 'jobs/index.html')


def dashboard(request):
    return render(request, 'jobs/dashboard.html')


def model_form_upload(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()
    return render(request, 'jobs/add.html', {'form': form})
