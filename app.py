from lib.user import User, CONN, CURSOR
from lib.pc import Pc, CONN, CURSOR
from lib.parts import Parts, CONN, CURSOR
import sqlite3
CONN = sqlite3.connect('lib/database.db')
CURSOR = CONN.cursor()

def app():
    choice = 0
    while choice != 3:
        print(''' 
                                                                                         ______________      _______
                                                                                        |.------------.|    | ___  o|   
 _______  _______    _______  __   __  ___   ___      ______   _______  ______          ||            ||    |[_-_]_ |
|       ||       |  |  _    ||  | |  ||   | |   |    |      | |       ||    _ |         ||            ||    |[_____]|  
|    _  ||       |  | |_|   ||  | |  ||   | |   |    |  _    ||    ___||   | ||         ||            ||    |[====o]|
|   |_| ||      _|  |       ||  |_|  ||   | |   |    | | |   ||   |___ |   |_||_        ||____________||    |[_.--_]| 
|    ___||     |_   |  _   | |       ||   | |   |___ | |_|   ||    ___||    __  |   .==.|""  ......    |.==.|[_____]|  
|   |    |       |  | |_|   ||       ||   | |       ||       ||   |___ |   |  | |   |::| '-.________.-' |::||      :|  
|___|    |_______|  |_______||_______||___| |_______||______| |_______||___|  |_|   |''|  (__________)-.|''|| _____:|
                                                                                    `""`                `""`      
        ''')
        print("Welcome to PC Builder!")
        print("1) Login")
        print("2) Sign up")
        print("3) Quit")
        try:
            choice = int(input())
        except:
            print("Enter one of the number options")

        if choice == 1:
            print("Enter your username:")
            login_input = input()
            query = "SELECT * FROM users WHERE LOWER(name) = LOWER(?)"
            CURSOR.execute(query, (login_input.lower(),))
            result = CURSOR.fetchone()
            if result:
                print(f"Welcome, {login_input.upper()}!")
                pc_choice = 0
                while pc_choice != 4:
                    print("What would you like to do?")
                    print("1) View PCs")
                    print("2) Create New PC")
                    print("3) Delete ALL pcs")
                    print("4) Logout")
                    try: pc_choice = int(input())
                    except: print("Enter one of the number options")
                    if pc_choice == 1:
                        print("VIEW ALL PCS")
                        all_pcs = Pc.get_all()
                        for pc in all_pcs:
                        #  print(pc)
                         print(f"{pc[0]}) {pc[1]}")
                        pc_choice = -1
                        while pc_choice != 0:
                            print("Select a PC to view, or enter '0' to exit View All")
                            try: pc_choice = int(input())
                            except: print("Enter one of the number options")
                            pc_chosen = False
                            chosen_pc = None
                            for pc in all_pcs:
                                if int(pc_choice) == int(pc[0]):
                                    pc_chosen = True
                                    chosen_pc = pc
                                    break
                            if pc_chosen == True:
                                # print(chosen_pc)
                                part_query = "SELECT * FROM parts WHERE pc = ?"
                                CURSOR.execute(part_query, (chosen_pc[1],))
                                pc_parts = CURSOR.fetchall()
                                print('''
                                    _____________
                                  /             /|
                                 /             / |
                                /____________ /  |
                               | ___________ |   |
                               ||           ||   |
                               ||  : )      ||   |
                               ||           ||   |
                               ||___________||   |
                               |   _______   |  /
                              /|  (_______)  | /
                             ( |_____________|/
                              \\
                            .=======================.
                            | ::::::::::::::::  ::: |
                            | ::::::::::::::[]  ::: |
                            |   -----------     ::: |
                            `-----------------------'
                                ''')
                                for part in pc_parts:
                                    print(f"{part[2]} : {part[1]} | ${part[4]} | {part[3]}W")
                                part_choice = 0
                                while part_choice != 7:
                                    print("1) Check Compatibility")
                                    print("2) Calculate Power Consumption")
                                    print("3) Calculate Price")
                                    print("4) Calculate Total RAM Memory")
                                    print("5) Calculate Total Storage")
                                    print("6) Display Parts Again")
                                    print("7) Exit")
                                    try: part_choice = int(input())
                                    except: print("Enter one of the number options")
                                    if part_choice == 1:
                                        mandatory_parts = ['Motherboard', 'CPU', 'Cooling', 'RAM', 'PSU']
                                        missing_parts = []
                                        for mandatory in mandatory_parts:
                                            part_found = False
                                            for part in pc_parts:
                                                if part[2] == mandatory:
                                                    part_found = True
                                                    break
                                            if not part_found:
                                                missing_parts.append(mandatory)
                                        if len(missing_parts) > 0:
                                            print("Missing Parts")
                                            for missing in missing_parts:
                                                print(missing)
                                        motherboard = None
                                        cpu = None
                                        psu = None
                                        case = None
                                        for part in pc_parts:
                                            if part[2] == 'Motherboard':
                                                motherboard = part
                                            elif part[2] == 'CPU':
                                                cpu = part
                                            elif part[2] == 'PSU':
                                                psu = part
                                            elif part [2] == 'Case':
                                                case = part
                                        if motherboard is not None and cpu is not None:
                                            if motherboard[5] != cpu[5]:
                                                print("Incompatible Chipset!!")
                                        if psu is not None:
                                            total_power = 0
                                            for part in pc_parts:
                                                if part[2] is not 'PSU':
                                                    total_power += part[3]
                                            if psu[3] < total_power:
                                                print("Power Supply Not Enough Power!!")
                                        if motherboard is not None and case is not None:
                                            mobo_size = 0
                                            case_size = 0
                                            if motherboard[6] == 'ATX':
                                                mobo_size = 3
                                            elif motherboard[6] == 'Micro ATX':
                                                mobo_size = 2
                                            elif motherboard[6] == 'Mini ITX':
                                                mobo_size = 1
                                
                                            if case[6] == 'ATX':
                                                case_size = 3
                                            elif case[6] == 'Micro ATX':
                                                case_size = 2
                                            elif case[6] == 'Mini ITX':
                                                case_size = 1
                                            if mobo_size > case_size:
                                                print("Case too small!!")

                                    elif part_choice == 2:
                                        total_power = 0
                                        for part in pc_parts:
                                            if part[2] != 'PSU':
                                                total_power += part[3]
                                        print(f"Total power consuption: {total_power}W")
                                        print("Make sure the Power Supply has at least that much power!")
                                    elif part_choice == 3:
                                        total_price = 0
                                        for part in pc_parts:
                                            total_price += part[4]
                                        print(f"Total price is ${round(total_price, 2)}")
                                    elif part_choice == 4:
                                        total_memory = 0 
                                        for part in pc_parts:
                                            if part[8] != None:
                                                total_memory += part[8]
                                        print(f"Total memory is {total_memory} GB")
                                    elif part_choice == 5:
                                        total_storage = 0
                                        terabytes = 0
                                        gigabytes = 0
                                        for part in pc_parts:
                                            if part[2] == 'Storage':
                                                total_storage += part[9]
                                        if total_storage > 1024:
                                            terabytes = int(total_storage / 1024)
                                            gigabytes = total_storage % 1024
                                            print(f"Total storage capacity is {terabytes}tb and {gigabytes}gb")
                                        else:
                                            print(f"Total storage capacity is {total_storage}gb")

                                    elif part_choice == 6:
                                        for part in pc_parts:
                                            print(f"{part[2]} : {part[1]} | ${part[4]} | {part[3]}W")
                            else:
                                print("Select a coresponding PC number")
                    elif pc_choice == 2:
                        Pc.create_table()
                        print("Name your PC <must be unique>")
                        pc_name = input()
                        query = "SELECT * FROM pcs WHERE LOWER(name) = LOWER(?)"
                        CURSOR.execute(query, (pc_name.lower(),))
                        result = CURSOR.fetchone()
                        if result:
                            print("Name already exists!")
                        else:
                            Pc.add_Pc(pc_name, login_input)
                            pc_cust_choice = 0
                            while pc_cust_choice != 9:
                                print("Select the part being added")
                                print("1) Motherboard")
                                print("2) CPU")
                                print("3) Cooling")
                                print("4) Case")
                                print("5) RAM")
                                print("6) GPU")
                                print("7) SSD/HDD Storage")
                                print("8) PSU")
                                print("9) Finalize PC")
                                try: pc_cust_choice = int(input())
                                except: print("Enter one of the number options")
                                if pc_cust_choice == 1:
                                    part_type = "Motherboard"
                                    create_part(part_type, pc_name)
                                elif pc_cust_choice == 2:
                                    part_type = "CPU"
                                    create_part(part_type, pc_name)
                                elif pc_cust_choice == 3:
                                    part_type = "Cooling"
                                    create_part(part_type, pc_name)
                                elif pc_cust_choice == 4:
                                    part_type = "Case"
                                    create_part(part_type, pc_name)
                                elif pc_cust_choice == 5:
                                    part_type = "RAM"
                                    create_part(part_type, pc_name)
                                elif pc_cust_choice == 6:
                                    part_type = "GPU"
                                    create_part(part_type, pc_name)
                                elif pc_cust_choice == 7:
                                    part_type = "Storage"
                                    create_part(part_type, pc_name)
                                elif pc_cust_choice == 8:
                                    part_type = "PSU"
                                    create_part(part_type, pc_name)
                                elif pc_cust_choice == 9:
                                    print("Pc Created!")    
                                else:
                                    print("Invalid Input")          
                    elif pc_choice == 3:
                        print("DELETING ALL")
                        Pc.delete_all()
                        Parts.delete_all()
                        print("All deleted. If that was a typo, sucks to suck")
                    elif pc_choice == 4:
                        print("Logging out")
                        print("Have a nice day!")
                    else:
                        print("Not a valid input")
            else:
                print("Username does not exist.")
        elif choice == 2:
            User.create_table()
            print("Enter a username:")
            new_name_input = input()
            if new_name_input == "":
                print("Invalid name")
            else:
                query = "SELECT * FROM users WHERE LOWER(name) = LOWER(?)"
                CURSOR.execute(query, (new_name_input.lower(),))
                result = CURSOR.fetchone()
                if result:
                    print("Name already exists!")
                else:
                    User.add_name(new_name_input)

        elif choice == 3:
            print("Quitting program")

        elif choice == 24601:
            print("DELETING EVERYTHING")
            User.delete_all()
            Pc.delete_all()
            Parts.delete_all()
        else:
            print("Not a valid input")
    print("Goodbye!")            
    CONN.close()

def create_part(part_type, pc):
    part_pc = pc
    part_list = []
    # Parts.drop_table()
    Parts.create_table()
    print("What is the model name?")
    part_name = input()
    while part_name == "":
        print("Field cannot be empty. Please enter a valid input:")
        part_name = input()
    part_list.append(part_name)
    part_chipset = None
    if part_type == "Motherboard" or part_type == "CPU":
        print("What is the motherboard's chipset?")
        part_chipset = input()
        while part_chipset == "":
            print("Field cannot be empty. Please enter a valid input:")
            part_chipset = input()
        part_list.append(part_chipset)
    part_size = None
    if part_type == "Case" or part_type == "Motherboard":
        case_choice = 0
        while case_choice == 0:
            print("Select a case size")
            print("1) ATX")
            print("2) Micro ATX")
            print("3) Mini ITX")
            try: case_choice = int(input())
            except: print("Enter one of the number options")
            if case_choice == 1:
                part_size = "ATX"
                part_list.append(part_size)
            elif case_choice == 2:
                part_size = "Micro ATX"
                part_list.append(part_size)
            elif case_choice == 3:
                part_size = "Micro ITX"
                part_list.append(part_size)
            else:
                case_choice = 0
                print("Not a valid input")
    part_ram = None
    part_ram_total = None
    if part_type == "RAM":
        ram_count = None
        while ram_count == None:
            print("How many sticks?")
            try: ram_count = int(input()) 
            except: print("Not a Number")
        ram_memory = None
        while ram_memory == None:
            print("How much memory in Gigabytes?")
            try: ram_memory = int(input()) 
            except: print("Not a Number. Do not Include GB")
        part_ram = f"{ram_memory}GB x{ram_count}"
        part_ram_total = ram_memory * ram_count
        part_list.append(part_ram)
    part_storage = None
    if part_type == "Storage":
        part_storage = None
        while part_storage == None:
            print("What is the Storage capacity in Gigabytes?")
            try: part_storage = int(input()) 
            except: print("Not a Number. Do not Include GB")
        part_list.append(part_storage)
    part_power = None
    while part_power == None:
        print("What is the power consumption in Watts?")
        try: part_power = int(input()) 
        except: print("Not a Number. Do not Include W")
    part_list.append(part_power)
    part_price = None
    while part_price == None:
        print("What is the price?")   
        try: part_price = float(input()) 
        except: print("Not a Number. Do not Include $")
    part_list.append(part_price)

    part_list.append(part_pc)
    print(part_list)
    Parts.add_parts(part_name, part_type, part_power, part_price, part_chipset, part_size, part_ram, part_ram_total, part_storage, part_pc)
            # new_part = Parts(name, type, power, price, chipset, size, memory, total_memory, storage, pc)

if __name__ == "__app__":
    app()