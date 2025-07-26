def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    decks = read_input_file_data().split('\n\n')
    player1_deck = list(map(int, decks[0].splitlines()[1:]))
    player2_deck = list(map(int, decks[1].splitlines()[1:]))
    
    while player1_deck and player2_deck:
        p1_card = player1_deck.pop(0)
        p2_card = player2_deck.pop(0)
        if p1_card > p2_card:
            player1_deck.append(p1_card)
            player1_deck.append(p2_card)
        else:
            player2_deck.append(p2_card)
            player2_deck.append(p1_card)
    
    winner_deck = player1_deck if player1_deck else player2_deck
    winner_deck.reverse()
    return sum([i * card for i, card in enumerate(winner_deck, 1)])

def solve_part_2():
    decks = read_input_file_data().split('\n\n')
    player1_deck = list(map(int, decks[0].splitlines()[1:]))
    player2_deck = list(map(int, decks[1].splitlines()[1:]))

    P1_WIN = True
    P2_WIN = False
    
    seen_games = {}
    def play_game(p1_deck, p2_deck):
        nonlocal seen_games
        seen_rounds = set()
        while True:
            if not p1_deck:
                for key in seen_rounds:
                    if key in seen_games:
                        assert seen_games[key] == P2_WIN
                    seen_games[key] = P2_WIN
                return P2_WIN
            if not p2_deck:
                for key in seen_rounds:
                    if key in seen_games:
                        assert seen_games[key] == P1_WIN
                    seen_games[key] = P1_WIN
                return P1_WIN
            
            key = (tuple(p1_deck), tuple(p2_deck))
            if key in seen_games:
                result = seen_games[key]
                for key in seen_rounds:
                    if key in seen_games:
                        assert seen_games[key] == result
                    seen_games[key] = result
                return result
            if key in seen_rounds:
                for key in seen_rounds:
                    if key in seen_games:
                        assert seen_games[key] == P1_WIN
                    seen_games[key] = P1_WIN
                return P1_WIN
            seen_rounds.add(key)

            p1_card = p1_deck.pop(0)
            p2_card = p2_deck.pop(0)
            if len(p1_deck) >= p1_card and len(p2_deck) >= p2_card:
                result = play_game(p1_deck[:p1_card], p2_deck[:p2_card])
            else:
                result = p1_card > p2_card
            if result == P1_WIN:
                p1_deck.append(p1_card)
                p1_deck.append(p2_card)
            else:
                p2_deck.append(p2_card)
                p2_deck.append(p1_card)

    result = play_game(player1_deck, player2_deck)
    winner_deck = player1_deck if result == P1_WIN else player2_deck
    winner_deck.reverse()
    return sum([i * card for i, card in enumerate(winner_deck, 1)])
    
print(solve_part_2())
