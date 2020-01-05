from random import randint,choice
import sys
import time
print("######################## DUNGEON "
    "ESCAPE #############################\n\n")   
print("Cách điều khiển:\n"
    "'w': Đi lên\n"
    "'a': Rẽ trái\n"
    "'s': Đi xuống\n"
    "'d': Rẽ phải\n"
    "'ctrl + z': Thoát game\n")
def exit_game():
    print("Đang thoát khỏi hầm!")
    sys.exit()
def play_again():
    print("Đang tạo map mới...")
    time.sleep(1)
    play()
def finish_game():
    while True:
        c = input("Bạn muốn chơi tiếp chứ? (C)ó hay (K)hông? ")
        if len(c)==0:
            print("Hãy thử lại!!")
        elif c[0].lower() == "c":
            play_again()
        elif c[0].lower() == "k":
            exit_game()
        else:
            print("Sai ký tự, hãy nhập lại!")


def play():
    walls=[
        [],
        [],
        [],
        [],
        []
    ]
    wall ={
        "symbol":"W"
    }
    player ={
        "symbol":"P",
        "have_key":False
    }
    key  = {
        "symbol":"K"
    }
    exit1 = {
        "symbol":"E"
    }
    traces={
        "symbol":"_"
    }
    x=0
    y=0
    q=4
    w=9
    a = randint(0,4)
    b = randint(0,9)
    while True:    
        
        map1 = [
        ["_", "_","_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_","_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_","_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_","_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_","_", "_", "_", "_", "_", "_", "_", "_"],
        ]
        map1[a][b]=key["symbol"]
        map1[x][y]=player["symbol"]
        map1[q][w]=exit1["symbol"]
        for i in range(5):
            r = randint(0,4)
            t = randint(0,8)
            walls[i].append(r)
            walls[i].append(t)
            map1[r][t]=wall["symbol"]
        print(walls)
        for item in map1:
            print(*item,sep=" ")
        while True:
            print(x,y)
            n = input("Nhập nước đi của bạn: \n"
            "Khi đến lối thoát hãy ấn enter!! \n")
            if n.lower() =="w":
                map1[x][y]=traces["symbol"]
                x-=1
                map1[x][y]=player["symbol"]
                
                if x==a and y==b:
                    player["have_key"]= True
                    print("Bạn đã lấy được chìa khoá!!\n"
                    "Khi đến lối thoát hãy ấn enter để sử dụng chìa!\n")
                    map1[q][w]=exit1["symbol"]
                for i in range(5):
                    if x and y in walls[i]:
                        map1[r][t]=wall["symbol"]
                        x+=1
                        map1[x][y]=player["symbol"]
                        print("Bạn đã đâm vào tường, hãy tìm hướng khác!!")
                if x<0:
                    print("Không thể đi quá map, hãy tìm đường khác!!")
                    map1[x][y]=traces["symbol"]
                    x+=1
                    map1[x][y]=player["symbol"]
                    
                elif x>4:
                    print("Không thể đi quá map, hãy tìm đường khác!!")
                    map1[x][y]=traces["symbol"]
                    x-=1
                    map1[x][y]=player["symbol"]
                    
                for item in map1:
                    print(*item, sep=" ")
            elif n.lower()=="a":
                map1[x][y]=traces["symbol"]
                y-=1
                map1[x][y]=player["symbol"]
                
                if x==a and y==b:
                    player["have_key"]= True
                    print("Bạn đã lấy được chìa khoá!!\n"
                    "Khi đến lối thoát hãy ấn enter để sử dụng chìa!\n")
                    map1[q][w]=exit1["symbol"]
                for i in range(5):
                    if x and y in walls[i]:
                        map1[r][t]=wall["symbol"]
                        y+=1
                        map1[x][y]=player["symbol"]
                        print("Bạn đã đâm vào tường, hãy tìm hướng khác!!")
                if y<0:
                    print("Không thể đi quá map, hãy tìm đường khác!!")
                    map1[x][y]=traces["symbol"]
                    y+=1
                    map1[x][y]=player["symbol"]
                    
                elif y>9:
                    print("Không thể đi quá map, hãy tìm đường khác!!")
                    map1[x][y]=traces["symbol"]
                    y-=1
                    map1[x][y]=player["symbol"]
                    
                for item in map1:
                    print(*item, sep=" ")
            elif n.lower()=="s":
                map1[x][y]=traces["symbol"]
                x+=1
                map1[x][y]=player["symbol"]
                if x==a and y==b:
                    player["have_key"]= True
                    print("Bạn đã lấy được chìa khoá!!\n"
                    "Khi đến lối thoát hãy ấn enter để sử dụng chìa!\n")
                    map1[q][w]=exit1["symbol"]
                for i in range(5):
                    if x and y in walls[i]:
                        map1[r][t]=wall["symbol"]
                        x-=1
                        map1[x][y]=player["symbol"]
                        print("Bạn đã đâm vào tường, hãy tìm hướng khác!!")
                if x<0:
                    print("Không thể đi quá map, hãy tìm đường khác!!")
                    map1[x][y]=traces["symbol"]
                    x+=1
                    map1[x][y]=player["symbol"]
                elif x>4:
                    print("Không thể đi quá map, hãy tìm đường khác!!")
                    map1[x][y]=traces["symbol"]
                    x-=1
                    map1[x][y]=player["symbol"]
                for item in map1:
                    print(*item, sep=" ")
            elif n.lower()=="d":
                map1[x][y]=traces["symbol"]
                y+=1
                map1[x][y]=player["symbol"]
                
                if x==a and y==b:
                    player["have_key"]= True
                    print("Bạn đã lấy được chìa khoá!!\n"
                    "Khi đến lối thoát hãy ấn enter để sử dụng chìa!\n")
                    map1[q][w]=exit1["symbol"]
                for i in range(5):
                    if x and y in walls[i]:
                        map1[r][t]=wall["symbol"]
                        y-=1
                        map1[x][y]=player["symbol"]
                        print("Bạn đã đâm vào tường, hãy tìm hướng khác!!")
                if y<0:
                    print("Không thể đi quá map, hãy tìm đường khác!!")
                    map1[x][y]=traces["symbol"]
                    y+=1
                    map1[x][y]=player["symbol"]
                    
                elif y>9:
                    print("Không thể đi quá map, hãy tìm đường khác!!")
                    map1[x][y]=traces["symbol"]
                    y-=1
                    map1[x][y]=player["symbol"]
                for item in map1:
                    print(*item, sep=" ")
            elif x==4 and y==9:
                print("Bạn đã đến lối thoát")
                if player["have_key"] == True:
                    print("Bạn đã vượt ngục thành công!!")
                    finish_game()
                    break
                else:
                    print("Hãy lấy chìa khoá để mở cửa ngục!!")
                    
play()


