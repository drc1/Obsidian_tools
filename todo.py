import os
notes_path = "/Users/daniel/Library/Mobile Documents/9CR7T2DMDG~com~ngocluu~onewriter/Documents/"
# notes_path = "/Users/Daniel/Obsidian_Test/"
content = ""
for path, dirs, files in os.walk(notes_path):
    for filename in files:
        if (filename[-3:] == ".md") and (filename != "TODO.md"):
            f = open(notes_path + filename, "r")
            lines = f.readlines()
            for line in lines:
                if line.find("- [ ]") == 0:
                    line = line.replace('\n', '')
                    content = content + line + " [[" + filename[:-3] + "]]" + '\n'
            f.close()
print(content)
f = open(notes_path + 'TODO.md', "+w")
f.write(content)
f.close()
