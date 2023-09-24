
def mergeAlternate(word1: str, word2: str):
    res = []
    if len(word1) > len(word2):
        for i in range(len(word1)):
            if i<len(word2):
                    res.append(word1[i])
                    res.append(word2[i])
            else:
                res.append(word1[i:])
                break
    else:
        for i in range(len(word2)):
            if i<len(word1):
                    res.append(word1[i])
                    res.append(word2[i])
            else:
                res.append(word2[i:])
                break
    
    return ''.join(res)

if __name__ == '__main__':
    print(mergeAlternate("ab", "pqrb"))