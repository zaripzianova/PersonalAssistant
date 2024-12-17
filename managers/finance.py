import json


class FinanceRecord:
    def __init__(self, record_id, category, amount, date, description=None):
        self.id:int = record_id
        self.amount:float = amount
        self.category:str = category
        self.date:str = date
        self.description:str = description

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'category': self.category,
            'date': self.date,
            'description': self.description,
        }

    @staticmethod
    def from_dict(data):
        return FinanceRecord(data['id'], data['amount'], data['category'], data['date'], data['description'])


class FinanceManager:
    def __init__(self, storage_file="data/finance.json"):
        self.storage_file = storage_file
        self.records = self.load_records()

    def load_records(self):
        try:
            with open(self.storage_file, "r") as file:
                return [FinanceRecord.from_dict(record) for record in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return 'Ошибка при загрузке файла'

    def save_records(self):
        with open(self.storage_file, "w") as file:
            json.dump([record.to_dict() for record in self.records], file, indent=4)

    def create_record(self, category, amount, date, description=None):
        record_id = max((record.id for record in self.records), default=0) + 1
        new_record = FinanceRecord(record_id, category, amount, date, description)
        self.records.append(new_record)
        self.save_records()
        return f"Финансовая запись '{category}' была добавлена успешно"

    def list_records(self):
        return self.records

    def view_record(self, record_id):
        return next((record for record in self.records if record.id == record_id), None)

    def delete_record(self, record_id):
        self.records = [record for record in self.records if record.id != record_id]
        self.save_records()
        return f"Финансовая запись '{record_id}' удалена успешно."
