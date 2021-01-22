from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.http import JsonResponse
from .forms import JobForm, TaskForm
from .models import TechExpert, Job, Status, Task
from .utils import calculateEstimatedTime

# Create your views here.

#Home
@login_required(login_url='/login')
def homePage(request):
    #Get expert list
    experts = TechExpert.objects.all()
    temp_list = []
    for expert in experts:
        tempex = {"expert_id": expert.expert_id, "expert_name": expert.expert_name}
        temp_list.append(tempex)
    experts = temp_list

    #Get status list
    statuses = Status.objects.all()
    temp_list = []
    for status in statuses:
        tempstat = {"status_id": status.status_id, "status_title": status.status_title}
        temp_list.append(tempstat)
    statuses = temp_list

    #Get Tasks
    tasks = Task.objects.all()
    temp_list = []
    for task in tasks:
        temptask = {"task_desc": task.task_desc, "task_job": task.task_job.job_title, "task_tech_expert": task.task_tech_expert.expert_name, "task_status_id": task.task_status_id, "task_created_date": task.task_created_date}
        temp_list.append(temptask)
    tasks = temp_list

    #Get Jobs
    jobs = Job.objects.all()
    temp_list = []
    for job in jobs:
        tempjob = {"job_title": job.job_title, "job_status": job.job_status.status_title, "job_tech_expert": job.job_tech_expert.expert_name, "job_id": job.job_id}
        temp_list.append(tempjob)
    jobs = temp_list
    context = {
        "experts" : experts,
        "stasuses": statuses,
        "tasks": tasks,
        "jobs": jobs,
        "date": now()
    }
    print(tasks)
    return render(request, 'home.html', context)

#Add Job
@login_required(login_url='/login')
def addJob(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid:
            form.save(commit=False)
            try:
                form.instance.job_tech_expert = TechExpert.objects.get(expert_id=(request.POST.get('expert_id')))
                form.instance.job_status = Status.objects.get(status_id=request.POST.get('status_id'))
                form.instance.job_estimated_time = calculateEstimatedTime(request.POST.get('job_desc'))
                form.save()
                response_text = "Job succesfully added"
                return JsonResponse({"status": 1, "message": response_text})
            except Exception as e:
                return JsonResponse({"status": 0, "message": "Error : " + str(e)})
        return JsonResponse({"status": 0, "message": "Data Error"})
    return JsonResponse({"status": 0, "message": "Only POST method accepted" })

#Add task
@login_required(login_url="/login")
def addTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save(commit=False)
            try:
                form.instance.task_tech_expert = TechExpert.objects.get(expert_id=(request.POST.get('expert_id')))
                form.instance.task_job = Job.objects.get(job_id=request.POST.get('job_id'))
                form.instance.task_status = Status.objects.get(status_id=request.POST.get('status_id'))
                form.save()
                response_text = "Task succesfully added"
                return JsonResponse({"status": 1, "message": response_text})
            except Exception as e:
                return JsonResponse({"status": 0, "message": "Error : " + str(e)})
        return JsonResponse({"status": 0, "message": "Data Error"})
    return JsonResponse({"status": 0, "message": "Only POST method accepted" })

#Get experts list
def getExperts(request):
    if request.method == 'GET':
        experts = TechExpert.objects.all()
        return_data = []
        for expert in experts:
            tempex = {"expert_id": expert.expert_id, "expert_name": expert.expert_name}
            return_data.append(tempex)
        return JsonResponse(return_data, safe=False)

#Get status list       
def getStatusList(request):
    if request.method == 'GET':
        statuses = Status.objects.all()
        return_data = []
        for status in statuses:
            tempstat = {"status_id": status.status_id, "status_title": status.status_title}
            return_data.append(tempstat)
        return JsonResponse(return_data, safe=False)

# Delete Job
def deleteJob(request, id):
    if request.method == 'GET':
        job_to_delete = Job.objects.get(job_id=id)
        job_to_delete.delete()
        return JsonResponse({"message":"işlem başarılı"})

# Delete Task
def deleteTask(request, id):
    if request.method == 'GET':
        task_to_delete = Task.objects.get(task_id=id)
        task_to_delete.delete()
        return JsonResponse({"message":"işlem başarılı"})

def test(request):
    return render(request, "test3.html")