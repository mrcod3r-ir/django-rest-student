import json
from django.shortcuts import redirect, render
import requests
# Create your views here.

# Get list
def student_list(request):
  response=requests.get('http://127.0.0.1:8000/myapp/student_list').json()
  context={
    "students":response
  }
  
  return render(request,"testapp/studentslist.html",context=context)


# Create student

def student_save(request):
  instance={"Name":"Hassan","Family":"Qomi","Code":"210"}
  jsondata = json.dumps(instance)
  headers={'content-type':"application/json"}
  
  requests.post('http://127.0.0.1:8000/myapp/student_save',data=jsondata,headers=headers)
  return redirect(student_list)