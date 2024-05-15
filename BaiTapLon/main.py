class Meaning:
    def __init__(self, word_type, meaning, example):
        self.word_type = word_type
        self.meaning = meaning
        self.example = example

class Node:
    def __init__(self, meaning):
        self.meaning = meaning
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, meaning):
        if not self.head:
            self.head = Node(meaning)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(meaning)

    # def remove(self, index):
    #     if index == 0:
    #         self.head = self.head.next
    #     else:
    #         prev = None
    #         current = self.head
    #         for i in range(index):
    #             prev = current
    #             current = current.next
    #         prev.next = current.next

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.meaning)
            current = current.next
        return result

class DictionaryEntry:
    def __init__(self, word):
        self.word = word
        self.meanings = {}

    def add_meaning(self, word_type, meaning, example):
        if word_type not in self.meanings:
            self.meanings[word_type] = LinkedList()
        self.meanings[word_type].append(Meaning(word_type, meaning, example))

    def remove_meaning(self, word_type, index):
        if word_type in self.meanings:
            self.meanings[word_type].remove(index)

class Dictionary:
    def __init__(self):
        self.entries = []

    def add_new_entry(self):
        word = input("Enter the word: ")
        existing_entry = next((entry for entry in self.entries if entry.word == word), None)

        while True:
            word_type = input("Enter the word type (noun, verb, adjective, etc.): ")
            meaning = input("Enter the meaning: ")
            example = input("Enter an example: ")

            if existing_entry:
                existing_entry.add_meaning(word_type, meaning, example)
            else:
                entry = DictionaryEntry(word)
                entry.add_meaning(word_type, meaning, example)
                self.entries.append(entry)

            more = input("Do you want to add another meaning for this word? (yes/no): ").lower()
            if more != 'yes':
                break

    def remove_entry(self, word):
        for entry in self.entries:
            if entry.word == word:
                self.entries.remove(entry)
                return True
        return False

    def delete_entry(self, word):
        filename = "N19DCCN105.txt"
        updated_entries = []

        with open(filename, 'r') as f:
            lines = f.readlines()

        word_found = False
        skip = False

        for line in lines:
            if line.strip().startswith("Word:") and line.strip().split(":")[1].strip() == word:
                word_found = True
                skip = True
            elif line.strip().startswith("Word:") and skip:
                skip = False

            if not skip:
                updated_entries.append(line)

        if word_found:
            with open(filename, 'w') as f:
                f.writelines(updated_entries)
            return True

        return False

    def lookup(self, word):
        for entry in self.entries:
            if entry.word == word:
                sorted_meanings = dict(sorted(entry.meanings.items()))
                return sorted_meanings
        return None

    def save_to_file(self):
        filename = "N19DCCN105.txt"
        with open(filename, 'r') as f:
            existing_lines = f.readlines()

        existing_entries = self._load_entries_from_lines(existing_lines)

        with open(filename, 'w') as f:
            merged_entries = {entry.word: entry for entry in existing_entries}

            for entry in self.entries:
                if entry.word in merged_entries:
                    existing_entry = merged_entries[entry.word]
                    for word_type, linked_list in entry.meanings.items():
                        if word_type in existing_entry.meanings:
                            existing_meanings = existing_entry.meanings[word_type].to_list()
                            new_meanings = linked_list.to_list()
                            for new_meaning in new_meanings:
                                if not any(m.meaning == new_meaning.meaning and m.example == new_meaning.example for m in existing_meanings):
                                    existing_entry.meanings[word_type].append(new_meaning)
                        else:
                            existing_entry.meanings[word_type] = linked_list
                else:
                    merged_entries[entry.word] = entry

            sorted_entries = sorted(merged_entries.values(), key=lambda x: x.word)

            for entry in sorted_entries:
                f.write(f"Word: {entry.word}\n")
                sorted_meanings = dict(sorted(entry.meanings.items()))
                for word_type, linked_list in sorted_meanings.items():
                    current = linked_list.head
                    while current:
                        f.write(f"Word Type: {word_type}\n")
                        f.write(f"Meaning: {current.meaning.meaning}\n")
                        f.write(f"Example: {current.meaning.example}\n")
                        current = current.next
                f.write("\n")

        self.reset()
        return filename

    def load_from_file(self):
        filename = "N19DCCN105.txt"
        with open(filename, 'r') as f:
            lines = f.readlines()
            self.entries = self._load_entries_from_lines(lines)
        return filename

    def _load_entries_from_lines(self, lines):
        entries = []
        word = None
        entry = None

        for line in lines:
            line = line.strip()
            if line.startswith("Word:"):
                if entry:
                    entries.append(entry)
                word = line.split(":")[1].strip()
                entry = DictionaryEntry(word)
            elif line.startswith("Word Type:"):
                word_type = line.split(":")[1].strip()
            elif line.startswith("Meaning:"):
                meaning = line.split(":")[1].strip()
            elif line.startswith("Example:"):
                example = line.split(":")[1].strip()
                entry.add_meaning(word_type, meaning, example)

        if entry:
            entries.append(entry)
        return entries

    def reset(self):
        self.entries = []

def main():
    dictionary = Dictionary()

    while True:
        print("\nMenu:")
        print("1. Add a new entry to the dictionary")
        print("2. Remove a dictionary entry")
        print("3. Look up the meaning of an entry in the dictionary")
        print("4. Save dictionary to a file")
        print("5. Load dictionary from a file")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            dictionary.add_new_entry()

        elif choice == '2':
            while True:
                print("\n\t2. Remove a dictionary entry")
                print("(1). Remove entry in the dictionary")
                print("(2). Remove entry in the dictionary from file")
                print("(3). Return to the main menu")
                choice2 = input("Enter your choice: ")

                if choice2 == '1':
                    word = input("Enter the word to remove: ")
                    if dictionary.remove_entry(word):
                        print(f"'{word}' has been successfully removed from the dictionary.")
                        break
                    else:
                        print(f"'{word}' does not exist in the dictionary.")

                elif choice2 == '2':
                    word = input("Enter the word of the entry to be deleted from the dictionary from the file: ")
                    if dictionary.delete_entry(word):
                        print(f"'{word}' has been successfully removed from the dictionary in file.")
                        break
                    else:
                        print(f"'{word}' does not exist in the dictionary.")

                elif choice2 == '3':
                    break

                else:
                    print('Invalid choice. Please choose 1, 2, or 3.')

        elif choice == '3':
            word = input("Enter the word to look up: ")
            meanings = dictionary.lookup(word)
            if meanings:
                for word_type, linked_list in meanings.items():

                    current = linked_list.head
                    while current:
                        print(f"Word Type: {word_type}")
                        print(f"Meaning: {current.meaning.meaning}")
                        print(f"Example: {current.meaning.example}")
                        print()
                        current = current.next
            else:
                print("Word not found in the dictionary.")

        elif choice == '4':
            filename = dictionary.save_to_file()
            print(f"Dictionary saved to file: {filename}")
            dictionary.reset()

        elif choice == '5':
            filename = dictionary.load_from_file()
            print(f"Dictionary loaded from file: {filename}")

        elif choice == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
