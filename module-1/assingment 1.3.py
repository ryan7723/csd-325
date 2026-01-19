#ryan barber assignment 1.3
def countdown(num_bottles: int) -> None:
    for bottles in range(num_bottles, 0, -1):
        if bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")

        print(f"Take one down and pass it around, {bottles - 1} bottle(s) of beer on the wall.\n")

def main() -> None:
    bottles = int(input("Enter the number of bottles: "))
    countdown(bottles)
    print("Time to buy more bottles of beer!")

if __name__ == "__main__":
    main()