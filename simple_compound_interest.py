def simple(principle,rate,time):
    si = (principle * rate * time)/100
    return si

def compound(principle,rate,time):
    ci = principle * ((1 + (rate/100))**time) -  principle
    return ci

principle,rate,time = (int(x) for x in input().split(' '))

print(simple(principle,rate,time))
print(compound(principle,rate,time))