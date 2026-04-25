import time

def calculate_view_score(file):
    """
    Simulated 'view count'
    Higher score = more frequently accessed
    """
    current_time = time.time()

    last_access_days = (current_time - file["last_access"]) / (60 * 60 * 24)
    last_modified_days = (current_time - file["last_modified"]) / (60 * 60 * 24)

    score = 0

    # Recent access → high score
    if last_access_days < 1:
        score += 5
    elif last_access_days < 7:
        score += 3
    elif last_access_days < 30:
        score += 1

    # Modified recently → also important
    if last_modified_days < 7:
        score += 2

    return score

def analyze_files(files):
    important = []
    junk = []

    current_time = time.time()

    for file in files:
        score = calculate_view_score(file)

        days_unused = (current_time - file["last_access"]) / (60 * 60 * 24)
        file["days_unused"] = int(days_unused)
        file["view_score"] = score

        if score >= 4:
            important.append(file)
        else:
            junk.append(file)

    return important, junk