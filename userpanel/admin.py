from django.contrib import admin

# Register your models here.
from userpanel.models import *

admin.site.register(CustomDocumentUploadModel)
admin.site.register(ProfileDocumentModel)
admin.site.register(SubmitPreVerifiedQuestion)
admin.site.register(SubmitFileQuestion)
admin.site.register(SubmitTextQuestion)
admin.site.register(JobSubmitTextQuestion)
admin.site.register(JobSubmitPreVerifiedQuestion)
admin.site.register(JobSubmitFileQuestion)