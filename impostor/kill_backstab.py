from os import system, name
from time import sleep
import curses, sys, os

amongus = ["""





         .---.       .---.
       _'   __'    _'   __'
      | |  (___)  | |  (___)
      | |     |   | |     |
      |_|  _  |   |_|  _  |
        |_| |_|     |_| |_| 
""","""





         .---.       .---.
       _'   __'    _'   __'
      | |  (___)  | |  (___)
      | |     |   | |     |
      |_|  _  |   |_|  _  |
        |_| |_|     |_| |_| 
""","""


                ,_____
            (__)|_____\\
                '
         .---.       .---.
       _'   __'    _'   __'
      | |  (___)  | |  (___)
      | |     |   | |     |
      |_|  _  |   |_|  _  |
        |_| |_|     |_| |_| 
""","""


                 ,_____
             (__)|_____\\
                 '
         .---.       .---.
       _'   __'    _'   __'
      | |  (___)  | |  (___)
      | |     |   | |     |
      |_|  _  |   |_|  _  |
        |_| |_|     |_| |_| 
""","""




                
         .---.   .(__),.---.
       _'   __'    \\ \\'   __'
      | |  (___)    | |  (___)
      | |     |    | |     |
      |_|  _  |   |_|  _  |
        |_| |_|     |_| |_| 
""","""




                
         .---.   .(__),.---.
       _'   __'    \\ \\'   __'
      | |  (___)    | |  (___)
      | |     |    | |     |
      |_|  _  |   |_|  _  |
        |_| |_|     |_| |_| 
""","""



              .(__),
                \\ \\
         .---.   \\ \\   .---.
       _'   __'   \\/ _'   __'
      | |  (___)    | |  (___)
      | |     |    | |     |
      |_|  _  |   |_|  _  |
        |_| |_|     |_| |_| 
""","""



              .(__),
                \\ \\
         .---.   \\ \\   .---.
       _'   __'   \\/ _'   __'
      | |  (___)    | |  (___)
      | |     |    | |     |
      |_|  _  |   |_|  _  |
        |_| |_|     |_| |_| 
""","""




                
         .---.   .(__),.---.
       _'   __'    \\ \\'   _.-.
      | |  (___)     | | (__.'
      | |     |     | |     |
      |_|  _  |    |_| _   |
        |_| |_|     |_| |_| 
""","""




                
         .---.   .(__),.---.
       _'   __'    \\ \\'   _.-.
      | |  (___)     | | (__.'
      | |     |     | |     |
      |_|  _  |    |_| _   |
        |_| |_|     |_| |_| 
""","""



               .(__),
                 \\ \\
         .---.    \\ \\  .---.
       _'   __'    \\/ '   _.-.
      | |  (___)     | | (__.'
      | |     |     | |     |
      |_|  _  |    |_| _   |
        |_| |_|     |_| |_| 
""","""



               .(__),
                 \\ \\
         .---.    \\ \\  .---.
       _'   __'    \\/ '   _.-.
      | |  (___)     | | (__.'
      | |     |     | |     |
      |_|  _  |    |_| _   |
        |_| |_|     |_| |_| 
""","""




                
         .---.   .(__),
       _'   __'    \\ \\ _.---.
      | |  (___)    \\ '   ___'
      | |     |     | |  (___)
      |_|  _  |    |_| _   |
        |_| |_|     |_| |_| 
""","""




                
         .---.   .(__),
       _'   __'    \\ \\ _.---.
      | |  (___)    \\ '   ___'
      | |     |     | |  (___)
      |_|  _  |    |_| _   |
        |_| |_|     |_| |_| 
""","""



               .(__),
                 \\ \\
         .---.    \\ \\
       _'   __'    \\/  _.---.
      | |  (___)     _'   ___'
      | |     |     | |  (___)
      |_|  _  |    |_| _   |
        |_| |_|     |_| |_| 
""","""



               .(__),
                 \\ \\
         .---.    \\ \\
       _'   __'    \\/  _.---.
      | |  (___)     _'   ___'
      | |     |     | |  (___)
      |_|  _  |    |_| _   |
        |_| |_|     |_| |_| 
""","""




                
         .---.   .(__),
       _'   __'    \\ \\ _.---.
      | |  (___)    \\ '   ___'
      | |     |     | |  (___)
      |_|  _  |    |_| _   |
        |_| |_|     |_| |_| 
""","""



               .(__),
                 \\ \\
         .---.    \\ \\
       _'   __'    \\/  _.---.
      | |  (___)     _'   ___'
      | |     |     | |  (___)
      |_|  _  |    |_| _   |
        |_| |_|     |_| |_| 
""","""




                
         .---.   .(__),.---.
       _'   __'    \\ \\'   _.-.    --.
      | |  (___)    \\| | (__.'  // //
      | |     |     | |     |   '__/
      |_|  _  |    |_| _   |
        |_| |_|     |_| |_| 
""","""




                
         .---.   .(__),.---.
       _'   __'    \\ \\'   _.-.    --.
      | |  (___)    \\| | (__.'  // //
      | |     |     | |     |   '__/
      |_|  _  |    |_| _   |
        |_| |_|     |_| |_| 
""","""




                
         .---.   .(__),.---.
       _'   __'    \\ \\'   _.-.    --.
      | |  (___)    \\| | (__.'  // //
      | |     |     | |     |   '__/
      |_|  _  |    |_| _   |
        |_| |_|     |_| |_| 
""","""




                
         .---.   .(__),.---.
       _'   __'    \\ \\'   _.-.     --.
      | |  (___)    \\| | (__.'   // //
      | |     |     | |     |    '__/
      |_|  _  |    |_| _   |
        |_| |_|     |_| |_| 
""","""




                
         .---.   .(__),.---.
       _'   __'    \\ \\'   _.-.     --.
      | |  (___)    \\| | |__.'   // //
      | |     |     | |     |    '__/
      |_|  _  |    |_| _   |
        |_| |_|     |_| |_| 
""","""




               (__)
         .---.   
       _'   __'           _
      | |  (___)        ,|_|,
      | |     |         _|_|
      |_|  _  |      .-|____|---.   ___
        |_| |_|     |________|'|_| /__\\\\
""","""




               (__)
         .---.   
       _'   __'            _
      | |  (___)         ,|_|,
      | |     |          _|_|
      |_|  _  |       .-|____|---.   ___
        |_| |_|      |________|'|_| /__\\\\
""","""




               
         .---.  (__)
       _'   __'             _
      | |  (___)          ,|_|,
      | |     |           _|_|
      |_|  _  |        .-|____|---.   ___
        |_| |_|       |________|'|_| /__\\\\
""","""




               
         .---.  
       _'   __'             _
      | |  (___)(__)      ,|_|,
      | |     |           _|_|
      |_|  _  |        .-|____|---.   ___
        |_| |_|       |________|'|_| /__\\\\
""","""




               
         .---.  
       _'   __'             _
      | |  (___)          ,|_|,
      | |     |           _|_|
      |_|  _  |        .-|____|---.   ___
        |_| |_|       |________|'|_| /__\\\\
""","""




               
         .---.  
       _'   __'             _
      | |  (___)          ,|_|,
      | |     |           _|_|
      |_|  _  |        .-|____|---.   ___
        |_| |_|       |________|'|_| /__\\\\
"""]

def clear(): 
	if name == 'nt': 
		_ = system('cls')
	else: 
		_ = system('clear')

au_fps = 15
clear()
def runanim(window):
	while(True):
		for n in amongus:
			try:
				window.addstr(0, 0, n)
				window.refresh()
				sleep(1/au_fps)
			except KeyboardInterrupt:
				curses.endwin()
				try: sys.exit(0)
				except SystemExit: os._exit(0)
			except:
				curses.endwin()
			
curses.wrapper(runanim)
