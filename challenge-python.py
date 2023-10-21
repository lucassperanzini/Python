import random
import registerOptions
import json
import re

user_data = dict(stop = False)

transport = ["Uber", "Metrô", "Ônibus", "A pé", "Bicicleta"]

def main():
    try:
        print("\n"+("=" * 45) + "PathFinder" + ("=" * 45))
        registerOptions.optionLogin()
        
        while user_data["stop"] == False:
            try:
                menu()
                typeTransport()
                end()
            except ValueError:
                error(1)
            except KeyError:
                error(2)
    except ValueError:
        error(1)
    except KeyError:
        error(2)
    except KeyboardInterrupt:
        pass
    finally: 
        print("\nPrograma encerrado.")

def menu(): 
    print("\nEscolha uma opção:")
    for i in choices:
        print(f"({i}) {choices[i]['name']} -> {choices[i]['types']}")

    choice = int(input())

    if choice > 6 or choice < 1:
        raise KeyError
    
    user_data.update({"choice": choices[choice]['name']})
    length = len(choices[choice]["location"]) - 1
    user_data.update({ "locations": choose(choice, length) })

def sort(length):
    sorted = []
    sort1 = random.randint(0, length)
    sort2 = random.randint(0, length)
    sorted.append(sort1)
    if sorted[0] == sort2:
        while sorted[0] == sort2:
            sort2 = random.randint(0, 2)
        sorted.append(sort2)
    else:
        sorted.append(sort2)
    return sorted

def choose(choice, length):
    sorted = sort(length)
    loc1 = choices[choice]["location"][sorted[0]]
    loc2 = choices[choice]["location"][sorted[1]]
    return [loc1, loc2]
    
def typeTransport():
    print("\nDe qual forma você pretende chegar ao destino?")
    for i in range(len(transport)):
        print(f"({i+1}) {transport[int(i)]}")
    choice = int(input())
    if choice < 1 or choice > 5:
        raise KeyError
    user_data.update({"transport": transport[choice-1]})

def end(): 
    print("\n"+("=" * 45) + "Resultado" + ("=" * 46))
    print(f"De acordo com as suas informações\n-O tipo de turismo escolhido é: {user_data['choice']}\n-O seu transporte será: {user_data['transport']}\n-O trajeto que recomendamos é: {user_data['locations'][0]} -> {user_data['locations'][1]}")
    print("="*100)
    print("Deseja escolher mais uma opção de trajeto ? (S/N)")
    stop = input()
    if stop.lower() == "n":
        print(f"Obrigado por usar o Path Finder {user_data['name']}!")
        user_data["stop"] = True

def error(value):
    print("="*100)
    match value:
        case 1:
            print("<ERROR> Digite um valor válido!")
        case 2:
            print("<ERROR> Essa opção não existe!")
        case 3:
            print("<ERROR> O Caminho do arquivo JSON não foi encontrado!")
    print("="*100)

try:
    with open("choices.json", "r", encoding="utf-8") as file:
        choices = json.loads(file.read())
except FileNotFoundError:
    error(3)

main()