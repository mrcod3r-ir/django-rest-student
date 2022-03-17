""" 
api_view for method type : POST GET ..
response for response
Student for model
serializers for serialize info
"""
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .models import Student
from .serializers import StudentSerializer

# show list of student
@api_view(["GET"])
def student_List(request):
  students=Student.objects.all()
  students_serialize=StudentSerializer(students,many=True)
  return Response(students_serialize.data)

# show student detail
@api_view(['GET'])
def student_Details(request,pk):
  student=Student.objects.get(id=pk)
  student_serialize=StudentSerializer(student,many=False)
  return Response(student_serialize.data)