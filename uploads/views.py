from django.shortcuts import render, redirect
from .forms import ProfileForm

def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProfileForm()
    return render(request, 'uploads/upload_profile.html', {'form': form})
def success(request):
    return render(request, 'uploads/success.html')