import string

def analyze_text(input_filename, output_filename):
    line_count = 0
    word_count = 0
    word_freq = {}

    try:
        # Opening and reading file
        with open(input_filename, 'r', encoding='utf-8') as file:
            for line in file:
                line_count += 1
                
                # Remove punctuation and convert to lowercase
                clean_line = line.translate(str.maketrans('', '', string.punctuation)).lower()
                
                # Split into words
                words = clean_line.split()
                word_count += len(words)
                
                # Count frequency
                for word in words:
                    word_freq[word] = word_freq.get(word, 0) + 1

        # Saving results
        with open(output_filename, 'w', encoding='utf-8') as out_file:
            out_file.write(f"Total Lines: {line_count}\n")
            out_file.write(f"Total Words: {word_count}\n")
            out_file.write("\nWord Frequencies:\n")
            # Sorting frequencies for a cleaner output
            for word, freq in sorted(word_freq.items()):
                out_file.write(f"{word}: {freq}\n")
                
        print(f"Saved to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")

if __name__ == "__main__":
    analyze_text('text.txt', 'analysis.txt')