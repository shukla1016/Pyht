def add_time(st,d,day=' '):
    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    lst=st.split(' ')
    lst1=lst[0].split(':')
    lst2=d.split(':')
    tm= lst[1].upper()
    if tm=='P.M.':
        h=int(lst1[0]) +12
    elif tm =='A.M.':
        h=int(lst1[0])
    else:
        print('Enter time in correct format (HH:MM A.M./P.M.)')
    h= h+ int(lst2[0])
    d1=int(h/24)
    if(h>24):
       h= h%24
    m= int(lst1[1])+int(lst2[1])
    if(m>60):
        h=h+1
        m=m%60
    if(d1==0):
        if (h<12):
            print(h,':',m," A.M.")
        else:
            h=h-12
            print(h,':',m," P.M.")
    if(d1==1):
        if (h<12):
            print(h,':',m," A.M. (next day)")
        else:
            h=h-12
            print(h,':',m," P.M. (next day)")
    if(d1>1):
        if (h<12):
            print(h,':',m," A.M. (",d1,' days later)')
        else:
            h=h-12
            print(h,':',m," P.M. (",d1,' days later)')
    for i in days:
        if(i==(day.lower())):
            r=days.index(i)
            r=r+d1
            while r>7:
                r=r%7
            print(days[r])
st=input("Enter starting time.")
d=input("Enter time duration.")
day=input("Enter starting day else press any key and enter.")
add_time(st,d,day)