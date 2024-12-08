import os
from nott import Not

class NotDefteri:
    def __init__(self, filename="notes.txt"):
        self.notes = []
        self.filename = filename
        self.load_notes()

    def add_note(self, content: str):
        new_note = Not(content)
        self.notes.append(new_note)
        self.notes.sort(key=lambda note: note.date)
        self.save_notes()

    def delete_note(self, content: str):
        self.notes = [note for note in self.notes if note.content != content]
        self.save_notes()

    def list_notes(self):
        if not self.notes:
            print("Hiç not bulunmamaktadır.")
        else:
            for note in self.notes:
                print(note)

    def save_notes(self):
        with open(self.filename, "w") as file:
            for note in self.notes:
                file.write(f"{note.date}|{note.content}\n")

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    date, content = line.strip().split("|", 1)
                    self.notes.append(Not(content, date))
