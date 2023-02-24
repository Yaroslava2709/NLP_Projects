import spacy

# Code extract 1
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''
What you found interesting about the similarities between cat, monkey and banana?
(1) Similarity between cat and monkey is 0.59 which is quite high because they are both animals.
(2) Similarity between monkey and banana is 0.40 which is quite high as well as we assume that the model already puts 
together that monkeys eat bananas.
(3) Similarity between cat and banana is 0.22 which is low. 
We can assume that cats do not eat bananas and cat is an animal while banana is a fruit.
'''

# Own example
nlp = spacy.load('en_core_web_md')
word1 = nlp("car")
word2 = nlp("wheel")
word3 = nlp("road")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''
What you found interesting about the similarities between car, wheel and plant?
(1) Similarity between car and wheel is 0.53 which is quite high because cars usually have wheels.
(2) Similarity between wheel and road is 0.33 which is quite low, however we can assume that the model puts 
together that cars have wheels and they drive on the roads.
(3) Similarity between car and road is 0.44, 
we can assume that the model recognises the relationships between car and road as the cars drive on the roads. 
'''

# Code extract 2
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Code extract 3
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"
             ]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ",  similarity)

'''
What you notice is different from model ‘en_core_web_sm’ compare with the model 'en_core_web_md'?

First of all, sm/md - refer to the sizes of the models (small, medium respectively).

When I run the example.py with sm model I got the UserWarning message: The model you're using has no word vectors loaded, 
so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity. 
This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors 
and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead.

Also I noticed that the models differences are statistical. 
md model provides with better and more accurate result overall. 
'''
