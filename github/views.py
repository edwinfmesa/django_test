from django.http import HttpResponse
from django.conf import settings

import commands
import os

# hace git pull 
def update(solicitud):
    os.chdir(os.path.dirname(os.path.dirname(__file__)))

    gitpull = commands.getstatusoutput('git pull')[1]

    return HttpResponse(gitpull)