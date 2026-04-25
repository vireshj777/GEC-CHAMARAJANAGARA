import os
import hashlib


def fast_hash(path):
    try:
        with open(path, "rb") as f:
            return hashlib.md5(f.read(4096)).hexdigest()
    except:
        return None


def find_duplicates(files):
    hash_map = {}
    duplicates = []

    for f in files:
        path = f.get("path")

        if not path or not os.path.exists(path):
            continue

        h = fast_hash(path)

        if not h:
            continue

        if h in hash_map:
            if hash_map[h] not in duplicates:
                duplicates.append(hash_map[h])
            duplicates.append(path)
        else:
            hash_map[h] = path

    return duplicates