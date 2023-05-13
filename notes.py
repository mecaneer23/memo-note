#!/usr/bin/env python3


import sys
import json
import os


def md_table_to_lines(
    first_line_idx: int,
    last_line_idx: int,
    filename: str = "README.md",
    remove: list[str] = [],
    column_count: int = 2,
):
    # get raw lines
    with open(str(filename)) as f:
        lines = f.readlines()[first_line_idx - 1 : last_line_idx - 1]

    # remove unwanted characters
    for i, _ in enumerate(lines):
        for item in remove:
            lines[i] = lines[i].replace(item, "")
        lines[i] = lines[i].split("|")[1:-1]
    # lines[1] = ["-" for _ in range(column_count)]

    # make lists of columns
    columns = [[0, []] for _ in range(column_count)]
    for i in range(column_count):
        for line in lines:
            columns[i][1].append(line[i])

    # find max length of each column
    for i, (_, v) in enumerate(columns):
        columns[i][0] = len(max([w.strip() for w in v], key=len))
    lines[1] = ["-" * (l + 1) for l, _ in columns]

    # join lines together
    for i, line in enumerate(lines):
        for j, v in enumerate(line):
            line[j] = v.lstrip() + v[-1]
        lines[i] = "".join(lines[i])
    return lines


def load_notes(filename="notes.json"):
    """Load notes from a JSON file."""
    with open(filename) as f:
        return json.load(f)


def add_note(notes, title_and_note):
    if len(title_and_note) < 2:
        print("Make sure to add both a title and memo")
        return
    title = title_and_note[0]
    note = " ".join(title_and_note[1:])
    notes[title] = note
    print(f"Added title: {title}, with note: {note}")
    return notes


def remove_note(notes, title):
    if title not in notes:
        print("Can't remove a note that doesn't exist")
        return notes
    notes.pop(title)
    print(f"Removed {title}")
    return notes


def save_notes(notes):
    with open("notes.json", "w") as f:
        json.dump(notes, f, indent=4)


def list_notes(notes):
    if not notes.keys():
        print("No stored memos")
        return
    print("\n".join(notes.keys()))


def show_note(notes, title):
    if title not in notes.keys():
        print("Can't show a note that doesn't exist")
        return
    print(notes[title])


def run(args):
    notes = load_notes()
    command = args[0]
    if command in ("help", "h"):
        print("\n".join(md_table_to_lines(7, 17, column_count=3)))
    elif command in ("add", "a"):
        notes = add_note(notes, args[1:])
    elif command in ("remove", "r"):
        if len(args) < 2:
            print("Make sure to include a note to remove")
        notes = remove_note(notes, args[1])
    elif command in ("list", "l", "ls"):
        list_notes(notes)
    elif command in ("rawlist", "rl"):
        print(notes)
    elif command in ("show", "s"):
        if len(args) < 2:
            print("Make sure to include a note to show")
            return
        show_note(notes, args[1])
    elif command in ("exit", "e", "q"):
        exit()
    elif command in ("clear", "c", "cls"):
        os.system("cls" if os.name == "nt" else "clear")
    else:
        print("Invalid command; input [help] for a list of commands")


def main():
    if len(sys.argv) <= 1:
        while True:
            run(input(">>> ").lower().split(" "))
    else:
        run(sys.argv[1:])


if __name__ == "__main__":
    main()
