# file_integrity_checker
# File Integrity Checker

## What's This About?
Ever wonder if someone’s tampering with your files? This handy Python script keeps an eye on your files by calculating and comparing their hash values. Think of it as your personal file security guard!

## What Can It Do?
- Detects changes in your files
- Tells you when new files appear
- Alerts you when files go missing

## What You Need
- Python 3.x installed
- Basic knowledge of Python and file paths

## Getting Started
1. Grab the script and open it up.
2. Set the directory you want to monitor:
   ```python
   directory = 'path_to_monitor'
   ```
   Replace `'path_to_monitor'` with the actual folder path you want to watch.

3. Run the script:
   ```bash
   python file_integrity_checker.py
   ```

4. The script will take a snapshot of your files and their hash values.

5. Make some changes (add, modify, or delete files) and hit Enter to rescan.

6. The script will show you:
   ```
   Modified files: [list_of_modified_files]
   New files: [list_of_new_files]
   Deleted files: [list_of_deleted_files]
   ```

## Example Output
```
Make some changes and press Enter to re-scan...
Modified files: ['test_directory/file1.txt']
New files: ['test_directory/new_file.txt']
Deleted files: ['test_directory/old_file.txt']
```

## How Does It Work?
1. **Calculate Hash:** It computes a unique hash for each file.
2. **Scan Directory:** It goes through all files in the directory and records their hashes.
3. **Compare Hashes:** It checks for differences between the old and new hash values to spot changes.

## What’s the Catch?
- Only works with local directories.
- You need to manually trigger the rescan.

## What’s Next?
- Automate the scanning process.
- Add logging and reporting features.

## License
MIT License

