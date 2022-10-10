from django.db import models

# Create your models here.
class AccountExpenses(models.Model):
    id =models.AutoField(primary_key=True)
    Date = models.DateField()
    Day =models.CharField(max_length=20,default="MON")
    Toner= models.IntegerField(default=0)
    TonerSpent= models.IntegerField(default=0)


    isSunday = models.IntegerField(default=0)
    isHoliday = models.IntegerField(default=0)
    isPaperCame= models.IntegerField(default=0)
    PaperQuantityCame= models.IntegerField(default=0)
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
    PaperSheet = models.IntegerField(default=0)
    PaperPresentToday =models.IntegerField(default=0)
    # PaperYesterday = models.DecimalField(max_digits=9 , decimal_places=3)
    PaperSoldToday =models.IntegerField(default=0)
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
    TajPresent = models.IntegerField()
    TajExpense = models.IntegerField()
    NoorPresent = models.IntegerField()
    NoorExpense = models.IntegerField()

    isTajHalfDay = models.IntegerField(default=0)
    isNoorHalfDay = models.IntegerField(default=0)
class RateSheet(models.Model):
    bata1 = models.IntegerField(default=90)
    bata2 = models.IntegerField(default=70)
    food= models.IntegerField(default=150)
    tajSalary = models.DecimalField(default=633.33,max_digits=9 , decimal_places=2)
    noorSalary = models.DecimalField(default=466.66,max_digits=9 , decimal_places=2)
    assanSalary = models.DecimalField(default=466.66,max_digits=9 , decimal_places=2)
    maniSalary = models.DecimalField(default=333.33,max_digits=9 , decimal_places=2)
    rasheedSalary = models.DecimalField(default=333.33,max_digits=9 , decimal_places=2)
    paperRate = models.DecimalField(default=0.50,max_digits=9 , decimal_places=2)
    tonerRate= models.DecimalField(default=800.00,max_digits=9 , decimal_places=2)
    singleRate= models.DecimalField(default=1.25,max_digits=9 , decimal_places=2)
    b2bRate= models.DecimalField(default=0.85,max_digits=9 , decimal_places=2)
    copiesPerToner = models.IntegerField(default=19000)

    tpmRent = models.DecimalField(default=516.66,max_digits=9 , decimal_places=2)
    kdmRent = models.DecimalField(default=800.00,max_digits=9 , decimal_places=2)

    currentBillKdm= models.IntegerField(default=110)
    currentBillTpm = models.IntegerField(default=110)
