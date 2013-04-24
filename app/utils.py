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


if __name__=='__main__':
    print sec_to_time(18000)