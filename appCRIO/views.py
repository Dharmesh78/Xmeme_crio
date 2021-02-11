#
# from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse,JsonResponse
# from appCRIO.forms import MemeForm
# from rest_framework import viewsets
# from rest_framework import permissions
# from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from appCRIO.models import Meme
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from appCRIO.serializers import MemeSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from django.shortcuts import render

# class MemeList(generics.ListCreateAPIView):
#     queryset = Meme.objects.all()
#     serializer_class = MemeSerializer
#
#
# class MemeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Meme.objects.all()
#     serializer_class = MemeSerializer

# class MemeList(APIView):
#     #context_object_name='meme_obj'
#     renderer_class=[TemplateHTMLRenderer]
#     def get(self, request):
#         queryset = Meme.objects.all()
#         serializer= MemeSerializer(queryset,many=True)
#         return render(request,'index.html',{'meme_obj':serializer.data})



@api_view(['GET','POST'])
def memeList(request):
	if request.method=='GET':
		meme = Meme.objects.all().order_by('-meme_id')[:100]
		serializer = MemeSerializer(meme, many=True)
	elif request.method=='POST':
		serializer=MemeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()

	return Response(serializer.data)



@api_view(['GET','POST'])
def memeDetail(request, pk):
	if request.method=='GET':
		meme = Meme.objects.get(meme_id=pk)
		serializer = MemeSerializer(meme, many=False)
	elif request.method=='POST':
		meme=Meme.objects.get(meme_id=pk)
		serializer=MemeSerializer(instance=meme,data=request.data)
		if serializer.is_valid():
			serializer.save()
	return Response(serializer.data)



@api_view(['DELETE'])
def memeDelete(request,pk):
    meme=Meme.objects.get(meme_id=pk)
    meme.delete()

    return Response("Deleted")





# class MemeListView(ListView):
#     context_object_name='meme_obj'
#     model=Meme #returns a list with name meme_list by default if above statement i smissing
#     template_name='index.html'
#
# def add_meme(request):
#     added=False
#
#     if request.method == "POST":
#         meme_form=MemeForm(data=request.POST)
#         if meme_form.is_valid():
#             meme=meme_form.save(commit=False)
#             #print("NAME:"+str(request.user))
#             #task.author=request.user
#             meme.save()
#             added=True
#             meme_obj=Meme.objects.order_by('mid')
#             #print(meme_obj)
#             return render(request,'index.html',{'meme_obj':meme_obj,'added':added})
#
#         else:
#             print(meme_form.errors)
#
#
#     else: #no request=POST yet
#         meme_form=MemeForm()
#
#     return render(request,'addMeme.html',{'added':added,'meme_form':meme_form})
