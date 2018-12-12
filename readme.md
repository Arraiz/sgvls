#README :)

##Dev

- first create the virtual enviroment
    
        python3 -m venv venv (venv is just the name)
        (if a venv is already created just do)
        source venv/bin/activate

- second install ALL the packages 

        pip install fbs PyQt5==5.9.2 PyInstaller==3.4

- third run the app in dev mode
        
        fbs run
- Somethimes there is usefull to create aliases making the development more friendly

        /<path>/<to>/<proyect>/SignalVisualizer/src/main/python/main.py
        
        
 ##Compiling for platforms
 
 - compile and generate installer 
 
 this will compile all the pips and create the target/ for distributing
 
    fbs freeze
 
 this will generate a executable depending on the platform
 
    fbs installer