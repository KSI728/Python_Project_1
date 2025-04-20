# 가위바위보 게임
from function import *

def main():
    count_win=0
    
    for i in range(10):
        print(f"\n{'-'*55}")
        print(f"\n[ {i+1}번째 가위바위보 게임 ✊ ✌️  🖐️  ]\n")
        player=input("가위, 바위, 보 중에 하나를 입력해주세요! : ")
        
        while player not in ["가위","바위","보"]:
            print("\n가위, 바위, 보만 입력해주세요!\n")
            player=input("가위, 바위, 보 중에 하나를 입력해주세요! : ")    
            
        computer=random_rcp()
        print(f'\nYOU : {player}   VS   {computer} : COM')
        print('\n가위바위보 결과 : ', end='')
        count_win+=compare(player, computer)
    
    print(f"\n{'-'*55}")
    print("\n[얼마나 많이 이겼을까요? ✊ ✌️  🖐️  ]")   
    win_rate=(count_win/10)*100
    print(f'\n당신의 가위바위보 승률(10게임) : {win_rate}%') 
    print(f"\n{'-'*55}")  
    
main()    