def loading(number):
    if number == 100:
        return (f"100% Complete!\n[%%%%%%%%%%]")
    else:
        return(f"{number}% [{'%' * (number // 10)}{'.' * (10 - number // 10)}]\nStill loading...")


number_bar = int(input())
print(loading(number_bar))
