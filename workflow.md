#Guia de desarrollo de Signal Visulizer


###Creacion de un modulo nuevo

en Signal Visualizer cada package consta de 3 scripts basicos aunque pueden ser mas

    ├── mi_modulo
       ├── __init__.py
       └── nombre_del_modulo.ui
       └── nombre_del_modulo.py 
       └── nombre_del_modulo_logic.py


el fichero **nombre_del_modulo.ui** generado con QtCreator sera la base de la interfaz
**nombre_del_modulo.py** sera generado automaticamente con 
        
        pyuic5 nombre_del_modulo.ui -o nombre_del_modulo.py
        
**nombre_del_modulo_logic** contendra toda la logica que implementemos en la interfaz



###Creacion de nuevos dialogos

