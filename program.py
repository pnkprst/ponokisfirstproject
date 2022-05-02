# 좌표는 5*5이기 때문에 5보다 큰 수를 적절히 잘라줘야 한다.
def five_clock(value):
    if value >= 5:
        return value - 5
    elif value < 0:
        return value + 5
    else:
        return value


test_map = [
    ["1", "0", "0", "0", "0"],   # 0y
    ["0", "0", "0", "0", "0"],   # 1y
    ["0", "0", "0", "0", "0"],   # 2y
    ["0", "0", "0", "0", "0"],   # 3y
    ["0", "0", "0", "0", "0"]    # 4y
]

player = {"y": 0, "x": 0}
moved = -1

while 1:
    moved += 1
    print("==", "%04d turn" % moved, "==")
    for x in range(len(test_map)):
        print("  ", end=" ")
        for y in range(len(test_map[x])):
            print(test_map[x][y], end=" ")
        print("")

    go_list = input("moving: ")
    for i in go_list:
        match i: # 명령이동
            case "w":
                # 기존자리를 비움
                test_map[player["y"]][player["x"]] = "0"
                # 기수 데이터 변경
                player["y"] = five_clock(player["y"] - 1)
                # 현재 기수 자리로 자리 표시
                test_map[player["y"]][player["x"]] = "1"
                # 이하 동일
            case "s":
                test_map[player["y"]][player["x"]] = "0"
                player["y"] = five_clock(player["y"] + 1)
                test_map[player["y"]][player["x"]] = "1"
            case "a":
                test_map[player["y"]][player["x"]] = "0"
                player["x"] = five_clock(player["x"] - 1)
                test_map[player["y"]][player["x"]] = "1"
            case "d":
                test_map[player["y"]][player["x"]] = "0"
                player["x"] = five_clock(player["x"] + 1)
                test_map[player["y"]][player["x"]] = "1"
            case "W":
                test_map[player["y"]][player["x"]] = "0"
                player["y"] = five_clock(player["y"] - 1)
                test_map[player["y"]][player["x"]] = "1"
            case "S":
                test_map[player["y"]][player["x"]] = "0"
                player["y"] = five_clock(player["y"] + 1)
                test_map[player["y"]][player["x"]] = "1"
            case "A":
                test_map[player["y"]][player["x"]] = "0"
                player["x"] = five_clock(player["x"] - 1)
                test_map[player["y"]][player["x"]] = "1"
            case "D":
                test_map[player["y"]][player["x"]] = "0"
                player["x"] = five_clock(player["x"] + 1)
                test_map[player["y"]][player["x"]] = "1"
            case _:
                print("Exit program.")
                break

