#author Edwin Recinos
import PySimpleGUI as sg

sg.theme('DarkBlue2')

layout = [  
            [  sg.Text('Food timer:', font=('Arial', 20)) ],                
            [  sg.Text( font=('Arial', 45), size=(10,1), key='OUTPUT1', justification = 'center') ],
 #         [   sg.Text('Food being cooked: '), sg.Output()],
 #           [  sg.Text('Type something in'), sg.Input()  ], 
            [  sg.Button('Start'),  sg.Button('Pause'), sg.Button('Exit'), sg.Button('Add 15mins'), 
            sg.Button('Subtract 15mins')]  ]                           

window = sg.Window("FOOD TIME!", layout)

count=0
timr= True


while True:

    event, values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    
    elif event in ('Start'):
        timr = True

    
    elif event in ('Pause'):
        timr= False


    elif event in ('Add 15mins'):
        if timr==False:
            count=count+1500
            window['OUTPUT1'].update('{:02d}:{:02d}.{:02d}'.format((count // 100) // 60, (count // 100) % 60, count % 100))
            
    
    elif event in ('Subtract 15mins'):
        if timr == False:
            count=count-1500
            window['OUTPUT1'].update('{:02d}:{:02d}.{:02d}'.format((count // 100) // 60, (count // 100) % 60, count % 100))
            

    if timr == True:
        window['OUTPUT1'].update('{:02d}:{:02d}.{:02d}'.format((count // 100) // 60, (count // 100) % 60, count % 100))
        count = count+1


window.close()
