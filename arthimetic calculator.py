def arthimetic_arranger(lst,mod='False'):
    if len(lst)>5 or len(lst)<1:
        print("**********Too many Problems*************")
        exit()
    for i in lst:
        lst1=list(i.split(" "))
        n=lst1[0]
        o=lst1[1] 
        d=lst1[2]
        if(len(n)>4 or len(d)>4):
            print("***********Numbers cannot be more than 4 digits************")
        if not n.isnumeric() or not d.isnumeric():
            print("**********Only Digits are allowed*********")
            exit()
        if o=='+':
            ans= int(n)+int(d)
        elif o=='-':
            ans= int(n)-int(d)
        else:
            print('**************only + and - are allowed***********')
            exit()
        if mod.upper()=='TRUE':
            print('  ',n,'\n',o,d,'\n-----','\n',ans)
        else:
            print('  ',n,'\n',o,d,'\n-----')
str1=input("Enter Arthimetic Expressions seperated by space bar.")
lst=list(str1.split(','))
m=input('Write true if you want answer else press any other key and press enter.')
arthimetic_arranger(lst,m)
