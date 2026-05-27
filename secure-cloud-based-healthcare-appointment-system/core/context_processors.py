from django.conf import settings

def project_settings(request):
    return {
        "CURRENCY_SYMBOL": getattr(settings, "CURRENCY_SYMBOL", "₦"),
        "PROJECT_NAME": getattr(settings, "PROJECT_NAME", "DocBook"),
    }
