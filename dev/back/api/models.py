from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


#事業所種別一覧
class OfficeTypeSet(models.Model):
    elem = models.CharField(verbose_name="事業所種別", max_length=32)
    class Meta:
        verbose_name="事業所種別"
        verbose_name_plural = "事業所種別一覧"
    def __str__(self):
        return self.elem

#支援状況一覧
class SupportStatusSet(models.Model):
    elem = models.CharField(verbose_name="支援状況", max_length=32)
    class Meta:
        verbose_name="支援状況"
        verbose_name_plural = "支援状況一覧"
    def __str__(self):
        return self.elem

#支援・受講方法一覧
class SupportApproachSet(models.Model):
    elem = models.CharField(verbose_name="支援・受講方法", max_length=32)
    class Meta:
        verbose_name="支援・受講方法"
        verbose_name_plural = "支援・受講方法一覧"
    def __str__(self):
        return self.elem
        
#支援テーマ一覧
class SupportThemeSet(models.Model):
    elem = models.CharField(verbose_name="支援テーマ", max_length=32)
    class Meta:
        verbose_name="支援テーマ"
        verbose_name_plural = "支援テーマ一覧"
    def __str__(self):
        return self.elem


#事業所一覧
class Office(models.Model):
    class Meta:
        verbose_name = "事業所"
        verbose_name_plural = "事業所一覧"
    id = models.CharField(verbose_name="識別子", help_text = "介護保険事業所番号_介護サービス分類コード　の半角文字列で構成されます。", max_length=32)   
    care_office_code = models.CharField(verbose_name="介護保険事業所番号", max_length=32, primary_key=True)
    name = models.CharField(verbose_name="事業所名", max_length=64)
    care_service_code = models.CharField(verbose_name="介護サービス分類コード", max_length=16)
    postal_code = models.CharField(verbose_name="郵便番号", max_length=16, null=True)
    address = models.CharField(verbose_name="事業所所在地", max_length=64, null=True)
    phone = models.CharField(verbose_name="電話番号", max_length=16, null=True)
    fax = models.CharField(verbose_name="FAX番号", max_length=16, null=True)
    town_code = models.CharField(verbose_name="事業所所在地の市区町村番号", max_length=16, null=True)
    longitude = models.IntegerField(verbose_name="経度", validators=[MinValueValidator(-180), MaxValueValidator(180)], null=True)
    latitude = models.IntegerField(verbose_name="緯度", validators=[MinValueValidator(-180), MaxValueValidator(180)], null=True)
    type = models.ForeignKey("OfficeTypeSet", verbose_name="法人種別", on_delete=models.SET_NULL, null=True)
    company = models.CharField(verbose_name="所属法人名", max_length=64)
    owner = models.CharField(verbose_name="経営者氏名", max_length=32, null=True)
    manager = models.CharField(verbose_name="責任者氏名", max_length=32, null=True)
    capacity_of_guests = models.IntegerField(verbose_name="定員", null=True)
    url = models.CharField(verbose_name="URL", max_length=64, null=True)
    foundation_date = models.DateField(verbose_name="設立年月日", null=True)
    number_of_employees = models.IntegerField(verbose_name="従業員人数", null=True)
    def __str__(self):
        return self.name


# #支援情報一覧
# class SupportInfo(models.Model):
#     class Meta:
#         verbose_name = "支援情報"
#         verbose_name_plural = "支援情報一覧"
#     #支援対象区分を法人毎と定義している（同一法人他事業所も同一視している）
#     company = models.OneToOneField("Office", db_column="company", verbose_name="支援事業所法人名", on_delete=models.SET_NULL, null=True)
#     application_date = models.DateField(verbose_name="申込日", null=True)
#     visit_date = models.DateField(verbose_name="訪問日", null=True)
#     begin_implementation_datetime = models.DateTimeField(verbose_name="実施開始日時", null=True)
#     end_implementation_datetime = models.DateTimeField(verbose_name="実施終了日時", null=True)
#     support_status = models.ForeignKey("SupportStatusSet", verbose_name="支援状況", on_delete=models.SET_NULL, null=True)
#     support_approach = models.ForeignKey("SupportApproachSet", verbose_name="支援・受講方法", on_delete=models.SET_NULL, null=True)
#     support_theme = models.ForeignKey("SupportThemeSet", verbose_name="支援テーマ", on_delete=models.SET_NULL, null=True)
#     support_toolstatus = models.ForeignKey("SupportStatusSet", verbose_name="支援状況", on_delete=models.SET_NULL, null=True)
#     # support_status = models.ForeignKey("SupportStatusSet", verbose_name="支援状況", on_delete=models.SET_NULL, null=True)
#     def __str__(self):
#         return self.name


# #支援情報一覧
# class SupportInfo(models.Model):
#     class Meta:
#         verbose_name = "支援情報"
#         verbose_name_plural = "支援情報一覧"
#     def __str__(self):
#         return self.name
