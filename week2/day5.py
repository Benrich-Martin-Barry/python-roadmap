def write_lines(path, lines):
  with open(path,"w") as f:
    for line in lines:
      f.write(line+"\n")      
def read_lines(path):
  result = []
  with open(path) as f:
    for line in f:
      result.append(line.strip())
  return result
from pathlib import Path

write_lines("t.txt", ["a", "b"])
assert read_lines("t.txt") == ["a", "b"]
write_lines("t.txt", [])
assert read_lines("t.txt") == []
Path("t.txt").unlink()
print("lines passed")


def write_lines(path, lines):
  with open(path,"w") as f:
    for line in lines:
      f.write(line + "\n")      
def count_lines(path):
  count = 0
  try:
    with open(path) as f:
      for line in f:
        count = count + 1
  except FileNotFoundError:
    return 0
  return count
from pathlib import Path
write_lines("t.txt", ["a", "b", "c"])
assert count_lines("t.txt") == 3
write_lines("t.txt", [])
assert count_lines("t.txt") == 0
Path("t.txt").unlink()
assert count_lines("t.txt") == 0      # the file is gone now
print("count_lines passed")

def write_lines(path, lines):
  with open(path,"w") as f:
    for line in lines:
      f.write(line + "\n")      
def word_count_file(path):
  count = 0
  try:
    count = {}
    with open(path) as f:
      for line in f:
        for w in line.lower().split():
          count[w] = count.get(w, 0) + 1
  except FileNotFoundError:
    return 0
  return count
write_lines("t.txt", ["The cat", "the Hat and the cat"])
assert word_count_file("t.txt") == {"the": 3, "cat": 2, "hat": 1, "and": 1}
write_lines("t.txt", [])
assert word_count_file("t.txt") == {}
Path("t.txt").unlink()
print("word_count_file passed")