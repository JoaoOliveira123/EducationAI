from typing import List

class OptionsMaker:
    def mountMenuAndReturnInputValue(self, options: List):
        indexesOfOptions = self.printOptionsWithIndexAndReturnThem(options)
        print('[0] CANCEL\n')
        return int(input(f'Choose one option {indexesOfOptions}: '))

    def printOptionsWithIndexAndReturnThem(self, options: List):
        listOfIndexes = [0]
        for index, option in enumerate(options):
            print(f'[{index + 1}] {option}')
            listOfIndexes.append(index + 1)
        return listOfIndexes

class AsksToUser:
    def __init__(self):
        self.askAndKeepSearchTerm()
        self.verifyAndKeepPrefixesAsked()

    def askAndKeepSearchTerm(self):
        self.searchTerm =  input('Type a Wikipedia search term: ')
    
    def verifyAndKeepPrefixesAsked(self):
        prefixes = ['Who Is', 'What Is', 'The History of']
        while True:
            indexOfPrefixChosen = self.askAndReturnPrefixes(prefixes)
            if indexOfPrefixChosen > len(prefixes):
                print('Please enter a valid prefix')
                continue
            break
        self.prefix = prefixes[indexOfPrefixChosen - 1]

    def askAndReturnPrefixes(self, prefixes: List):
        optionsMaker = OptionsMaker()
        return optionsMaker.mountMenuAndReturnInputValue(prefixes)

if __name__ == '__main__':
    userAsking = AsksToUser()
    print(userAsking.prefix + ' ' + userAsking.searchTerm)