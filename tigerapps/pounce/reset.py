# Resets Pounce for a new semester.

# HEY: YOU MUST ALSO KILL -9 THE CURRENTLY RUNNING
# UPDATE PROCESSES!

import sys,os
sys.path.insert(0,os.path.abspath("/srv/tigerapps"))
import settings
from django.core.management import setup_environ
setup_environ(settings)

from pounce.models import *

for subscription in Subscription.objects.all():
	subscription.delete()
	
for theclass in Class.objects.all():
	theclass.delete()
	
for course in Course.objects.all():
	course.delete()
	
for entry in Entry.objects.all():
	entry.delete()
	
CoursesList.objects.all()[0].delete()
