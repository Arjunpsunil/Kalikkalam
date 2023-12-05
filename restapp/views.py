from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from restapp.models import*
from restapp.serializers import*
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def getdata(request):
#     if request.method=='GET':
#         student=Student.objects.all()
#         serializer=Studentserializer(student,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method=='POST':
#         data=JSONParser().parse(request)
#         serializer=Studentserializer(data=data)
#         if serializer.is_valid():
#             # serializer.save()
#             Student.objects.create(**serializer.validated_data)
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors,status=400)

# @csrf_exempt
# def update(request,id):
#     try:
#         students=Student.objects.get(id=id)
#     except Student.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method=='GET':
#         serializer=Studentserializer(students)
#         return JsonResponse(serializer.data)
#     elif request.method=='PUT':
#         data=JSONParser().parse(request)
#         serializer=Studentserializer(students,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         else:
#              JsonResponse(serializer.errors,status=400)
#     elif request.method=='DELETE':
#         students.delete()
#         return HttpResponse(status=204)
    

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def getdata(request):
    if request.method=='GET':
        student=Student.objects.all()
        serializer=Studentserializer(student,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=Studentserializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            Student.objects.create(**serializer.validated_data)
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)


@api_view(['GET','PUT','DELETE'])
def update(request,id):
    try:
        students=Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponse(status=404)
    if request.method=='GET':
        serializer=Studentserializer(students)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=Studentserializer(students,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
             Response(serializer.errors,status=400)
    elif request.method=='DELETE':
        students.delete()
        return Response(status=204)


# Create your views here.
