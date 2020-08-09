# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 18:22:08 2020

@author: Manoj
"""
from tkinter import *
from tkinter import messagebox
import random
#from tkinter import PhotoImage
import time

class Minesweeper():
    
    #Button style and dimensions
    BUTTON_HEIGHT = 1
    BUTTON_WIDTH = 4
    BUTTON_BORDER_WIDTH = 4
    BUTTON_STYLE = "groove"
    win_flag = True
    
    GAME_DIFFICULTY_OPTIONS = ["Easy", "Medium", "Hard"]
    
    EASY_ROWS = 10
    EASY_COLUMNS = 10
    EASY_MINES = 10
    MEDIUM_ROWS = 20
    MEDIUM_COLUMNS = 20
    MEDIUM_MINES = 40
    HARD_ROWS = 30
    HARD_COLUMNS = 30
    HARD_MINES = 99
    
    def __init__(self,rows,columns,number_of_mines):
        self.rows = rows
        self.columns = columns
        self.buttons=[]
        self.number_of_mines = number_of_mines
        self.flag_count = self.number_of_mines
        self.start_time=time.time()
        self.revealed=list(range(0,self.rows*self.columns))
        self.revealed[:]=['nr']*len(self.revealed)
        self.flag=list(range(0,self.rows*self.columns))
        self.flag[:]=['nf']*len(self.flag)
        
        self.mine_cells,self.mine_counts = self.load_mines(self.number_of_mines)
        
        self.window = Tk()
        self.window.title("Minesweeper")
        self.upper_frame = Frame(self.window)
        self.lower_frame = Frame(self.window)
        self.upper_frame.pack()
        self.lower_frame.pack()
        
        self.difficulty = StringVar(self.upper_frame)
        self.difficulty.set(self.GAME_DIFFICULTY_OPTIONS[1])
        self.difficulty.trace("w", self.set_difficulty)
        opt = OptionMenu(self.upper_frame, self.difficulty, *self.GAME_DIFFICULTY_OPTIONS) 
        opt.grid(row=0,column=0,padx=50)
        self.flag_label = Label(self.upper_frame, text="Flags: "+str(number_of_mines))
        self.flag_label.grid(row=0,column=1,padx=50)
        
        self.score_display = Label(self.upper_frame, text="Time")
        self.score_display.after(200,self.timer)
        self.score_display.grid(row=0,column=2,padx=50)
        
        
        for self.row in range(0,self.rows):
            for self.column in range(0,self.columns):
                self.button = Button(self.lower_frame,height=self.BUTTON_HEIGHT, 
                                     width=self.BUTTON_WIDTH,  borderwidth=self.BUTTON_BORDER_WIDTH, 
                                     relief=self.BUTTON_STYLE)
                self.position = [self.row, self.column]        
                self.button.bind("<Button-2>", lambda event,position=self.position: 
                                 self.right_click(event,position))
                self.button.bind("<Button-3>", lambda event,position=self.position: 
                                 self.right_click(event,position))        
                self.button.bind("<Button-1>", lambda event,position=self.position: 
                                 self.left_click(event,position))   
                self.button.grid(row=self.row,column=self.column)
                self.buttons.append(self.button)  
        self.window.resizable(False,False)
        self.window.mainloop()
    
    def left_click(self,event,position):
        row = position[0]
        column = position[1]
        self.label_to_button(row,column)
        
    def right_click(self,event,position):
        row = position[0]
        column = position[1]        

        if self.flag[self.rows*row+column]=='f' and self.revealed[self.rows*row+column] != 'r':
            event.widget.destroy()        
            button = Button(self.lower_frame,height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH, 
                            borderwidth=self.BUTTON_BORDER_WIDTH, relief=self.BUTTON_STYLE)
  
            button.bind("<Button-2>", lambda event,position=position: 
                        self.right_click(event,position))
            button.bind("<Button-3>", lambda event,position=position: 
                        self.right_click(event,position))        
            button.bind("<Button-1>", lambda event,position=position: 
                        self.left_click(event,position)) 
            #,padx=1,pady=1
            button.grid(row=position[0],column=position[1])
            self.buttons[self.rows*position[0]+position[1]] = button
            self.flag[self.rows*position[0]+position[1]]='nf'
            self.flag_count+=1  
            #this is for upper frame
            self.flag_label.configure(text="Flags: "+str(self.flag_count))
            
        elif self.revealed[self.rows*row+column] != 'r':
            if self.flag_count==0:
                return
            event.widget.configure(bg="pink")
            self.flag[self.rows*position[0]+position[1]]='f'
            self.flag_count-=1
            #this is for upper frame            
            self.flag_label.configure(text="Flags: "+str(self.flag_count))   
            
    def timer(self):

        self.score_display.configure(text="Time: "+str(int(time.time()-self.start_time)))
        if self.win_flag:
            self.score_display.after(200,self.timer)            
            
    def surroundings(self,row,column):
        surrounding=[]
        if row != 0 and column !=0 and row !=self.rows-1 and column!=self.columns-1:
            surrounding.append([(self.rows*(row+1))+(column-1),row+1,column-1])
            surrounding.append([(self.rows*(row+1))+(column),row+1,column])
            surrounding.append([(self.rows*(row+1))+(column+1),row+1,column+1])         
            surrounding.append([(self.rows*(row-1))+(column-1),row-1,column-1])
            surrounding.append([(self.rows*(row-1))+(column),row-1,column])
            surrounding.append([(self.rows*(row-1))+(column+1),row-1,column+1]) 
            surrounding.append([(self.rows*row)+column-1,row,column-1])               
            surrounding.append([(self.rows*row)+column+1,row,column+1])  
            
        elif row==0 and column==0:
            surrounding.append([1,0,1])
            surrounding.append([self.columns,1,0])
            surrounding.append([self.columns+1,1,1])
    
        elif row==0 and column==self.columns-1:
            surrounding.append([self.columns-2,0,self.columns-2])
            surrounding.append([2*self.columns-1,1,self.columns-1])
            surrounding.append([2*self.columns-2,1,self.columns-2])
                
        elif row==0 and column!=0 and column!=self.columns-1:
            surrounding.append([(self.rows*(row+1))+(column-1),row+1,column-1])
            surrounding.append([(self.rows*(row+1))+(column),row+1,column])
            surrounding.append([(self.rows*(row+1))+(column+1),row+1,column+1])
            surrounding.append([(self.rows*row)+column+1,row,column+1])
            surrounding.append([(self.rows*row)+column-1,row,column-1])
    
        elif  row==self.rows-1 and column!=0 and column!=self.columns-1:
            surrounding.append([(self.rows*(row-1))+(column-1),row-1,column-1])
            surrounding.append([(self.rows*(row-1))+(column),row-1,column])
            surrounding.append([(self.rows*(row-1))+(column+1),row-1,column+1])
            surrounding.append([(self.rows*row)+column+1,row,column+1])
            surrounding.append([(self.rows*row)+column-1,row,column-1])
            
        elif column==0 and row!=0 and row!=self.rows-1 :
            surrounding.append([(self.rows*(row+1))+(column),row+1,column])
            surrounding.append([(self.rows*(row+1))+(column+1),row+1,column+1]) 
            surrounding.append([(self.rows*(row-1))+(column),row-1,column])
            surrounding.append([(self.rows*(row-1))+(column+1),row-1,column+1])
            surrounding.append([(self.rows*row)+column+1,row,column+1])    
            
        elif column==self.columns-1 and row!=0 and row!=self.rows-1 :
            surrounding.append([(self.rows*(row+1))+(column-1),row+1,column-1])
            surrounding.append([(self.rows*(row+1))+(column),row+1,column])
            surrounding.append([(self.rows*(row-1))+(column-1),row-1,column-1])
            surrounding.append([(self.rows*(row-1))+(column),row-1,column])
            surrounding.append([(self.rows*row)+column-1,row,column-1])
                                                          
        elif row==self.rows-1 and column==0:
            surrounding.append([(self.rows*row)+column+1,row,column+1])
            surrounding.append([(self.rows*(row-1))+column,row-1,column])
            surrounding.append([(self.rows*(row-1))+column+1,row-1,column+1])
                
        elif column==self.columns-1 and  row==self.rows-1:
            surrounding.append([(self.rows*row)+column-1,row,column-1])
            surrounding.append([(self.rows*(row-1))+column,row-1,column])
            surrounding.append([(self.rows*(row-1))+column-1,row-1,column-1])
            
        return surrounding        

    def load_mines(self,number_of_mines):
    
        mine_cells = list(range(self.rows*self.columns))
        mine_cells[0:number_of_mines] =[1] * number_of_mines
        mine_cells[number_of_mines:] = [0] * (len(mine_cells)-number_of_mines)
        random.shuffle(mine_cells)
        random.shuffle(mine_cells)
 
    
        mine_counts=[]
        for row in range(0,self.rows):
                for column in range(0,self.columns):
                    if mine_cells[self.rows*row+column]==1:
                        mine_counts.append('b') 
                        continue
                     
                    mine_count = 0
                    surroundings=self.surroundings(row,column)
                    for cell in surroundings:
                        mine_count+=mine_cells[cell[0]]
                    mine_counts.append(mine_count)
        for row in range(0,len(mine_counts)):            
            
            if int(mine_cells[row]) == 1:
                mine_cells[row]='b' 
            else:
                mine_cells[row]=mine_counts[row]
                
        print('\n')
        for row in range(0,self.rows):
                li=[]
                for column in range(0,self.columns):
    
                    li.append(mine_cells[self.rows*row+column])
                
                print(li)            
                          
        return mine_cells,mine_counts

            
    
    def label_to_button(self,row,column):
        
        if self.revealed[self.rows*row+column] == 'r':
            return
        
        if self.flag[self.rows*row+column]=='f':
            button = Button(self.lower_frame,height= self.BUTTON_HEIGHT, 
                            width=self.BUTTON_WIDTH, borderwidth=self. BUTTON_BORDER_WIDTH, 
                            relief= self.BUTTON_STYLE)
            position=[row,column]        
            button.bind("<Button-2>", lambda event, position = position: 
                        self.right_click(event,position))
            button.bind("<Button-3>", lambda event, position = position: 
                        self.right_click(event, position))        
            button.bind("<Button-1>", lambda event, position = position: 
                        self.left_click(event, position))           
            button.grid(row=row,column=column)
            self.buttons[self.rows*row+column] = button
            self.flag[self.rows*row+column]='nf'           
        
        if self.mine_cells[self.rows*row+column] == 'b':
            #,height=1,width=3,
            #mine_image = PhotoImage(file="E:\My git repos\minesweeper-using-tkinter\mines.gif")
            for k in range(0,self.rows):
                for l in range(0,self.columns):
                    if self.mine_cells[self.rows*k+l] == 'b':
                        self.buttons[self.rows*k+l].configure(state=DISABLED,bg='orange')
                        self.revealed[self.rows*k+l]='r'
                        self.mine_counts[self.rows*k+l]=" self.revealed"  
                    self.buttons[self.rows*row+column].configure(state=DISABLED,bg='red')
                    self.revealed[self.rows*row+column]='r'
            self.game_lost()
            return
            
        elif self.mine_cells[self.rows*row+column] != 0 and self.mine_cells[self.rows*row+column] != 'b':
            if self.mine_cells[self.rows*row+column] == 1:
                #.center(10), height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH,  borderwidth=self.BUTTON_BORDER_WIDTH, relief=self.BUTTON_STYLE
                self.buttons[self.rows*row+column].configure(state=DISABLED,width=3,
                                    fg='green',font="-weight bold ", 
                                    text=str(self.mine_counts[self.rows*row+column]).strip())
            elif self.mine_cells[self.rows*row+column] == 2:
                self.buttons[self.rows*row+column].configure(state=DISABLED,width=3,
                                    fg='green',font="-weight bold ", 
                                    text=str(self.mine_counts[self.rows*row+column]))
            else :
                self.buttons[self.rows*row+column].configure(state=DISABLED,width=3,
                                    fg='red',font="-weight bold ", 
                                    text=str(self.mine_counts[self.rows*row+column]))
            self.revealed[self.rows*row+column]='r'
            
        elif self.mine_counts[self.rows*row+column] == 0:
            
            def clear_cell(cell_data):
                if self.revealed[cell_data[0]]=='r':
                    return
                elif self.revealed[cell_data[0]]=='nr' and self.mine_counts[cell_data[0]]!=0:
                    self.label_to_button(cell_data[1],cell_data[2])        
                    return
                elif self.mine_counts[cell_data[0]]==0 and self.revealed[cell_data[0]]=='nr':
                        self.buttons[self.rows*cell_data[1]+cell_data[2]].configure(state=DISABLED,bg='#0077be')
                        self.revealed[self.rows*cell_data[1]+cell_data[2]]='r' 
                        surroundings=self.surroundings(cell_data[1],cell_data[2]) 
                        for cell in surroundings:
                            clear_cell(cell)
            clear_cell([self.rows*row+column,row,column])
        
        win_count=0
        for check_win in range(0,self.rows*self.columns):
                if self.mine_counts[check_win]!='b' and self.revealed[check_win]=='r':
                    win_count+=1
        if win_count == (self.rows*self.columns)-self.number_of_mines:
                            self.win_flag = False
                            self.game_win()

    def game_win(self):
        
        self.score = int(time.time()-self.start_time)

        self.window.update_idletasks()            
        message_answer = messagebox.askyesno(title="Win Game"
                                          ,message="You swept all the mines "+"\n"+"Score: "+str(self.score)+". Do you want to play again??")
        if message_answer:
            self.new_game()
        else:
            self.window.destroy()
        
    def game_lost(self):
        self.window.update_idletasks()
        message_answer = messagebox.askyesno(title="Better luck next time :(",message="Game lost!!. Do you want to try again??")
        if message_answer:
            self.new_game()
        else:
            self.window.destroy()
        
    def set_difficulty(self,*args):
        self.new_game()
        pass
        
    def new_game(self):
        #self.difficulty.get()
        self.window.destroy()
        difficulty = self.difficulty.get()
        if difficulty == "Easy":            
            self.__init__(self.EASY_ROWS,self.EASY_COLUMNS,self.EASY_MINES)
        if difficulty == "Medium":
            self.__init__(self.MEDIUM_ROWS,self.MEDIUM_COLUMNS,self.MEDIUM_MINES)
        if difficulty == "Hard":
            self.__init__(self.HARD_ROWS,self.HARD_COLUMNS,self.HARD_MINES)
                            
                            
game = Minesweeper(20,20,40)
