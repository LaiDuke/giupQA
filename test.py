import json
import json_lines

with open("phimle.json", "rb") as read_file:
    data = json.load(read_file)
    for cnt in data:
        print(cnt)

with open('phimle.jl', 'rb') as f:
    item = json_lines.reader(f)
    for tmp in item:
        print(tmp)
