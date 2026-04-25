import os
import string


def get_all_drives():
    drives = []
    for letter in string.ascii_uppercase:
        drive = f"{letter}:\\"
        if os.path.exists(drive):
            drives.append(drive)
    return drives


def scan_directory(path=None):
    file_list = []

    # If no path → scan all drives
    paths = [path] if path else get_all_drives()

    for base_path in paths:
        for root, dirs, files in os.walk(base_path, topdown=True):

            # ✅ SKIP SYSTEM/PROTECTED FOLDERS (VERY IMPORTANT)
            dirs[:] = [d for d in dirs if not d.startswith("$") and d not in [
                "Windows", "Program Files", "Program Files (x86)", "System Volume Information"
            ]]

            for file in files:
                try:
                    full_path = os.path.join(root, file)

                    # ✅ FAST SAFE STAT
                    stat = os.stat(full_path, follow_symlinks=False)

                    file_list.append({
                        "path": full_path,
                        "name": file,
                        "size": stat.st_size,
                        "last_access": stat.st_atime,
                        "last_modified": stat.st_mtime
                    })

                except (PermissionError, FileNotFoundError, OSError):
                    continue

    return file_list