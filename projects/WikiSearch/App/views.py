from django.shortcuts import render, HttpResponse 
import wikipedia 


# Create your views here. 
def home(request): 
	if request.method == "POST": 
		search = request.POST['search'] 
		try: 
			result = wikipedia.summary(search,sentences = 3) #No of sentences that you want as output 
		except: 
			return HttpResponse("Wrong Input") 
		return render(request, "index.html", {"result":result}) 
	return render(request, "index.html") 
