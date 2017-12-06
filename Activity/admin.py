from django.contrib import admin
from .models import UcsmAddAcivity, StandaloneTestBedSetup, UcsmTestBedSetup, TestExecution, StandaloneTestBedSetupFinal, UcsmTestBedSetupFinal


# Register your models here.
admin.site.register(UcsmAddAcivity)
admin.site.register(StandaloneTestBedSetup)
admin.site.register(UcsmTestBedSetup)



class Final(admin.ModelAdmin):
    readonly_fields = ('event',)
admin.site.register(StandaloneTestBedSetupFinal, Final)
admin.site.register(UcsmTestBedSetupFinal, Final)
admin.site.register(TestExecution, Final)
