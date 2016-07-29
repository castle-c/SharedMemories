import sys
import picke


class Margaret:


  def prompt(self):
    note = input("Enter quick note > ")

  def serialize(self):
    with open('notes.txt', 'wb+') as f:
      pickle.dump(self.all_notes, f)

    with open('notes.txt', 'rb') as f:
      binary = f.read()

    return binary
