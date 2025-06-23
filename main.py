from stats import get_num_words,get_character_counts
import sys

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents

def main():
  if len(sys.argv)!=2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
  book=get_book_text(sys.argv[1])
  num_words=get_num_words(book)
  num_characters=get_character_counts(book)
  print('============ BOOKBOT ============')
  print(f'Analyzing book found at {sys.argv[1]}...')
  print('----------- Word Count ----------')
  print(f'Found {num_words} total words')
  print('--------- Character Count -------')
  for item in num_characters:
    print(f'{item["char"]}: {item["num"]}')
  print('============= END ===============')

main()
