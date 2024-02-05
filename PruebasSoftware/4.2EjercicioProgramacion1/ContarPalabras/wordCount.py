# pylint: disable=C0103
# pylint: disable=W0718
"""
Script - Count Words
"""
import sys
import time

def word_count(file_path):
    """
    Count the frequency of distinct words in a file.

    Args:
        file_path (str): Path to the input file.

    Returns:
        dict: A dictionary containing distinct words as keys and their frequencies as values.
    """
    word_frequency = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.lower()  # Convert to lowercase to treat words case-insensitively
                    word_frequency[word] = word_frequency.get(word, 0) + 1
    except FileNotFoundError as file_error:
        print(f"Error: File not found: {file_error}")
        sys.exit(1)
    except UnicodeDecodeError as decode_error:
        print(f"Error: Unable to decode the file with UTF-8 encoding: {decode_error}")
        sys.exit(1)
    except Exception as e:
        handle_unexpected_error(e)

    return word_frequency

def handle_unexpected_error(error):
    """
    Handle unexpected errors by printing an error message and exiting.

    Args:
        error (Exception): The unexpected error.
    """
    print(f"Unexpected Error: {type(error).__name__}: {error}")
    sys.exit(1)

def print_results(word_freq):
    """
    Print word frequencies to the console with headers.

    Args:
        word_freq (dict): Dictionary containing distinct words and their frequencies.
    """
    print("Row Labels\tCount")
    for word, count in word_freq.items():
        print(f"{word}\t{count}")

def save_results(word_freq, elapsed_time):
    """
    Save word frequencies and elapsed time to a file with headers.

    Args:
        word_freq (dict): Dictionary containing distinct words and their frequencies.
        elapsed_time (float): Time elapsed for the execution.
    """
    with open("WordCountResults.txt", 'w', encoding='utf-8') as results_file:
        results_file.write("Row Labels\tCount\n")
        for word, count in word_freq.items():
            results_file.write(f"{word}\t{count}\n")

        results_file.write(f"\nElapsed Time: {elapsed_time:.2f} seconds")

def main():
    """
    Main function to execute the word count program.
    """
    start_time = time.time()

    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python wordCount.py fileWithData.txt")

        input_file = sys.argv[1]
        word_freq = word_count(input_file)
        print_results(word_freq)
        elapsed_time = time.time() - start_time
        print(f"\nElapsed Time: {elapsed_time:.2f} seconds")
        save_results(word_freq, elapsed_time)
    except Exception as e:
        handle_unexpected_error(e)

if __name__ == "__main__":
    main()
