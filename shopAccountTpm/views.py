from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from shopAccountTpm.models import AccountExpenses,LabourExpenses
from shopAccountTpm.serializers import AccountExpensesSerializer,LabourExpensesSerializer
# Create your views here.
@csrf_exempt
def AccountApi(request, id=0):
    if(request.method=='GET'):
        if(id != 0):
            account=AccountExpenses.objects.get(id=id)
            account_serializer= AccountExpensesSerializer(account)
            return JsonResponse(account_serializer.data,safe=False)
        account= AccountExpenses.objects.all()
        account_serializer= AccountExpensesSerializer(account, many=True)
        return JsonResponse(account_serializer.data,safe=False)
    elif(request.method=='POST'):
        account_data= JSONParser().parse(request)
        account_serializer=AccountExpensesSerializer(data=account_data)
        if(account_serializer.is_valid()):
            account_serializer.save()
            return JsonResponse("ADDED SUCCESSFULLY!", safe=False)
        return JsonResponse("FAILED TO ADD", safe=False)

    elif(request.method=='PUT'):
        account_data= JSONParser().parse(request)
        account_model_data = AccountExpenses.objects.get(id=account_data['id'])
        account_serializer=AccountExpensesSerializer(account_model_data,data=account_data)
        if(account_serializer.is_valid()):
            account_serializer.save()
            return JsonResponse("UPDATED SUCCESSFULLY!", safe=False)
        return JsonResponse("FAILED TO UPDATE", safe=False)
    elif(request.method=='DELETE'):
        account=AccountExpenses.objects.get(id=id)
        account.delete()
        return JsonResponse("DELETED SUCCESSFULLY",safe=False)


@csrf_exempt
def LabourApi(request, id=0):
    # if(request.method=='GET'):
    #     if(id != 0):
    #         labour=LabourExpenses.objects.get(id=id)
    #         labour_serializer= LabourExpensesSerializer(labour)
    #         return JsonResponse(labour_serializer.data,safe=False)
    #     labour= LabourExpenses.objects.all()
    #     labour_serializer= LabourExpensesSerializer(labour, many=True)
    #     return JsonResponse(labour_serializer.data,safe=False)
    # elif(request.method=='POST'):
    #     labour_data= JSONParser().parse(request)
    #     labour_serializer=LabourExpensesSerializer(data=labour_data)
    #     if(labour_serializer.is_valid()):
    #         labour_serializer.save()
    #         return JsonResponse("ADDED SUCCESSFULLY!", safe=False)
    #     return JsonResponse("FAILED TO ADD", safe=False)

    # elif(request.method=='PUT'):
    #     labour_data= JSONParser().parse(request)
    #     labour_model_data = LabourExpenses.objects.get(id=labour_data['id'])
    #     labour_serializer=LabourExpensesSerializer(labour_model_data,data=labour_data)
    #     if(labour_serializer.is_valid()):
    #         labour_serializer.save()
    #         return JsonResponse("UPDATED SUCCESSFULLY!", safe=False)
    #     return JsonResponse("FAILED TO UPDATE", safe=False)
    # elif(request.method=='DELETE'):
    #     labour=LabourExpenses.objects.get(id=id)
    #     labour.delete()
    #     return JsonResponse("DELETED SUCCESSFULLY",safe=False)
    
    if(request.method=='GET'):
        if(id != 0):
            labour=LabourExpenses.objects.get(id=id)
            labour_serializer= LabourExpensesSerializer(labour)
            return JsonResponse(labour_serializer.data,safe=False)
        labour= LabourExpenses.objects.all()
        labour_serializer= LabourExpensesSerializer(labour, many=True)
        return JsonResponse(labour_serializer.data,safe=False)



    if(request.method=='GET'):
        labour= LabourExpenses.objects.all()
        labour_serializer= LabourExpensesSerializer(labour, many=True)
        return JsonResponse(labour_serializer.data,safe=False)
    elif(request.method=='POST'):
        labour_data= JSONParser().parse(request)
        labour_serializer=LabourExpensesSerializer(data=labour_data)
        if(labour_serializer.is_valid()):
            labour_serializer.save()
            return JsonResponse("ADDED SUCCESSFULLY!", safe=False)
        return JsonResponse("FAILED TO ADD", safe=False)

    elif(request.method=='PUT'):
        labour_data= JSONParser().parse(request)
        labour_model_data = LabourExpenses.objects.get(id=labour_data['id'])
        labour_serializer=LabourExpensesSerializer(labour_model_data,data=labour_data)
        if(labour_serializer.is_valid()):
            labour_serializer.save()
            return JsonResponse("UPDATED SUCCESSFULLY!", safe=False)
        return JsonResponse("FAILED TO UPDATE", safe=False)
    elif(request.method=='DELETE'):
        labour=LabourExpenses.objects.get(id=id)

        labour.delete()
        return JsonResponse("DELETED SUCCESSFULLY",safe=False)
    