import uuid
import os
import datetime

datetime.datetime.today().weekday()


filename = str(uuid.uuid4())


if 6 > datetime.datetime.today().weekday() > 0: 
    for i in random.randint(1, 15):
    	filename = str(uuid.uuid4())
    	with open(filename, 'w') as file:
        	file.write(filename)

    	os.system('git add *')
    	os.system('git commit -m {0}'.format(filename))
    	os.system('git push origin master')
