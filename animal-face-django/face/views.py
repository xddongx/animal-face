from django.shortcuts import render

def face(request):
    return render(
        request,
        'face/face.html',
    )
