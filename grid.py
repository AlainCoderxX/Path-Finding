'''references
https://gamedev.stackexchange.com/questions/197165/java-simple-2d-grid-pathfinding
https://svn.sable.mcgill.ca/sable/courses/COMP763/oldpapers/yap-02-grid-based.pdf
'''
import pygame
import math
class App:
    def __init__(self) -> None:
        self.HEIGHT,self.WIDTH=600,600
        self.FPS=200
        self.CLOCK=pygame.time.Clock()
        self.WINDOW=pygame.display.set_mode((self.HEIGHT,self.WIDTH))
        self.x,self.y=None,None
        self.next=[]
        pass

    def run(self):

        board=grid.make2dArray(cols,rows)
        mouse=mousepressed()

        while True:  
            self.WINDOW.fill((211,211,211))
            pygame.display.set_caption(f"Path Finding {self.CLOCK.get_fps()}")

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit()

                if event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==1:
                        self.x,self.y=mouse.select(event.pos)
                        board[self.x][self.y]=1
                        x1,y1=self.x,self.y
                    if event.button==3:
                        self.x,self.y=mouse.select(event.pos)
                        board[self.x][self.y]=2
                        x2,y2=self.x,self.y
                    if event.button==2:
                        board=grid.clear(board)
                        print(grid.distance(x1,y1,x2,y2),'Units')

                        ...
            grid.draw(board)
            pygame.display.flip()
            self.CLOCK.tick(self.FPS)	



class Grid(App):

    def __init__(self) -> None:
        super().__init__()
        self.resolution=10
        self.color='White'
        self.cols=int(self.HEIGHT/self.resolution)
        self.rows=int(self.WIDTH/self.resolution)

    def getRC(self):
        return (self.cols,self.rows)
    
    def givevals(self,val,grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j]=val
        return grid

    def distance(self,x1,y1,x2,y2):
        return math.sqrt(((x2-x1)*(x2-x1))+(y2-y1)*(y2-y1))
    
    def draw(self,grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                x=i*self.resolution
                y=j*self.resolution
                if grid[i][j]==1:
                    pygame.draw.rect(self.WINDOW,('Blue'),pygame.Rect(x,y,self.resolution,self.resolution))   
                if grid[i][j]==2:
                    pygame.draw.rect(self.WINDOW,('Red'),pygame.Rect(x,y,self.resolution,self.resolution))                   
                pygame.draw.rect(self.WINDOW,('Black'),pygame.Rect(x,y,self.resolution,self.resolution),1)

    def make2dArray(self,cols,rows):
        arr=[0]*cols
        for i in range(len(arr)):
            arr[i]=[0]*rows
        return arr

    def clear(self,grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j]=0
        return grid



class mousepressed(Grid):
    def __init__(self) -> None:
        super().__init__()
    
    def select(self,pos):
        x,y=pos[0]//self.resolution,pos[1]//self.resolution
        return (x,y)
        

grid=Grid()
cols,rows=grid.getRC()



if __name__=="__main__":
    app=App()
    app.run()