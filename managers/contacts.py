import csv
import json


class Contact:
    def __init__(self, id, name, phone, email):
        self.id: int = id
        self.name: str = name
        self.phone: str = phone
        self.email: str = email

    @staticmethod
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }

    @staticmethod
    def from_dict(contact_dict):
        contact = Contact(contact_dict['id'], contact_dict['name'], contact_dict['phone'], contact_dict['email'])
        return contact

class ContactManager:
    def __init__(self, contacts_path='..data/contacts.json'):
        self.contacts_path: str = contacts_path
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.contacts_path, "r") as file:
                return [contact.from_dict() for contact in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return 'Ошибка при загрузке файла'

    def save_contacts(self):
        with open(self.contacts_path, "w") as file:
            json.dump([note.to_dict() for note in self.contacts], file, indent=4)

    def create_contact(self, name, phone, email):
        contact_id = max((contact.id for contact in self.contacts), default=0) + 1
        new_note = Contact(contact_id, name, phone, email)
        self.contacts.append(new_note)
        self.save_contacts()
        return f'Контакт с id={contact_id} был создан'

    def list_contacts(self):
        return self.contacts

    def see_contact(self, contact_id):
        return next((contact for contact in self.contacts if contact.id == contact_id), None)

    def update_contact(self, contact_id, new_name=None, new_phone=None, new_email=None, new_address=None):
        contact = self.see_contact(contact_id)
        if contact:
            if new_name:
                contact.name = new_name
            if new_phone:
                contact.phone = new_phone
            if new_email:
                contact.email = new_email
            if new_address:
                contact.address = new_address
            self.save_contacts()
            return f"Контакт {contact_id} обновлен успешно"
        return f"Контакт с id={contact_id} не найден"

    def export_to_csv(self, file_path):
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=['id', 'name', 'phone', 'email']
            )
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.to_dict())
        return f"Контакты загружены в файл={file_path}."

    def import_from_csv(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    contact = Contact.from_dict(
                        {
                            'id': int(row['id']),
                            'name': row['name'],
                            'phone': row['phone'],
                            'email': row['email']
                        }
                    )
                    self.contacts.append(contact)
            return f'Контакты были успешно выгружен с файла={file_path}'
        except FileNotFoundError:
            return f'Файл={file_path} не найден'


    def delete_contact(self, contact_id):
        self.contacts = [contact for contact in self.contacts if contact.id != contact_id]
        self.save_contacts()
        return f'Контакт с id={contact_id} был успешно удален'


