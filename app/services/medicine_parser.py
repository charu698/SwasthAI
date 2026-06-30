import re


def extract_medicine_names(text: str):

    medicines = []

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) < 3:
            continue

        if re.search(r"[A-Za-z]", line):
            medicines.append(line)

    return medicines