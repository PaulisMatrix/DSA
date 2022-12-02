opp_dict = {
    "A":"rock",
    "B":"paper",
    "C":"scissor"
}

you_dict = {
    "X":"rock",
    "Y":"paper",
    "Z":"scissor"
}

scores_dict = {
    "rock":1,
    "paper":2,
    "scissor":3

}

win_list = [["rock","scissor"],["scissor","paper"],["paper","rock"]]

def solution(file):
    you_score = 0
    with open(file) as file:
        for line in file:
            opp,you = line.strip().split(" ")
            
            # opp wins
            if [opp_dict[opp],you_dict[you]] in win_list:
                you_score+=(0+scores_dict[you_dict[you]])
            
            # you win
            elif [opp_dict[opp],you_dict[you]][::-1] in win_list:
                you_score+=(6+scores_dict[you_dict[you]])
            # draw
            else:
                you_score+=(3+scores_dict[you_dict[you]])
    
    print(you_score)

if __name__ == "__main__":
    file = "input.txt"
    solution(file)