import os

# write
# with open('file1.txt', 'w') as f:
#     f.write('Hello, World!')

print(os.path.dirname(__file__))
print(os.path.abspath(__file__))

with open('file1.txt', 'r') as f:
    content = f.read()
for i in range(10):
    print(content)