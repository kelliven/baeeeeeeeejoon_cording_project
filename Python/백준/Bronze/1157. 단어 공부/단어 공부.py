from collections import Counter
a=input().upper()
counter=Counter(a)
max_counter=max(counter.values())
most=[w for w, s in counter.items() if s==max_counter]
upper_ch=[ch.upper() for ch in most]
if len(most)>1:print("?")
else:print(''.join(upper_ch))