def findPokerHand(hand):

    ranks = []
    suits = []
    possibleRanks = []

    for card in hand:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
        else:
            rank = card[0:2]
            suit = card[2]


        if rank == "A":
            rank = 14
        elif rank == "K":
            rank = 13
        elif rank == "Q":
            rank = 12
        elif rank == "J":
            rank = 11

        ranks.append(int(rank))
        suits.append(suit)


    #print(ranks)
    sortedRanks = sorted(ranks)
    #print(sortedRanks)

    #Royal Flush, Straight Flush and Flush
    if suits.count(suits[0]) == 5:
        #Royal FLush
        if 14 in sortedRanks and 13 in sortedRanks and 12 in sortedRanks and 11 in sortedRanks and 10 in sortedRanks:
            possibleRanks.append(10)
        #Straight Flush
        elif all(sortedRanks[i] == sortedRanks[i - 1] + 1 for i in range(1, len(sortedRanks))):
            possibleRanks.append(9)
        #Flush
        else:
            possibleRanks.append(6)
    #Straight
    if all(sortedRanks[i] == sortedRanks[i-1] + 1 for i in range(1,len(sortedRanks))):
        possibleRanks.append(5)

    handUniqueVals = list(set(sortedRanks))


    if len(handUniqueVals) == 2:
        for val in handUniqueVals:
           #Four of a kind
           if sortedRanks.count(val) == 4:
               possibleRanks.append(8)
           #Full House
           if sortedRanks.count(val) == 3:
               possibleRanks.append(7)

    if len(handUniqueVals) == 3:
        for val in handUniqueVals:
            #Three of a kind
            if sortedRanks.count(val) == 3:
                possibleRanks.append(4)
            #Two pair
            if sortedRanks.count(val) == 2:
                possibleRanks.append(3)

    #Pair
    if len(handUniqueVals) == 4:
        possibleRanks.append(2)

    #print(handUniqueVals)

    #High Card
    if not possibleRanks:
        possibleRanks.append(1)

    pokerHandRanks = {10: "Royal Flush", 9: "Straight Flush",8: "Four of a Kind", 7: "Full house", 6:"Flush",
                      5:"Straight", 4: "Three of a kind" ,3: "Two pair", 2: "Pair", 1: "High Card"}

    output = pokerHandRanks[max(possibleRanks)]
    print(hand, output)
    return output

if __name__ == "__main__":
    findPokerHand(["KH","AH","QH","JH","10H"]) #RoyalFlush
    findPokerHand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush
    findPokerHand(["5C", "5S", "5H", "5D", "QH"])  # Four of a Kind
    findPokerHand(["2H", "2D", "2S", "10H", "10C"])  # Full house
    findPokerHand(["2D", "KD", "7D", "6D", "5D"])  # Flush
    findPokerHand(["JC", "10H", "9C", "8C", "7D"])  # Straight
    findPokerHand(["10H", "10C", "10D", "2D", "5S"])  # Three of a Kind
    findPokerHand(["KD", "KH", "5C", "5S", "6D"])  # Two pair
    findPokerHand(["2D", "2S", "9C", "KD", "10C"])  # Pair
    findPokerHand(["KD", "5H", "2D", "10C", "JH"])  # High Card