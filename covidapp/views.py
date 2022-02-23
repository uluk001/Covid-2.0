from ast import Delete
import  requests
from django.shortcuts import render, HttpResponseRedirect
import requests
# Create your views here.
def main(request):
    return  render (request, 'index.html')


def search(request):
        country = request.POST.get('covid')
        url = f"https://covid-api.mmediagroup.fr/v1/cases?country={country}"
        res  = requests.get(url)
        json_covid = res.json()
        country = json_covid['All']['country']
        confirmed = json_covid['All']['confirmed']
        recovered = json_covid['All']['recovered']
        deaths = json_covid['All']['deaths']
        population = json_covid['All']['population']
        return render(request, 'index.html', {'country':country, 'confirmed':confirmed, 'recovered':recovered, 'deaths':deaths, 'population':population})



# def main_covid(request):
#         url = f"https://covid-api.mmediagroup.fr/v1/cases?country=world"
#         res  = requests.get(url).json()
#         json_covid = res
#         for i in json_covid:
#                 # print(i['All']['confirmed'])
#                 # confirmedd = int(i['All']['confirmed'])
#                 # countrry = str(i['All']['country'])
#                 return render(request, 'index.html', {'i':i})


def main_covid(request):
        token_API = f"https://covid-api.mmediagroup.fr/v1/cases"
        covid= requests.get(token_API)
        covid_json=covid.json()
        cheknumber=[]
        chekcountry=[]
        finish={}
        for i in covid_json:
            cheknumber.append(covid_json[i]['All']['confirmed'])
            chekcountry.append(i)
            a=max(cheknumber[:-1])
            index = cheknumber.index(a)
            for i in range(10):
                a=max(cheknumber[:-1])
                index = cheknumber.index(a)
                finish[chekcountry[index]]=cheknumber[index]
                chekcountry.pop(index)
                cheknumber.pop(index)
        return render(request, 'index.html', {'finish':cheknumber})
