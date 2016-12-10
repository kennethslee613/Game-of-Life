import random

def ran():
    n = random.randint(0,1)
    return n

siz = 32
grid = [[ran() for i in range(siz)] for n in range(siz)] # list comprehension
s = [[0 for i in range(siz)] for n in range(siz)]
sum = [[0 for i in range(siz)] for n in range(siz)]

w = 20 # width of each cell

def life():
    for i in range(siz - 1):
        for j in range(siz - 1):
            sum[i][j] = grid[(i-1)%siz][j%siz] + grid[(i-1)%siz][(j+1)%siz] + grid[i%siz][(j+1)%siz] + grid[(i+1)%siz][(j+1)%siz] + grid[(i+1)%siz][j%siz] + grid[(i+1)%siz][(j-1)%siz] + grid[i%siz][(j-1)%siz] + grid[(i-1)%siz][(j-1)%siz]
            
    for i in range(siz - 1):
        for j in range(siz - 1):
            if (sum[i][j] == 2 or sum[i][j] == 3) and grid[i][j] == 1:
                grid[i][j] = 1
            elif grid[i][j] == 0 and sum[i][j] == 3:
                grid[i][j] = 1
            else:
                grid[i][j] = 0


def setup():
    size(800,800)
    
def draw():
    x,y = 0,0 # starting position

    for i in range(siz - 1):
        for j in range(siz - 1):
            s[i][j] = grid[(i-1)%siz][j%siz] + grid[(i-1)%siz][(j+1)%siz] + grid[i%siz][(j+1)%siz] + grid[(i+1)%siz][(j+1)%siz] + grid[(i+1)%siz][j%siz] + grid[(i+1)%siz][(j-1)%siz] + grid[i%siz][(j-1)%siz] + grid[(i-1)%siz][(j-1)%siz]
            if grid[i][j] == 1:
                if s[i][j] == 8 or s[i][j] == 7 or s[i][j] == 6 or s[i][j] == 5 or s[i][j] == 4:
                    fill(0,100,0)
                elif s[i][j] == 3:
                    fill(34,139,34)
                elif s[i][j] == 2:
                    fill(50,205,50)
                elif s[i][j] == 1:
                    fill(124,252,0)
                else:
                    fill(173,255,47)
            else:
                fill(255)
            rect(x, y, w, w)
            x = x + w  # move right
        y = y + w # move down
        x = 0 # rest to left edge
    if not pause:
        life()
    else:
        None

def setup():
    global pause
    pause = False
    
def keyPressed():
    global pause
    if key == " ":
        pause = not pause
    if key == "n":
        pause = True
        for i in range(siz - 1):
            for j in range(siz - 1):
                sum[i][j] = 0
                s[i][j] = 0
                grid[i][j] = 0
        pause = False
    if key == "r":
        for i in range(siz - 1):
            for j in range(siz - 1):
                grid[i][j] = ran()

def mousePressed():
    if grid[mouseY//w][mouseX//w] == 0:
        grid[mouseY//w][mouseX//w] = 1 + grid[mouseY//w][mouseX//w]  
    else:
        grid[mouseY//w][mouseX//w] = 0 * grid[mouseY//w][mouseX//w]
    # integer division is good here!