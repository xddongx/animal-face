from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import FaceForm
from django.views.generic.edit import FormView
from django.views.generic import CreateView, DetailView
from .models import FaceHist

def face(request):
    if request.method == 'POST':
        form = FaceForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender_field']
            age = form.cleaned_data['age_field']
            image = form.cleaned_data['image_field']
            form.save()
            context = {gender, age, image}
            # return render(request, 'face/face_detail.html', context)
    else:
        form = FaceForm()
    context = {'form':form}
    # return render(request, 'face/face.html', context)
    
# class FaceCreateView(CreateView):
#     print('-----faceview file------')
#     form_class = FaceForm
#     template_name = 'face/face.html'
#     # success_url = '/<int:pk>/'

#     def form_valid(self, form):
#         print('--------submit-------')
#         if form.is_valid():
#             age = form.instance.age
#             gender = form.instance.gender
#             image = form.instance.image
#             print(age)
#             print(gender)
#             print(image)
#             return super().form_valid(form)
#         return super(FaceCreateView, self).form_valid(form)

class FaceDV(DetailView):
    model = FaceHist
