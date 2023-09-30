import os
import time

# Define the named pipe (FIFO) file path
pipe_name = "message_pipe"

# Create the named pipe (FIFO) if it doesn't exist
if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)

# Open the named pipe for reading
pipe_fd = os.open(pipe_name, os.O_RDONLY)

try:
    while True:
        # Read a message from the named pipe
        message = os.read(pipe_fd, 512).decode("utf-8").strip()
        
        if message == "exit":
            print("Server exiting...")
            break

        # Process the received message (application logic)
        print(f"Received message from client: {message}")

finally:
    # Close the named pipe
    os.close(pipe_fd)
    # Remove the named pipe (FIFO) file
    os.unlink(pipe_name)

