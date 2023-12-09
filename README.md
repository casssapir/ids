# ids
tiny sequential ids for use in databases

- run with `python ids.py`
- optionally use character count (max 16) and max ids flags. exs/ 
- `python ids.py --char_count 5 --max_ids 100000`
- `python ids.py --char_count 3 --num_ids all`

### Notes
- generate a list of sequential ids for use in a database
- smallest possible file size
- 62 unique characters [0-9][A-Z][a-z]
- variables for 
- follows the Unicode standard for sorting strings [0-9][A-Z][a-z] standard in most DBs and programming languages including Python.

### Output size

Characters | Max Ids | File Size (MB)
2 | 3,844 | 12 KB
3 | 238,328 | 953 KB
4 | 14,776,336 | 73.9 MB

Each ID is followed by a newline character. 
Assuming a newline character is 1 byte, each ID+newline pair takes char_count + 1 bytes.