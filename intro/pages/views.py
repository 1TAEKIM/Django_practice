from django.shortcuts import render

# Create your views here.
def lotto(request):
    import random
    
    lotto_list = []
    for i in range(6):
        lotto_list.append(random.randint(1, 31))
        
    context = {
        'lotto_list': lotto_list
        
    }

    return render(request, 'pages/lotto.html', context)
