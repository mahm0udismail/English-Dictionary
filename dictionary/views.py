from django.shortcuts import render
from pydictionary import Dictionary

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dict = Dictionary(search)
    meaning = dict.meanings()
    synonyms = dict.synonyms()
    antonyms = dict.antonyms()
    context = {
        'meaning': meaning[0],
        'synonyms': synonyms,
        'antonyms': antonyms
    }
    return render(request, 'word.html', context)