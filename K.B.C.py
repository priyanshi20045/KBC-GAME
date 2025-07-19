from questions import questions

print("Enter your name :")
name = input()
print("Good to have you here,", name)
print("Let's get started!")
print("Here are your questions:")

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for idx, i in enumerate(questions):
    print("\n" + i["question"])
    for option in i["options"]:
        print(option)

    user_ans = input("Enter your answer (a/b/c/d): ").strip().lower()

    if user_ans == i["answer"]:
        print("✅ Correct Answer!")
        if idx < len(levels):
            money = levels[idx]
        print(f"🎉 You have won Rs. {money}")
    else:
        print("❌ Wrong Answer!")
        break

print(f"\n🏆 Congratulations {name}, you take home Rs. {money} 🏆")
