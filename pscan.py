
# Port Scanner
# Roods Jacques

# Import Modules
import socket
import time
from datetime import datetime

def main():
    # AF_INET == ipv4
    # SOCK_STREAM == TCP
    # create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #yes and no lists for when user chooses yes or no
    yesList = ["y","yeah","yea","yes","yeap"]
    noList  = ["n","no","nope"]

    #current date and time
    now = datetime.now()
    #formatting date and time to dd/mm/YY H:M:S
    date_string = now.strftime("%m/%d/%Y %H:%M:%S")
    #scanned ports will be save in this file
    scanfile = open("PortResults", "w")

    # Prompt user inputs: IP address
    IP_host = input("Please Enter Host IP Address: ")

    # Verify if Ip address is valid or Invalid
    while True:
        try:
            HostIpAddress = socket.gethostbyname(IP_host)
            break
        except:
            print("Invalid IP Address. Please Enter a Valid IP Address! " + "\n")
            # If IP address is invalid, the return main() will start the program over and prompt user for IP address again
            return main()
    try:
        # Using port 4 as nothing listens on that unassigned port.
        s.connect((IP_host, 4))
    except socket.error as error:
        result = str(error)
    s.close()
    # Parsing the error code. 10060 means timeout. 10061 means target refused it (which means it is alive)
    if (result.startswith("[WinError 10061]")):
        pass
    else:
        print("Host IP seems not to be responding or unreachable.")
        scanfile.write(IP_host)
        scanfile.write(" is not responding." + "\n" +
                       "Please check connection and try again."+"\n" +
                       "Scan aborted at "+ date_string + "\n")
        scanfile.close()
        exit()
    # This function is used for host and port connections
    def ScanPort(IP_host, port):
        s = socket.socket()
        try:
            s.connect((IP_host, port))
        except:
            return False
        else:
            return True
    start_Time = time.time()
    #function will scan the default range of 1 to 1025
    def main_Range():
        print("")#to print a new line
        welcome_Message = "Welcome to Port Scanner!"
        time_Scan = "Ports have started scanning at "+date_string
        defaultMessage = "The default range of 1 to 1025 will be scanned."

        #displays messages to user
        print(welcome_Message)
        print("Host:",IP_host)
        print(defaultMessage + "\n")
        print(time_Scan + "\n")

        #write welcome message and time scan to scanfile.
        scanfile.write(welcome_Message + "\n")
        scanfile.write("Host: "+ IP_host + "\n")
        scanfile.write(defaultMessage + "\n")
        scanfile.write(time_Scan + "\n")
        scanfile.write("\n")
        #default port range 1 to 1025
        default_Range = range(1, 1025+1, 1)

        #for loop to check each port from the range provided
        for x in default_Range:
            if ScanPort(IP_host, x):
                print("port", x, " is open")
                scanfile.write("Port ")
                scanfile.write(str(x))
                scanfile.write(" is open \n")
            else:
                #displaying closed ports to users
                print("port", x, " is closed")
                scanfile.write("Port ")
                scanfile.write(str(x))
                scanfile.write(" is closed \n")

    # Function to prompt user input for Starting Range and Ending Range, after IP address has been validated
    def input_Range():
        while True:#exception if user type a str or invalid input
            try:
                start_Range = int(input("Enter Starting Port Number: "))
                ending_Range = int(input("Enter Ending Port Number: "))
            except ValueError:
                print("Invalid. Number has to be an Integer.")
                continue
            else:
                break

            #nforming the user to input a number greater or equal to the start_Range
            if ending_Range < start_Range:
                print("The Ending Port Number has to be greater than the Starting Port Number.")
                ending_Range = int(input("Enter Ending Port Number: "))

        print("")#to print a new line
        welcome_Message = "Welcome to Port Scanner!"
        time_Scan = "Ports have started scanning at "+date_string

        #displays messages to user
        print(welcome_Message)
        print("Host:",IP_host)
        print("Port Range Selected:", start_Range," - ", ending_Range)
        print(time_Scan + "\n")

        #write welcome message and time scan to scanfile.
        scanfile.write(welcome_Message + "\n")
        scanfile.write("Host: "+ IP_host + "\n")
        scanfile.write("Port Range Selected: "+ str(start_Range) + " - " + str(ending_Range) +"\n")
        scanfile.write(time_Scan + "\n")
        scanfile.write("\n")
        Scan_Range = range(start_Range, ending_Range + 1, 1)

        #check each port in the range or default range
        for x in Scan_Range:
            if ScanPort(IP_host, x):
                print("port", x, " is open")
                scanfile.write("Port ")
                scanfile.write(str(x))
                scanfile.write(" is open \n")
            else:
                #displaying closed ports to users
                print("port", x, " is closed")
                scanfile.write("Port ")
                scanfile.write(str(x))
                scanfile.write(" is closed \n")

    #will ask user if they would like to scan ports from a range, if not the system will the default range (1 to 1025)
    #if user says yes then it will call input_range() function
    #if user say no then it will call main_Range() funtion
    user_Range = input("Would you like to scan from a range? ").lower()
    if user_Range in yesList:
        input_Range()
    else:
        print("The default range of 1 to 1025 will be scanned.")
        main_Range()

    end_Time = time.time()
    total_Scan_Time = end_Time - start_Time

    now = datetime.now()
    date_string = now.strftime("%m/%d/%Y %H:%M:%S")
    print("\n")
    print("Ports scan completed at: ", date_string,"\n")
    print("Ports scan time:", "%.2f" %total_Scan_Time, "seconds.")
    scanfile.write("\n")
    scanfile.write("Ports scan completed at:" + date_string + "\n")
    scanfile.write("Ports scan time: "+ "%.2f" %total_Scan_Time + " seconds" + "\n")

    # Prompt user if they would like to start over
    userConfirm = input("Would you like to Enter a different Host IP Address? ").lower()
    if userConfirm in yesList:
        return main()
    elif userConfirm in noList:
        exit()
    else:
        exit()


main()
