global pos1
global pos2
global a
pos1=150
pos2=300
lista=[color(1,156,156), color(155,0,155), color(255,0,0), color(122,55,85),color(0,255,22), color(0,0,255)]
def setup():
    size(400,400)
def draw():
    losowykolor=int(random(6))
    background(0)
    global pos1
    global pos2
    square(pos1,pos2,100)
    pos1+=1
    pos2-=1
    fill(lista[losowykolor])
    if pos2==150:
        noLoop()
