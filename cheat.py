import uuid
import os

filename = str(uuid.uuid4())

with open(filename, 'w') as file:
    file.write(filename)

os.system('git add *')
os.system('git commit -m {0}'.format(filename))
os.system('git push origin master')
