# I have Created This file - Asim
from django.http import HttpResponse
from django.shortcuts import render

#code for video 6
# def index(request):
#     return HttpResponse("<h1>Asim</h1>")

# def about(request):
#     return HttpResponse("About Hello Asim")

#code for video 7
def index(request):
    return render(request, 'index2.html')
    # return HttpResponse("Home")

def ex1(request):
    s = '''<h2>Navigation bar<br></h2>
        <a href="https://www.youtube.com/">youtube</a><br>
        <a href="https://www.facebook.com/">Facebook</a><br>
        <a href="https://www.google.com/">Googele</a><br>'''
    return HttpResponse(s)

def analyze(request):
    # get the text 
    djtext = request.POST.get('text', 'default')
    # checkbox value 
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # charactercounter = request.POST.get('charactercounter', 'off')
    # print(djtext)
    # print(removepunc)
    if(removepunc == "on"):
        # analyze = djtext 
        punctuations = '''!()-[]{};:'",<>/?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        
        params = {'purpose': 'Removed Punctuations', 'Analyze_text': analyzed}
        djtext = analyzed
        # analyze the text 
        # return render(request, 'analyze2.html', params)
        # return HttpResponse("remove punc <a href='/'>back</a>")

    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to uppercase', 'analyze_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', params)

    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed Newlines', 'analyze_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', params)

    if(extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Newlines', 'analyze_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze2.html', params)

    # if(charactercounter == 'on'):
    #     analyzed = 0
    #     for char in djtext:
    #         analyzed = analyzed + 1
    #     params = {'purpose': 'Removed Newlines', 'analyze_text': analyzed-1}
    #     djtext = analyzed
        # return render(request, 'analyze2.html', params)

    if(removepunc != "on" and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on'):
        analyzed = "Please Mark Some Operations"
        params = {'purpose': 'Error', 'analyze_text': analyzed}

    return render(request, 'analyze2.html', params)
