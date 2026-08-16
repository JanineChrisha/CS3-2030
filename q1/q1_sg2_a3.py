9 - Samat
21 - Ducos, Janine Chrisha M.

birth = int(input("Enter your birth year: "))
if birth < 1900:
    print("Invalid Year, it should not be earlier than 1900")
else:
    zodiacsign = (birth - 1900) % 12



    if zodiacsign == 0:
        print("Your Chinese Zodiac Sign is : Rat (鼠 / Shǔ)")
        
    elif zodiacsign == 1:
        print("Your Chinese Zodiac Sign is : Ox (牛 / Niú)")
        
    elif zodiacsign == 2:
        print("Your Chinese Zodiac Sign is : Tiger (虎 / Hǔ)")
        
    elif zodiacsign == 3:
        print("Your Chinese Zodiac Sign is : Rabbit (兔 / Tù)")
        
    elif zodiacsign == 4:
        print("Your Chinese Zodiac Sign is : Dragon (龙 / Lóng)")
        
    elif zodiacsign == 5:
        print("Your Chinese Zodiac Sign is : Snake (蛇 / Shé)")
        
    elif zodiacsign == 6:
        print("Your Chinese Zodiac Sign is : Horse (马 / Mǎ)")
        
    elif zodiacsign == 7:
        print("Your Chinese Zodiac Sign is : Goat (羊 / Yáng)")
        
    elif zodiacsign == 8:
        print("Your Chinese Zodiac Sign is : Monkey (猴 / Hóu)")
        
    elif zodiacsign == 9:
        print("Your Chinese Zodiac Sign is : Rooster (鸡 / Jī)")
        
    elif zodiacsign == 10:
        print("Your Chinese Zodiac Sign is : Dog (狗 / Gǒu)")
        
    elif zodiacsign == 11:
        print("Your Chinese Zodiac Sign is : Pig (猪 / Zhū)")
        
