name = input("Enter your name: ")
mood = input("What's your current mood? (Happy/Sad/Excited/Scared): ")
prefer_genre = input("Preferred genre? (Action/Comedy/Romance/Horror): ")

print("\nHello", name, "! Based on your inputs, here are some movie suggestions:")

if prefer_genre.lower() == "action":
    if mood.lower() == "excited":
        print("You might enjoy:fast")
    elif mood.lower() == "happy":
        print("You might enjoy:The Batman")
    else:
        print("You might enjoy:Rebel Ridge")

elif prefer_genre.lower() == "comedy":
    if mood.lower() == "happy":
        print("You might enjoy:Hot Frosty")
    elif mood.lower() == "sad":
        print("You might enjoy: three idiots")
    else:
        print("You might enjoy: jab we met")


elif prefer_genre.lower() == "horror":
    if mood.lower() == "scared":
        print("You might enjoy: it ")
    elif mood.lower() == "excited":
        print("You might enjoy: joker")
    else:
        print("You might enjoy:doll")

else:
    print("Sorry, we don't have suggestions for that genre.")

print("\nEnjoy the movie!")









