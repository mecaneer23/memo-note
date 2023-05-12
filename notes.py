#!/usr/bin/env python3


import sys
import json
import os


def md_table_to_lines(filename, first_line_idx, last_line_idx, remove=[]):
    with open(str(filename)) as f:
        lines = f.readlines()[first_line_idx - 1 : last_line_idx - 1]
    for i, _ in enumerate(lines):
        for item in remove:
            lines[i] = lines[i].replace(item, "")
        lines[i] = lines[i].split("|")[1:-1]
    lines[1] = ("-", "-")
    key_max = len(max([k.strip() for k, _ in lines], key=len))
    value_max = len(max([v.strip() for _, v in lines], key=len))
    lines[1] = ("-" * (key_max + 2), "-" * value_max)
    for i, (k, v) in enumerate(lines):
        lines[i] = (k.strip() + " " * (key_max - len(k.strip()) + 2) + v.strip()).ljust(
            key_max + value_max + 2
        )
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


def run(single_instance=False):
    notes = load_notes()
    input_args = sys.argv[1:] if single_instance else input(">>> ").lower().split(" ")
    command = input_args[0]
    if command in ("help", "h"):
        print(
            md_table_to_lines("README.md", 7, 17)
        )  # TODO: make sure these are the right numbers
    elif command in ("add", "a"):
        notes = add_note(notes, input_args[1:])
    elif command in ("remove", "r"):
        if len(input_args) < 2:
            print("Make sure to include a note to remove")
        notes = remove_note(notes, input_args[1])
    elif command in ("list", "l", "ls"):
        list_notes(notes)
    elif command in ("rawlist", "rl"):
        print(notes)
    elif command in ("show", "s"):
        if len(input_args) < 2:
            print("Make sure to include a note to show")
            return
        show_note(notes, input_args[1])
    elif command in ("exit", "e"):
        exit()
    elif command in ("clear", "c", "cls"):
        os.system("cls" if os.name == "nt" else "clear")
    else:
        print("Invalid command; input [help] for a list of commands")


def main():
    if len(sys.argv) > 1:
        while True:
            run()
    else:
        run(True)


if __name__ == "__main__":
    main()
