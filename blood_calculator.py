def interface():
    print("Blood Test Analysis")
    keep_running = True
    while keep_running:
        print("Options:")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            keep_running = False
    return 
   
def accept_input(test_result):
    entry = input("Enter the {} test result".format(test_result))
    return int(entry)

interface()