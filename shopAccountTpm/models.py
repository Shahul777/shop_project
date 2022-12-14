from ssl import Options
from django.db import models

# Create your models here.
class AccountExpenses(models.Model):
    id =models.AutoField(primary_key=True)
    Date = models.DateField()
    Day =models.CharField(max_length=20,default="MON")
    isSunday = models.IntegerField(default=0)
    isHoliday = models.IntegerField(default=0)
    isPaperCame= models.IntegerField(default=0)
    PaperQuantityCame = models.IntegerField(default=0)
    isPaperSent= models.IntegerField(default=0)
    
    PaperQuantitySent= models.IntegerField(default=0)
    isTonerCame= models.IntegerField(default=0)
    isTonerSent = models.IntegerField(default=0)
    TonerQuantityCame = models.IntegerField(default=0)
    TonerQuantitySent= models.IntegerField(default=0)
    isItemsCame =models.IntegerField(default=0)
    ItemsInfo = models.CharField(max_length=200,default="")


    BlackMachineReading1 = models.IntegerField(default=0)
    BlackMachineReading2 = models.IntegerField(default=0)
    ColourMachineReading1= models.IntegerField(default=0)
    ColourMachineReading2= models.IntegerField(default=0)
    BlackCopies = models.IntegerField()
    ColourCopies = models.IntegerField()
    B2bCopies = models.IntegerField()
    PaperPresentToday = models.IntegerField(default=0)
    # PaperYesterday = models.DecimalField(max_digits=9 , decimal_places=3)
    PaperSoldToday =models.IntegerField(default=0)
    PaperSheet = models.IntegerField(default=0)
    Toner  = models.IntegerField(default=0)
    TonerSpent= models.IntegerField(default=0)
    Bindings = models.IntegerField()
    Expenses = models.IntegerField()
    TodayStayDetail = models.CharField(max_length=200,default="")
    PastStayDetail= models.CharField(max_length=200,default="")
    PastSoldDetail = models.CharField(max_length=200,default="")
    TodayStayingCopies= models.IntegerField()
    TodayStayingMoney= models.IntegerField()
    OldStayingMoney =models.IntegerField(default=0)
    OldStayingCopies=models.IntegerField(default=0)
    GoneCopiesPast= models.IntegerField()
    GoneMoneyPast= models.IntegerField()
    NotesToday= models.CharField(max_length=200)
    CashIncome= models.IntegerField()
    PaytmIncome= models.IntegerField()
    TotalIncome = models.IntegerField()
    OpeningBalance = models.IntegerField()
    NetProfit= models.IntegerField(default=1)
    GetTime=models.IntegerField(default=1)

class LabourExpenses(models.Model):
    id =models.AutoField(primary_key=True)
    Date = models.DateField()
    Day =models.CharField(max_length=10,default="MON")
    GetTime=models.IntegerField(default=1)
    AssanPresent = models.IntegerField()
    AssanExpense = models.IntegerField()
    RasheedPresent = models.IntegerField()
    RasheedExpense = models.IntegerField()
    ManiPresent = models.IntegerField()
    ManiExpense = models.IntegerField()
    isRasheedHalfDay =models.IntegerField(default=0)
    isAssanHalfDay=models.IntegerField(default=0)
    isManiHalfDay=models.IntegerField(default=0)
