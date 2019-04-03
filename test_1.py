__author__ = 'terry'

import random
phone_title = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187','188',
           '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
phone_str = '0123456789'
a=[]
b=''
phone = random.choice(phone_title)
for i in range(8):
    a.append(random.choice(phone_str))
    print(a)
    b=''.join(a)
    print(b)