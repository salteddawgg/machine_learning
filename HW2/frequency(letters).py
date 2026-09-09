



from urllib.request import urlopen as get

url = 'https://www.gutenberg.org/files/20727/20727.txt'
with get(url) as response:
    text = response.read().decode('utf-8').lower()
    
    counts = {}
    
    for char in text:
        if char.isalpha():
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
    
    for char in sorted(counts):
        print(f'{char}: {counts[char]}')