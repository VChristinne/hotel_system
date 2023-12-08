from backend.models.client import Client


def main():
    print(Client.list_clients())


if __name__ == '__main__':
    main()
