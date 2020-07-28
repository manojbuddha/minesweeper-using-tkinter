from tkinter import *
from tkinter import messagebox
import random
import time

rows = 10
columns = 10
number_of_mines = 10

def load_mines(event, number_of_mines):
    mine_cells = list(range(rows*columns))
    mine_cells[0:number_of_mines] =[1] * number_of_mines
    mine_cells[number_of_mines:] = [0] * (len(mine_cells)-number_of_mines)
    random.shuffle(mine_cells)
    random.shuffle(mine_cells)
    for i in range(0,rows):
            li=[]
            for j in range(0,columns):

                li.append(mine_cells[rows*i+j])
            
            print(li)    

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
            
    print('\n')
    for i in range(0,rows):
            li=[]
            for j in range(0,columns):

                li.append(mine_cells[rows*i+j])
            
            print(li)            
                      
    return mine_cells,mine_counts

def label_to_button(i,j):
    
    if rev[rows*i+j] == 'r':
        return
    
    if flag[rows*i+j]=='f':
        bt = Button(window, width=4, borderwidth=4, relief="groove")
        d=[i,j]        
        bt.bind("<Button-2>", lambda event,s=d: right_click(event,s))
        bt.bind("<Button-3>", lambda event,s=d: right_click(event,s))        
        bt.bind("<Button-1>", lambda event,s=d: left_click(event,s))           
        bt.grid(row=i,column=j,padx=1,pady=1,sticky='NSEW')
        btn[rows*i+j] = bt
        flag[rows*i+j]='nf'           
    
    if mine_cells[10*i+j] == 'b':
        
        for k in range(0,rows):
            for l in range(0,columns):
                if mine_cells[rows*k+l] == 'b':
                    btn[rows*k+l].configure(state=DISABLED,height=1,width=3, bg='orange',font="-weight bold ", text="x".center(10))
                    #Label(window, width=3, bg='orange',text="x".center(10)).grid(row=k,column=l)
                    #btn[10*k+l].destroy()
                    rev[10*k+l]='r'
                    mine_counts[rows*k+l]="revealed"  
                #Label(window, width=3, text="x".center(10), bg='red').grid(row=i,column=j)
                btn[rows*i+j].configure(state=DISABLED,bg='red',height=1,width=3,font="-weight bold ", text="x".center(10))
                rev[10*i+j]='r'
        window.update_idletasks()     
        messagebox.showinfo(title="lose Game",message="Game lost!! you got the wrong block..")
        return
        
    elif mine_cells[10*i+j] != 0 and mine_cells[10*i+j] != 'b':
        if mine_cells[10*i+j] == 1:
            btn[rows*i+j].configure(state=DISABLED,height=1,width=3,fg='blue',font="-weight bold ", text=str(mine_counts[rows*i+j]).center(10))
            #Label(window, width=4,fg='blue',font="-weight bold ", text=str(mine_counts[rows*i+j]).center(10)).grid(row=i,column=j)
        elif mine_cells[10*i+j] == 2:
            #Label(window, width=4,fg='green' ,font="-weight bold", text=str(mine_counts[rows*i+j]).center(10)).grid(row=i,column=j)
            btn[rows*i+j].configure(state=DISABLED,height=1,width=3,fg='green',font="-weight bold ", text=str(mine_counts[rows*i+j]).center(10))
        else :
            #Label(window, width=4,fg='red',font="-weight bold ", text=str(mine_counts[rows*i+j]).center(10)).grid(row=i,column=j)            
            btn[rows*i+j].configure(state=DISABLED,height=1,width=3,fg='red',font="-weight bold ", text=str(mine_counts[rows*i+j]).center(10))
        rev[10*i+j]='r'
        #btn[rows*i+j].destroy()        
        
    elif mine_counts[10*i+j] == 0:
        

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
                label_to_button(cell_data[1],cell_data[2])
                # if mine_counts[cell_data[0]]==1:
                #     Label(window, width=4,fg='green',font=("bold"), text=str(mine_counts[cell_data[0]]).center(10)).grid(row=cell_data[1],column=cell_data[2])
                # elif mine_counts[cell_data[0]]==2:
                #     Label(window, width=4,fg='blue',font=("bold"), text=str(mine_counts[cell_data[0]]).center(10)).grid(row=cell_data[1],column=cell_data[2])
                # else :
                #     Label(window, width=4,fg='red',font=("bold"), text=str(mine_counts[cell_data[0]]).center(10)).grid(row=cell_data[1],column=cell_data[2])                    
                
                # btn[cell_data[0]].destroy()
                # rev[10*cell_data[1]+cell_data[2]]='r'        
                return
            elif mine_counts[cell_data[0]]==0 and rev[cell_data[0]]=='nr':
                    btn[rows*cell_data[1]+cell_data[2]].configure(state=DISABLED,height=1,width=3,bg='#0077be',font="-weight bold ")
                    #Label(window, width=4, bg='sky blue',text="r".center(10)).grid(row=cell_data[1],column=cell_data[2])
                    #btn[cell_data[0]].destroy()
                    rev[10*cell_data[1]+cell_data[2]]='r' 
                    surr=surroundings(cell_data[1],cell_data[2]) 
                    for cell in surr:
                        clear_tile(cell)
        clear_tile([rows*i+j,i,j])
    
    win_count=0
    for check_win in range(0,rows*columns):
            if mine_counts[check_win]!='b' and rev[check_win]=='r':
                win_count+=1
    if win_count == (rows*columns)-number_of_mines:
                        window.update_idletasks()     
                        messageanswer=messagebox.showinfo(title="Win Game",message="You swept all the mines ")
start_time=time.time()
def timer():
    
    times.configure(text="time: "+str(int(time.time()-start_time)))
    times.after(200,timer)
        
btn=[]
window = Tk()
window.title("Minesweeper")
upper_frame = Frame(window)

lower_frame = Frame(window)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)



#Label(upper_frame, text="Difficulty").grid(row=0,column=0,padx=50)
slider = Scale(upper_frame, from_=10, to=20, orient=HORIZONTAL)
slider.bind("<ButtonRelease-1>",lambda event,val=slider.get(): load_mines(event, int(val)))
slider.grid(row=0,column=0,padx=50)
Label(upper_frame, text="Minesweeper").grid(row=0,column=1,padx=50)
times=Label(upper_frame, text="Time")
times.after(200,timer)
times.grid(row=0,column=2,padx=50)
def right_click(event,s):
    if flag[rows*s[0]+s[1]]=='f' and rev[rows*s[0]+s[1]] != 'r':
        event.widget.destroy()        
        bt = Button(window, width=4, borderwidth=4, relief="groove")
        i=s[0]
        j=s[1]
        d=[i,j]        
        bt.bind("<Button-2>", lambda event,s=d: right_click(event,s))
        bt.bind("<Button-3>", lambda event,s=d: right_click(event,s))        
        bt.bind("<Button-1>", lambda event,s=d: left_click(event,s))           
        bt.grid(row=s[0],column=s[1],padx=1,pady=1,sticky='NSEW')
        btn[rows*s[0]+s[1]] = bt
        flag[rows*s[0]+s[1]]='nf'            
    elif rev[rows*s[0]+s[1]] != 'r':
        event.widget.configure(text="F".center(10),width=3,bg='black',fg="orange",font=("bold"))
        flag[rows*s[0]+s[1]]='f'         

def left_click(event,s):
    c=s[0]
    d=s[1]
    label_to_button(c,d)

for i in range(0,rows):
    for j in range(0,columns):
        bt=Button(lower_frame,height=1, width=4, text=" ".center(10), borderwidth=4, relief="groove")
        d=[i,j]        
        bt.bind("<Button-2>", lambda event,s=d: right_click(event,s))
        bt.bind("<Button-3>", lambda event,s=d: right_click(event,s))        
        bt.bind("<Button-1>", lambda event,s=d: left_click(event,s))   
        window.grid_rowconfigure(i, weight=1)
        window.grid_columnconfigure(j, weight=1)
        bt.grid(row=i,column=j,padx=1,pady=1,sticky='NSEW')
        btn.append(bt)  
   
mine_cells,mine_counts = load_mines(Event(),number_of_mines)
rev=list(range(0,rows*columns))
rev[:]=['nr']*len(rev)

flag=list(range(0,rows*columns))
flag[:]=['nf']*len(flag)
upper_frame.pack()
lower_frame.pack()
#window.resizable(0,0)
window.mainloop()