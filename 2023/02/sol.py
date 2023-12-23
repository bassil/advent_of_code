import math


def parse_input(input_filename):
    with open(input_filename) as fp:
        games = [game.strip() for game in fp.readlines()]
    game_results = {}
    for game in games:
        game_number, results = game.split(":")
        game_number = int(game_number.split()[1])
        subgames = results.strip().split(";")
        subgame_results = []
        for subgame in subgames:
            subgame = subgame.strip().split(",")
            subgame_map = {}
            for cube in subgame:
                num_cubes, color = cube.split()
                num_cubes = int(num_cubes)
                subgame_map[color] = num_cubes
            subgame_results.append(subgame_map)
        game_results[game_number] = subgame_results
    return game_results


def part_1(games, max_num_cubes):
    result = 0
    for game_number, game_results in games.items():
        possible = True
        for game_result in game_results:
            for color, num_cubes in game_result.items():
                if num_cubes > max_num_cubes[color]:
                    possible = False
        if possible:
            result += game_number
    return result

def part_2(games):
    result = 0
    for game in games.values():
        min_num_cubes_of_color = {"red": 0, "green": 0, "blue": 0}
        for subgame in game:
            for color, num_cubes in subgame.items():
                if min_num_cubes_of_color[color] < num_cubes:
                    min_num_cubes_of_color[color] = num_cubes
        result += math.prod(min_num_cubes_of_color.values())
    return result


def main():
    input_filename = "input.txt"
    games = parse_input(input_filename)
    max_num_cubes = {"red": 12, "green": 13, "blue": 14}

    print("part 1:", part_1(games, max_num_cubes))
    print("part 2:", part_2(games))


if __name__ == "__main__":
    main()

    
