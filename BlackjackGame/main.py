import random
 
def play():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    me = random.sample(cards, 2)
    pc = random.sample(cards, 2)
 
    my_score = sum(me)
    pc_score = sum(pc)
 
    winner = False
 
    print(f'Your cards: {", ".join([str(c) for c in me])}, current score: {my_score}')
    print(f'PC first card: {pc[0]}')
 
    if my_score == 21:
        winner = True
        print('Congratulations! You hit a blackjack!')
    elif pc_score == 21:
        winner = True
        print('Oops, sorry! The PC hit a blackjack!')
        print(f'PC final hand: {", ".join([str(c) for c in pc])}, final score: {pc_score}')
 
    if not winner:
        while pc_score < 17:
            pc_card = random.choice(cards)
            cards.remove(pc_card)
            pc.append(pc_card)
            pc_score += pc_card
            if 11 in pc:
                if pc_score > 21:
                    pc_score -= 10
 
        while True:
            draw = input('Type hit to draw a new card, or stand to pass: ')
            if draw not in ['hit', 'stand']:
                print('Please enter a valid command - hit or stand')
            elif draw == 'hit':
                my_card = random.choice(cards)
                cards.remove(my_card)
                me.append(my_card)
                my_score += my_card
                print(f'Card {my_card} added to cards ({", ".join([str(c) for c in me])}) with a new score of {my_score}')
 
                if 11 in me:
                    if my_score > 21:
                        my_score -= 10
                        print(f'You have an Ace in your hand and your total score is above 21,'
                              f' so the Ace is even to 1. New score: {my_score}')
 
                if my_score >= 21:
                    break
            elif draw == 'stand':
                break
 
        print(f'Your final hand: {", ".join([str(c) for c in me])}, final score: {my_score}')
        print(f'PC final hand: {", ".join([str(c) for c in pc])}, final score: {pc_score}')
 
        if pc_score > 21:
            print('PC went over, you win!')
        elif my_score > 21:
            print('You went over, pc wins!')
        elif my_score > pc_score:
            print('You are closer to 21, you win!')
        elif pc_score > my_score:
            print('PC is closer to 21, pc wins!')
        elif pc_score == my_score:
            print('No one wins')
 
    while True:
        play_again = input('Do you want to go again? (yes or no) ')
        if play_again not in ['yes', 'no']:
            print('Please enter a valid command - yes or no')
        else:
            break
 
    print()
 
    if play_again == 'yes':
        play()
 
if __name__ == '__main__':
    play()