"""tile.py: 铺砖
__author__ = "Zhangyinuo"
__pkuid__  = "1800011770"
__email__  = "1800011770@pku.edu.cn"
"""
def determine(x, wall, a, b, m, n):
    """判断砖可否铺好
    """
    if m-(x%m)>= a and n-(x//m) >= b:
        h = True
        for i in range(1, a):
            h = h and wall[x+i]
    else:
        h = False
    return h

def pu(x, m, a, b, wall, way):
    """铺上一块砖
    """
    wy = way
    wl = wall
    tup = []
    for i in range(a):
        for j in range(b):
            x_ = x+i+j*m
            wl[x_] = False
            tup.append(x_)
    wy.append(tuple(tup))
    return (wy, wl)

def pucizhuan(s, wall, a, b, m, n, mn, way):
    """铺瓷砖
    """
    for x in range(s, mn):
        if wall[x]:
            if determine(x, wall, a, b, m, n):
                wy, wl = pu(x, m, a, b, wall, way)
                pucizhuan(x+a, wl, a, b, m, n, mn, wy)

            if determine(x, wall, b, a, m, n):
                wy, wl = pu(x, m, b, a, wall, way)
                pucizhuan(x+b, wl, a, b, m, n, mn, wy)
            return
    global tile
    tile.append(way)

def pucizhuan_(s, wall, a, m, n, mn, way):
    """如果是正方形，铺瓷砖
    """
    for x in range(s, mn):
        if wall[x]:
            if determine(x, wall, a, a, m, n):
                wy, wl = pu(x, m, a, a, wall, way)
                pucizhuan_(x+a, wl, a, m, n, mn, wy)
            return
    global tile
    tile.append(way)

def tat(m, t, i0, i_1):
    """画墙
    """
    t.pu()
    t.goto(i0 % m*20, i0//m*20)
    t.pd()
    t.goto(i_1 % m*20+20, i0//m*20)
    t.goto(i_1 % m*20+20, i_1//m*20+20)
    t.goto(i0 % m*20, i_1//m*20+20)
    t.goto(i0 % m*20, i0//m*20)

def tur(m, p, mn):
    """画砖铺过的墙
    """
    import turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    global tile
    for i in tile[p]:
        tat(m, t, i[0], i[-1])
    turtle.done()

def tile_(m, n, a, b):
    """开始铺砖
    """
    mn = m*n
    if (mn) % (a*b) == 0 and max(m, n) >= max(a, b) and min(m, n) >= min(a, b):
        wall = []
        for y in range(mn):
            wall.append(True)
        if a != b:
            pucizhuan(0, wall, a, b, m, n, mn, [])
        else:
            pucizhuan_(0, wall, a, m, n, mn, [])

def output(m, n, a, b):
    """结果输出
    """
    mn = int(m*n/a/b)

    global tile
    long = len(tile)

    if long == 0:
        print('无法铺满')
    elif long == 1:
        print('这仅有一种方法：')
        print(tile[0])
        tur(m, 0, mn)
    else:
        print('这有', long, '种方法')
        for p in range(long):
            print(p, ' : ', tile[p])
        p = int(input('选择一个号码'))
        tur(m, p, mn)

def main():
    """主函数
    """
    m=int(input('墙的长度:'))
    n=int(input('墙的宽度:'))
    a=int(input('砖的长度:'))
    b=int(input('砖的宽度:'))
    tile_(m, n, a, b)
    output(m, n, a, b)

if __name__ == '__main__':
    tile = []
    main()
