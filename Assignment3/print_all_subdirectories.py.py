import os

#n = ""


def print_all_subdirectories(path):
    #global n
    # Whenever thefunction is called, two spaces are added to the indentation.
    #n += "  "

    mapp = os.scandir(path)

    try:
        for n in mapp:
            # Disregard hidden folders
             if n.name == ("_") or n.name == ("."):
              continue
            # If the path is a directory, we call the function within itself.
             if n.is_dir():
                print(f"{n.name}")
                print_all_subdirectories(n.path)

             elif n.is_file():
                print(f"{n.name}")
    except Exception as e:
        print(e)
    #n = n [:-2]


path = os.getcwd()
print_all_subdirectories(path)