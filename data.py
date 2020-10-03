# Start of file
# Pre-requisites-
# Google Calendar API enabled
# Client ID: 236094030713-os491vaippa5ob1hgak5cbvovu91h5jg.apps.googleusercontent.com
# Client Secret: eZA6iP-XIp6Fkuccpooti9z1

# modules used
import calendar


def func():
    # The variables are temporary and will be replaced by inputs from the GUI, which will interact with the user
    # This section has insurance information
    insurance_type = input("Enter insurance type (HMO/PPO)\n")  # Could be either HMO or PPO

    company_id = input("Enter company code\n")
    personal_id = input("Enter your insurance account number\n")

    # This section has user preferences
    ins_hospital = input("Which is your preferred hospital?\n")
    nurse_option = input("Are your symptoms severe (T/F)?")
    while True:
        if nurse_option == "T" or nurse_option == "F":
            break
        else:
            nurse_option = input("Incorrect input, please try again... (T/F)\n")
    if nurse_option == "T":
        preferred_doctor = input("Who is your preferred doctor?\n")
    else:
        preferred_doctor = "Nurse"

    ins_file = open("insurance_file.txt", "w+")
    ins_file.write("Insurance Information\n" + "Type: " + insurance_type + "\nCompany ID: " + company_id +
                   "\nPersonal ID: " + personal_id + "\n")
    ins_file.close()

    pref_file = open("preferences_file.txt", "w+")
    pref_file.write("Preferences\n" + "DR: " + preferred_doctor + "\nHospital: " + ins_hospital + "\nNurse: "
                    + str(nurse_option) + "\n")

    pref_file.close()
    year = input("What year is it (YYYY)?\n")
    month = input("What month do you want to search (MM)?\n")
    calendar_file = open("calendar_file.txt", "w+")
    calendar_file.write(calendar.month(int(year), int(month)))


# End of file
