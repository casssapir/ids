# ids
tiny sequential ids for use in databases

- run with `python ids.py`
- optionally use character count (max 16) and max ids flags. exs/ 
- `python ids.py --char_count 5 --max_ids 100000`
- `python ids.py --char_count 3 --num_ids all`

### Notes
- generate a list of sequential ids for use in a database
- 62 unique characters [0-9][A-Z][a-z]
- follows the Unicode standard for sorting strings [0-9][A-Z][a-z] standard in most DBs and programming languages including Python.
- outputs in batches of 10,000,000 id text files

### Output size

Characters | Max Ids | File Size (MB)
2 | 3,844 | 12 KB
3 | 238,328 | 953 KB
4 | 14,776,336 | 73.9 MB
etc...

