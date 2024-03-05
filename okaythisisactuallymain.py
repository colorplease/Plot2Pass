intro_string = """
██████╗ ██╗      ██████╗ ████████╗██████╗ ██████╗  █████╗ ███████╗███████╗
██╔══██╗██║     ██╔═══██╗╚══██╔══╝╚════██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝██║     ██║   ██║   ██║    █████╔╝██████╔╝███████║███████╗███████╗
██╔═══╝ ██║     ██║   ██║   ██║   ██╔═══╝ ██╔═══╝ ██╔══██║╚════██║╚════██║
██║     ███████╗╚██████╔╝   ██║   ███████╗██║     ██║  ██║███████║███████║
╚═╝     ╚══════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝                                                                                    
"""

avaliable_options_string = """
+==========================================+
| A. Input Grades from Class into New File |
| B. Plot Grades from Existing File        |
| C. Edit Grades from Existing File        |
+==========================================+
"""

#main calls
print(intro_string)
print(avaliable_options_string)
input_action = input("Welcome! What do you wish to do? (A, B, or C): ")