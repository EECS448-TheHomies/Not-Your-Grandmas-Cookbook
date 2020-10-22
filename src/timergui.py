#author Edwin Recinos
import PySimpleGUI as sg

sg.theme('DarkBlue2')

layout = [  
            [  sg.Text('Food timer:', font=('Arial', 20)) ],                
            [  sg.Text( font=('Arial', 45), size=(10,1), key='OUTPUT1', justification = 'center') ],
 #         [   sg.Text('Food being cooked: '), sg.Output()],
 #           [  sg.Text('Type something in'), sg.Input()  ], 
            [  sg.Button('Start/Pause'),  sg.Button('Exit'), sg.Button('Add 15mins'), 
            sg.Button('Subtract 15mins')]  ]                           

window = sg.Window("FOOD TIME!", layout)

count=0
timr= True

while True:

    event, values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    
    elif event in ('Start/Pause'):
        timr = not timr

    
    elif event in ('Add 15mins'):
        print('r')
        break
    
    elif event in ('Subtract 15mins'):
        break

    if timr == True:
        window['OUTPUT1'].update('{:02d}:{:02d}.{:02d}'.format((count // 100) // 60, (count // 100) % 60, count % 100))
        count = count+1


window.close()
