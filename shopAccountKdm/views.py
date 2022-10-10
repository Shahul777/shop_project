from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from shopAccountKdm.models import AccountExpenses,LabourExpenses,RateSheet
from shopAccountKdm.serializers import AccountExpensesSerializer,LabourExpensesSerializer,RateSheetSerializer
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

    #     if(id != 0):
    #         account=AccountExpenses.objects.get(id=id)
    #         account_serializer= AccountExpensesSerializer(account, many=True)
    #         return JsonResponse(account_serializer.data,safe=False)
    #     else:
        
 
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

@csrf_exempt
def RateApi(request, id=0):
    if(request.method=='GET'):
        rate= RateSheet.objects.all()
        rate_serializer= RateSheetSerializer(rate, many=True)
        return JsonResponse(rate_serializer.data,safe=False)
    elif(request.method=='POST'):
        rate_data= JSONParser().parse(request)
        rate_serializer=RateSheetSerializer(data=rate_data)
        if(rate_serializer.is_valid()):
            rate_serializer.save()
            return JsonResponse("ADDED SUCCESSFULLY!", safe=False)
        return JsonResponse("FAILED TO ADD", safe=False)

    elif(request.method=='PUT'):
        rate_data= JSONParser().parse(request)
        rate_model_data = RateSheet.objects.get(id=rate_data['id'])
        rate_serializer=RateSheetSerializer(rate_model_data,data=rate_data)
        if(rate_serializer.is_valid()):
            rate_serializer.save()
            return JsonResponse("UPDATED SUCCESSFULLY!", safe=False)
        return JsonResponse("FAILED TO UPDATE", safe=False)
    elif(request.method=='DELETE'):
        rate=RateSheet.objects.get(id=id)

        rate.delete()
        return JsonResponse("DELETED SUCCESSFULLY",safe=False)
