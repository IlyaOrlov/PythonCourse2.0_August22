import re

# pattern = re.compile(r"git clone https.*\.git[\"]")
# pattern = re.compile(r"git push")

# pattern = re.compile(r"git [a-z]{3,5} (?:--set-upstream origin .*|\w* \w*|.*.py|.*/.*.git\")")


# pattern = re.compile(r"git [a-z]{3,8} (?:(?:|--set-upstream\s)origin .*|.*.py|.*/.*.git\"|"
#                      r"\w*@.*.git |-\w (?:\w+|\".*\"))")


# pattern = re.compile(r"git [a-z]{3,8} (?:(?:|--set-upstream\s)origin .*|.*.py|https[a-zA-Z0-9_/./:]*\.git|"
#                      r".*@[a-zA-Z0-9_/./:]*\.git|-\w (?:\w+|\".*\"))")

pattern = re.compile(r"git [a-z]{3,8} (?:(?:|--set-upstream\s)origin .*|.*.py|"
                     r"(?:https|.*@)[a-zA-Z0-9_/./:]*\.git"
                     r"|-\w (?:\w+|\".*\"))")

# pattern = re.compile(r"git [a-z]{3,5} (?:|--set-upstream\s)origin .*")
# pattern = re.compile(r"git [a-z]{3,5} ")
# pattern = re.compile(r"git (?:push --set-upstream origin my_branch"
#                                 r"|pull .* .*"
#                                 r"|(?:commit|checkout) -\w (?:\w+|\".*\")"
#                                 r"|add .*.py|push)")


# pattern = re.compile(r"git (?:(?:\w{4} --set-upstream origin my_branch|push)"
#                                 r"|pull .* .*"
#                                 r"|(?:commit|checkout) -\w (?:\w+|\".*\")"
#                                 r"|add .*.py)")

# pattern = re.compile(r"git (?:push"
#                                 r"|pull .* .*"
#                                 r"|(?:commit|checkout) -\w (?:\w+|\".*\")"
#                                 r"|add .*.py)")

with open(r"../../README.md", encoding="utf") as file:
    f = file.read()
print(f)
x = re.findall(pattern, f)
print(x)
