import random

def dec_bin_quiz_mixed():
    print("🔄 十進位 ↔ 4-bit 二進位 小測驗（0~15）")
    print("✅ 答對繼續，❌ 答錯就結束\n")

    while True:
        num = random.randint(0, 15)
        question_type = random.choice(['dec_to_bin', 'bin_to_dec'])

        if question_type == 'dec_to_bin':
            # 題型：十進位 ➜ 二進位
            correct_answer = format(num, '04b')
            user_input = input(f"請輸入十進位數 {num} 的4-bit二進位： ")
            if user_input == correct_answer:
                print("✅ 正確！繼續...\n")
            else:
                print(f"❌ 答錯了！正確答案是：{correct_answer}")
                break

        else:
            # 題型：二進位 ➜ 十進位
            binary_str = format(num, '04b')
            correct_answer = str(num)
            user_input = input(f"請輸入4-bit二進位 {binary_str} 的十進位： ")
            if user_input == correct_answer:
                print("✅ 正確！繼續...\n")
            else:
                print(f"❌ 答錯了！正確答案是：{correct_answer}")
                break

# 執行程式
dec_bin_quiz_mixed()
