from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import FaceForm
from django.views.generic.edit import FormView
from django.views.generic import CreateView, DetailView
from .models import Face, FaceHist

# def face(request):
#     if request.method == 'POST':
#         form = FaceForm(request.POST)
#         if form.is_valid():
#             gender = form.cleaned_data['gender_field']
#             age = form.cleaned_data['age_field']
#             image = form.cleaned_data['image_field']
#             form.save()
#             context = {gender, age, image}
            # return render(request, 'face/face_detail.html', context)
    # else:
    #     form = FaceForm()
    # context = {'form':form}
    # return render(request, 'face/face.html', context)
    
class FaceCV(CreateView):
    print('-----faceview file------')
    form_class = FaceForm
    template_name = 'face/face.html'

    def form_valid(self, form):
        print('--------submit-------')
        if form.is_valid():
            form.age = form.instance.age,
            form.gender = form.instance.gender,
            form.image = form.instance.image,
            data = {
                'message' : '정상처리',
                'face_pk' : Face.objects.filter(face='공룡상'),
            }
            print(data)
            # form.add(message)
            # form.add(face_pk)
            print('befor : ',form)
            # hist.save()
            # print('after : ',hist)
        #     return super().form_valid(form)
        # return super(FaceCV, self).form_valid(form)

class FaceDV(DetailView):
    model = FaceHist
