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

class BSTNode:
    def __init__(self, entry):
        self.entry = entry
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, entry):
        if self.root is None:
            self.root = BSTNode(entry)
        else:
            self._insert(self.root, entry)

    def _insert(self, node, entry):
        if entry.word < node.entry.word:
            if node.left is None:
                node.left = BSTNode(entry)
            else:
                self._insert(node.left, entry)
        elif entry.word > node.entry.word:
            if node.right is None:
                node.right = BSTNode(entry)
            else:
                self._insert(node.right, entry)

    def find(self, word):
        return self._find(self.root, word)

    def _find(self, node, word):
        if node is None:
            return None
        if word == node.entry.word:
            return node.entry
        elif word < node.entry.word:
            return self._find(node.left, word)
        else:
            return self._find(node.right, word)

    def delete(self, word):
        self.root, deleted = self._delete(self.root, word)
        return deleted

    def _delete(self, node, word):
        if node is None:
            return node, False

        if word < node.entry.word:
            node.left, deleted = self._delete(node.left, word)
        elif word > node.entry.word:
            node.right, deleted = self._delete(node.right, word)
        else:
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            min_larger_node = self._find_min(node.right)
            node.entry = min_larger_node.entry
            node.right, _ = self._delete(node.right, min_larger_node.entry.word)
            return node, True

        return node, deleted

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def in_order_traversal(self, node=None, entries=None):
        if entries is None:
            entries = []
        if node is None:
            node = self.root
        if node is not None:
            if node.left is not None:
                self.in_order_traversal(node.left, entries)
            entries.append(node.entry)
            if node.right is not None:
                self.in_order_traversal(node.right, entries)
        return entries

class HashTable:
    def __init__(self, size=26):
        self.size = size
        self.table = [None] * size

    def _hash(self, word):
        return ord(word[0].lower()) - ord('a')

    def insert(self, entry):
        index = self._hash(entry.word)
        if self.table[index] is None:
            self.table[index] = BST()
        self.table[index].insert(entry)

    def find(self, word):
        index = self._hash(word)
        if self.table[index] is not None:
            return self.table[index].find(word)
        return None

    def delete(self, word):
        index = self._hash(word)
        if self.table[index] is not None:
            return self.table[index].delete(word)
        return False

    def in_order_traversal(self):
        entries = []
        for bst in self.table:
            if bst is not None:
                entries.extend(bst.in_order_traversal())
        return entries

class Dictionary:
    def __init__(self):
        self.hash_table = HashTable()

    def add_new_entry(self):
        while True:
            word = input("Enter the word: ").strip()
            if not word:
                print("Word cannot be blank. Please enter a valid word.")
                continue
            break

        existing_entry = self.hash_table.find(word)

        if existing_entry is None:
            existing_entry = DictionaryEntry(word)
            self.hash_table.insert(existing_entry)

        while True:
            while True:
                word_type = input("Enter the word type: ").strip()
                if not word_type:
                    print("Word type cannot be blank. Please enter a valid word type.")
                    continue
                break

            while True:
                meaning = input("Enter the meaning: ").strip()
                if not meaning:
                    print("Meaning cannot be blank. Please enter a valid meaning.")
                    continue
                break

            while True:
                example = input("Enter an example: ").strip()
                if not example:
                    print("Example cannot be blank. Please enter a valid example.")
                    continue
                break

            existing_entry.add_meaning(word_type, meaning, example)

            more = input("Do you want to add another meaning for this word? (yes/no): ").lower().strip()
            if more != 'yes':
                break

    def remove_entry(self, word):
        return self.hash_table.delete(word)

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
        entry = self.hash_table.find(word)
        if entry:
            sorted_meanings = dict(sorted(entry.meanings.items()))
            return sorted_meanings
        return None

    def save_to_file(self):
        filename = "N19DCCN105.txt"

        # Load existing entries from file
        existing_entries = []
        if self._file_exists(filename):
            with open(filename, 'r') as f:
                existing_entries = self._load_entries_from_lines(f.readlines())

        # Merge existing entries with the current hash table entries
        merged_entries = {entry.word: entry for entry in existing_entries}
        new_entries = self.hash_table.in_order_traversal()
        for entry in new_entries:
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

        # Save all merged entries to file
        sorted_entries = sorted(merged_entries.values(), key=lambda x: x.word)
        with open(filename, 'w') as f:
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

    # def load_from_file(self):
    #     filename = "N19DCCN105.txt"
    #     with open(filename, 'r') as f:
    #         lines = f.readlines()
    #         entries = self._load_entries_from_lines(lines)
    #         for entry in entries:
    #             self.hash_table.insert(entry)
    #     return filename

    def load_from_file(self):
        filename = "N19DCCN105.txt"
        with open(filename, 'r') as f:
            lines = f.readlines()

        # Load existing entries from file
        existing_entries = self._load_entries_from_lines(lines)

        # Merge existing entries with the current hash table entries
        for entry in existing_entries:
            existing_entry = self.hash_table.find(entry.word)
            if existing_entry:
                # Merge meanings if the entry already exists in the hash table
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
                self.hash_table.insert(entry)

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

    def _file_exists(self, filename):
        try:
            with open(filename, 'r'):
                return True
        except FileNotFoundError:
            return False

    def reset(self):
        self.hash_table = HashTable()

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
                    while True:
                        word = input("Enter the word to remove: ").strip()
                        if not word:
                            print("Word cannot be blank. Please enter a valid word.")
                            continue
                        break

                    if dictionary.remove_entry(word):
                        print(f"'{word}' has been successfully removed from the dictionary.")
                        break
                    else:
                        print(f"'{word}' does not exist in the dictionary.")

                elif choice2 == '2':
                    while True:
                        word = input("Enter the word of the entry to be deleted from the dictionary from the file: ").strip()
                        if not word:
                            print("Word cannot be blank. Please enter a valid word.")
                            continue
                        break

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
            while True:
                word = input("Enter the word to look up: ").strip()
                if not word:
                    print("Word cannot be blank. Please enter a valid word.")
                    continue
                break

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
