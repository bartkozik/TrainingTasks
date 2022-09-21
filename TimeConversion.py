def timeConversion(s):
    if s[8:] == 'PM':
        if int(s[:2]) != 12:
            hour = int(s[:2])+12
            rest = s[2:].strip('PM')
            return "{}{}".format(hour,rest)
        return s.strip('PM')
    elif s[8:] == 'AM' and int(s[:2]) != 12:
        return s.strip('AM')
    else:
        return "00:{}".format(s[3:8])