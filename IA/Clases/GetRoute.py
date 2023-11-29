import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

def GetRoute(ruta,fichero):
   
    try:
        import google.colab
        IN_COLAB = True
    except:
        IN_COLAB = False
    
    if IN_COLAB:
        # montar el drive, que es donde tenemos el dataset
        from google.colab import drive
        drive.mount("/content/drive")
        data_dir = "/content/drive/MyDrive/2023/Publica/Alumnos/"
        sys.path.append(data_dir)
    else:
        import os
        data_dir = os.path.join(os.path.dirname(os.path.abspath('Carpeta')))
    return data_dir
    