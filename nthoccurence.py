def nth_occurence(list, word, n):
    count = 0
    for i in range(len(list)):
        if list[i] == word:
            count += 1
            if count == n:
                del list[i] # remove the nth occurence
                return list  # stop after removing
            
    return list # Return the list unchanged if nth occurence is not found

words = ["apple","banana","apple","orange","apple","banana"]

print(nth_occurence(words , "apple" , 2))  #['apple', 'banana', 'orange', 'apple', 'banana']