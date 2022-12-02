opp_dict = {
    "A":"rock",
    "B":"paper",
    "C":"scissor"
}

choose_list = ["rock","paper","scissor"]

scores_dict = {
    "rock":1,
    "paper":2,
    "scissor":3

}

strategy = {
    "X":"lose",
    "Y":"draw",
    "Z":"win"
}

win_list = [["rock","scissor"],["scissor","paper"],["paper","rock"]]

def solution(file):
    you_score = 0
    with open(file) as file:
        for line in file:
            opp,you = line.strip().split(" ")

            if strategy[you] == "lose":
                for you_choice in choose_list:
                    
                    # opp must win
                    if [opp_dict[opp],you_choice] in win_list:
                        you_score+=(0+scores_dict[you_choice])
                
            elif strategy[you] == "draw":
                you_score+=(3+scores_dict[opp_dict[opp]])
            elif strategy[you] == "win":
                for you_choice in choose_list:
                    
                    # you must win
                    if [opp_dict[opp],you_choice][::-1] in win_list:
                        you_score+=(6+scores_dict[you_choice])
            
    
    print(you_score)

if __name__ == "__main__":
    file = "input.txt"
    solution(file)