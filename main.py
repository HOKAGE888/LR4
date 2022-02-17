import os

def fanal():
    path = input('Введите путь к необходимой директории: ')
    path.replace('/', '\\')
    return path

def fps():
  for filename in os.listdir(path):
        try:
            path_to_file = os.path.join(path, filename)
            if os.path.isdir(path_to_file):
                fps(path_to_file)
            else:
                dictionary[path_to_file] = os.path.getsize(path_to_file)
        except PermissionError:
            pass
    return dictionary
def fpupp():
  pass

def fvf():
  pass

