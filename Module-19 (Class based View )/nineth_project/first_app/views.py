from django.shortcuts import render
from datetime import datetime , timedelta
from django.http import HttpResponse
# Create your views here.
def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'rahim')
    # response.set_cookie('name', 'karim', expires=datetime.utcnow()+timedelta(days=7))
    response.set_cookie('name', 'karim', max_age=5)
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request , 'get_cookie.html' , {'name':name})


def delete_cookie(request):
    response = render(request , 'del_cookie.html')
    response.delete_cookie('name')
    return response


def set_session(request):
    data = {
        'name' : 'rahim',
        'age' : 23,
        'language' : 'bangla'
    }
    print(request.session.get_session_cookie_age())  #koto somoy session tar meyad thakbe (Second e answer dai)
    print(request.session.get_expiry_date())  #Koto din meyad thakbe bole dai( 2 week thake )
    request.session.update(data)
    return render(request , 'home.html')


# def get_session(request):
#     name = request.session.get('name' , 'guest')
#     age = request.session.get('age')
#     return render(request , 'get_session.html' , {'name':name , 'age':age})


def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name' , 'guest')
        request.session.modified = True
        return render(request , 'get_session.html' , {'name':name})
    else:
        return HttpResponse("Your Session has been Expired. Login again")




def delete_session(request):
    # del request.session['name']      #kono particular data delete korar jonno
    request.session.flush()         #ekshate Sob data delete kore debe
    return render(request , 'del_cookie.html' )
