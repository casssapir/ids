import itertools
import string
import argparse

def generate_unique_ids(char_count, num_ids=None):
    if not 1 <= char_count <= 16:
        raise ValueError("Character count must be between 1 and 16. Given: {}".format(char_count))

    characters = string.digits + string.ascii_uppercase + string.ascii_lowercase
    all_combinations = itertools.product(characters, repeat=char_count)

    if num_ids is None or num_ids == 'all':
        return (''.join(combination) for combination in all_combinations)
    else:
        if int(num_ids) <= 0:
            raise ValueError("Number of IDs must be a positive number or 'all'. Given: {}".format(num_ids))
        return itertools.islice((''.join(combination) for combination in all_combinations), int(num_ids))

def save_ids_to_file(ids, filename_prefix, max_ids_per_file=10000000):
    file_number = 1
    id_count = 0

    file = open(f"{filename_prefix}_{file_number}.txt", 'w')
    print(f"Starting new file: {filename_prefix}_{file_number}.txt")

    for id in ids:
        file.write(id + '\n')
        id_count += 1

        if id_count % 100000 == 0:
            print(f"{id_count} IDs added to {filename_prefix}_{file_number}.txt")

        if id_count >= max_ids_per_file:
            file.close()
            print(f"Finished writing {filename_prefix}_{file_number}.txt")
            file_number += 1
            id_count = 0
            file = open(f"{filename_prefix}_{file_number}.txt", 'w')
            print(f"Starting new file: {filename_prefix}_{file_number}.txt")

    file.close()
    print(f"Finished writing {filename_prefix}_{file_number}.txt")

def main():
    parser = argparse.ArgumentParser(description="Generate a list of unique IDs.")
    parser.add_argument("--char_count", type=int, default=3, help="Number of characters in each ID (between 1 and 16)")
    parser.add_argument("--num_ids", default='all', help="Number of IDs to generate or 'all' for no limit")
    args = parser.parse_args()

    # Convert num_ids to None if it's 'all'
    num_ids = None if args.num_ids == 'all' else int(args.num_ids)

    unique_ids = generate_unique_ids(args.char_count, num_ids)
    filename_prefix = 'ids'
    save_ids_to_file(unique_ids, filename_prefix)

    print(f"Unique IDs have been saved to {filename_prefix}_*.txt files")

if __name__ == "__main__":
    main()
