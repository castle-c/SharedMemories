import sys
import pickle


class Mary:

  def __init__(self):
    self.d = {}
    try:
      self.d = self.deserialize()
    except FileNotFoundError:
      pass

  def prompt(self):
    # self.d = {'Mary': []}

    self.deserialize()

    message = input("<")
    # try:
    #   self.d['Mary'].append(message)

    # except KeyError:
    #   pass
    self.d.setdefault("Mary", []).append(message)

    self.serialize()

    print(self.d)



  def serialize(self):
    with open('messages.txt', 'wb+') as f:
      pickle.dump(self.d, f)


  def deserialize(self):
    try:
      with open('messages.txt', 'rb+') as f: #rb in read binary
        self.d = pickle.load(f)


    except FileNotFoundError:
      self.d = {}

      print(self.d)

      return self.d


if __name__ == '__main__':
  mary = Mary()
  mary.prompt()
