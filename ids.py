# Run wiht optional flags. For example: --char_count 3 --max_ids 1000

import itertools
import string
import argparse

def generate_unique_ids(char_count, max_ids=1000):
    if not 1 <= char_count <= 16:
        raise ValueError("Character count must be between 1 and 16")
    if max_ids <= 0:
        raise ValueError("Max IDs must be a positive number")

    characters = string.ascii_lowercase + string.digits  # a-z and 0-9
    all_combinations = list(itertools.product(characters, repeat=char_count))
    sorted_ids = sorted(''.join(combination) for combination in all_combinations)
    return sorted_ids[:max_ids]

def save_ids_to_file(ids, filename):
    with open(filename, 'w') as file:
        for id in ids:
            file.write(id + '\n')

def main():
    parser = argparse.ArgumentParser(description="Generate a list of unique IDs.")
    parser.add_argument("--char_count", type=int, default=3, help="Number of characters in each ID (between 1 and 16)")
    parser.add_argument("--max_ids", type=int, default=1000, help="Maximum number of IDs to generate")
    args = parser.parse_args()

    # Generate and save the unique IDs
    unique_ids = generate_unique_ids(args.char_count, args.max_ids)
    filename = 'ids.txt'
    save_ids_to_file(unique_ids, filename)
    print(f"Unique IDs have been saved to {filename}")

if __name__ == "__main__":
    main()
