log_file = "/home/endo/workspace/logs/logs.txt"

def log_write(input: str):
    print(input)
    with open(log_file, "a") as file:
        file.write(f"{input}\n")