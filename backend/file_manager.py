import fcntl
import json


class FileManager:
    @staticmethod
    def load_data(file_path):
        file = open(file_path, "r")
        try:
            fcntl.lockf(file, fcntl.LOCK_SH)  # add read lock
            return json.load(file)
        except FileNotFoundError:
            return []
        finally:
            fcntl.lockf(file, fcntl.LOCK_UN)  # releasing the lock after reading
            file.close()  # ensure that the file is closed correctly

    @staticmethod
    def save_data(file_path, data):
        file = open(file_path, "w")
        try:
            fcntl.lockf(file, fcntl.LOCK_EX)  # add write lock
            json.dump(data, file)
        except FileNotFoundError:
            return []
        finally:
            fcntl.lockf(file, fcntl.LOCK_UN)  # releasing the lock after writing
            file.close()  # ensure that the file is closed correctly
