from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from equipementsApp.models import Commutateur, Routeur, Terminale
from .forms import AddTerminaleForm



# Create your views here.

def index(request):
    machines=Terminale.objects.all(), Commutateur.objects.all(),Routeur.objects.all() 

    context = {}

    return render(request, 'index.html', context)

def machine_list_view(request) :
        terminales = Terminale.objects.all()
        commutateurs = Commutateur.objects.all()
        routeurs = Routeur.objects.all()
        context ={'routeurs': routeurs, 'terminales': terminales, 'commutateurs': commutateurs   }
        return render(request, 'computerapp/machine_list.html', context )

def machine_detail_view(request, pk):
        terminales = get_object_or_404(Terminale, id=pk )
        commutateurs =get_object_or_404(Commutateur, id=pk )
        routeurs = get_object_or_404(Routeur, id=pk )
        context ={'routeurs': routeurs,'terminales': terminales, 'commutateurs': commutateurs }
        return render(request, 'computerapp/machhine_detail.html', context )


""" def commutateur_list(request):
    commutateurs = Commutateur.objects.all()
    context={'commutateurs'=commutateurs}
    return render(request, 'equipementsApp/commutateur_list.html',context)

def terminal_list(request):
    terminales = Terminale.objects.all()
    context={'terminales'=terminales}
    return render(request, 'equipementsApp/terminal_list.html',context)

def routeur_list(request):
    routeurs = Routeur.objects.all()
    context={'routeurs'=routeurs}
    return render(request, 'equipementsApp/routeurs_list.html',context)
 """

def machine_add_form(request):
    if request.method == 'POST':
            form = AddTerminaleForm(request.POST or None)
            if form.is_valid():
                    new_machine = Terminale(nom=form.cleaned_data['nom'])
                    new_machine.save()
                    return HttpResponseRedirect('machines')
    else:
        form = AddTerminaleForm()
        context = {'form': form}
        return render(request,'computerapp/machine_add.html',context)
