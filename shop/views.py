from datetime import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from shop.forms import storeForm, itemForm, usageForm
from shop.models import item, store, usage


def home(request):
   return render(request, 'home.html',
                 {'shop': home})


def items(request):

    itemList=item.objects.all()
    return render(request,'items.html',{'items':itemList})



def stores(request):

    storeList=store.objects.all()
    return render(request,'store.html',{'stores':storeList})

def usages(request):

    storeList=usage.objects.all()
    return render(request,'usage.html',{'stores':storeList})



def store_edit(request, pk):
   stores = get_object_or_404(store, pk=pk)
   if request.method == "POST":
       # update
       form = storeForm(request.POST, instance=stores)
       if form.is_valid():
           stores = form.save(commit=False)
           # stores.updated_date = timezone.now()
           stores.save()
           storeList = store.objects.all()
           return render(request, 'store.html', {'stores': storeList})
   else:
        # edit
        form = storeForm(instance=stores)
   return render(request, 'store-edit.html', {'form': form})



def item_edit(request, pk):
   items = get_object_or_404(item, pk=pk)
   if request.method == "POST":
       # update
       form =  itemForm(request.POST, instance=items)
       if form.is_valid():
           items = form.save(commit=False)
           # stores.updated_date = timezone.now()
           items.save()
           itemList = item.objects.all()
           return render(request, 'items.html', {'items': itemList})
   else:
        # edit
        form = itemForm(instance=items)
   return render(request, 'item-edit.html', {'form': form})

def usage_edit(request, pk):
   usages = get_object_or_404(usage, pk=pk)
   if request.method == "POST":
       # update
       form =  usageForm(request.POST, instance=usages)
       if form.is_valid():
           usages = form.save(commit=False)
           # stores.updated_date = timezone.now()
           usages.save()
           storeList = usage.objects.all()
           return render(request, 'usage.html', {'stores': storeList})
   else:
        # edit
        form = usageForm(instance=usages)
   return render(request, 'usage-edit.html', {'form': form})

def item_new(request):
   if request.method == "POST":
       form = itemForm(request.POST)
       if form.is_valid():
           service = form.save(commit=False)
           service.created_date = timezone.now()
           service.save()
           itemList = item.objects.all()
           return render(request, 'items.html', {'items': itemList})
   else:
       form = itemForm()
       # print("Else")
   return render(request, 'item-new.html', {'form': form})


def store_new(request):
   if request.method == "POST":
       form = storeForm(request.POST)
       if form.is_valid():
           service = form.save(commit=False)

           service.save()
           storeList = store.objects.all()
           return render(request, 'store.html', {'stores': storeList})
   else:
       form = storeForm()
       # print("Else")
   return render(request, 'store_new.html', {'form': form})




def item_new(request):
   if request.method == "POST":
       form = itemForm(request.POST)
       if form.is_valid():
           service = form.save(commit=False)
           service.user=request.user

           service.save()
           itemList = item.objects.all()
           return render(request, 'items.html', {'items': itemList})
   else:
       form = itemForm()
       # print("Else")
   return render(request, 'item-new.html', {'form': form})


def usage_new(request):
    if request.method == "POST":
        form = usageForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)

            service.save()
            storeList = usage.objects.all()
            return render(request, 'usage.html', {'stores': storeList})
    else:
        form = usageForm()
        # print("Else")
    return render(request, 'usage-new.html', {'form': form})
