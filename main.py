try:
    def sortByLength(words):
        return sorted(words, key=len)


    with open("newFile", 'r') as f:
        lines = f.readlines()
        print(lines)

        words = []

        for line in lines:
            arr = [str for str in line.split()]
            words.extend(arr)

        words = sortByLength(words)

        with open("b.txt", "w") as f2:
            for word in words:
                word += str(len(word)) + " "
                f2.write(word)




except:
    print('File Not Found')