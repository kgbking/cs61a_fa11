def make_rat(num, den):
    return (num, den)

def num(rat):
    return rat[0]

def den(rat):
    return rat[1]

def mul_rat(a, b):
    new_num = num(a) * num(b)
    new_den = den(a) * den(b)
    return make_rat(new_num, new_den)

def str_rat(x):  #from lecture notes
       """Return a string 'n/d' for numerator n and denominator d."""
       return '{0}/{1}'.format(num(x), den(x))
    
def div_rat(a, b):
    new_num = num(a) * den(b)
    new_den = den(a) * num(b)
    return make_rat(new_num, new_den)

def make_point(x,y):
    return (x,y)

def x_point(point):
    return point[0]

def y_point(point):
    return point[1]

def make_segment(start,end):
    return (start,end)

def start_segment(segment):
    return segment[0]

def end_segment(segment):
    return segment[1]

def midpoint_segment(segment):
    start,end=start_segment(segment),end_segment(segment)
    return make_point((x_point(start)+x_point(end))/2,(y_point(start)+y_point(end))/2)

def make_pair(x, y):
    """Return a function that behaves like a pair."""
    def dispatch(m):
        assert (m==0) or(m==1) or (m=='pair'), 'Message not recognized'
        if m == 0:
            return x
        if m == 1:
            return y
        if m=='pair':
            return (x,y)   
    return dispatch
    
def make_rectangle(point0,point1,point2,point3):
    """start0=start_segment(segment0)
    end0=end_segment(segment0)
    start1=start_segment(segment1)
    end1=end_segment(segment1)
    a=(start0==start1)
    b=(start0==end1)
    c=(end0==start1)
    d=(end0==end1)
    assert a or b or c or d, 'Segements should be connected end to end.'
    """
    #basepoint=point0
    line10=pow((pow(point1[0]-point0[0],2)+pow(point1[1]-point0[1],2)),0.5)
    line20=pow((pow(point2[0]-point0[0],2)+pow(point2[1]-point0[1],2)),0.5)
    line30=pow((pow(point3[0]-point0[0],2)+pow(point3[1]-point0[1],2)),0.5)
    m=max(line10,line20,line30)
    if m==line10:
        temp=point1
        point1=point2
        point2=temp
    if m==line30:
        temp=point3
        point3=point2
        point2=temp
    vector01=(x_point(point0)-x_point(point1),y_point(point0)-y_point(point1))
    vector12=(x_point(point1)-x_point(point2),y_point(point1)-y_point(point2))
    vector23=(x_point(point2)-x_point(point3),y_point(point2)-y_point(point3))
    vector30=(x_point(point3)-x_point(point0),y_point(point3)-y_point(point0))
    a=vector01[0]*vector12[0]+vector01[1]*vector12[1]
    b=vector12[0]*vector23[0]+vector12[1]*vector23[1]
    c=vector23[0]*vector30[0]+vector23[1]*vector30[1]
    assert a==0 and b==0 and c==0, 'Segements should be perpendicular to each other.'

    return (point0,point1,point2,point3)

def perimeter_rectangle(rectangle):
    line10=pow((pow(rectangle[1][0]-rectangle[0][0],2)+pow(rectangle[1][1]-rectangle[0][1],2)),0.5)
    line21=pow((pow(rectangle[2][0]-rectangle[1][0],2)+pow(rectangle[2][1]-rectangle[1][1],2)),0.5)
    return 2*(line10+line21)

def area_rectangle(rectangle):
    line10=pow((pow(rectangle[1][0]-rectangle[0][0],2)+pow(rectangle[1][1]-rectangle[0][1],2)),0.5)
    line21=pow((pow(rectangle[2][0]-rectangle[1][0],2)+pow(rectangle[2][1]-rectangle[1][1],2)),0.5)
    return line10*line21








    
