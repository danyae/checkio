import math

def checkio(coords):
    (x1,y1),(x2,y2),(x3,y3)=eval(coords)
    
    A = x2 - x1
    B = y2 - y1
    C = x3 - x1
    D = y3 - y1
    E = A * (x1 + x2) + B * (y1 + y2)
    F = C * (x1 + x3) + D * (y1 + y3)
    G = 2 * (A * (y3 - y2) - B * (x3 - x2))
    xc = (D * E - B * F) / G
    yc = (A * F - C * E) / G
    r = math.sqrt(math.pow((x1 - xc), 2) + math.pow((y1 - yc), 2))
    
    xc = round(xc, 2)
    if (xc).is_integer():
        xc = int(xc)
    
    yc = round(yc, 2)   
    if (yc).is_integer():
        yc = int(yc)
    
    r = round(r, 2)  
    if (r).is_integer():
        r = int(r)
        
    part1 = ''
    part2 = ''
    if xc > 0:
        part1 = '(x-{0})^2+'.format(xc)
    else:
        part1 = '(x{0})^2+'.format(xc)
    if yc > 0:
        part2 = '(y-{0})^2={1}^2'.format(yc, r)
    else:
        part2 = '(y{0})^2={1}^2'.format(yc, r)
    return part1 + part2

if __name__ == "__main__":
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
    assert checkio("(7,3),(9,6),(3,6)") == "(x-6)^2+(y-5.83)^2=3^2"