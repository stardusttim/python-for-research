# pathlib
from pathlib import Path

p = Path('.')  # current directory

print([x for x in p.iterdir() if x.is_dir()])

print(list(p.glob('**/*.py')))

p = Path('C:/Windows')  # Windows
q = p / 'notepad.exe'

print(q)
print(q.resolve())

print(q.exists())
print(q.is_dir())

p = Path('.') / 'exercises' / 'test.txt'
p.write_text('This is a test.\nGood', encoding='utf-8')

with p.open(encoding='utf-8') as f: 
    print(f.readline())
    
with p.open(encoding='utf-8') as f: 
    print(f.read())
    
print(p.read_text(encoding='utf-8'))