
from rest_framework import serializers
from shopAccountTpm.models import AccountExpenses,LabourExpenses

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
    'Bindings' ,
    'Expenses' ,
    'TodayStayDetail',
    'PastStayDetail',
    'PastSoldDetail',
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
        'AssanPresent',
        'AssanExpense',
        'RasheedPresent',
        'RasheedExpense',
        'ManiPresent',
        'ManiExpense',
        'isRasheedHalfDay',
        'isAssanHalfDay',
        'isManiHalfDay')