from .settings import PORTAL_URL

def basic_proc(request):
    return {'PORTAL_URL' : PORTAL_URL}
