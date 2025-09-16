def main():
    time=input("Enter time:").strip()
    if 6<=convert(time)<=8:
        print ("Breakfast time")
    if 12<=convert(time)<=13:
        print("lunch time")
    if 18<=convert(time)<=19:
        print("dinner time")

def convert(time):
    hours, minutes=time.split(":")
    hours=int (hours)
    minutes= int(minutes)
    x= float (hours) + float (minutes)/60
    return x

if __name__ == "__main__":
    main()
