from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


#事業所種別
class OfficeTypeSet(models.Model):
    elem = models.CharField(max_length=32)
    class Meta:
        verbose_name_plural = "事業所種別"

    def __str__(self):
        return self.elem


#事業所
class Office(models.Model):
    class Meta:
        verbose_name_plural = "事業所"
    id = models.CharField(verbose_name="識別子(事業所番号＠分類コード)", max_length=32)   
    code = models.CharField(verbose_name="介護保険事業所番号", max_length=32, primary_key=True)
    name = models.CharField(verbose_name="事業所名", max_length=64)
    service_code = models.CharField(verbose_name="介護サービス分類コード", max_length=16)
    postal_code = models.CharField(verbose_name="郵便番号", max_length=16)
    address = models.CharField(verbose_name="事業所所在地", max_length=64)
    phone_number = models.CharField(verbose_name="電話番号", max_length=16)
    fax_number = models.CharField(verbose_name="FAX番号", max_length=16)
    town_code = models.CharField(verbose_name="事業所所在地の市区町村番号", max_length=16)
    longitude = models.IntegerField(verbose_name="経度", validators=[MinValueValidator(-180), MaxValueValidator(180)])
    latitude = models.IntegerField(verbose_name="緯度", validators=[MinValueValidator(-180), MaxValueValidator(180)])
    type = models.ForeignKey('OfficeTypeSet', verbose_name="法人種別", on_delete=models.SET_NULL, null=True)
    company_name = models.CharField(verbose_name="所属法人名", max_length=64)
    owner = models.CharField(verbose_name="経営者氏名", max_length=32, null=True)
    manager = models.CharField(verbose_name="責任者氏名", max_length=32, null=True)
    capacity_employment = models.IntegerField(verbose_name="定員")
    url = models.CharField(verbose_name="URL", max_length=64)


    def __str__(self):
        return self.name
