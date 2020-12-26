class shape():
    def __init__(self, area):
        self.area = area

    def __add__(self, p):
        return shape(self.area+p.area)

    def __gt__(self, p):
        return self.area > p.area

    def __ge__(self, p):
        return self.area >= p.area

    def __ie__(self, p):
        return self.area == p.area

    def __lt__(self, p):
        return self.area < p.area

    def __le__(self, p):
        return self.area <= p.area

    def __str__(self):
        return str(self.area)


class triangle(shape):
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def perimeter(self):
        return self.a+self.b+self.c

    def area(self):
        s = (self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**(1/2)


class rect(shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return (2*(self.a+self.b))

    def area(self):
        return self.a*self.b


class circle(shape):
    def __init__(self, r):
        self.rad = r

    def perimeter(self):
        return 2*(22/7)*self.rad

    def area(self):
        return (22/7)*(self.rad**2)


class cylinder(shape):
    def __init__(self, r, h):
        self.rad = r
        self.h = h

    def perimeter(self):
        return 2*(22/7)*self.rad*self.h

    def area(self):
        return (22/7)*(self.rad**2)*self.h


if __name__ == '__main__':
    r0 = int(input("No. of items to calc. perimeter or area: "))
    
    ta = 0
    ra = 0
    cia = 0
    cya = 0
    tp = 0
    rp = 0
    cip = 0
    cyp = 0
    
    for i in range(r0):
        print("Enter 1 for triangle,2 for square or rectangle,3 for circle,4 for cylinder")
        x = int(input("Enter a number 1 to 4: "))

        if(x == 1):
            # the item is triangle
            a1 = int(input("side 1: "))
            a2 = int(input("side 2: "))
            a3 = int(input("side 3: "))
            m = triangle(a1, a2, a3)
            z = input("area(Y) or perimeter(N): ")
            if(z == 'Y' or z == 'y'):
                ta = m.area()
            elif(z == 'N' or z == 'n'):
                tp = m.perimeter()

        if(x == 2):
            # the item is square or rectangle
            b1 = int(input("Side 1: "))
            b2 = int(input("Side 2: "))
            n = rect(b1, b2)
            z = input("area(Y) or perimeter(N): ")
            if(z == 'Y' or z == 'y'):
                ra = n.area()
            elif(z == 'N' or z == 'n'):
                rp = n.perimeter()

        if(x == 3):
            # the item is circle
            r = int(input("Enter the radius: "))
            o = circle(r)
            z = input("area(Y) or perimeter(N): ")
            if(z == 'Y' or z == 'y'):
                cia = o.area()
            elif(z == 'N' or z == 'n'):
                cip = o.perimeter()

        if(x == 4):
            # the item is cylinder
            r = int(input("Enter the radius: "))
            h = int(input("Enter the height: "))
            p = cylinder(r, h)
            z = input("area(Y) or perimeter(N): ")
            if(z == 'Y' or z == 'y'):
                cya = p.area()
            elif(z == 'N' or z == 'n'):
                cyp = p.perimeter()
    x=shape(ta)+shape(ra)+shape(cia)+shape(cya)
    
    print(x)
    
    