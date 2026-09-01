from urllib.request import urlopen as get

url = 'https://www.gutenberg.org/files/20727/20727.txt'
with get(url) as response:
    text = response.read().decode('utf-8')
    
    counts = {}
    for word in text.split(' '):
        word = word.strip().lower()
        if len(word) <= 5:
            continue
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    
    counts = sorted([(counts[k], k) for k in counts], reverse=True)
    for count, word in counts[:10]:
        print(f'{word:10} {count}')