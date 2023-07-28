def tally_scores(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

            # Process each line (student record) and print the summary
            for line in lines:
                parts = line.strip().split()
                name = parts[0]
                scores = [int(score) for score in parts[1:]]

                # Print the student's name and test scores
                print(f"{name}: {' '.join(map(str, scores))}")

                # Calculate and print the average score
                average_score = sum(scores) / len(scores)
                print(f"average = {average_score}\n")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    file_name = "./Module 7/records.txt"  # Replace with the name of your input file
    tally_scores(file_name)
