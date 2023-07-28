def word_stats(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()

            # Count the total number of words
            words = content.split()
            total_words = len(words)

            # Calculate the total length of all words
            total_length = sum(len(word) for word in words)

            # Calculate the average word length
            average_length = total_length / total_words

            print(f"Total words    = {total_words}")
            print(f"Average length = {average_length:.1f}")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    file_name = "quiz.txt"  # Replace with the name of your input file
    word_stats(file_name)
