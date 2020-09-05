import copy
import random
class Hat:
    def __init__(self,red=0,yellow=0,blue=0,green=0,orange=0,black=0,pink=0,stripped=0):
        if (red==0 and yellow==0 and blue==0 and green==0 and orange==0 and black==0 and pink==0 and stripped==0):
            print('hat cannot be empty')
            exit()
        s=red*' red'+yellow*' yellow'+ ' blue'*blue+ ' green'*green+' orange'*orange+' black'*black+' pink'*pink+' stripped '*stripped
        self.contents=s.split(' ')
        for i in self.contents:
            if i=='':
                self.contents.remove(i)
    def draw(self,n):
        if n>=len(self.contents):
            return self.contents
        else:
            self.pick=list()
            for i in range(n): 
                st=random.choice(self.contents)
                self.pick.append(st)
                self.contents.remove(st)
            return self.pick
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    hat1=hat.contents.copy()
    v=list(expected_balls.values())
    k=list(expected_balls.keys())
    s=list()
    for i in range(len(v)):
        for j in range(int(v[i])):
            s.append(k[i])
    bd=hat.draw(num_balls_drawn)
    M=0
    for i in range(num_experiments):
        te=0
        for i in range(len(s)):
            for j in range(len(bd)):
                if s[i]==bd[j]:
                    te+=1
                    bd.remove(bd[j])
                    break
        if(te==len(s)):
            M+=1
    p=M/num_experiments
    print(p) 
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)