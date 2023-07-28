def print_golf_records(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

            # Process every two lines (name and score) and print the records
            for i in range(0, len(lines), 2):
                name = lines[i].strip()
                score = lines[i+1].strip()
                print(f"Name:{name}")
                print(f"Score:{score}\n")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    file_name = "./Module 7/golf.txt"
    print_golf_records(file_name)
