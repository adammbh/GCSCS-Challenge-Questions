import random
text = ""

text = input("What color do you think the traffic light is? ")

match text:
    case "Green":
        print('Go.')
    case "Yellow":
        print('Ready.')
    case "Red":
        print('Stop.')