import os

def fanal():
  pass

def fps():
  pass

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

def fvf():
  pass
