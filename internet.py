import socket


def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 443))
        return True
    except OSError:
        pass
    return False


print(is_connected())