import json
set_json = open("settings.json", "r")
settings = json.loads(set_json.read())
start_position = settings["start"]
position_point = start_position
var_names_arr = settings["var_arr"]
variables_count = len(var_names_arr)
numb_arr = settings["num_arr"]
set_json.close()
dictator = {
    str(start_position): {

    }
}


def update_globals():
    set_json_u = open("settings.json", "r")
    settings_u = json.loads(set_json_u.read())
    globals()["start_position"] = settings_u["start"]
    globals()["position_point"] = start_position
    globals()["var_names_arr"] = settings_u["var_arr"]
    globals()["variables_count"] = len(var_names_arr)
    globals()["numb_arr"] = settings_u["num_arr"]
    globals()["dictator"] = {str(start_position): {}}


def settings_set():
    print("1 -- start position", "2 -- keys", "3 -- variables types", "4 -- exit settings", sep="\n")
    n = int(input("select option: "))
    file = json.loads(open("settings.json", "r").read())
    match n:
        case 1:
            file["start"] = int(input("type start position: "))
            open("settings.json", "w").write(json.dumps(file, indent=4))
            settings_set()
        case 2:
            arr_l = input("how many keys: ")
            arr = []
            for i in range(int(arr_l)):
                key = input("type key: ")
                arr.append(key)
            file["var_arr"] = arr
            open("settings.json", "w").write(json.dumps(file, indent=4))
            settings_set()
        case 3:
            print("0 -- string", "1 -- int", "2 -- float", sep="\n")
            arr = []
            for i in range(len(file["var_arr"])):
                k = int(input("type: "))
                arr.append(k)
            file["num_arr"] = arr
            open("settings.json", "w").write(json.dumps(file, indent=4))
            settings_set()
        case 4:
            update_globals()
            main()
        case _:
            settings_set()


def proceed():
    if position_point != start_position:
        dictator.update({str(position_point): {}})
    dictt = {

    }
    for i in range(variables_count):
        var = input(var_names_arr[i]+": ")
        match numb_arr[i]:
            case 0:
                dictt.update({var_names_arr[i]: var})
            case 1:
                dictt.update({var_names_arr[i]: int(var)})
            case 2:
                dictt.update({var_names_arr[i]: float(var)})
    dictator[str(position_point)].update(dictt)
    globals()['position_point'] += 1
    main()


def main():

    print("WELCOME TO JSON WRITER")
    print("1 -- change settings")
    print("2 -- proceed")
    print("3 -- save & exit")
    print(position_point)
    n = input("select option: ")
    match int(n):
        case 1:
            settings_set()
        case 2:
            proceed()
        case 3:
            f = open("C:\\Users\\Sebas\\Desktop\\json_writer.txt", "w")
            f.write(json.dumps(dictator, indent=4))
            f.close()
            print(json.dumps(dictator, indent=4))
            return 0


main()
