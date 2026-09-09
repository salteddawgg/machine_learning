#Qestion 12. The code snippet in listing 1 reads the plain text of the novel The Cosmic Computer by the famous
#American science fiction writer Henry Beam Piper over the internet and saves it to a string variable text.
#1 from urllib . request import urlopen as get
#2
#3 url = ’ https :// www . gutenberg . org / files /20727/20727. txt ’
#4 with get ( url ) as response :
#5 text = response . read () . decode ( ’utf -8 ’)
#6
#7 print ( text )
#Listing 1. A Python program to download the text of the The Cosmic Computer by Piper.
#Write a Python program that prints out the ten most used words in the novel that have more than 5 letters.
#State your findings. Put your code in a file called frequency.py.



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