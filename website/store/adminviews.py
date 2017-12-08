from django.shortcuts import render

#Admin index - comicfire.com/admin/
from store.database.adminGetData import ifUserExists


def admin(request):
    return render(request, 'admin/admin.html')

#De searchusers functie -> zoekt users aan de hand van ID of naam
def searchusers(request):
    if request.method == 'GET':
        if 'query' in request.GET:
            return searchusersresults(request)
    return render(request, 'admin/searchuser.html')

#De result pagina van de searchusers functie
def searchusersresults(request):
    getUserPar = request.GET['query']
    return render(request, 'admin/searchuser.html', {
        'query' : getUserPar,
    })

#De edituser functie
def edituser(request, userid):
    return render(request, 'admin/edituser.html', {

    })