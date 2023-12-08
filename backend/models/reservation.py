from backend.file_manager import FileManager


class Reservation:

    def __init__(self, room_number, client_number, start_date, end_date):
        self.number = None
        self.room_number = room_number
        self.client_number = client_number
        self.start_date = start_date
        self.end_date = end_date
        self.file_path = "reservations_list.json"
        self.reservations = FileManager.load_data(self.file_path)

    def add_reservation(self):
        new_reservation = [self.room_number, self.client_number, self.start_date, self.end_date]
        self.reservations.append(new_reservation)
        FileManager.save_data(self.file_path, self.reservations)

    @staticmethod
    def list_reservations():
        reservations_list = FileManager.load_data("reservations_list.json")
        result = "\nReservations:\n"

        for r in reservations_list:
            result += f"- Room: {r[0]}, Client: {r[1]}, Start date: {r[2]}, End date: {r[3]}\n"

        return result

