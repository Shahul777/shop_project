from dataclasses import fields
from rest_framework import serializers
from shopAccountKdm.models import AccountExpenses,LabourExpenses,RateSheet

class AccountExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountExpenses
        fields=(   'id', 'Date' ,'Day','isSunday','isHoliday','BlackMachineReading1',
        'BlackMachineReading2','ColourMachineReading1','ColourMachineReading2',

    'BlackCopies' ,
    'ColourCopies' ,
    'B2bCopies' ,
    'PaperPresentToday' ,
  'PaperSheet',
  'Toner',
  'TonerSpent',

    'PaperSoldToday', 
    'Bindings' ,
    'Expenses' ,
      'TodayStayDetail',
    'PastStayDetail',
    'PastSoldDetail',
        'isPaperCame',
        'PaperQuantityCame',
        'isPaperSent',
        'PaperQuantitySent',
    'isTonerCame',
    'isTonerSent',
    'TonerQuantityCame',
    'TonerQuantitySent',
'isItemsCame',
'ItemsInfo',
    'TodayStayingCopies',
    'TodayStayingMoney',
    'OldStayingMoney',
    'OldStayingCopies',
    'GoneCopiesPast',
    'GoneMoneyPast',
    'NotesToday',
    'CashIncome',
    'PaytmIncome',
    'TotalIncome' ,
    'OpeningBalance' ,
    'NetProfit',
    'GetTime')
class LabourExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabourExpenses
        fields =('id','Date','Day','GetTime',
        'TajPresent',
        'TajExpense',
        'NoorPresent',
        'NoorExpense',
        'isTajHalfDay',
        'isNoorHalfDay')
class RateSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model=RateSheet
        fields=('bata1','bata2','food','tajSalary',
        'noorSalary',
        'assanSalary',
        'maniSalary',
        'rasheedSalary',
        'paperRate',
        'tonerRate',
        'singleRate',
        'b2bRate',
        'copiesPerToner',
        'tpmRent',
        'kdmRent',
        'currentBillKdm',
        'currentBillTpm',
        )

           