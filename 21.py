import random


#Deal the cards
#dealer_cards
#Display cards
#dealer card hidden

#SUM of dealer cards

if __name__ == '__main__':
    # dealer cards
    dealer_cards = []
    # player cards
    player_cards = []
    print("NOW PLAYING BLACKJAC")
    while (len(dealer_cards) != 2):
        dealer_cards.append(random.randint(1, 11))
        if (len(dealer_cards) == 2):
            print("Dealer has X &", dealer_cards[1])

    while (len(player_cards) != 2):
        player_cards.append(random.randint(1, 11))
        if (len(player_cards) == 2):
            print("You have ", player_cards)

    print("SUM OF YOUR CARDS = ",sum(player_cards))
    if(sum(player_cards)==21):
        print("WINNER WINNER CHICKEN DINNER")
        print("Dealer had ",dealer_cards," SUM ",sum(dealer_cards))

    while(sum(player_cards)<21):
        print("HIT OR STAY?")
        if(str(input())=='hit'):
            player_cards.append(random.randint(1,11))
            if (sum(player_cards) == 21):
                print("WINNER WINNER CHICKEN DINNER")
            elif(sum(player_cards)>21):
                print("BUST,LOSER")
                break
            print("YOUR HAND = ", player_cards, " SUM =", sum(player_cards))
        else:
            print("YOUR FINAL HAND = ",player_cards," SUM =",sum(player_cards))
            break
    print("DEALER HAS ",dealer_cards, " with a sum of ",sum(dealer_cards))
    if(sum(dealer_cards)==21):
        print("THE HOUSE ALWAYS WINS")

    if(sum(dealer_cards)>sum(player_cards)):
        print("YOU LOSE!!")
    else:
        while(sum(dealer_cards) < sum(player_cards) ):
            dealer_cards.append(random.randint(1,11))
            print("DEALER NOW HAS ",dealer_cards," SUM =",sum(dealer_cards))
            if(sum(dealer_cards)>21):
                print("YOU WIN!!")
            elif(sum(dealer_cards)>=sum(player_cards)):
                print("YOU LOSE")







#sum of player cards
#Compare sum of D and P
#STATES
#If P card < 21, Option to HIT or STAY
#If SUM(P) > 21, BUST, P LOSES
#If P stays, Check SUM(D)
#if SUM(D) > 21, P wins
#If SUM(P) < SUM(D), D wins