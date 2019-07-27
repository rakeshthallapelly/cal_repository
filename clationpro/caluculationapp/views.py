from django.shortcuts import render,redirect
from django.http import HttpResponse
i = None
j = None
def input(request):
	return render(request,'add.html')
def output(request):
	val1 = request.GET['t1']
	val2 = request.GET['t2']
	global i
	global j
	i = int(val1)
	j = int(val2)
	z = request.GET['but']
	if z =='add':
		return redirect(add)
	if z =='sub':
		return redirect(sub)
	if z =='mul':
		return redirect(mul)
	if z =='div':
		return redirect(div)	
def add(request):
	k=i+j
	#data = "the output:",k
	#return HttpResponse(data)
	return HttpResponse(k)

def sub(request):
	k=i-j
	#data = "the output:" k
	#return HttpResponse(data)
	return HttpResponse(k)
def mul(request):
	k=i*j
	#data = "the output:" k
	#return HttpResponse(data)
	return HttpResponse(k)
def div(request):
	k=i/j
	#data = "the output:" k
	#return HttpResponse(data)
	return HttpResponse(k)		
