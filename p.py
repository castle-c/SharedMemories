import pickle

with open('messages.txt', 'rb+') as f: #rb in read binary
  deserialized = pickle.load(f)

  print(deserialized)
