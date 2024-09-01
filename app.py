import socket
import hashlib

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("server", 8080))

# Receive the file contents and checksum from the server
data = client_socket.recv(1024)
checksum = client_socket.recv(1024)

# Verify the checksum
file_contents = data.decode("utf-8")
calculated_checksum = hashlib.md5(file_contents.encode("utf-8")).hexdigest()
if calculated_checksum == checksum.decode("utf-8"):
    print("Checksum verified!")
else:
    print("Checksum mismatch!")

client_socket.close()
