value = input("What do you want to print >: ")
times = input("how many times >: ")

times_val = int(times)
counter = 0

while counter < times_val:
    #print("Times " + str(counter) +  "/" + str(times_val) + " " + value)
    print(f"Times {counter}/{times_val} {value}")
    counter = counter + 1

    if counter % 1000 == 0:
        reply = input(f" do you wish to continue ?")
        if(reply=="y"):
            input("ok i will continue.... press enter key")
        else:
            break    

print("Have a nice day!!!!!")

