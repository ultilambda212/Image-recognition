class TextClass:
    def readText(self, filePath):
        f = open(filePath, "r")
        if f.mode != 'r':
            print('The file could not be opened in read mode.')
            exit(0)

        fileContents = f.readlines()
        f.close()

        imageNames = []
        imageLabels = []
        numberOfImages = len(fileContents)
        for i in range(numberOfImages):
            imageName = ""
            readName = False
            imageLabel = 0
            for character in fileContents[i]:
                if readName == True:
                    imageLabel = int(character)
                    break
                elif character == ',' and readName == False:
                    readName = True
                elif readName == False:
                    imageName = imageName + character

            imageNames.append(imageName)
            imageLabels.append(imageLabel)

        return imageNames, imageLabels

    def readTestText(self, filePath):
        f = open(filePath, "r")
        if f.mode != 'r':
            print('The file could not be opened in read mode.')
            exit(0)

        fileContents = f.readlines()
        f.close()

        imageNames = []
        numberOfImages = len(fileContents)
        for i in range(numberOfImages):
            imageName = ""
            for character in fileContents[i]:
                if character == '\n':
                    break
                else:
                    imageName += character
            imageNames.append(imageName)

        return imageNames


    def writeText(self, filePath, imageNames, imageLabels):
        lines = []
        numberOfImages = len(imageNames)
        lines.append('id,label\n')
        for i in range(numberOfImages):
            line = imageNames[i] + ',' + str(imageLabels[i]) + '\n'
            lines.append(line)

        f = open(filePath, 'w')
        f.writelines(lines)
        f.close()

