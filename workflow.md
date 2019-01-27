#Guia de desarrollo de Signal Visualizer

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
        
##Basic proyect strunture

In order to be multiplatform the structure of files is a little bit special 



 ##Compiling for platforms
 
 - compile and generate installer 
 
 this will compile all the pips and create the target/ for distributing
 
    fbs freeze
 
 this will generate a executable depending on the platform
 
    fbs installer

###Creacion de un modulo nuevo

en Signal Visualizer cada package consta de 3 scripts basicos aunque pueden ser mas

    ├── mi_modulo
       ├── __init__.py
       └── nombre_del_modulo.ui
       └── nombre_del_modulo.py 
       └── nombre_del_modulo_logic.py
       
the files at the root (files inside python folder) are not a package so NOT PUT A __init__.py file there


el fichero **nombre_del_modulo.ui** generado con QtCreator sera la base de la interfaz
**nombre_del_modulo.py** sera generado automaticamente con 
        
        pyuic5 nombre_del_modulo.ui -o nombre_del_modulo.py
        
**nombre_del_modulo_logic** contendra toda la logica que implementemos en la interfaz





