#author Edwin Recinos
#originally set up to run the script that would pull up the timer
import PySimpleGUI as sg

"""Timer Overview

PySimpleGui used, sg is the class and any method call is sg.___

This script, when run will popup a timer which the user can add/subtract time from. 

Attributes:

    layout (rows of the window layout): 
        sg.Text Sets text so Food timer and the key 'OUTPUT1" is displayed on the counter
        sg.Button() sets buttons titled what is within the parenthesis
            Start starts the counter, Pause pauses, Exit closes the program
            +15mins, -15mins, etc does what it says it does.
        Everything within the brackets is a row.

    while loop, with if statements within to check what needs to be done.
        if Start event is activated, timer runs 
        if Pause event is activated, timer is paused
        if Exit event is activated, timer window is closed down
        if +15mins event, timer +15 mins
        etc....
        

"""

#sg.theme is an sg class method that sets theme to DarkBlue2
sg.theme('DarkBlue2')
sg.Print(do_not_reroute_stdout=False)

#layout is how the window will look
#each field of commands within a bracket is a row. 

layout = [  
            [  sg.Text('Food timer:', font=('Arial', 20)) ],                
            [  sg.Text( font=('Arial', 45), size=(10,1), key='OUTPUT1', justification = 'center') ],
 #         [   sg.Text('Food being cooked: '), sg.Output()],
 #           [  sg.Text('Type something in'), sg.Input()  ], 
            [  sg.Button('Start'),  sg.Button('Pause'), sg.Button('Exit')],
            [ sg.Button('+15mins'), sg.Button('-15mins'),  sg.Button('+1min'), sg.Button('-1min'),  sg.Button('+30secs'), sg.Button('-30secs')] 
               ]                           


window = sg.Window("FOOD TIME!", layout)

#@count is the number that the counter should display
#@timr is a variable that indicates if the timer is running
count=0
timr= True

#while event loop is going, no break activated, the 'count' variable will keep rising unless paused
#and another button is pressed. Those are the if statements.
#If statements are checked once the timer is paused to see if user wants to add or subtract time.


while True:

    """While loop run will check for events
    Summary:
        Premade Variables:
            count(int): will keep track of the timer count
            timr(bool): bool check to see if timr has been stopped by user

        Actions:
            While Loop: runs until break is detected which is if window is closed or the event hits Exit
                if statements are meant to keep track of the premade variables and where the event is currently on
                    event in Exit or user closes window then break
                    event in Start then the timer starts, timr set to true
                    event in Pause then the timer pauses, timr set to false
                    event in +15mins has nested if statement checking if timr is set to false
                        as a check to see if timer is paused. If so then adds 15 mins to counter.
                    event in -15mins has nested if statement checking if timr is set to false
                        as a check to see if timer is paused. If so then subtracts 15 mins from counter
                    events same for +1/-1mins and +30/-30secs. Buttons doing what the events are labeled as

                everytime the while loop loops, you have an if timr == true which if it is the case, the timer is
                    running. Which everytime it loops and timr is True, it will add 1 to the counter.
                
            Once broken out of the while loop, the window will close, hence the window.close()
    """

    event, values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    
    elif event in ('Start'):
        timr = True

    
    elif event in ('Pause'):
        timr= False


    elif event in ('+15mins'):
        if timr==False:
            count=count+1500
            window['OUTPUT1'].update('{:02d}:{:02d}.{:02d}'.format((count // 100) // 60, (count // 100) % 60, count % 100))
            
    
    elif event in ('-15mins'):
        if timr == False:
            count=count-1500
            window['OUTPUT1'].update('{:02d}:{:02d}.{:02d}'.format((count // 100) // 60, (count // 100) % 60, count % 100))
            
    elif event in ('+1min'):
        if timr==False:
            count=count+100
            window['OUTPUT1'].update('{:02d}:{:02d}.{:02d}'.format((count // 100) // 60, (count // 100) % 60, count % 100))
            
    
    elif event in ('-1min'):
        if timr == False:
            count=count-100
            window['OUTPUT1'].update('{:02d}:{:02d}.{:02d}'.format((count // 100) // 60, (count // 100) % 60, count % 100))

    elif event in ('+30secs'):
        if timr==False:
            count=count+30
            window['OUTPUT1'].update('{:02d}:{:02d}.{:02d}'.format((count // 100) // 60, (count // 100) % 60, count % 100))
            
        
    elif event in ('-30secs'):
        if timr == False:
            count=count-30
            window['OUTPUT1'].update('{:02d}:{:02d}.{:02d}'.format((count // 100) // 60, (count // 100) % 60, count % 100))
        

    if timr == True:
        window['OUTPUT1'].update('{:02d}:{:02d}.{:02d}'.format((count // 100) // 60, (count // 100) % 60, count % 100))
        count = count+1
        print(count)


window.close()

