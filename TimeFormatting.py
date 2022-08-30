'''
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
'''

def format_duration(seconds):
    
    time = []
    form = []
    out = ''
    #1, 60, 3600, 86400, 31536000
    
    time.append(seconds // 31536000)
    seconds -= time[0] * 31536000
    time.append(seconds // 86400)
    seconds -= time[1] * 86400
    time.append(seconds // 3600)
    seconds -= time[2] * 3600
    time.append(seconds // 60)
    seconds -= time[3] * 60
    time.append(seconds // 1)
    seconds -= time[4] * 1
    
    if time[0] > 0:
        out += f'{time[0]} year'
        if time[0] > 1:
            out += 's'
        form.append(out)
        out = ''
    
    if time[1] > 0:
        out += f'{time[1]} day'
        if time[1] > 1:
            out += 's'
        form.append(out)
        out = ''
    
    if time[2] > 0:
        out += f'{time[2]} hour'
        if time[2] > 1:
            out += 's'
        form.append(out)
        out = ''
    
    if time[3] > 0:
        out += f'{time[3]} minute'
        if time[3] > 1:
            out += 's'
        form.append(out)
        out = ''
    
    if time[4] > 0:
        out += f'{time[4]} second'
        if time[4] > 1:
            out += 's'
        form.append(out)
        out = ''
    
    if len(form) == 0:
        return 'now'
    if len(form) == 1:
        return form[0]
    
    forml = [', '.join(form[:-1])]    
    forml.append(form[-1])   
    return ' and '.join(forml)