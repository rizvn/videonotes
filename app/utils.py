__author__ = 'riz'

def sec_to_time(sec):
    sec = int(sec)
    hrs = sec / 3600
    sec -= hrs * 3600
    mins = sec / 60
    sec -= mins * 60
    if hrs:
        hrs = pad(hrs)+':'
    else:
        hrs = ''
    return "%s%s:%s" % (hrs, pad(mins), pad(sec))

def pad(number):
    if number < 10:
        return '0%d' % (number,)
    else:
        return '%d' % (number,)

def jsonSerializer(obj):
    import datetime
    if isinstance(obj, datetime.datetime):
        return obj.strftime("%d/%m/%y")
    else:
        return ""

def generateRandomString():
    import random
    import string
    population = string.ascii_letters + string.digits
    return random.sample(population, 10)

def encrypt(value):
    import hashlib
    salt = 'da9429c7d22at4d0'
    return hashlib.md5(salt + value).hexdigest()
