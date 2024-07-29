a, b = map(int, input().split())
wordlist = list(map(str, input().split()))
word =" ".join(wordlist[b:]) + " " + " ".join(wordlist[:b])
print(word)