from datetime import datetime
import json


class Note:
    def __init__(self, id, title, content):
        self.id: int = id
        self.title: str = title
        self.content: str = content
        self.timestamp: str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp
        }

    @staticmethod
    def from_dict(data):
        note = Note(data['id'], data['title'], data['content'])
        note.timestamp = data['timestamp']
        return note


class NoteManager:
    def __init__(self, notes_path='data/notes.json'):
        self.notes_path: str = notes_path
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.notes_path, "r") as file:
                data = json.load(file)
                notes = []
                for note_data in data:
                    try:
                        notes.append(Note.from_dict(note_data))
                    except Exception as e:
                        print(f"Ошибка при создании заметки из данных {note_data}: {e}")
                return notes
        except (FileNotFoundError, json.JSONDecodeError):
            print("Ошибка при загрузке файла. Возвращается пустой список.")
            return []

    def save_notes(self):
        with open(self.notes_path, "w") as file:
            json.dump([note.to_dict() for note in self.notes], file, indent=4)

    def create_note(self, title, content):
        note_id = max((note.id for note in self.notes), default=0) + 1
        new_note = Note(note_id, title, content)
        self.notes.append(new_note)
        self.save_notes()
        return f'Заметка с id={note_id} была создана'

    def see_list_notes(self):
        return self.notes

    def see_note(self, note_id):
        return next((note for note in self.notes if note.id == note_id), None)

    def update_note(self, note_id, title=None, content=None):
        note = self.see_note(note_id)
        if note:
            if title:
                note.title = title
            if content:
                note.content = content
            note.timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.save_notes()
            return f'Заметка с id={note_id} была успешно обновлена'
        else:
            return f'Заметка с id={note_id} не найдена'

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()
        return f'Заметка с id={note_id} была успешно удалена'


