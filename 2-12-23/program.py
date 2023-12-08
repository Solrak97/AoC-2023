import sys

input_path = './input'

max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

valid_games = []

with open(input_path) as f:
    for line in f:
        game = line.split(':')
        records = game[1].split(';')

        is_game_valid = True
        
        for set in records:
            cubes = {'red': 0,
                     'green': 0,
                     'blue': 0}
            
            num = ''
            for i, c in enumerate(set):
                if c.isdigit():
                    num += (c)
                    continue
                
                for key in cubes.keys():
                    if set[i:].startswith(key):
                        cubes[key] = int(num)
                        num = ''
 
            is_valid = True
            for key in cubes.keys():
                if cubes[key] > max_cubes[key]:
                    is_game_valid = False
                    print(f'FAULTY [{game[0][5:]}]')
                    continue

            if not is_game_valid:
                continue
        
        if is_game_valid:

            valid_games.append(int(game[0][5:]))
            print(game[1])
            print(int(game[0][5:]))

print(sum(valid_games))






set_pows = []

with open(input_path) as f:
    for line in f:
        game = line.split(':')
        records = game[1].split(';')
        
        game_minimum = {'red': 0,
                     'green': 0,
                     'blue': 0}
        
        for set in records:
            cubes = {'red': 0,
                     'green': 0,
                     'blue': 0}
            
            num = ''
            for i, c in enumerate(set):
                if c.isdigit():
                    num += (c)
                    continue
                
                for key in cubes.keys():
                    if set[i:].startswith(key):
                        cubes[key] = int(num)
                        num = ''
 
            for key in cubes.keys():
                if cubes[key] >= game_minimum[key]:
                    game_minimum[key] = cubes[key]
            
            print((game_minimum, game_minimum['red'] * game_minimum['green'] * game_minimum['blue']))
                    


        set_pows.append(game_minimum['red'] * game_minimum['green'] * game_minimum['blue'])

print(sum(set_pows))
