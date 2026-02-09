import random

# ------------------------------
# Romaji to Hiragana mapping
# ------------------------------
romaji_to_hira = {
    "a":"あ","i":"い","u":"う","e":"え","o":"お",
    "ka":"か","ki":"き","ku":"く","ke":"け","ko":"こ",
    "sa":"さ","shi":"し","su":"す","se":"せ","so":"そ",
    "ta":"た","chi":"ち","tsu":"つ","te":"て","to":"と",
    "na":"な","ni":"に","nu":"ぬ","ne":"ね","no":"の",
    "ha":"は","hi":"ひ","fu":"ふ","he":"へ","ho":"ほ",
   # "ma":"ま","mi":"み","mu":"む","me":"め","mo":"も",
    #"ya":"や","yu":"ゆ","yo":"よ",
#    "ra":"ら","ri":"り","ru":"る","re":"れ","ro":"ろ",
 #   "wa":"わ","wi":"ゐ", "we":"ゑ", "wo":"を",
  #  "n":"ん",
    # Voiced sounds...
    # "ga":"が","gi":"ぎ","gu":"ぐ","ge":"げ","go":"ご",
    # "za":"ざ","ji":"じ","zu":"ず","ze":"ぜ","zo":"ぞ",
    # "da":"だ","ji":"ぢ","zu":"づ","de":"で","do":"ど",
    # "ba":"ば","bi":"び","bu":"ぶ","be":"べ","bo":"ぼ",
    # "pa":"ぱ","pi":"ぴ","pu":"ぷ","pe":"ぺ","po":"ぽ"
}
hira_to_romaji_map = {v: k for k, v in romaji_to_hira.items()}

known_romaji = list(romaji_to_hira.keys())

# ------------------------------
# Functions
# ------------------------------

def print_romaji_table(mapping, cols=5):
    items = list(mapping.items())
    max_key_len = max(len(k) for k in mapping.keys())

    display_items = []
    for k, v in items:
        display_items.append((k, v))

        # Insert two empty slots after ya and yu
        if k in ("ya", "yu", "wi"):
            display_items.append((None, None))

    for i in range(0, len(display_items), cols):
        row = display_items[i:i + cols]
        cells = []

        for k, v in row:
            if k is None:
                cells.append(" " * (max_key_len + 5))
            else:
                cells.append(f"{k.ljust(max_key_len)} → {v}")

        print("   ".join(cells))

def generate_romaji(length):
    return [random.choice(known_romaji) for _ in range(length)]

def romaji_to_hiragana(romaji_list):
    return [romaji_to_hira[r] for r in romaji_list]

def exercise_romaji_to_hira(length):
    romaji_list = generate_romaji(length)
    print("\nWrite this in hiragana:")
    print(" ".join(romaji_list))
    input("Press Enter to see the answer...")
    print("Answer:")
    print(" ".join(romaji_to_hiragana(romaji_list)))

def exercise_hira_to_romaji(length):
    romaji_list = generate_romaji(length)
    hira_list = romaji_to_hiragana(romaji_list)
    print("\nWrite the romaji for this hiragana string:")
    print("".join(hira_list))

    user_input = input("Enter romaji separated by spaces: ").strip().split()

    mistakes = []
    for idx, (hira, correct, user) in enumerate(zip(hira_list, romaji_list, user_input)):
        if user != correct:
            mistakes.append(f"{idx+1}: {hira} -> {user} ✗ (correct: {correct})")

    # Handle missing input
    if len(user_input) < len(romaji_list):
        for idx in range(len(user_input), len(romaji_list)):
            mistakes.append(f"{idx+1}: {hira_list[idx]} -> (no input) ✗ (correct: {romaji_list[idx]})")
    # Handle extra input
    elif len(user_input) > len(romaji_list):
        for idx in range(len(romaji_list), len(user_input)):
            mistakes.append(f"{idx+1}: (extra input) -> {user_input[idx]} ✗ (no kana)")

    if mistakes:
        print("\nMistakes:")
        for m in mistakes:
            print(m)
    else:
        print("\nAll correct! 🎉")

# ------------------------------
# Hiragana to Katakana conversion
# ------------------------------
def hira_to_kata(hira):
    return chr(ord(hira) + 0x60)

romaji_to_kata = {k: hira_to_kata(v) for k, v in romaji_to_hira.items()}
kata_to_romaji_map = {v: k for k, v in romaji_to_kata.items()}

def romaji_to_katakana(romaji_list):
    return [romaji_to_kata[r] for r in romaji_list]

def exercise_romaji_to_kata(length):
    romaji_list = generate_romaji(length)
    print("\nWrite this in katakana:")
    print(" ".join(romaji_list))
    input("Press Enter to see the answer...")
    print("Answer:")
    print(" ".join(romaji_to_katakana(romaji_list)))

def exercise_kata_to_romaji(length):
    romaji_list = generate_romaji(length)
    kata_list = romaji_to_katakana(romaji_list)
    print("\nWrite the romaji for this katakana string:")
    print("".join(kata_list))

    user_input = input("Enter romaji separated by spaces: ").strip().split()

    mistakes = []
    for idx, (kata, correct, user) in enumerate(zip(kata_list, romaji_list, user_input)):
        if user != correct:
            mistakes.append(f"{idx+1}: {kata} -> {user} ✗ (correct: {correct})")

    if len(user_input) < len(romaji_list):
        for idx in range(len(user_input), len(romaji_list)):
            mistakes.append(
                f"{idx+1}: {kata_list[idx]} -> (no input) ✗ (correct: {romaji_list[idx]})"
            )
    elif len(user_input) > len(romaji_list):
        for idx in range(len(romaji_list), len(user_input)):
            mistakes.append(f"{idx+1}: (extra input) -> {user_input[idx]} ✗ (no kana)")

    if mistakes:
        print("\nMistakes:")
        for m in mistakes:
            print(m)
    else:
        print("\nAll correct! 🎉")


# ------------------------------
# Main Program
# ------------------------------

def main():
    print("=== Hiragana Practice Config ===")
    try:
        romaji_to_hira_length = int(input("Length of Romaji→Hiragana exercise (default 15): ") or 15)
        hira_to_romaji_length = int(input("Length of Hiragana→Romaji exercise (default 30): ") or 30)
    except ValueError:
        print("Invalid input, using default lengths 15 and 30.")
        romaji_to_hira_length = 15
        hira_to_romaji_length = 30

    while True:
        print("\nChoose exercise type:")
        print("1 - Romaji → Hiragana (exercise)")
        print("2 - Hiragana → Romaji (exercise)")
        print("")
        print("3 - Romaji → Katakana (exercise)")
        print("4 - Katakana → Romaji (exercise)")
        print("")
        print("5 - Show romaji → Kana chart")
        print("0 - Quit")

        choice = input().strip()

        if choice == "1":
            exercise_romaji_to_hira(romaji_to_hira_length)
        elif choice == "2":
            exercise_hira_to_romaji(hira_to_romaji_length)
        elif choice == "3":
            exercise_romaji_to_kata(romaji_to_hira_length)
        elif choice == "4":
            exercise_kata_to_romaji(hira_to_romaji_length)
        elif choice == "5":
            print_romaji_table(romaji_to_hira)
            print("")
            print_romaji_table(romaji_to_kata)
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

