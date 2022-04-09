
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    if removepunc=='on':
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punc:
                analyzed += char
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed
    if capfirst == 'on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Capitalize the charcters', 'analyzed_text': analyzed}
        djtext = analyzed
    if newlineremover=='on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}
        djtext = analyzed
    if spaceremover=='on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed += char
        params = {'purpose': 'Remove spaces', 'analyzed_text': analyzed}
        djtext = analyzed
    if removepunc != 'on' and newlineremover != 'on' and capfirst != 'on' and spaceremover != 'on':
        return HttpResponse('<h1><b>Error....</b></h1>')
    return render(request, 'analyze.html', params)

