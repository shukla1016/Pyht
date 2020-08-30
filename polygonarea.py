class rectangle:
    def __init__(self,w,h):
        self.width= w
        self.height= h
    def set_width(self,w):
        self.width=w
    def set_height(self,h):
        self.height=h
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return (2*(self.height+self.width))
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def get_picture(self):
        if(self.width>50 or self.height>50):
            print("Too big for picture.")
            exit()
        else:
           for i in range(self.height):
                for j in range(self.width):
                    print('*', end='')
                print(' ')
    def get_amount_inside(self,ob):
        a= self.width*self.height
        a1=ob.width*ob.height
        n=int(a/a1)
        return n
    def __str__(self):
            return f'Rectangle(width={self.width} , height={self.height})'

class square(rectangle):
    def __init__(self,s):
        self.width=s
        self.height=s
    def set_side(self,s):
        self.width = s
        self.height=s
    def __str__(self):
        return f'Square(width={self.width})'
rect = rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
rect.get_picture()
 
sq = square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
sq.get_picture()
 
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

