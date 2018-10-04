from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Photos
from .form import PhotoUploadform
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

def home(request):
  documents = Photos.objects.all()
  context = {
    "documents":documents
  }
  return render(request,'home.html',context)

def simple_upload(request):
  if request.method == "POST" and  request.FILES['myfile']:
    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name,myfile)
    uploaded_file_url = fs.url(filename)
    return render(request,"simple_upload.html",{
      'uploaded_file_url':uploaded_file_url
    })
  return render(request,'simple_upload.html')

def model_form_upload(request):
  if request.method == "POST":
    form = PhotoUploadform(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return redirect("home")
  else:
    form = PhotoUploadform()
  return render(request,"model_form_upload.html",{
    'form':form
  })

def web(request):
  query = Photos.objects.all()
  paginator = Paginator(query, 5) # Show 25 contacts per page
  page = request.GET.get('page')
  query = paginator.get_page(page)

  context ={
    "Qu" :query,
    "title" : "myApp"
    
  }
  
  return render(request,"index.html" ,context)


def post_detail(request,id = None):
  postdetail =get_object_or_404(Photos,id = id)
  context={
    "title":postdetail.title,
    "instance":postdetail,
  }
  return render(request,"webindex.html" ,context)

def post_delete(request,id=None):
  instance = get_object_or_404(Photos,id =id)
  instance.delete()
  return redirect("home")



