from backend.file_manager import FileManager


class Client:

    def __init__(self, name, surname, birthday, mail):
        self.number = None
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.mail = mail
        self.file_path = "lists_json/clients_list.json"
        self.clients = FileManager.load_data(self.file_path)

    def add_client(self):
        new_client = [self.name, self.surname, self.birthday, self.mail]
        self.clients.append(new_client)
        FileManager.save_data(self.file_path, self.clients)

    @staticmethod
    def list_clients():
        clients_list = FileManager.load_data("lists_json/clients_list.json")
        result = "\nClients:\n"

        for c in clients_list:
            result += f"- Name: {c[0]}, Surname: {c[1]}, Birthday: {c[2]}, Mail: {c[3]}\n"

        return result
