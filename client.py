import os

# Define the named pipe (FIFO) file path
pipe_name = "message_pipe"

try:
    # Open the named pipe for writing
    pipe_fd = os.open(pipe_name, os.O_WRONLY)

    while True:
        # Get user input for the message
        message = input("Enter a message (type 'exit' to quit): ")

        # Write the message to the named pipe
        os.write(pipe_fd, message.encode("utf-8"))

        if message == "exit":
            break

finally:
    # Close the named pipe
    os.close(pipe_fd)

