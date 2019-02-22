from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Test URL")

# function takes a name in the URL and returns a response with "hello [NAME]"
def getHello(request, name):
    return HttpResponse("hello" + name)

# function takes an argument in the URL and returns a response with
# "The product times 2 is: [ANSWER]"
def times2(request, number):
    answer = (number*2)
    return HttpResponse("The product times 2 is:"+ str(answer))

# function takes an integer in the URL and returns a response with
# "The sum of all numbers from 0 to the integer is: [SUM]"
def total(request, integer ):
    sumAllIntegers = ""
    for x in range(integer):
        x += integer + ", "
    return HttpResponse("The sum of all numbers from 0 to the integer is:"+ str(sumAllIntegers))

# function prints out all entry purchaseTimes and create another new endpoint to change
# the material text of cups manufactured after 2012 to be "Slightly New".
def list_purchaseTimes(request):
    purchaseTimes = purchaseTimes.objects.all()
    print()
    return HttpResponse(purchaseTimes)


# function to change the material text of cups manufactured after 2012 to be "Slightly New".
def changeMaterial():
    

# phoneApp
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Phone
#
#
# # Create your views here.
# def index(request):
#     return HttpResponse("This is the phoneApp route!")
#
#
# def add5(request, number):
#     return HttpResponse("Your number plus 5 is: "+ str(number+5))
#
#
# def names100(request, name):
#     newString = ""
#
#     for x in range(100):
#         newString += name + ", "
#
#     return HttpResponse(newString)
#
#
# def all(request):
#     getAllPhones  = Phone.objects.all()
#     higherThanFive = Phone.objects.filter(version__gt = 5)
#     context = {
#         "getAllPhones": getAllPhones,
#         "higherThanFive": higherThanFive,
#     }
#
#     return render(request, "phoneApp/index.html", context)


# computerApp
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Computer
#
#
# # Create your views here.
# def root(request):
#     return HttpResponse("Go to the /phone or /computer routes please")
#
# def index(request):
#     return HttpResponse("This is the computerApp route!")
#
#
# def create(request):
#     newObject = Computer.objects.create(name="Dell Optipex", speed= 2.0, cores=2)
#
#     newObject2 = Computer(name="Dell Optipex", speed= 2.0, cores=2)
#     newObject2.save()
#     return HttpResponse()
#
#
# def computerIndex(request):
#     computer_list = Computer.objects.all()
#     context = {
#         'allComputers': computer_list,
#         'myName': "Kenn",
#         "myAge": 50
#     }
#     return render(request, 'computerApp/index.html', context)
