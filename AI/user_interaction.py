from typing import List

class OptionsMaker:
    def mountMenu(self, options: List):
        self.printOptionsWithIndex(options)
        print('[0] CANCEL\n')

    def printOptionsWithIndex(self, options: List):
        for index, option in enumerate(options):
            print(f'[{index + 1}] {option}')

class AsksToUser:
    def __init__(self):
        self.askAndKeepWikipediaSearchTerm()
        self.correctAndKeepPrefixesAsked()

    def askAndKeepWikipediaSearchTerm(self):
        self.searchTerm =  input('Type a Wikipedia search term: ')
    
    def correctAndKeepPrefixesAsked(self, prefixes: List=['Who Is', 'What Is', 'The History of']):
        indexOfPrefixChosen = self.askPrefixesAndReturnIndex(prefixes)
        while True:
            if self.verifyPrefixesAsked(indexOfPrefixChosen, len(prefixes)):
                break
        self.prefix = prefixes[indexOfPrefixChosen - 1]
    
    def verifyPrefixesAsked(self, index: int, prefixes_quantity: int):
        try:
            return self.verifyNumberOfPrefixesAsked(index, prefixes_quantity)
        except:
            print('Please type a integer number')

    def verifyNumberOfPrefixesAsked(self, index: int, prefixes_quantity: int):
        if 0 > index > prefixes_quantity:
            print('Invalid Number, try again\n')
            return False
        return True

    def askPrefixesAndReturnIndex(self, prefixes: List):
        optionsMaker = OptionsMaker()
        optionsMaker.mountMenu(prefixes)
        return int(input(f'Type a number to choose a prefix for {self.searchTerm}'))

if __name__ == '__main__':
    userAsking = AsksToUser()
    print(userAsking.prefix + ' ' + userAsking.searchTerm)