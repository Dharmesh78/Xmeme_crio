#
# from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse,JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from appCRIO.models import Meme
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from appCRIO.serializers import MemeSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from django.shortcuts import render




@api_view(['GET','POST'])
def memeList(request):
	if request.method=='GET':
		meme = Meme.objects.all().order_by('-id')[:100]
		serializer = MemeSerializer(meme, many=True)
	elif request.method=='POST':
		serializer=MemeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()

	serJS = JsonResponse(serializer.data,safe=False)
	return render(request,'list.html',{'data':serJS.content.decode()})

@api_view(['GET','POST'])
def memeListAPI(request):
	if request.method=='GET':
		meme = Meme.objects.all().order_by('-id')[:100]
		serializer = MemeSerializer(meme, many=True)
	elif request.method=='POST':
		serializer=MemeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()

	return Response(serializer.data)



@api_view(['GET','POST'])
def memeDetail(request, pk):
	if request.method=='GET':
		try:
			meme = Meme.objects.get(id=pk)
		except Meme.DoesNotExist:
			return HttpResponse(status=404)
		serializer = MemeSerializer(meme, many=False)
	elif request.method=='POST':
		meme=Meme.objects.get(id=pk)
		serializer=MemeSerializer(instance=meme,data=request.data)
		if serializer.is_valid():
			serializer.save()
	serJS = JsonResponse(serializer.data,safe=False)
	return render(request,'list.html',{'data':serJS.content.decode()})

@api_view(['GET','POST'])
def memeDetailAPI(request, pk):
	if request.method=='GET':
		try:
			meme = Meme.objects.get(id=pk)
		except Meme.DoesNotExist:
			return HttpResponse(status=404)
		serializer = MemeSerializer(meme, many=False)
	elif request.method=='POST':
		meme=Meme.objects.get(id=pk)
		serializer=MemeSerializer(instance=meme,data=request.data)
		if serializer.is_valid():
			serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def memeDelete(request,pk):
    meme=Meme.objects.get(id=pk)
    meme.delete()

    return Response("Deleted")
