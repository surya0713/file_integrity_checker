import hashlib
import os


def calculate_hash(file_path, algorithm='sha256'):
    hash_func = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def scan_directory(directory_path, algorithm='sha256'):
    file_hashes = {}
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path, algorithm)
            file_hashes[file_path] = file_hash
    return file_hashes


def compare_hashes(old_hashes, new_hashes):
    changes = {
        'modified': [],
        'new': [],
        'deleted': []
    }

    for file, new_hash in new_hashes.items():
        old_hash = old_hashes.get(file)
        if old_hash is None:
            changes['new'].append(file)
        elif old_hash != new_hash:
            changes['modified'].append(file)

    for file in old_hashes:
        if file not in new_hashes:
            changes['deleted'].append(file)

    return changes


if __name__ == "__main__":
    # Directory to monitor
    directory = 'path_to_monitor'

    # Initial scan
    old_hashes = scan_directory(directory)

    # Simulate some file changes and re-scan
    input("Make some changes and press Enter to re-scan...")
    new_hashes = scan_directory(directory)

    # Compare the hashes
    changes = compare_hashes(old_hashes, new_hashes)

    # Output the results
    print("Modified files:", changes['modified'])
    print("New files:", changes['new'])
    print("Deleted files:", changes['deleted'])
