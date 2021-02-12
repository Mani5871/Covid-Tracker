from django.shortcuts import render, HttpResponse
from covid import Covid


# Create your views here.


def index(request):
    covid = Covid()
    countries = covid.list_countries()
    country_list = []
    country_list = [sub['name'] for sub in countries]
    country_list.sort()
    context = {
        'list': country_list
    }
    return render(request, 'index.html', context)


def result(request):
    # return HttpResponse("Result")

    if request.method == 'POST':
        covid = Covid()
        country = request.POST.get('country')
        cases = covid.get_status_by_country_name(country)
        status = request.POST.get('choices')
        status.lower()
        context = {
            'name': country,
            'status': status,
            'number': cases[status]
        }
        return render(request, 'result.html', context)

