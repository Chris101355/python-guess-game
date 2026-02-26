import random

def guess_number_game():
    # 電腦隨機選一個 1 到 100 的數字
    answer = random.randint(1, 100)
    guess_count = 0
    is_correct = False

    print("--- 歡迎來到猜數字遊戲 ---")
    print("我已經想好了一個 1 到 100 之間的數字，你猜是多少？")

    # 使用迴圈讓玩家可以重複猜測，直到猜中
    while not is_correct:
        try:
            # 取得玩家輸入並轉換成整數
            player_guess = int(input("輸入你的猜測："))
            guess_count += 1

            if player_guess < answer:
                print("太小了！再試一次。")
            elif player_guess > answer:
                print("太大了！再試一次。")
            else:
                print(f"恭喜你！猜中了！答案就是 {answer}。")
                print(f"你總共猜了 {guess_count} 次。")
                is_correct = True
        except ValueError:
            print("請輸入有效的數字喔！")

if __name__ == "__main__":
    guess_number_game()
