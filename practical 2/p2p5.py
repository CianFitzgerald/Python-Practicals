#(a) when x and y are the same

animals = "herd of animals"
seg = animals[2:2]
print("Segment is", seg)

#(b) when x is greater than y

animals = "herd of animals"
seg = animals[3:1]
print("Segment is", seg)

#(c) when x is omitted

animals = "herd of animals"
seg = animals[:4]
print("Segment is",seg)

#(d) when y is omitted

animals = "herd of animals"
seg = animals[1:15]
print("Segment is", seg)

#(e) when both x and y are omitted

animals = "herd of animals"
seg = animals[:]
print("Segment is", seg)



