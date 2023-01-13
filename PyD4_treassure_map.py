print("Welcome to tressure Map!")
row1=["💕","💕","💕"]
row2=["💕","💕","💕"]
row3=["💕","💕","💕"]
row=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
choice = input("Please enter where you want to put the treassure: ")
first = int(choice[0])-1
second = int(choice[1])-1
row[first][second]="💙"
print(f"{row1}\n{row2}\n{row3}\n")