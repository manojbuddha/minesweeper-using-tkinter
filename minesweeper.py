from tkinter import *
from tkinter import messagebox
import random

rows = 10
columns = 10

def load_mines(number_of_mines = 15):
    mine_cells = list(range(rows*columns))
    mine_cells[0:number_of_mines] =[1] * number_of_mines
    mine_cells[number_of_mines:] = [0] * (len(mine_cells)-number_of_mines)
    random.shuffle(mine_cells)
    random.shuffle(mine_cells)

    mine_counts=[]
    for i in range(0,rows):
            for j in range(0,columns):
                if mine_cells[rows*i+j]==1:
                    mine_counts.append('b') 
                    continue
                
                mine_count = 0
                if i != 0 and j !=0 and i !=rows-1 and j!=columns-1:

                    mine_count+=sum(mine_cells[(rows*(i+1))+(j-1):(rows*(i+1))+(j+2)])
                    mine_count+=sum(mine_cells[(rows*(i-1))+(j-1):(rows*(i-1))+(j+2)])
                    mine_count+=mine_cells[(rows*i)+j+1]
                    mine_count+=mine_cells[(rows*i)+j-1]
                    mine_counts.append(mine_count)  

                elif i==0 and j==0: 
                    mine_count+=mine_cells[1]
                    mine_count+=mine_cells[columns]
                    mine_count+=mine_cells[columns+1]
                    mine_counts.append(mine_count)

                elif i==0 and j==columns-1:
                    mine_count+=mine_cells[columns-2]
                    mine_count+=mine_cells[2*columns-1]
                    mine_count+=mine_cells[2*columns-2] 
                    mine_counts.append(mine_count)
                        
                elif i==0 and j!=0 and j!=columns-1:
                    mine_count+=sum(mine_cells[(rows*(i+1))+(j-1):(rows*(i+1))+(j+2)])
                    mine_count+=mine_cells[(rows*i)+j+1]
                    mine_count+=mine_cells[(rows*i)+j-1]
                    mine_counts.append(mine_count)

                elif i==rows-1 and j!=0 and j!=columns-1:
                    mine_count+=sum(mine_cells[(rows*(i-1))+(j-1):(rows*(i-1))+(j+2)])
                    mine_count+=mine_cells[(rows*i)+j+1]
                    mine_count+=mine_cells[(rows*i)+j-1]
                    mine_counts.append(mine_count) 
                    
                elif j==0 and i!=0 and i!=rows-1 :
                    mine_count+=sum(mine_cells[(rows*(i+1))+(j):(rows*(i+1))+(j+2)])
                    mine_count+=sum(mine_cells[(rows*(i-1))+(j):(rows*(i-1))+(j+2)])
                    mine_count+=mine_cells[(rows*i)+j+1]
                    mine_counts.append(mine_count)       
                    
                elif j==columns-1 and i!=0 and i!=rows-1 :
                    mine_count+=sum(mine_cells[(rows*(i+1))+(j-1):(rows*(i+1))+(j+1)])
                    mine_count+=sum(mine_cells[(rows*(i-1))+(j-1):(rows*(i-1))+(j+1)])
                    mine_count+=mine_cells[(rows*i)+j-1]
                    mine_counts.append(mine_count)                                    
                                
                elif i==rows-1 and j==0:                   
                    mine_count+=mine_cells[(rows*i)+j+1]
                    mine_count+=mine_cells[(rows*(i-1))+j]
                    mine_count+=mine_cells[(rows*(i-1))+j+1]
                    mine_counts.append(mine_count)
                        
                elif j==columns-1 and  i==rows-1:
                    mine_count+=mine_cells[(rows*i)+j-1]
                    mine_count+=mine_cells[(rows*(i-1))+j]                       
                    mine_count+=mine_cells[(rows*(i-1))+j-1]
                    mine_counts.append(mine_count)
                    
    for i in range(0,len(mine_counts)):            
        
        if int(mine_cells[i]) == 1:
            mine_cells[i]='b' 
        else:
            mine_cells[i]=mine_counts[i]
            
          
    return mine_cells,mine_counts
    

def label_to_button(i,j):

    if mine_cells[10*i+j] == 'b':
        
        for k in range(0,rows):
            for l in range(0,columns):
                if mine_cells[rows*k+l] == 'b':
                    Label(window, width=3, bg='orange',text="x".center(10)).grid(row=k,column=l)
                    btn[10*k+l].destroy()
                    mine_counts[rows*k+l]="revealed"  
                Label(window, width=3, text="x".center(10), bg='red').grid(row=i,column=j)
        window.update_idletasks()     
        messageanswer=messagebox.askquestion("Game over ")
        
    elif mine_cells[10*i+j] != 0 and mine_cells[10*i+j] != 'b':
        Label(window, width=3, text=str(mine_counts[rows*i+j]).center(10)).grid(row=i,column=j)
        rev[10*i+j]='r'
        btn[rows*i+j].destroy()        
        
    elif mine_counts[10*i+j] == 0:
        # Label(window, width=3, bg='blue',text="r".center(10)).grid(row=i,column=j)
        # btn[rows*i+j].destroy()     
        # rev[10*i+j]='r'

        def surroundings(i,j):
            surr=[]
            if i != 0 and j !=0 and i !=rows-1 and j!=columns-1:
                surr.append([(rows*(i+1))+(j-1),i+1,j-1])
                surr.append([(rows*(i+1))+(j),i+1,j])
                surr.append([(rows*(i+1))+(j+1),i+1,j+1])         
                surr.append([(rows*(i-1))+(j-1),i-1,j-1])
                surr.append([(rows*(i-1))+(j),i-1,j])
                surr.append([(rows*(i-1))+(j+1),i-1,j+1]) 
                surr.append([(rows*i)+j-1,i,j-1])               
                surr.append([(rows*i)+j+1,i,j+1])  
                
            elif i==0 and j==0:
                surr.append([1,0,1])
                surr.append([columns,1,0])
                surr.append([columns+1,1,1])

            elif i==0 and j==columns-1:
                surr.append([columns-2,0,columns-2])
                surr.append([2*columns-1,1,columns-1])
                surr.append([2*columns-2,1,columns-2])
                    
            elif i==0 and j!=0 and j!=columns-1:
                surr.append([(rows*(i+1))+(j-1),i+1,j-1])
                surr.append([(rows*(i+1))+(j),i+1,j])
                surr.append([(rows*(i+1))+(j+1),i+1,j+1])
                surr.append([(rows*i)+j+1,i,j+1])
                surr.append([(rows*i)+j-1,i,j-1])

            elif i==rows-1 and j!=0 and j!=columns-1:
                surr.append([(rows*(i-1))+(j-1),i-1,j-1])
                surr.append([(rows*(i-1))+(j),i-1,j])
                surr.append([(rows*(i-1))+(j+1),i-1,j+1])
                surr.append([(rows*i)+j+1,i,j+1])
                surr.append([(rows*i)+j-1,i,j-1])
                
            elif j==0 and i!=0 and i!=rows-1 :
                surr.append([(rows*(i+1))+(j),i+1,j])
                surr.append([(rows*(i+1))+(j+1),i+1,j+1]) 
                surr.append([(rows*(i-1))+(j),i-1,j])
                surr.append([(rows*(i-1))+(j+1),i-1,j+1])
                surr.append([(rows*i)+j+1,i,j+1])    
                
            elif j==columns-1 and i!=0 and i!=rows-1 :
                surr.append([(rows*(i+1))+(j-1),i+1,j-1])
                surr.append([(rows*(i+1))+(j),i+1,j])
                surr.append([(rows*(i-1))+(j-1),i-1,j-1])
                surr.append([(rows*(i-1))+(j),i-1,j])
                surr.append([(rows*i)+j-1,i,j-1])
                                                              
            elif i==rows-1 and j==0:
                surr.append([(rows*i)+j+1,i,j+1])
                surr.append([(rows*(i-1))+j,i-1,j])
                surr.append([(rows*(i-1))+j+1,i-1,j+1])
                    
            elif j==columns-1 and  i==rows-1:
                surr.append([(rows*i)+j-1,i,j-1])
                surr.append([(rows*(i-1))+j,i-1,j])
                surr.append([(rows*(i-1))+j-1,i-1,j-1])
                
            return surr
        
        # surr=surroundings(surr,i,j) 
        def clear_tile(cell_data):
            if rev[cell_data[0]]=='r':
                return
            elif rev[cell_data[0]]=='nr' and mine_counts[cell_data[0]]!=0:
                Label(window, width=3, text=str(mine_counts[cell_data[0]]).center(10)).grid(row=cell_data[1],column=cell_data[2])
                rev[10*cell_data[1]+cell_data[2]]='r'                
                return
            elif mine_counts[cell_data[0]]==0 and rev[cell_data[0]]=='nr':
                    Label(window, width=3, bg='blue',text="r".center(10)).grid(row=cell_data[1],column=cell_data[2])
                    btn[cell_data[0]].destroy()
                    rev[10*cell_data[1]+cell_data[2]]='r' 
                    surr=surroundings(cell_data[1],cell_data[2]) 
                    for cell in surr:
                        clear_tile(cell)
        clear_tile([rows*i+j,i,j])
        
        
btn=[]
window = Tk()
window.title("Minesweeper")
# for i in range(0,rows):
#     for j in range(0,columns):
#         btn.append(Button(window, width=3, command=lambda c=i,d=j: label_to_button(c,d)))
#         btn[rows*i+j].grid(row=i,column=j)

for i in range(0,rows):
    for j in range(0,columns):
        bt=Button(window, width=3, command=lambda c=i,d=j: label_to_button(c,d))
        btn.append(bt)
        
        btn[rows*i+j].grid(row=i,column=j)


mine_cells,mine_counts = load_mines()
rev=list(range(len(mine_cells)))
rev[:]=['nr']*len(rev)

window.mainloop()
                