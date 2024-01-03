from django.shortcuts import render
from .forms import Raise_Request_Model_Form

def raise_a_request(request):
    form = Raise_Request_Model_Form(request.POST or None)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        form = Raise_Request_Model_Form()
        # print(customer_name = form.cleaned_data["customer_name"])

        # obj = Raise_Request_Form()
        # obj.customer_name = customer_name
        # obj.save()
        # form = Raise_Request_Form()
    context = {"form":form}
    return render(request,'raise_request.html',context)