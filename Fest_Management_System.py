import mysql.connector
from tkinter import *
from tkinter import messagebox

# Global variables for MySQL credentials
username = ""
password = ""

# Function to prompt user for MySQL username and password
def get_mysql_credentials():
    root = Tk()
    root.title("MySQL Credentials")
    root.geometry("600x300")
    text = Text(root)
    
    root.config(bg="#EADBC8")

    def submit_credentials():
        global username
        global password
        username = username_entry.get()
        password = password_entry.get()
        root.destroy()

    username_label = Label(root, text="Username:")
    username_label.grid(row=0, column=0)
    username_entry = Entry(root)
    username_entry.grid(row=0, column=1)

    username_label.place(relx=0.35, rely=0.3, anchor=CENTER)
    username_entry.place(relx=0.55, rely=0.3, anchor=CENTER)
    username_label.config(bg="#EADBC8")

    password_label = Label(root, text="Password:")
    password_label.grid(row=1, column=0)
    password_entry = Entry(root, show="*")
    password_entry.grid(row=1, column=1)
    
    password_label.place(relx=0.35, rely=0.4, anchor=CENTER)
    password_entry.place(relx=0.55, rely=0.4, anchor=CENTER)
    password_label.config(bg="#EADBC8")

    submit_button = Button(root, text="Submit", command=submit_credentials)
    submit_button.grid(row=2, columnspan=2)

    submit_button.place(relx=0.485, rely=0.5, anchor=CENTER)

    root.mainloop()

# Function to connect to MySQL database
def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS Fest_Management")
        mydb = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database="Fest_Management"
        )
        return mydb
    except mysql.connector.Error as err:
        print("Error:", err)

# Check if Fest table exists, if not, create it
def create_fest_table():
    try:
        mycursor.execute("CREATE TABLE IF NOT EXISTS Fest (Name VARCHAR(255) PRIMARY KEY, Date DATE, Board VARCHAR(255))")
    except mysql.connector.Error as err:
        print("Error:", err)


    # Function to handle opening the Sponsors window
def open_sponsors_window():
        def add_sponsors():
            def add_sponsors_data():
                try:
                    # Check if the Sponsors table exists
                    mycursor.execute("SELECT 1 FROM Sponsors LIMIT 1")
                    mycursor.fetchone()  # Consume the result
                except mysql.connector.Error as err:
                    # Create the Sponsors table if it doesn't exist
                    try:
                        mycursor.execute("CREATE TABLE IF NOT EXISTS Sponsors (Sponsor_ID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Amount DECIMAL(10, 2), Type VARCHAR(255), Mobile_No VARCHAR(15), Email VARCHAR(255), Person_Incharge VARCHAR(255), Status VARCHAR(50))")
                        mydb.commit()
                    except mysql.connector.Error as err:
                        print("Error:", err)

                # Get sponsor details from entry fields
                sponsor_id = sponsor_id_entry.get()
                name = name_entry.get()
                amount = amount_entry.get()
                sponsor_type = type_entry.get()
                mobile_no = mobile_no_entry.get()
                email = email_entry.get()
                person_in_charge = person_in_charge_entry.get()
                status = status_entry.get()

                # Insert sponsor details into Sponsors table
                try:
                    insert_query = "INSERT INTO Sponsors (Sponsor_ID, Name, Amount, Type, Mobile_No, Email, Person_Incharge, Status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    sponsor_data = (sponsor_id, name, amount, sponsor_type, mobile_no, email, person_in_charge, status)
                    mycursor.execute(insert_query, sponsor_data)
                    mydb.commit()  # Commit the transaction
                    messagebox.showinfo("Success", "Sponsor added successfully!")
                    add_sponsors_window.destroy()  # Close the window after adding sponsor
                except mysql.connector.Error as err:
                    print("Error:", err)


            add_sponsors_window = Toplevel()
            add_sponsors_window.title("Add Sponsor")
            add_sponsors_window.geometry("1750x1250")

            # Sponsor ID input
            sponsor_id_label = Label(add_sponsors_window, text="Sponsor ID:", font=("ARIAL", 20))
            sponsor_id_label.grid(row=0, column=0)
            sponsor_id_entry = Entry(add_sponsors_window)
            sponsor_id_entry.grid(row=0, column=1)
            sponsor_id_label.place(relx=0.4, rely=0.1, anchor=CENTER)
            sponsor_id_entry.place(relx=0.525, rely=0.1, anchor=CENTER)
            sponsor_id_label.config(bg="#C6EBC5")


            # Name input
            name_label = Label(add_sponsors_window, text="Name:", font=("ARIAL", 20))
            name_label.grid(row=1, column=0)
            name_entry = Entry(add_sponsors_window)
            name_entry.grid(row=1, column=1)
            name_label.place(relx=0.4, rely=0.2, anchor=CENTER)
            name_entry.place(relx=0.525, rely=0.2, anchor=CENTER)
            name_label.config(bg="#C6EBC5")

            # Amount input
            amount_label = Label(add_sponsors_window, text="Amount:", font=("ARIAL", 20))
            amount_label.grid(row=2, column=0)
            amount_entry = Entry(add_sponsors_window)
            amount_entry.grid(row=2, column=1)
            amount_label.place(relx=0.4, rely=0.3, anchor=CENTER)
            amount_entry.place(relx=0.525, rely=0.3, anchor=CENTER)
            amount_label.config(bg="#C6EBC5")

            # Type input
            type_label = Label(add_sponsors_window, text="Type:", font=("ARIAL", 20))
            type_label.grid(row=3, column=0)
            type_entry = Entry(add_sponsors_window)
            type_entry.grid(row=3, column=1)
            type_label.place(relx=0.4, rely=0.4, anchor=CENTER)
            type_entry.place(relx=0.525, rely=0.4, anchor=CENTER)
            type_label.config(bg="#C6EBC5")

            # Mobile No input
            mobile_no_label = Label(add_sponsors_window, text="Mobile No:", font=("ARIAL", 20))
            mobile_no_label.grid(row=4, column=0)
            mobile_no_entry = Entry(add_sponsors_window)
            mobile_no_entry.grid(row=4, column=1)
            mobile_no_label.place(relx=0.4, rely=0.5, anchor=CENTER)
            mobile_no_entry.place(relx=0.525, rely=0.5, anchor=CENTER)
            mobile_no_label.config(bg="#C6EBC5")

            # Email input
            email_label = Label(add_sponsors_window, text="Email:", font=("ARIAL", 20))
            email_label.grid(row=5, column=0)
            email_entry = Entry(add_sponsors_window)
            email_entry.grid(row=5, column=1)
            email_label.place(relx=0.4, rely=0.6, anchor=CENTER)
            email_entry.place(relx=0.525, rely=0.6, anchor=CENTER)
            email_label.config(bg="#C6EBC5")

            # Person in Charge input
            person_in_charge_label = Label(add_sponsors_window, text="Person in Charge:", font=("ARIAL", 20))
            person_in_charge_label.grid(row=6, column=0)
            person_in_charge_entry = Entry(add_sponsors_window)
            person_in_charge_entry.grid(row=6, column=1)
            person_in_charge_label.place(relx=0.4, rely=0.7, anchor=CENTER)
            person_in_charge_entry.place(relx=0.525, rely=0.7, anchor=CENTER)
            person_in_charge_label.config(bg="#C6EBC5")

            # Status input
            status_label = Label(add_sponsors_window, text="Status:", font=("ARIAL", 20))
            status_label.grid(row=7, column=0)
            status_entry = Entry(add_sponsors_window)
            status_entry.grid(row=7, column=1)
            status_label.place(relx=0.4, rely=0.8, anchor=CENTER)
            status_entry.place(relx=0.525, rely=0.8, anchor=CENTER)
            status_label.config(bg="#C6EBC5")

            # Submit button
            submit_button = Button(add_sponsors_window, text="Submit", command=add_sponsors_data, height=3, width=10)
            submit_button.grid(row=8, columnspan=2)
            submit_button.place(relx=0.5, rely=0.875, anchor=CENTER)

            add_sponsors_window.config(bg="#C6EBC5")

        def delete_sponsors():
            def delete_sponsors_data():
                sponsor_id = sponsor_id_entry.get()

                # Check if sponsor ID exists
                try:
                    mycursor.execute("SELECT * FROM Sponsors WHERE Sponsor_ID = %s", (sponsor_id,))
                    if not mycursor.fetchone():
                        messagebox.showerror("Error", "Sponsor ID does not exist!")
                        return
                except mysql.connector.Error as err:
                    print("Error:", err)

                # Confirm deletion
                confirm = messagebox.askyesno("Confirm Deletion", f"Do you want to delete sponsor with ID {sponsor_id}?")
                if confirm:
                    # Delete sponsor
                    try:
                        mycursor.execute("DELETE FROM Sponsors WHERE Sponsor_ID = %s", (sponsor_id,))
                        mydb.commit()
                        messagebox.showinfo("Success", f"Sponsor with ID {sponsor_id} deleted successfully!")
                        delete_sponsors_window.destroy()  # Close the window after deletion
                    except mysql.connector.Error as err:
                        print("Error:", err)

            delete_sponsors_window = Toplevel()
            delete_sponsors_window.title("Delete Sponsor")
            delete_sponsors_window.geometry("1750x1250")

            # Sponsor ID input
            sponsor_id_label = Label(delete_sponsors_window, text="Enter Sponsor ID:", font=("ARIAL", 20))
            sponsor_id_label.grid(row=0, column=0)
            sponsor_id_label.place(relx=0.4, rely=0.4, anchor=CENTER)
            sponsor_id_label.config(bg="#FA7070")

            sponsor_id_entry = Entry(delete_sponsors_window)
            sponsor_id_entry.grid(row=0, column=1)
            sponsor_id_entry.place(relx=0.525, rely=0.4, anchor=CENTER)

            # Delete button
            delete_button = Button(delete_sponsors_window, text="Delete", command=delete_sponsors_data, height=3, width=12)
            delete_button.grid(row=1, columnspan=2)
            delete_button.place(relx=0.5, rely=0.5)

            delete_sponsors_window.config(bg="#FA7070")

        def all_sponsors():
            try:
                mycursor.execute("SELECT * FROM Sponsors")
                sponsors = mycursor.fetchall()
                if sponsors:
                    all_sponsors_window = Toplevel()
                    all_sponsors_window.title("All Sponsors")
                    all_sponsors_window.geometry("1750x1250")

                    for i, sponsor in enumerate(sponsors):
                        label = Label(all_sponsors_window, text=f"{i + 1}. Sponsor ID: {sponsor[0]}, Name: {sponsor[1]}, Amount: {sponsor[2]}, Type: {sponsor[3]}, Mobile No.: {sponsor[4]}, Email: {sponsor[5]}, Person In Charge: {sponsor[6]}, Status: {sponsor[7]}",font=("ARIAL",10))
                        label.config(bg="#FFF3C7")
                        label.pack()
                        label.place(relx=0.5, rely=0.2+i*0.05, anchor=CENTER)

                    all_sponsors_window.config(bg="#FFF3C7")
                else:
                    messagebox.showinfo("Info", "No sponsors found!")
            except mysql.connector.Error as err:
                print("Error:", err)

        def load_type():
            def load_type_data():
                sponsor_type = type_entry.get()

                try:
                    mycursor.execute("SELECT * FROM Sponsors WHERE Type = %s", (sponsor_type,))
                    sponsors = mycursor.fetchall()
                    if sponsors:
                        load_type_window = Toplevel()
                        load_type_window.title("Sponsors of Type")
                        load_type_window.geometry("1750x1250")

                        for i, sponsor in enumerate(sponsors):
                            label = Label(load_type_window, text=f"{i + 1}. Sponsor ID: {sponsor[0]}, Name: {sponsor[1]}, Amount: {sponsor[2]}, Type: {sponsor[3]}, Mobile No.: {sponsor[4]}, Email: {sponsor[5]}, Person In Charge: {sponsor[6]}, Status: {sponsor[7]}")
                            label.config(bg="#FFF3C7")
                            label.pack()
                        load_type_window.config(bg="#FFF3C7")
                    else:
                        messagebox.showinfo("Info", f"No sponsors found for type {sponsor_type}!")
                except mysql.connector.Error as err:
                    print("Error:", err)

            load_type_window = Toplevel()
            load_type_window.title("Load Type")
            load_type_window.geometry("1750x1250")

            type_label = Label(load_type_window, text="Enter Type:", font=("ARIAL", 20))
            type_label.grid(row=0, column=0)
            type_label.place(relx=0.4, rely=0.4, anchor=CENTER)
            type_label.config(bg="#FFF3C7")

            type_entry = Entry(load_type_window)
            type_entry.grid(row=0, column=1)
            type_entry.place(relx=0.525, rely=0.4, anchor=CENTER)

            load_button = Button(load_type_window, text="Load", command=load_type_data, height=3, width=12)
            load_button.grid(row=1, columnspan=2)
            load_button.place(relx=0.5, rely=0.5)

            load_type_window.config(bg="#FFF3C7")


        sponsors_window = Toplevel()
        sponsors_window.title("Sponsors")
        sponsors_window.geometry("1750x1250")

        # Add Sponsors button
        add_sponsors_button = Button(sponsors_window, text="Add Sponsors", command=add_sponsors, font=("ARIAL", 20))
        add_sponsors_button.pack()
        add_sponsors_button.place(relx=0.3, rely=0.3, anchor=CENTER)
        add_sponsors_button.config(bg="#B47B84")

        # Delete Sponsors button
        delete_sponsors_button = Button(sponsors_window, text="Delete Sponsors", command=delete_sponsors, font=("ARIAL", 20))
        delete_sponsors_button.pack()
        delete_sponsors_button.place(relx=0.3, rely=0.6, anchor=CENTER)
        delete_sponsors_button.config(bg="#B47B84")

        # All Sponsors button
        all_sponsors_button = Button(sponsors_window, text="All Sponsors", command=all_sponsors, font=("ARIAL", 20))
        all_sponsors_button.pack()
        all_sponsors_button.place(relx=0.7, rely=0.3, anchor=CENTER)
        all_sponsors_button.config(bg="#B47B84")

        # Load Type button
        load_type_button = Button(sponsors_window, text="Load Type", command=load_type, font=("ARIAL", 20))
        load_type_button.pack()
        load_type_button.place(relx=0.7, rely=0.6, anchor=CENTER)
        load_type_button.config(bg="#B47B84")

        sponsors_window.config(bg="#CAA6A6")


    # Function to handle opening the Events window
def open_events_window():
        def add_event():
            def add_event_data():
                try:
                # Check if the Events table exists
                    mycursor.execute("SELECT 1 FROM Events LIMIT 1")
                    mycursor.fetchone() # Consume the result
                except mysql.connector.Error as err:
                    # Create the Events table if it doesn't exist
                    try:
                        mycursor.execute("CREATE TABLE IF NOT EXISTS Events (Event_ID INT AUTO_INCREMENT PRIMARY KEY, Event_Name VARCHAR(255), Date DATE, Time TIME, Duration VARCHAR(50), Event_Lead VARCHAR(255), Member_ID INT, Prize_Money DECIMAL(10, 2), Club_Name VARCHAR(255), Venue VARCHAR(255), No_of_Rounds INT)")
                        mydb.commit()
                    except mysql.connector.Error as err:
                        print("Error:", err)

                # Get event details from entry fields
                event_id = event_id_entry.get()
                event_name = event_name_entry.get()
                date = date_entry.get()
                time = time_entry.get()
                duration = duration_entry.get()
                event_lead = event_lead_entry.get()
                member_id = member_id_entry.get()
                prize_money = prize_money_entry.get()
                club_name = club_name_entry.get()
                venue = venue_entry.get()
                rounds = rounds_entry.get()

                # Insert event details into Events table
                try:
                    insert_query = "INSERT INTO Events (Event_ID, Event_Name, Date, Time, Duration, Event_Lead, Member_ID, Prize_Money, Club_Name, Venue, No_of_Rounds) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    event_data = (event_id, event_name, date, time, duration, event_lead, member_id, prize_money, club_name, venue, rounds)
                    mycursor.execute(insert_query, event_data)
                    mydb.commit()  # Commit the transaction
                    messagebox.showinfo("Success", "Event added successfully!")
                    add_event_window.destroy()  # Close the window after adding event
                except mysql.connector.Error as err:
                    print("Error:", err)

            add_event_window = Toplevel()
            add_event_window.title("Add Event")
            add_event_window.geometry("1750x1250")

            # Event ID input
            event_id_label = Label(add_event_window, text="Event ID:", font=("ARIAL", 20))
            event_id_label.grid(row=0, column=0)
            event_id_entry = Entry(add_event_window)
            event_id_entry.grid(row=0, column=1)
            event_id_label.place(relx=0.4, rely=0.07, anchor=CENTER)
            event_id_entry.place(relx=0.525, rely=0.07, anchor=CENTER)
            event_id_label.config(bg="#FEC7B4")

            # Event Name input
            event_name_label = Label(add_event_window, text="Event Name:", font=("ARIAL", 20))
            event_name_label.grid(row=1, column=0)
            event_name_entry = Entry(add_event_window)
            event_name_entry.grid(row=1, column=1)
            event_name_label.place(relx=0.4, rely=0.14, anchor=CENTER)
            event_name_entry.place(relx= 0.525, rely=0.14, anchor=CENTER)
            event_name_label.config(bg="#FEC7B4")

            # Date input
            date_label = Label(add_event_window, text="Date (YYYY-MM-DD):", font=("ARIAL", 20))
            date_label.grid(row=2, column=0)
            date_entry = Entry(add_event_window)
            date_entry.grid(row=2, column=1)
            date_label.place(relx=0.38, rely=0.21, anchor=CENTER)
            date_entry.place(relx=0.525, rely=0.21, anchor=CENTER)
            date_label.config(bg="#FEC7B4")

            # Time input
            time_label = Label(add_event_window, text="Time (HH:MM:SS):", font=("ARIAL", 20))
            time_label.grid(row=3, column=0)
            time_entry = Entry(add_event_window)
            time_entry.grid(row=3, column=1)
            time_label.place(relx=0.4, rely=0.28, anchor=CENTER)
            time_entry.place(relx=0.525, rely=0.28, anchor=CENTER)
            time_label.config(bg="#FEC7B4")

            # Duration input
            duration_label = Label(add_event_window, text="Duration:", font=("ARIAL", 20))
            duration_label.grid(row=4, column=0)
            duration_entry = Entry(add_event_window)
            duration_entry.grid(row=4, column=1)
            duration_label.place(relx=0.4, rely=0.35, anchor=CENTER)
            duration_entry.place(relx=0.525, rely=0.35, anchor=CENTER)
            duration_label.config(bg="#FEC7B4")

            # Event Lead input
            event_lead_label = Label(add_event_window, text="Event Lead:", font=("ARIAL", 20))
            event_lead_label.grid(row=5, column=0)
            event_lead_entry = Entry(add_event_window)
            event_lead_entry.grid(row=5, column=1)
            event_lead_label.place(relx=0.4,rely=0.42, anchor=CENTER)
            event_lead_entry.place(relx=0.525, rely=0.42, anchor=CENTER)
            event_lead_label.config(bg="#FEC7B4")

            # Member ID input
            member_id_label = Label(add_event_window, text="Member ID:", font=("ARIAL", 20))
            member_id_label.grid(row=6, column=0)
            member_id_entry = Entry(add_event_window)
            member_id_entry.grid(row=6, column=1)
            member_id_label.place(relx=0.4, rely=0.49, anchor=CENTER)
            member_id_entry.place(relx=0.525, rely=0.49, anchor=CENTER)
            member_id_label.config(bg="#FEC7B4")

            # Prize Money input
            prize_money_label = Label(add_event_window, text="Prize Money:", font=("ARIAL", 20))
            prize_money_label.grid(row=7, column=0)
            prize_money_entry = Entry(add_event_window)
            prize_money_entry.grid(row=7, column=1)
            prize_money_label.place(relx=0.4, rely=0.56, anchor=CENTER)
            prize_money_entry.place(relx=0.525, rely=0.56, anchor=CENTER)
            prize_money_label.config(bg="#FEC7B4")

            # Club Name input
            club_name_label = Label(add_event_window, text="Club Name:", font=("ARIAL", 20))
            club_name_label.grid(row=8, column=0)
            club_name_entry = Entry(add_event_window)
            club_name_entry.grid(row=8, column=1)
            club_name_label.place(relx=0.4, rely=0.63, anchor=CENTER)
            club_name_entry.place(relx=0.525, rely=0.63, anchor=CENTER)
            club_name_label.config(bg="#FEC7B4")

            # Venue input
            venue_label = Label(add_event_window, text="Venue:", font=("ARIAL", 20))
            venue_label.grid(row=9, column=0)
            venue_entry = Entry(add_event_window)
            venue_entry.grid(row=9, column=1)
            venue_label.place(relx=0.4, rely=0.7, anchor=CENTER)
            venue_entry.place(relx=0.525, rely=0.7, anchor=CENTER)
            venue_label.config(bg="#FEC7B4")

            # No. of Rounds input
            rounds_label = Label(add_event_window, text="No. of Rounds:", font=("ARIAL", 20))
            rounds_label.grid(row=10, column=0)
            rounds_entry = Entry(add_event_window)
            rounds_entry.grid(row=10, column=1)
            rounds_label.place(relx=0.4, rely=0.77, anchor=CENTER)
            rounds_entry.place(relx=0.525, rely=0.77, anchor=CENTER)
            rounds_label.config(bg="#FEC7B4")
            # Submit button
            submit_button = Button(add_event_window, text="Submit", command=add_event_data, height=3, width=12)
            submit_button.grid(row=11, columnspan=2)
            submit_button.place(relx=0.5, rely=0.82, anchor=CENTER)

            add_event_window.config(bg="#FEC7B4")

        def delete_event():
            def delete_event_data():
                event_id = event_id_entry.get()

                # Check if event ID exists
                try:
                    mycursor.execute("SELECT * FROM Events WHERE Event_ID = %s", (event_id,))
                    if not mycursor.fetchone():
                        messagebox.showerror("Error", "Event ID does not exist!")
                        return
                except mysql.connector.Error as err:
                    print("Error:", err)

                # Confirm deletion
                confirm = messagebox.askyesno("Confirm Deletion", f"Do you want to delete event with ID {event_id}?")
                if confirm:
                    # Delete event
                    try:
                        mycursor.execute("DELETE FROM Events WHERE Event_ID = %s", (event_id,))
                        mydb.commit()
                        messagebox.showinfo("Success", f"Event with ID {event_id} deleted successfully!")
                        delete_event_window.destroy()  # Close the window after deletion
                    except mysql.connector.Error as err:
                        print("Error:", err)

            delete_event_window = Toplevel()
            delete_event_window.title("Delete Event")
            delete_event_window.geometry("1750x1250")

            # Event ID input
            event_id_label = Label(delete_event_window, text="Enter Event ID:", font=("ARIAL", 20))
            event_id_label.grid(row=0, column=0)
            event_id_label.place(relx=0.4, rely=0.4, anchor=CENTER)
            event_id_label.config(bg="#FA7070")

            event_id_entry = Entry(delete_event_window)
            event_id_entry.grid(row=0, column=1)
            event_id_entry.place(relx=0.5, rely=0.4)

            # Delete button
            delete_button = Button(delete_event_window, text="Delete", command=delete_event_data, height=3, width=12)
            delete_button.grid(row=1, columnspan=2)
            delete_button.place(relx=0.5, rely=0.5, anchor=CENTER)

            delete_event_window.config(bg="#FA7070")


        def all_events():
            try:
                mycursor.execute("SELECT * FROM Events")
                events = mycursor.fetchall()
                if events:
                    all_events_window = Toplevel()
                    all_events_window.title("All Events")
                    all_events_window.geometry("1750x1250")

                    for i, event in enumerate(events):
                        label = Label(all_events_window, text=f"{i + 1}. Event ID: {event[0]}, Event Name: {event[1]}, Date: {event[2]}, Time: {event[3]}, Duration: {event[4]}, Event Lead: {event[5]}, Member ID: {event[6]}, Prize Money: {event[7]}, Club Name: {event[8]}, Venue: {event[9]}, No. of Rounds: {event[10]}",font=("ARIAL", 10))
                        label.config(bg="#E5E483")
                        label.pack()
                        label.place(relx=0.5, rely=0.2+i*0.05, anchor=CENTER)
                    all_events_window.config(bg="#E5E483")
                else:
                    messagebox.showinfo("Info", "No events found!")
            except mysql.connector.Error as err:
                print("Error:", err)

        def load_event():
            def load_event_data():
                event_id = event_id_entry.get()

                try:
                    mycursor.execute("SELECT * FROM Events WHERE Event_ID = %s", (event_id,))
                    event = mycursor.fetchone()
                    if event:
                        load_event_window = Toplevel()
                        load_event_window.title("Event Details")
                        load_event_window.geometry("1750x1250")

                        Label(load_event_window, text=f"Event ID: {event[0]}").pack()
                        Label(load_event_window, text=f"Event Name: {event[1]}").pack()
                        Label(load_event_window, text=f"Date: {event[2]}").pack()
                        Label(load_event_window, text=f"Time: {event[3]}").pack()
                        Label(load_event_window, text=f"Duration: {event[4]}").pack()
                        Label(load_event_window, text=f"Event Lead: {event[5]}").pack()
                        Label(load_event_window, text=f"Member ID: {event[6]}").pack()
                        Label(load_event_window, text=f"Prize Money: {event[7]}").pack()
                        Label(load_event_window, text=f"Club Name: {event[8]}").pack()
                        Label(load_event_window, text=f"Venue: {event[9]}").pack()
                        Label(load_event_window, text=f"No. of Rounds: {event[10]}").pack()
                    else:
                        messagebox.showinfo("Info", f"No event found for ID {event_id}!")
                except mysql.connector.Error as err:
                    print("Error:", err)

            load_event_window = Toplevel()
            load_event_window.title("Load Event")
            load_event_window.geometry("1750x1250")

            event_id_label = Label(load_event_window, text="Enter Event ID:", font=("ARIAL", 20))
            event_id_label.grid(row=0, column=0)
            event_id_label.place(relx=0.4, rely=0.4, anchor=CENTER)
            event_id_label.config(bg="#E5E483")

            event_id_entry = Entry(load_event_window)
            event_id_entry.grid(row=0, column=1)
            event_id_entry.place(relx=0.525, rely=0.4, anchor=CENTER)

            load_button = Button(load_event_window, text="Load", command=load_event_data, height=3, width=12)
            load_button.grid(row=1, columnspan=2)
            load_button.place(relx=0.5, rely=0.5, anchor=CENTER)

            load_event_window.config(bg="#E5E483")

        events_window = Toplevel()
        events_window.title("Events")
        events_window.geometry("1750x1250")

        # Add Events button
        add_event_button = Button(events_window, text="Add Event", command=add_event, font=("ARIAL", 20))
        add_event_button.pack()
        add_event_button.place(relx=0.3, rely=0.3, anchor=CENTER)
        add_event_button.config(bg="#E2BFB3")


        # Delete Events button
        delete_event_button = Button(events_window, text="Delete Event", command=delete_event, font=("ARIAL", 20))
        delete_event_button.pack()
        delete_event_button.place(relx=0.3, rely=0.6, anchor=CENTER)
        delete_event_button.config(bg="#E2BFB3")

        # All Events button
        all_events_button = Button(events_window, text="All Events", command=all_events, font=("ARIAL", 20))
        all_events_button.pack()
        all_events_button.place(relx=0.7, rely=0.3, anchor=CENTER)
        all_events_button.config(bg="#E2BFB3")

        # Load Event button
        load_event_button = Button(events_window, text="Load Event", command=load_event, font=("ARIAL", 20))
        load_event_button.pack()
        load_event_button.place(relx=0.7, rely=0.6, anchor=CENTER)
        load_event_button.config(bg="#E2BFB3")

        events_window.config(bg="#F7DED0")


    # Function to handle opening the Teams window
def teams_window():
        teams_window = Toplevel()
        teams_window.title("Teams")
        teams_window.geometry("1750x1250")

        def team_window(team_name):
            def add_member():
                def add_member_data():
                    try:
                        # Check if the team's table exists
                        mycursor.execute(f"SELECT 1 FROM {team_name} LIMIT 1")
                        mycursor.fetchone() # Consume the result
                    except mysql.connector.Error as err:
                        # Create the team's table if it doesn't exist
                        try:
                            mycursor.execute(f"CREATE TABLE IF NOT EXISTS {team_name} (Member_ID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Roll_No VARCHAR(20), Designation VARCHAR(255))")
                            mydb.commit()
                        except mysql.connector.Error as err:
                            print("Error:", err)

                    # Get member details from entry fields
                    name = name_entry.get()
                    roll_no = roll_no_entry.get()
                    designation = designation_entry.get()

                    # Insert member details into team's table
                    try:
                        insert_query = f"INSERT INTO {team_name} (Name, Roll_No, Designation) VALUES (%s, %s, %s)"
                        member_data = (name, roll_no, designation)
                        mycursor.execute(insert_query, member_data)
                        mydb.commit()  # Commit the transaction
                        messagebox.showinfo("Success", "Member added successfully!")
                        add_member_window.destroy()  # Close the window after adding member
                    except mysql.connector.Error as err:
                        print("Error:", err)

                add_member_window = Toplevel()
                add_member_window.title("Add Member")
                add_member_window.geometry("1750x1250")

                # Name input
                name_label = Label(add_member_window, text="Name:", font=("ARIAL", 20))
                name_label.grid(row=0, column=0)
                name_label.place(relx=0.4, rely=0.3, anchor=CENTER)
                name_entry = Entry(add_member_window)
                name_entry.grid(row=0, column=1)
                name_entry.place(relx=0.525, rely=0.3, anchor=CENTER)
                name_label.config(bg="#C6DCBA")

                # Roll No input
                roll_no_label = Label(add_member_window, text="Roll No:", font=("ARIAL", 20))
                roll_no_label.grid(row=1, column=0)
                roll_no_label.place(relx=0.4, rely=0.45, anchor=CENTER)
                roll_no_entry = Entry(add_member_window)
                roll_no_entry.grid(row=1, column=1)
                roll_no_entry.place(relx=0.525, rely=0.45, anchor=CENTER)
                roll_no_label.config(bg="#C6DCBA")

                # Designation input
                designation_label = Label(add_member_window, text="Designation:", font=("ARIAL", 20))
                designation_label.grid(row=2, column=0)
                designation_label.place(relx=0.4, rely=0.6, anchor=CENTER)
                designation_entry = Entry(add_member_window)
                designation_entry.grid(row=2, column=1)
                designation_entry.place(relx=0.525, rely=0.6, anchor=CENTER)
                designation_label.config(bg="#C6DCBA")

                # Submit button
                submit_button = Button(add_member_window, text="Submit", command=add_member_data, height=3, width=12)
                submit_button.grid(row=3, columnspan=2)
                submit_button.place(relx=0.5, rely=0.7, anchor=CENTER)

                add_member_window.config(bg="#C6DCBA")

            def delete_member():
                def delete_member_data():
                    member_id = member_id_entry.get()

                    # Check if member ID exists in the team's table
                    try:
                        mycursor.execute(f"SELECT * FROM {team_name} WHERE Member_ID = %s", (member_id,))
                        if not mycursor.fetchone():
                            messagebox.showerror("Error", "Member ID does not exist!")
                            return
                    except mysql.connector.Error as err:
                        print("Error:", err)

                    # Confirm deletion
                    confirm = messagebox.askyesno("Confirm Deletion", f"Do you want to delete member with ID {member_id}?")
                    if confirm:
                        # Delete member
                        try:
                            mycursor.execute(f"DELETE FROM {team_name} WHERE Member_ID = %s", (member_id,))
                            mydb.commit()
                            messagebox.showinfo("Success", f"Member with ID {member_id} deleted successfully!")
                            delete_member_window.destroy()  # Close the window after deletion
                        except mysql.connector.Error as err:
                            print("Error:", err)

                delete_member_window = Toplevel()
                delete_member_window.title("Delete Member")
                delete_member_window.geometry("1750x1250")

                # Member ID input
                member_id_label = Label(delete_member_window, text="Enter Member ID:", font=("ARIAL", 20))
                member_id_label.grid(row=0, column=0)
                member_id_label.place(relx=0.4, rely=0.4, anchor=CENTER)
                member_id_label.config(bg="#FA7070")

                member_id_entry = Entry(delete_member_window)
                member_id_entry.grid(row=0, column=1)
                member_id_entry.place(relx=0.525, rely=0.4, anchor=CENTER)

                # Delete button
                delete_button = Button(delete_member_window, text="Delete", command=delete_member_data, height=3, width=12)
                delete_button.grid(row=1, columnspan=2)
                delete_button.place(relx=0.5, rely=0.5, anchor=CENTER)

                delete_member_window.config(bg="#FA7070")



            def all_members():
                try:
                    mycursor.execute(f"SELECT * FROM {team_name}")
                    members = mycursor.fetchall()
                    if members:
                        all_members_window = Toplevel()
                        all_members_window.title(f"All Members of {team_name}")
                        all_members_window.geometry("1750x1250")

                        for i, member in enumerate(members):
                            label = Label(all_members_window, text=f"{i + 1}. Member ID: {member[0]}, Name: {member[1]}, Roll No: {member[2]}, Designation: {member[3]}", font=("ARIAL",10))
                            label.config(bg="#88AB8E")
                            label.pack()
                            label.place(relx=0.5, rely=0.2+i*0.05, anchor=CENTER)
                        all_members_window.config(bg="#88AB8E")
                    else:
                        messagebox.showinfo("Info", f"No members found in {team_name}!")
                except mysql.connector.Error as err:
                    print("Error:", err)


            team_window = Toplevel()
            team_window.title(team_name)
            team_window.geometry("1750x1250")

            # Add Members button
            add_member_button = Button(team_window, text="Add Members", command=add_member, font=("ARIAL", 20))
            add_member_button.pack()
            add_member_button.place(relx=0.5, rely=0.3, anchor=CENTER)
            add_member_button.config(bg="#BBAB8C")

            # Delete Members button
            delete_member_button = Button(team_window, text="Delete Members", command=delete_member, font=("ARIAL", 20))
            delete_member_button.pack()
            delete_member_button.place(relx=0.5, rely=0.45, anchor=CENTER)
            delete_member_button.config(bg="#BBAB8C")

            # All Members button
            all_members_button = Button(team_window, text="All Members", command=all_members, font=("ARIAL", 20))
            all_members_button.pack()
            all_members_button.place(relx=0.5, rely=0.6, anchor=CENTER)
            all_members_button.config(bg="#BBAB8C")

            team_window.config(bg="#DED0B6")

        # Sponsorship Team button
        sponsorship_button = Button(teams_window, text="Sponsorship Team", command=lambda: team_window("Sponsorship_Team"), font=("ARIAL", 20))
        sponsorship_button.pack()
        sponsorship_button.place(relx=0.3, rely=0.3, anchor=CENTER)
        sponsorship_button.config(bg="#776B5D")

        # Event and Management Team button
        event_management_button = Button(teams_window, text="Event and Management Team", command=lambda: team_window("Event_and_Management_Team"), font=("ARIAL", 20))
        event_management_button.pack()
        event_management_button.place(relx=0.3, rely=0.6, anchor=CENTER)
        event_management_button.config(bg="#776B5D")

        # Web and Creative Team button
        web_creative_button = Button(teams_window, text="Web and Creative Team", command=lambda: team_window("Web_and_Creative_Team"), font=("ARIAL", 20))
        web_creative_button.pack()
        web_creative_button.place(relx=0.7, rely=0.3, anchor=CENTER)
        web_creative_button.config(bg="#776B5D")

        # Media and Publicity Team button
        media_publicity_button = Button(teams_window, text="Media and Publicity Team", command=lambda: team_window("Media_and_Publicity_Team"), font=("ARIAL", 20))
        media_publicity_button.pack()
        media_publicity_button.place(relx=0.7, rely=0.6, anchor=CENTER)
        media_publicity_button.config(bg="#776B5D")

        # Public and Relations Team button
        public_relations_button = Button(teams_window, text="Public and Relations Team", command=lambda: team_window("Public_and_Relations_Team"), font=("ARIAL", 20))
        public_relations_button.pack()
        public_relations_button.place(relx=0.5, rely=0.8, anchor=CENTER)
        public_relations_button.config(bg="#776B5D")

        teams_window.config(bg="#B0A695")


    # Function to handle opening the Participants window
def open_participants_window():
        def add_participant():
            def add_participant_data():
                try:
                    # Check if the Participants table exists
                    mycursor.execute("SELECT 1 FROM Participants LIMIT 1")
                    mycursor.fetchone() # Consume the result
                except mysql.connector.Error as err:
                    # Create the Participants table if it doesn't exist
                    try:
                        mycursor.execute("CREATE TABLE IF NOT EXISTS Participants (Participant_ID INT AUTO_INCREMENT PRIMARY KEY, Participant_Name VARCHAR(255), College VARCHAR(255), Event_ID INT, Phone_Number VARCHAR(15), Email_ID VARCHAR(255), CONSTRAINT fk_event FOREIGN KEY (Event_ID) REFERENCES Events(Event_ID) ON DELETE CASCADE)")
                        mydb.commit()
                    except mysql.connector.Error as err:
                        print("Error:", err)

                # Get participant details from entry fields
                participant_name = participant_name_entry.get()
                college = college_entry.get()
                event_id = event_id_entry.get()
                phone_number = phone_number_entry.get()
                email_id = email_id_entry.get()

                # Insert participant details into Participants table
                try:
                    insert_query = "INSERT INTO Participants (Participant_Name, College, Event_ID, Phone_Number, Email_ID) VALUES (%s, %s, %s, %s, %s)"
                    participant_data = (participant_name, college, event_id, phone_number, email_id)
                    mycursor.execute(insert_query, participant_data)
                    mydb.commit()  # Commit the transaction
                    messagebox.showinfo("Success", "Participant added successfully!")
                    add_participant_window.destroy()  # Close the window after adding participant
                except mysql.connector.Error as err:
                    print("Error:", err)

            add_participant_window = Toplevel()
            add_participant_window.title("Add Participant")
            add_participant_window.geometry("1750x1250")

            # Participant Name input
            participant_name_label = Label(add_participant_window, text="Participant Name:", font=("ARIAL", 20))
            participant_name_label.grid(row=0, column=0)
            participant_name_label.place(relx=0.4, rely=0.15, anchor=CENTER)
            participant_name_label.config(bg="#99BC85")
            participant_name_entry = Entry(add_participant_window)
            participant_name_entry.grid(row=0, column=1)
            participant_name_entry.place(relx=0.525, rely=0.15, anchor=CENTER)

            # College input
            college_label = Label(add_participant_window, text="College:", font=("ARIAL", 20))
            college_label.grid(row=1, column=0)
            college_label.place(relx=0.4, rely=0.3, anchor=CENTER)
            college_label.config(bg="#99BC85")
            college_entry = Entry(add_participant_window)
            college_entry.grid(row=1, column=1)
            college_entry.place(relx=0.525, rely=0.3, anchor=CENTER)

            # Event ID input
            event_id_label = Label(add_participant_window, text="Event ID:", font=("ARIAL", 20))
            event_id_label.grid(row=2, column=0)
            event_id_label.place(relx=0.4, rely=0.45, anchor=CENTER)
            event_id_label.config(bg="#99BC85")
            event_id_entry = Entry(add_participant_window)
            event_id_entry.grid(row=2, column=1)
            event_id_entry.place(relx=0.525, rely=0.45, anchor=CENTER)

            # Phone Number input
            phone_number_label = Label(add_participant_window, text="Phone Number:", font=("ARIAL", 20))
            phone_number_label.grid(row=3, column=0)
            phone_number_label.place(relx=0.4, rely=0.6, anchor=CENTER)
            phone_number_label.config(bg="#99BC85")
            phone_number_entry = Entry(add_participant_window)
            phone_number_entry.grid(row=3, column=1)
            phone_number_entry.place(relx=0.525, rely=0.6, anchor=CENTER)

            # Email ID input
            email_id_label = Label(add_participant_window, text="Email ID:", font=("ARIAL", 20))
            email_id_label.grid(row=4, column=0)
            email_id_label.place(relx=0.4, rely=0.75, anchor=CENTER)
            email_id_label.config(bg="#99BC85")
            email_id_entry = Entry(add_participant_window)
            email_id_entry.grid(row=4, column=1)
            email_id_entry.place(relx=0.525, rely=0.75, anchor=CENTER)

            # Submit button
            submit_button = Button(add_participant_window, text="Submit", command=add_participant_data, height=3, width=12)
            submit_button.grid(row=5, columnspan=2)
            submit_button.place(relx=0.5, rely=0.8)

            add_participant_window.config(bg="#99BC85")

        def delete_participant():
            def delete_participant_data():
                participant_id = participant_id_entry.get()

                # Check if participant ID exists
                try:
                    mycursor.execute("SELECT * FROM Participants WHERE Participant_ID = %s", (participant_id,))
                    if not mycursor.fetchone():
                        messagebox.showerror("Error", "Participant ID does not exist!")
                        return
                except mysql.connector.Error as err:
                    print("Error:", err)

                # Confirm deletion
                confirm = messagebox.askyesno("Confirm Deletion", f"Do you want to delete participant with ID {participant_id}?")
                if confirm:
                    # Delete participant
                    try:
                        mycursor.execute("DELETE FROM Participants WHERE Participant_ID = %s", (participant_id,))
                        mydb.commit()
                        messagebox.showinfo("Success", f"Participant with ID {participant_id} deleted successfully!")
                        delete_participant_window.destroy()  # Close the window after deletion
                    except mysql.connector.Error as err:
                        print("Error:", err)

            delete_participant_window = Toplevel()
            delete_participant_window.title("Delete Participant")
            delete_participant_window.geometry("1750x1250")

            # Participant ID input
            participant_id_label = Label(delete_participant_window, text="Enter Participant ID:", font=("ARIAL", 20))
            participant_id_label.grid(row=0, column=0)
            participant_id_label.place(relx=0.4, rely=0.4, anchor=CENTER)
            participant_id_label.config(bg="#FA7070")

            participant_id_entry = Entry(delete_participant_window)
            participant_id_entry.grid(row=0, column=1)
            participant_id_entry.place(relx=0.525, rely=0.4, anchor=CENTER)

            # Delete button
            delete_button = Button(delete_participant_window, text="Delete", command=delete_participant_data, height=3, width=12)
            delete_button.grid(row=1, columnspan=2)
            delete_button.place(relx=0.5, rely=0.5, anchor=CENTER)

            delete_participant_window.config(bg="#FA7070")

        def all_participants():
            try:
                mycursor.execute("SELECT * FROM Participants")
                participants = mycursor.fetchall()
                if participants:
                    all_participants_window = Toplevel()
                    all_participants_window.title("All Participants")
                    all_participants_window.geometry("1750x1250")

                    for i, participant in enumerate(participants):
                        label = Label(all_participants_window, text=f"{i + 1}. Participant ID: {participant[0]}, Participant Name: {participant[1]}, College: {participant[2]}, Event ID: {participant[3]}, Phone Number: {participant[4]}, Email ID: {participant[5]}",font = ("ARIAL", 10))
                        label.config(bg="#E5E483")
                        label.pack()
                        label.place(relx=0.5,rely=0.2+i*0.05,anchor=CENTER)

                    label.config(bg="#E5E483")
                else:
                    messagebox.showinfo("Info", "No participants found!")
            except mysql.connector.Error as err:
                print("Error:", err)

        def load_participant():
            def load_participant_data():
                participant_id = participant_id_entry.get()

                try:
                    mycursor.execute("SELECT * FROM Participants WHERE Participant_ID = %s", (participant_id,))
                    participant = mycursor.fetchone()
                    if participant:
                        load_participant_window = Toplevel()
                        load_participant_window.title("Participant Details")
                        load_participant_window.geometry("400x200")

                        Label(load_participant_window, text=f"Participant ID: {participant[0]}").pack()
                        Label(load_participant_window, text=f"Participant Name: {participant[1]}").pack()
                        Label(load_participant_window, text=f"College: {participant[2]}").pack()
                        Label(load_participant_window, text=f"Event ID: {participant[3]}").pack()
                        Label(load_participant_window, text=f"Phone Number: {participant[4]}").pack()
                        Label(load_participant_window, text=f"Email ID: {participant[5]}").pack()
                    else:
                        messagebox.showinfo("Info", f"No participant found for ID {participant_id}!")
                except mysql.connector.Error as err:
                    print("Error:", err)

            load_participant_window = Toplevel()
            load_participant_window.title("Load Participant")
            load_participant_window.geometry("1750x1250")

            participant_id_label = Label(load_participant_window, text="Enter Participant ID:", font=("ARIAL", 20))
            participant_id_label.grid(row=0, column=0)
            participant_id_label.place(relx=0.4, rely=0.4, anchor=CENTER)
            participant_id_label.config(bg="#E5E483")

            participant_id_entry = Entry(load_participant_window)
            participant_id_entry.grid(row=0, column=1)
            participant_id_entry.place(relx=0.525, rely=0.4, anchor=CENTER)

            load_button = Button(load_participant_window, text="Load", command=load_participant_data, height=3, width=12)
            load_button.grid(row=1, columnspan=2)
            load_button.place(relx=0.5, rely=0.5, anchor=CENTER)

            load_participant_window.config(bg="#E5E483")

        participants_window = Toplevel()
        participants_window.title("Participants")
        participants_window.geometry("1750x1250")

        # Add Participant button
        add_participant_button = Button(participants_window, text="Add Participant", command=add_participant, font=("ARIAL", 20))
        add_participant_button.pack()
        add_participant_button.place(relx=0.3, rely=0.3, anchor=CENTER)
        add_participant_button.config(bg="#776B5D")

        # Delete Participant button
        delete_participant_button = Button(participants_window, text="Delete Participant", command=delete_participant, font=("ARIAL", 20))
        delete_participant_button.pack()
        delete_participant_button.place(relx=0.3, rely=0.6, anchor=CENTER)
        delete_participant_button.config(bg="#776B5D")

        # All Participants button
        all_participants_button = Button(participants_window, text="All Participants", command=all_participants, font=("ARIAL", 20))
        all_participants_button.pack()
        all_participants_button.place(relx=0.7, rely=0.3, anchor=CENTER)
        all_participants_button.config(bg="#776B5D")

        # Load Participant button
        load_participant_button = Button(participants_window, text="Load Participant", command=load_participant, font=("ARIAL", 20))
        load_participant_button.pack()
        load_participant_button.place(relx=0.7, rely=0.6, anchor=CENTER)
        load_participant_button.config(bg="#776B5D")

        participants_window.config(bg="#B0A695")


    # Function to handle opening the Artist List window
def open_artist_list_window():
        def add_artist():
            def add_artist_data():
                try:
                    # Check if the Artists table exists
                    mycursor.execute("SELECT 1 FROM Artists LIMIT 1")
                    mycursor.fetchone() # Consume the result
                except mysql.connector.Error as err:
                    # Create the Artists table if it doesn't exist
                    try:
                        mycursor.execute("CREATE TABLE IF NOT EXISTS Artists (Artist_ID INT AUTO_INCREMENT PRIMARY KEY, Artist_Name VARCHAR(255), College VARCHAR(255), Status VARCHAR(50), Date_Of_Performance DATE, Charge DECIMAL(10, 2), Type VARCHAR(255), Person_Of_Contact VARCHAR(255), Phone_Number VARCHAR(15), Email_ID VARCHAR(255))")
                        mydb.commit()
                    except mysql.connector.Error as err:
                        print("Error:", err)

                # Get artist details from entry fields
                artist_name = artist_name_entry.get()
                college = college_entry.get()
                status = status_entry.get()
                date_of_performance = date_of_performance_entry.get()
                charge = charge_entry.get()
                artist_type = type_entry.get()
                person_of_contact = person_of_contact_entry.get()
                phone_number = phone_number_entry.get()
                email_id = email_id_entry.get()

                # Insert artist details into Artists table
                try:
                    insert_query = "INSERT INTO Artists (Artist_Name, College, Status, Date_Of_Performance, Charge, Type, Person_Of_Contact, Phone_Number, Email_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    artist_data = (artist_name, college, status, date_of_performance, charge, artist_type, person_of_contact, phone_number, email_id)
                    mycursor.execute(insert_query, artist_data)
                    mydb.commit()  # Commit the transaction
                    messagebox.showinfo("Success", "Artist added successfully!")
                    add_artist_window.destroy()  # Close the window after adding artist
                except mysql.connector.Error as err:
                    print("Error:", err)

            add_artist_window = Toplevel()
            add_artist_window.title("Add Artist")
            add_artist_window.geometry("1750x1250")

            # Artist Name input
            artist_name_label = Label(add_artist_window, text="Artist Name:", font=("ARIAL", 20))
            artist_name_label.grid(row=0, column=0)
            artist_name_label.place(relx=0.4, rely=0.09, anchor=CENTER)
            artist_name_label.config(bg="#99BC85")
            artist_name_entry = Entry(add_artist_window)
            artist_name_entry.grid(row=0, column=1)
            artist_name_entry.place(relx=0.525, rely=0.09, anchor=CENTER)

            # College input
            college_label = Label(add_artist_window, text="College:", font=("ARIAL", 20))
            college_label.grid(row=1, column=0)
            college_label.place(relx=0.4, rely=0.18, anchor=CENTER)
            college_label.config(bg="#99BC85")
            college_entry = Entry(add_artist_window)
            college_entry.grid(row=1, column=1)
            college_entry.place(relx=0.525, rely=0.18, anchor=CENTER)

            # Status input
            status_label = Label(add_artist_window, text="Status:", font=("ARIAL", 20))
            status_label.grid(row=2, column=0)
            status_label.place(relx=0.4, rely=0.27, anchor=CENTER)
            status_label.config(bg="#99BC85")
            status_entry = Entry(add_artist_window)
            status_entry.grid(row=2, column=1)
            status_entry.place(relx=0.525, rely=0.27, anchor=CENTER)

            # Date of Performance input
            date_of_performance_label = Label(add_artist_window, text="Date of Performance:", font=("ARIAL", 20))
            date_of_performance_label.grid(row=3, column=0)
            date_of_performance_label.place(relx=0.4, rely=0.36, anchor=CENTER)
            date_of_performance_label.config(bg="#99BC85")
            date_of_performance_entry = Entry(add_artist_window)
            date_of_performance_entry.grid(row=3, column=1)
            date_of_performance_entry.place(relx=0.525, rely=0.36, anchor=CENTER)

            # Charge input
            charge_label = Label(add_artist_window, text="Charge:", font=("ARIAL", 20))
            charge_label.grid(row=4, column=0)
            charge_label.place(relx=0.4, rely=0.45, anchor=CENTER)
            charge_label.config(bg="#99BC85")
            charge_entry = Entry(add_artist_window)
            charge_entry.grid(row=4, column=1)
            charge_entry.place(relx=0.525, rely=0.45, anchor=CENTER)

            # Type input
            type_label = Label(add_artist_window, text="Type:", font=("ARIAL", 20))
            type_label.grid(row=5, column=0)
            type_label.place(relx=0.4, rely=0.54, anchor=CENTER)
            type_label.config(bg="#99BC85")
            type_entry = Entry(add_artist_window)
            type_entry.grid(row=5, column=1)
            type_entry.place(relx=0.525, rely=0.54, anchor=CENTER)

            # Person of Contact input
            person_of_contact_label = Label(add_artist_window, text="Person of Contact:", font=("ARIAL", 20))
            person_of_contact_label.grid(row=6, column=0)
            person_of_contact_label.place(relx=0.4, rely=0.63, anchor=CENTER)
            person_of_contact_label.config(bg="#99BC85")
            person_of_contact_entry = Entry(add_artist_window)
            person_of_contact_entry.grid(row=6, column=1)
            person_of_contact_entry.place(relx=0.525, rely=0.63, anchor=CENTER)

            # Phone Number input
            phone_number_label = Label(add_artist_window, text="Phone Number:", font=("ARIAL", 20))
            phone_number_label.grid(row=7, column=0)
            phone_number_label.place(relx=0.4, rely=0.72, anchor=CENTER)
            phone_number_label.config(bg="#99BC85")
            phone_number_entry = Entry(add_artist_window)
            phone_number_entry.grid(row=7, column=1)
            phone_number_entry.place(relx=0.525, rely=0.72, anchor=CENTER)

            # Email ID input
            email_id_label = Label(add_artist_window, text="Email ID:", font=("ARIAL", 20))
            email_id_label.grid(row=8, column=0)
            email_id_label.place(relx=0.4,rely=0.81, anchor=CENTER)
            email_id_label.config(bg="#99BC85")
            email_id_entry = Entry(add_artist_window)
            email_id_entry.grid(row=8, column=1)
            email_id_entry.place(relx=0.525, rely=0.81, anchor=CENTER)

            # Submit button
            submit_button = Button(add_artist_window, text="Submit", command=add_artist_data, height=3, width=12)
            submit_button.grid(row=9, columnspan=2)
            submit_button.place(relx=0.5, rely=0.86, anchor=CENTER)

            add_artist_window.config(bg="#99BC85")

        def delete_artist():
            def delete_artist_data():
                artist_id = artist_id_entry.get()

                # Check if artist ID exists
                try:
                    mycursor.execute("SELECT * FROM Artists WHERE Artist_ID = %s", (artist_id,))
                    if not mycursor.fetchone():
                        messagebox.showerror("Error", "Artist ID does not exist!")
                        return
                except mysql.connector.Error as err:
                    print("Error:", err)

                # Confirm deletion
                confirm = messagebox.askyesno("Confirm Deletion", f"Do you want to delete artist with ID {artist_id}?")
                if confirm:
                    # Delete artist
                    try:
                        mycursor.execute("DELETE FROM Artists WHERE Artist_ID = %s", (artist_id,))
                        mydb.commit()
                        messagebox.showinfo("Success", f"Artist with ID {artist_id} deleted successfully!")
                        delete_artist_window.destroy()  # Close the window after deletion
                    except mysql.connector.Error as err:
                        print("Error:", err)

            delete_artist_window = Toplevel()
            delete_artist_window.title("Delete Artist")
            delete_artist_window.geometry("1750x1250")

            # Artist ID input
            artist_id_label = Label(delete_artist_window, text="Enter Artist ID:")
            artist_id_label.grid(row=0, column=0)
            artist_id_label.place(relx=0.4, rely=0.4, anchor=CENTER)
            artist_id_label.config(bg="#FA7070")

            artist_id_entry = Entry(delete_artist_window)
            artist_id_entry.grid(row=0, column=1)
            artist_id_entry.place(relx=0.525, rely=0.4, anchor=CENTER)

            # Delete button
            delete_button = Button(delete_artist_window, text="Delete", command=delete_artist_data, height=3, width=12)
            delete_button.grid(row=1, columnspan=2)
            delete_button.place(relx=0.5, rely=0.5, anchor=CENTER)

            delete_artist_window.config(bg="#FA7070")

        def all_artists():
            try:
                mycursor.execute("SELECT * FROM Artists")
                artists = mycursor.fetchall()
                if artists:
                    all_artists_window = Toplevel()
                    all_artists_window.title("All Artists")
                    all_artists_window.geometry("1750x1250")

                    for i, artist in enumerate(artists):
                        label = Label(all_artists_window, text=f"{i + 1}. Artist ID: {artist[0]}, Artist Name: {artist[1]}, College: {artist[2]}, Status: {artist[3]}, Date of Performance: {artist[4]}, Charge: {artist[5]}, Type: {artist[6]}, Person of Contact: {artist[7]}, Phone Number: {artist[8]}, Email ID: {artist[9]}",font=("ARIAL",10))
                        label.config(bg="#E5E483")
                        label.pack()
                        label.place(relx=0.5,rely=0.2+i*0.05,anchor=CENTER)
                    all_artists_window.config(bg="#E5E483")
                else:
                    messagebox.showinfo("Info", "No artists found!")
            except mysql.connector.Error as err:
                print("Error:", err)

        def load_artist():
            def load_artist_data():
                artist_id = artist_id_entry.get()

                try:
                    mycursor.execute("SELECT * FROM Artists WHERE Artist_ID = %s", (artist_id,))
                    artist = mycursor.fetchone()
                    if artist:
                        load_artist_window = Toplevel()
                        load_artist_window.title("Artist Details")
                        load_artist_window.geometry("1750x1250")

                        Label(load_artist_window, text=f"Artist ID: {artist[0]}").pack()
                        Label(load_artist_window, text=f"Artist Name: {artist[1]}").pack()
                        Label(load_artist_window, text=f"College: {artist[2]}").pack()
                        Label(load_artist_window, text=f"Status: {artist[3]}").pack()
                        Label(load_artist_window, text=f"Date of Performance: {artist[4]}").pack()
                        Label(load_artist_window, text=f"Charge: {artist[5]}").pack()
                        Label(load_artist_window, text=f"Type: {artist[6]}").pack()
                        Label(load_artist_window, text=f"Person of Contact: {artist[7]}").pack()
                        Label(load_artist_window, text=f"Phone Number: {artist[8]}").pack()
                        Label(load_artist_window, text=f"Email ID: {artist[9]}").pack()
                    else:
                        messagebox.showinfo("Info", f"No artist found for ID {artist_id}!")
                except mysql.connector.Error as err:
                    print("Error:", err)

            load_artist_window = Toplevel()
            load_artist_window.title("Load Artist")
            load_artist_window.geometry("1750x1250")

            artist_id_label = Label(load_artist_window, text="Enter Artist ID:", font=("ARIAL", 20))
            artist_id_label.grid(row=0, column=0)
            artist_id_label.place(relx=0.4, rely=0.4, anchor=CENTER)
            artist_id_label.config(bg="#E5E483")

            artist_id_entry = Entry(load_artist_window)
            artist_id_entry.grid(row=0, column=1)
            artist_id_entry.place(relx=0.525, rely=0.4, anchor=CENTER)

            load_button = Button(load_artist_window, text="Load", command=load_artist_data, height=3, width=12)
            load_button.grid(row=1, columnspan=2)
            load_button.place(relx=0.5, rely=0.5, anchor=CENTER)

            load_artist_window.config(bg="#E5E483")


        artists_window = Toplevel()
        artists_window.title("Artist Lists")
        artists_window.geometry("1750x1250")

        # Add Artist button
        add_artist_button = Button(artists_window, text="Add Artist", command=add_artist, font=("ARIAL", 20))
        add_artist_button.pack()
        add_artist_button.place(relx=0.3, rely=0.3, anchor=CENTER)
        add_artist_button.config(bg="#776B5D")

        # Delete Artist button
        delete_artist_button = Button(artists_window, text="Delete Artist", command=delete_artist, font=("ARIAL", 20))
        delete_artist_button.pack()
        delete_artist_button.place(relx=0.3, rely=0.6, anchor=CENTER)
        delete_artist_button.config(bg="#776B5D")

        # All Artists button
        all_artists_button = Button(artists_window, text="All Artists", command=all_artists, font=("ARIAL", 20))
        all_artists_button.pack()
        all_artists_button.place(relx=0.7, rely=0.3, anchor=CENTER)
        all_artists_button.config(bg="#776B5D")

        # Load Artist button
        load_artist_button = Button(artists_window, text="Load Artist", command=load_artist, font=("ARIAL", 20))
        load_artist_button.pack()
        load_artist_button.place(relx=0.7, rely=0.6, anchor=CENTER)
        load_artist_button.config(bg="#776B5D")

        artists_window.config(bg="#B0A695")


    # Function to handle opening the Budget window
def open_budget_window():
        def add_bill():
            def add_bill_data():
                try:
                    # Check if the Bills table exists
                    mycursor.execute("SELECT 1 FROM Bills LIMIT 1")
                    mycursor.fetchone() # Consume the result
                except mysql.connector.Error as err:
                    # Create the Bills table if it doesn't exist
                    try:
                        mycursor.execute("CREATE TABLE IF NOT EXISTS Bills (Bill_No INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Member_ID INT, Amount DECIMAL(10, 2), Purpose VARCHAR(255), StatusOfBill VARCHAR(50))")
                        mydb.commit()
                    except mysql.connector.Error as err:
                        print("Error:", err)

                # Get bill details from entry fields
                name = name_entry.get()
                member_id = member_id_entry.get()
                amount = amount_entry.get()
                purpose = purpose_entry.get()
                status = status_entry.get()

                # Insert bill details into Bills table
                try:
                    insert_query = "INSERT INTO Bills (Name, Member_ID, Amount, Purpose, StatusOfBill) VALUES (%s, %s, %s, %s, %s)"
                    bill_data = (name, member_id, amount, purpose, status)
                    mycursor.execute(insert_query, bill_data)
                    mydb.commit()  # Commit the transaction
                    messagebox.showinfo("Success", "Bill added successfully!")
                    add_bill_window.destroy()  # Close the window after adding bill
                except mysql.connector.Error as err:
                    print("Error:", err)

            add_bill_window = Toplevel()
            add_bill_window.title("Add Bill")
            add_bill_window.geometry("1750x1250")

            # Name input
            name_label = Label(add_bill_window, text="Name:", font=("ARIAL", 20))
            name_label.grid(row=0, column=0)
            name_label.place(relx=0.4, rely=0.15, anchor=CENTER)
            name_label.config(bg="#F3D7CA")
            name_entry = Entry(add_bill_window)
            name_entry.grid(row=0, column=1)
            name_entry.place(relx=0.525, rely=0.15, anchor=CENTER)

            # Member ID input
            member_id_label = Label(add_bill_window, text="Member ID:", font=("ARIAL", 20))
            member_id_label.grid(row=1, column=0)
            member_id_label.place(relx=0.4, rely=0.30, anchor=CENTER)
            member_id_label.config(bg="#F3D7CA")
            member_id_entry = Entry(add_bill_window)
            member_id_entry.grid(row=1, column=1)
            member_id_entry.place(relx=0.525, rely=0.30, anchor=CENTER)

            # Amount input
            amount_label = Label(add_bill_window, text="Amount:", font=("ARIAL", 20))
            amount_label.grid(row=2, column=0)
            amount_label.place(relx=0.4, rely=0.45, anchor=CENTER)
            amount_label.config(bg="#F3D7CA")
            amount_entry = Entry(add_bill_window)
            amount_entry.grid(row=2, column=1)
            amount_entry.place(relx=0.525, rely=0.45, anchor=CENTER)

            # Purpose input
            purpose_label = Label(add_bill_window, text="Purpose:", font=("ARIAL", 20))
            purpose_label.grid(row=3, column=0)
            purpose_label.place(relx=0.4, rely=0.6, anchor=CENTER)
            purpose_label.config(bg="#F3D7CA")
            purpose_entry = Entry(add_bill_window)
            purpose_entry.grid(row=3, column=1)
            purpose_entry.place(relx=0.525, rely=0.6, anchor=CENTER)

            # Status input
            status_label = Label(add_bill_window, text="Status:", font=("ARIAL", 20))
            status_label.grid(row=4, column=0)
            status_label.place(relx=0.4, rely=0.75, anchor=CENTER)
            status_label.config(bg="#F3D7CA")
            status_entry = Entry(add_bill_window)
            status_entry.grid(row=4, column=1)
            status_entry.place(relx=0.525, rely=0.75, anchor=CENTER)

            # Submit button
            submit_button = Button(add_bill_window, text="Submit", command=add_bill_data, height=3, width=12)
            submit_button.grid(row=5, columnspan=2)
            submit_button.place(relx=0.5, rely=0.8)

            add_bill_window.config(bg="#F3D7CA")

        def delete_bill():
            def delete_bill_data():
                bill_no = bill_no_entry.get()

                # Check if bill number exists
                try:
                    mycursor.execute("SELECT * FROM Bills WHERE Bill_No = %s", (bill_no,))
                    if not mycursor.fetchone():
                        messagebox.showerror("Error", "Bill number does not exist!")
                        return
                except mysql.connector.Error as err:
                    print("Error:", err)

                # Confirm deletion
                confirm = messagebox.askyesno("Confirm Deletion", f"Do you want to delete bill with number {bill_no}?")
                if confirm:
                    # Delete bill
                    try:
                        mycursor.execute("DELETE FROM Bills WHERE Bill_No = %s", (bill_no,))
                        mydb.commit()
                        messagebox.showinfo("Success", f"Bill with number {bill_no} deleted successfully!")
                        delete_bill_window.destroy()  # Close the window after deletion
                    except mysql.connector.Error as err:
                        print("Error:", err)

            delete_bill_window = Toplevel()
            delete_bill_window.title("Delete Bill")
            delete_bill_window.geometry("1750x1250")

            # Bill number input
            bill_no_label = Label(delete_bill_window, text="Enter Bill Number:", font=("ARIAL", 20))
            bill_no_label.grid(row=0, column=0)
            bill_no_label.place(relx=0.4, rely=0.4, anchor=CENTER)
            bill_no_label.config(bg="#FA7070")

            bill_no_entry = Entry(delete_bill_window)
            bill_no_entry.grid(row=0, column=1)
            bill_no_entry.place(relx=0.525, rely=0.4, anchor=CENTER)

            # Delete button
            delete_button = Button(delete_bill_window, text="Delete", command=delete_bill_data, height=3, width=12)
            delete_button.grid(row=1, columnspan=2)
            delete_button.place(relx=0.5, rely=0.5, anchor=CENTER)

            delete_bill_window.config(bg="#FA7070")

        def all_bills():
            try:
                mycursor.execute("SELECT * FROM Bills")
                bills = mycursor.fetchall()
                if bills:
                    all_bills_window = Toplevel()
                    all_bills_window.title("All Bills")
                    all_bills_window.geometry("1750x1250")

                    for i, bill in enumerate(bills):
                        label = Label(all_bills_window, text=f"{i + 1}. Bill Number: {bill[0]}, Name: {bill[1]}, Member ID: {bill[2]}, Amount: {bill[3]}, Purpose: {bill[4]}, Status: {bill[5]}", font=("ARIAL",10))
                        label.config(bg="#E5E483")
                        label.pack()
                        label.place(relx=0.5, rely=0.2+i*0.05, anchor=CENTER)
                    all_bills_window.config(bg="#E5E483")
                else:
                    messagebox.showinfo("Info", "No bills found!")
            except mysql.connector.Error as err:
                print("Error:", err)

        def load_bill():
            def load_bill_data():
                bill_no = bill_no_entry.get()

                try:
                    mycursor.execute("SELECT * FROM Bills WHERE Bill_No = %s", (bill_no,))
                    bill = mycursor.fetchone()
                    if bill:
                        load_bill_window = Toplevel()
                        load_bill_window.title("Bill Details")
                        load_bill_window.geometry("400x200")

                        Label(load_bill_window, text=f"Bill Number: {bill[0]}").pack()
                        Label(load_bill_window, text=f"Name: {bill[1]}").pack()
                        Label(load_bill_window, text=f"Member ID: {bill[2]}").pack()
                        Label(load_bill_window, text=f"Amount: {bill[3]}").pack()
                        Label(load_bill_window, text=f"Purpose: {bill[4]}").pack()
                        Label(load_bill_window, text=f"Status: {bill[5]}").pack()
                    else:
                        messagebox.showinfo("Info", f"No bill found for number {bill_no}!")
                except mysql.connector.Error as err:
                    print("Error:", err)

            load_bill_window = Toplevel()
            load_bill_window.title("Load Bill")
            load_bill_window.geometry("1750x1250")

            bill_no_label = Label(load_bill_window, text="Enter Bill Number:", font=("ARIAL", 20))
            bill_no_label.grid(row=0, column=0)
            bill_no_label.place(relx=0.4, rely=0.4, anchor=CENTER)
            bill_no_label.config(bg="#E5E483")

            bill_no_entry = Entry(load_bill_window)
            bill_no_entry.grid(row=0, column=1)
            bill_no_entry.place(relx=0.525, rely=0.4, anchor=CENTER)

            load_button = Button(load_bill_window, text="Load", command=load_bill_data, height=3, width=12)
            load_button.grid(row=1, columnspan=2)
            load_button.place(relx=0.5, rely=0.5, anchor=CENTER)

            load_bill_window.config(bg="#E5E483")

        budget_window = Toplevel()
        budget_window.title("Budget")
        budget_window.geometry("1750x1250")

        # Add Bill button
        add_bill_button = Button(budget_window, text="Add Bill", command=add_bill, font=("ARIAL", 20))
        add_bill_button.pack()
        add_bill_button.place(relx=0.3, rely=0.3, anchor=CENTER)
        add_bill_button.config(bg="#776B5D")

        # Delete Bill button
        delete_bill_button = Button(budget_window, text="Delete Bill", command=delete_bill, font=("ARIAL", 20))
        delete_bill_button.pack()
        delete_bill_button.place(relx=0.3, rely=0.6, anchor=CENTER)
        delete_bill_button.config(bg="#776B5D")

        # All Bills button
        all_bills_button = Button(budget_window, text="All Bills", command=all_bills, font=("ARIAL", 20))
        all_bills_button.pack()
        all_bills_button.place(relx=0.7, rely=0.3, anchor=CENTER)
        all_bills_button.config(bg="#776B5D")

        # Load Bill button
        load_bill_button = Button(budget_window, text="Load Bill", command=load_bill, font=("ARIAL", 20))
        load_bill_button.pack()
        load_bill_button.place(relx=0.7, rely=0.6, anchor=CENTER)
        load_bill_button.config(bg="#776B5D")


        budget_window.config(bg="#B0A695")

# Function to handle loading a fest
def load_fest():
    def load_fest_data():
        fest_name = fest_name_entry.get()
        try:
            mycursor.execute("SELECT * FROM Fest WHERE Name = %s", (fest_name,))
            fest = mycursor.fetchone()
            if fest:
                messagebox.showinfo("Success", f"Fest {fest_name} loaded successfully!")
                open_fest_management_window()
            else:
                messagebox.showerror("Error", f"Fest {fest_name} not found!")
        except mysql.connector.Error as err:
            print("Error:", err)


    def open_fest_management_window():
            # Open Fest Management window
            fest_management_window = Toplevel()
            fest_management_window.title("Fest Management")
            fest_management_window.geometry("1750x1250")

            # Buttons for different functionalities
            sponsors_button = Button(fest_management_window, text="Sponsors", command=open_sponsors_window, height=7, width=20)
            sponsors_button.grid(row=0, column=0)
            sponsors_button.place(relx=0.3, rely=0.2, anchor = CENTER)
            sponsors_button.config(bg="#A79277")

            events_button = Button(fest_management_window, text="Events", command=open_events_window, height=7, width=20)
            events_button.grid(row=0, column=1)
            events_button.place(relx=0.3, rely=0.4, anchor=CENTER)
            events_button.config(bg="#A79277")

            teams_button = Button(fest_management_window, text="Teams", command=teams_window, height=7, width=20)
            teams_button.grid(row=0, column=2)
            teams_button.place(relx=0.3, rely=0.6, anchor=CENTER)
            teams_button.config(bg="#A79277")

            participants_button = Button(fest_management_window, text="Participants", command=open_participants_window, height=7, width=20)
            participants_button.grid(row=1, column=0)
            participants_button.place(relx=0.7, rely=0.2, anchor=CENTER)
            participants_button.config(bg="#A79277")

            artist_list_button = Button(fest_management_window, text="Artist List", command=open_artist_list_window, height=7, width=20)
            artist_list_button.grid(row=1, column=1)
            artist_list_button.place(relx=0.7, rely=0.4, anchor=CENTER)
            artist_list_button.config(bg="#A79277")

            budget_button = Button(fest_management_window, text="Budget", command=open_budget_window, height=7, width=20)
            budget_button.grid(row=1, column=2)
            budget_button.place(relx=0.7, rely=0.6, anchor=CENTER)
            budget_button.config(bg="#A79277")

            fest_management_window.config(bg="#EAD8C0")

    load_window = Toplevel()
    load_window.title("Load Fest")
    load_window.geometry("1750x1250")

    fest_name_label = Label(load_window, text="Enter Fest Name:", font=("ARIAL", 15))
    fest_name_label.grid(row=0, column=0)
    fest_name_label.place(relx=0.4, rely=0.4, anchor=CENTER)

    fest_name_entry = Entry(load_window)
    fest_name_entry.grid(row=0, column=1)
    fest_name_entry.place(relx=0.5, rely=0.4, anchor=CENTER)

    load_button = Button(load_window, text="Load", command=load_fest_data, height=3, width=12)
    load_button.grid(row=1, columnspan=2)
    load_button.place(relx=0.5, rely = 0.5, anchor=CENTER)

    load_window.config(bg="#5BBCFF")
    fest_name_label.config(bg="#5BBCFF")

# Function to handle deleting a fest
def delete_fest():
    def delete_fest_data():
        fest_name = fest_name_entry.get()
        try:
            mycursor.execute("SELECT * FROM Fest WHERE Name = %s", (fest_name,))
            fest = mycursor.fetchone()
            if fest:
                confirm = messagebox.askyesno("Confirm Deletion", f"Do you want to delete fest {fest_name}?")
                if confirm:
                    mycursor.execute("DELETE FROM Fest WHERE Name = %s", (fest_name,))
                    mydb.commit()
                    messagebox.showinfo("Success", f"Fest {fest_name} deleted successfully!")
            else:
                messagebox.showerror("Error", f"Fest {fest_name} not found!")
        except mysql.connector.Error as err:
            print("Error:", err)

    delete_window = Toplevel()
    delete_window.title("Delete Fest")
    delete_window.geometry("1750x1250")

    fest_name_label = Label(delete_window, text="Enter Fest Name:", font=("ARIAL", 15))
    fest_name_label.grid(row=0, column=0)
    fest_name_label.place(relx=0.4, rely=0.4, anchor=CENTER)


    fest_name_entry = Entry(delete_window)
    fest_name_entry.grid(row=0, column=1)
    fest_name_entry.place(relx=0.525, rely=0.4, anchor=CENTER)

    delete_button = Button(delete_window, text="Delete", command=delete_fest_data, height=3, width=12)
    delete_button.grid(row=1, columnspan=2)

    delete_button.place(relx=0.525, rely = 0.5, anchor=CENTER)

    delete_window.config(bg="#FA7070")
    fest_name_label.config(bg="#FA7070")

# Function to handle displaying all fests
def all_fests():
    try:
        mycursor.execute("SELECT Name FROM Fest")
        fests = mycursor.fetchall()
        if fests:
            all_fests_window = Toplevel()
            all_fests_window.title("All Fests")
            all_fests_window.geometry("1750x1250")

            for i, fest in enumerate(fests):
                label = Label(all_fests_window, text=f"{i + 1}. {fest[0]}", font=("ARIAL", 12))
                label.config(bg="#5BBCFF")
                label.pack()
                label.place(relx=0.5, rely=0.2+i*0.05, anchor=CENTER)

        else:
            messagebox.showinfo("Info", "No fests found!")
    except mysql.connector.Error as err:
        print("Error:", err)

    all_fests_window.config(bg="#5BBCFF")

# Function to handle Submit button in New Fest window
def new_fest_submit():
    # Function to handle opening the Fest Management window and saving fest details
    def open_fest_management_window():
        fest_name = name_entry.get()
        fest_date = date_entry.get()
        fest_board = board_entry.get()

        try:
            # Insert fest details into Fest table
            insert_query = "INSERT INTO Fest (Name, Date, Board) VALUES (%s, %s, %s)"
            fest_data = (fest_name, fest_date, fest_board)
            mycursor.execute(insert_query, fest_data)
            mydb.commit()  # Commit the transaction
            messagebox.showinfo("Success", f"Fest {fest_name} details saved successfully!")

            # Open Fest Management window
            fest_management_window = Toplevel()
            fest_management_window.title("Fest Management")
            fest_management_window.geometry("1750x1250")

            # Buttons for different functionalities
            sponsors_button = Button(fest_management_window, text="Sponsors", command=open_sponsors_window, height=7, width=20)
            sponsors_button.grid(row=0, column=0)
            sponsors_button.place(relx=0.3, rely=0.2, anchor = CENTER)
            sponsors_button.config(bg="#A79277")

            events_button = Button(fest_management_window, text="Events", command=open_events_window, height=7, width=20)
            events_button.grid(row=0, column=1)
            events_button.place(relx=0.3, rely=0.4, anchor=CENTER)
            events_button.config(bg="#A79277")

            teams_button = Button(fest_management_window, text="Teams", command=teams_window, height=7, width=20)
            teams_button.grid(row=0, column=2)
            teams_button.place(relx=0.3, rely=0.6, anchor=CENTER)
            teams_button.config(bg="#A79277")

            participants_button = Button(fest_management_window, text="Participants", command=open_participants_window, height=7, width=20)
            participants_button.grid(row=1, column=0)
            participants_button.place(relx=0.7, rely=0.2, anchor=CENTER)
            participants_button.config(bg="#A79277")

            artist_list_button = Button(fest_management_window, text="Artist List", command=open_artist_list_window, height=7, width=20)
            artist_list_button.grid(row=1, column=1)
            artist_list_button.place(relx=0.7, rely=0.4, anchor=CENTER)
            artist_list_button.config(bg="#A79277")

            budget_button = Button(fest_management_window, text="Budget", command=open_budget_window, height=7, width=20)
            budget_button.grid(row=1, column=2)
            budget_button.place(relx=0.7, rely=0.6, anchor=CENTER)
            budget_button.config(bg="#A79277")

            fest_management_window.config(bg="#EAD8C0")

        except mysql.connector.Error as err:
            print("Error:", err)

    # Create a new window for adding a new fest
    new_fest_window = Toplevel()
    new_fest_window.title("New Fest")
    new_fest_window.geometry("1750x1250")

    # Fest name input
    name_label = Label(new_fest_window, text="Name:", font=("ARIAL", 20))
    name_label.grid(row=0, column=0)
    name_entry = Entry(new_fest_window)
    name_entry.grid(row=0, column=1)
    name_label.place(relx=0.4, rely=0.3, anchor=CENTER)
    name_entry.place(relx=0.5, rely=0.3, anchor=CENTER)
    name_label.config(bg="#BED7DC")

    # Fest date input
    date_label = Label(new_fest_window, text="Date:", font=("ARIAL", 20))
    date_label.grid(row=1, column=0)
    date_entry = Entry(new_fest_window)
    date_entry.grid(row=1, column=1)
    date_label.place(relx=0.4, rely=0.4, anchor=CENTER)
    date_entry.place(relx=0.5, rely=0.4, anchor=CENTER)
    date_label.config(bg="#BED7DC")

    # Fest board input
    board_label = Label(new_fest_window, text="Board:", font=("ARIAL", 20))
    board_label.grid(row=2, column=0)
    board_entry = Entry(new_fest_window)
    board_entry.grid(row=2, column=1)
    board_label.place(relx=0.4, rely=0.5, anchor=CENTER)
    board_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
    board_label.config(bg="#BED7DC")

    # Submit button
    submit_button = Button(new_fest_window, text="Submit", command=open_fest_management_window, height=3, width=10)
    submit_button.grid(row=3, columnspan=2)
    submit_button.place(relx=0.5, rely=0.6, anchor=CENTER)
    new_fest_window.config(bg="#BED7DC")

# Function to handle main window
def main_window():
    root = Tk()
    root.title("Fest Management System")
    root.geometry("1750x1250")

    # Create button for New Fest
    new_fest_button = Button(root, text="New Fest", command=new_fest_submit, height=7, width=20)
    new_fest_button.pack()
    new_fest_button.place(relx=0.3, rely=0.25, anchor=CENTER)
    new_fest_button.config(bg="#FFCF96")

    # Load Fest button
    load_fest_button = Button(root, text="Load Fest", command=load_fest, height=7, width=20)
    load_fest_button.pack()
    load_fest_button.place(relx=0.3, rely=0.6, anchor=CENTER)
    load_fest_button.config(bg="#FFCF96")

    # Delete Fest button
    delete_fest_button = Button(root, text="Delete Fest", command=delete_fest, height=7, width=20)
    delete_fest_button.pack()
    delete_fest_button.place(relx=0.7, rely=0.25, anchor=CENTER)
    delete_fest_button.config(bg="#FFCF96")

    # All Fests button
    all_fests_button = Button(root, text="All Fests", command=all_fests, height=7, width=20)
    all_fests_button.pack()
    all_fests_button.place(relx=0.7, rely=0.6, anchor=CENTER)
    all_fests_button.config(bg="#FFCF96")

    root.config(bg="#F6FDC3")



    root.mainloop()

# Main code
if __name__ == "__main__":
    get_mysql_credentials()
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    create_fest_table()
    main_window()
