# Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

# result = info.split(":")
# result = "+".join(result)
result = info.replace(':','+')

print(result)
