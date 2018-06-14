from django.contrib import admin
from IPTVStopSystem.models import IPTVProgram
from IPTVStopSystem.models import IPTVEPG
from IPTVStopSystem.models import IPTVCDNOperationLog
from IPTVStopSystem.models import IPTVCDNNode
from IPTVStopSystem.models import IPTVAuthCode
from IPTVStopSystem.models import IPTVProgramOperationLog

admin.site.register(IPTVProgram)
admin.site.register(IPTVEPG)
admin.site.register(IPTVCDNOperationLog)
admin.site.register(IPTVCDNNode)
admin.site.register(IPTVAuthCode)
admin.site.register(IPTVProgramOperationLog)