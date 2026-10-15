a = "the cat and the hat and the bat"
count = {}
words = a.split()
for w in words:
    if w in count:
        count[w] = count[w] + 1
    else:
        count[w] = 1
print(count)
print(count["the"])


marks = {"Asha": 78, "Ravi": 91, "Meena": 85}

top_name = ""
top_mark = -1
for name, mark in marks.items():
    if mark > top_mark:
        top_mark = mark
        top_name = name
print(top_name)