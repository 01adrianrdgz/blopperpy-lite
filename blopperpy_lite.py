#import module
import os
from termcolor import colored

#variables
run = True
menu = True
about_app = False
searching_wireless = False
filesearch = False
path = os.getcwd()

#main app
while run:
    while menu:
        print('\n')
        print(colored('~~ ~ ~~ [blopperpy lite] ~~ ~ ~~', 'white', 'on_blue'))
        print(colored('1. about application', 'white', 'on_light_magenta'))
        print(colored('2. open files to hack', 'white', 'on_light_magenta'))
        print(colored('3. run scripts', 'white', 'on_light_magenta'))
        print(colored('4. search for wireless drivers', 'white', 'on_light_magenta'))
        print(colored('5. quit', 'white', 'on_light_magenta'))
        print(colored(r'''
                              /|      __
*             +      / |   ,-~ /             +
     .              Y :|  //  /                .         *
         .          | jj /( .^     *
               *    >-"~"-v"              .        *        .
*                  /       Y
   .     .        jo  o    |     .            +
                 ( ~T~     j                     +     .
      +           >._-' _./         +
               /| ;-"~ _  l
  .           / l/ ,-"~    \     +
              \//\/      .- \
       +       Y        /    Y
               l       I     !
               ]\      _\    /"\
              (" ~----( ~   Y.  )
          ~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''', 'light_magenta'))
        print('\n')
        choice = input(colored('> ', 'white', 'on_red'))       
        if choice == '1':
            about_app = True
            menu = False
        elif choice == '2':
            filesearch = True
            menu = False
        elif choice == '3':
            filesearch = True
            menu = False
        elif choice == '4':
            searching_wireless = True
            menu = False
        elif choice == '5':
            quit()
        elif choice:
            pass            
    while about_app:
        print('\n')
        print(colored('~~ ~ ~~ about application ~~ ~ ~~', 'white', 'on_blue'))
        print('this software app is licensed under the mit License.')
        print('all the things it does are fake and do not harm your computer in any way. thank you for downloading it!' '\n' '')
        print('\n')
        print('type [9] and enter to go back to the menu.')
        print('\n')        
        choice_about_app = input(colored('> ', 'white', 'on_red'))
        if choice_about_app == '9':
            about_app = False
            menu = True
        elif choice_about_app:
            pass           
    while searching_wireless:
        print('\n')
        print(colored('~~ ~ ~~ searching for wireless drivers ~~ ~ ~~', 'white', 'on_blue'))
        print('[                                   ]')
        print('[                                   ]')
        print('[                                   ]')
        print('[                                   ]')
        print('[                                   ]')
        print('[                                   ]')
        print('[                                   ]')
        print('[                                   ]')
        print('[                                   ]')
        print('\n')
        print('type [9] and enter to go back to the menu if nothing was detected.')
        print('\n')       
        choice_sw = input(colored('> ', 'white', 'on_red'))
        if choice_sw == '9':
            searching_wireless = False
            menu = True
        elif choice_sw:
            pass       
    while filesearch:
        print('\n')
        print(colored('~~ ~ ~~ run scripts or open files ~~ ~ ~~', 'white', 'on_blue'))
        print(path)
        print('\n')
        print('type [9] and \'enter\' to go back.')
        print('type [name of file] and \'enter\' to select file')
        print('\n')       
        choice_file = input(colored('> ', 'white', 'on_red'))
        if choice_file == '9':
            filesearch = False
            menu = True
        elif choice_file:
            pass

