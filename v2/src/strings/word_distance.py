
strings = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
distance = len(strings)

word_1_index = word_2_index =-1

for word in range(0, len(strings)):
    if word1 == strings[word]:
        word_1_index = word
        print("word 1 index" + str(word_1_index))
        if word_2_index > 0:
            distance = min(distance, abs(word_2_index-word_1_index))
            print("Distance" + str(distance))
            
    
    if word2 == strings[word]:
        word_2_index = word
        print("word 2 index" + str(word_2_index))
        if word_1_index > 0:
            distance = min(distance, abs(word_2_index-word_1_index))
            
            print("Distance" + str(distance))

# print("The distance between 2 words in array " + str(distance)) 
