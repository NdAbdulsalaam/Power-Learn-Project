from django.shortcuts import render, redirect, get_object_or_404
from .models import Pharmacy, Review
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout #, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pharmacy_list')
    else:
        form = UserCreationForm()
    return render(request, 'locator/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('pharmacy_list')
    else:
        form = AuthenticationForm()
    return render(request, 'locator/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')



def pharmacy_list(request):
    pharmacies = Pharmacy.objects.all()
    return render(request, 'locator/pharmacy_list.html', {'pharmacies': pharmacies})

def pharmacy_detail(request, pharmacy_id):
    pharmacy = get_object_or_404(Pharmacy, id=pharmacy_id)
    reviews = Review.objects.filter(pharmacy=pharmacy)
    return render(request, 'locator/pharmacy_detail.html', {'pharmacy': pharmacy, 'reviews': reviews})

@login_required
def add_review(request, pharmacy_id):
    pharmacy = get_object_or_404(Pharmacy, id=pharmacy_id)
    if request.method == 'POST':
        rating = request.POST['rating']
        comment = request.POST['comment']
        Review.objects.create(pharmacy=pharmacy, user=request.user, rating=rating, comment=comment)
        # return HttpResponseRedirect(reverse('pharmacy_detail', args=[pharmacy.id]))
        return redirect(reverse('pharmacy_detail', args=[pharmacy.id]))

    return render(request, 'locator/add_review.html', {'pharmacy': pharmacy})
