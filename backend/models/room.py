from backend.file_manager import FileManager


class Room:

    def __init__(self, number, capacity, price, is_occupied):
        self.number = number
        self.capacity = capacity
        self.price = price
        self.is_occupied = is_occupied
        self.file_path = "rooms_list.json"
        self.rooms = FileManager.load_data(self.file_path)

    def add_room(self):
        new_room = [self.number, self.capacity, self.price, self.is_occupied]
        self.rooms.append(new_room)
        FileManager.save_data(self.file_path, self.rooms)

    def is_available(self):
        for r in self.rooms:
            if r[0] == self.number and not r[3]:
                return True
        return False

    def reserve_room(self):
        for r in self.rooms:
            if r[0] == self.number:
                r[3] = True
                FileManager.save_data(self.file_path, self.rooms)
                return True
        return False

    @staticmethod
    def list_rooms(rooms_list):
        rooms_list = FileManager.load_data("reservations_list.json")
        result = "\nRooms:\n"

        for r in rooms_list:
            result += f"- Number: {r[0]}, Capacity: {r[1]}, Price: {r[2]}, Occupied: {r[3]}\n"

        return result
