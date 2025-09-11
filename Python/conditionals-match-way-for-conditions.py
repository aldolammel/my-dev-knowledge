def handle_command(command):
    match command:
        case "start":
            return "Starting the process..."
        case "stop":
            return "Stopping the process..."
        case "restart":
            return "Restarting..."
        case _:
            return "Unknown command"

print(handle_command("start"))  # Output: Starting the process...