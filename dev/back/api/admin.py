from django.contrib import admin
from .models import Office, OfficeTypeSet

admin.site.register(Office)
admin.site.register(OfficeTypeSet)


admin.site.site_header = '介護労働安定センター | データ管理'
admin.site.index_title = 'モデルリスト'