import os

def fanal():
    path = input('Введите путь к необходимой директории: ')
    if !(os.path.exists(path)):
        print('Такого пути не существует, перезапустите программу')
        sys.exit()
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

def fpupp(dictionary):
  dublicates = {}
  for value in dictionary.values():
    identical_size = {}
    for key in dictionary.keys():
      if dictionary[key] == value:
        file_name = os.path.basename(key)
        if file_name in identical_size:
          identical_size[file_name].append(key)
        else:
          identical_size[file_name] = [key]
    for key in identical_size.keys():
      if len(identical_size[key]) > 1:
        dublicates[key] = identical_size[key]
  return dublicates


def fvf(doubles):
  for k, v in dict.items(doubles):
    if v > 1:
      print(k + ': ' + str(v))

if __name__=='__main__':
      print(fvf(fanal())
