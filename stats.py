def get_num_words(book):
  num_words=book.split()
  return len(num_words)

def sort_on(items):
    return items["num"]

def get_character_counts(text):
  result={}
  for char in text.lower():
    if char.isalpha():
      if char in result:
        result[char]+=1
      else:
        result[char] = 1
  sorted_list = [{"char": char, "num": count} for char, count in result.items()]
  sorted_list.sort(reverse=True,key=sort_on)
  return sorted_list
