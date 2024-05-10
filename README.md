**Fest Management System**

---

### Overview

The Fest Management System is a Python application designed to streamline the organization and management of college fests. It provides functionality for assigning details of events, sponsors, teams, participants, and more, all within an intuitive graphical user interface (GUI) built using Tkinter. The system is backed by a MySQL database for efficient data storage and retrieval.

### Features

- **Event Management**: Add, edit, and delete events along with their details such as name, date, time, venue, and description.
- **Sponsor Management**: Manage sponsors by adding, editing, and removing sponsor information including name, contact details, and sponsorship level.
- **Team Management**: Organize teams participating in events by adding, editing, and deleting team information.
- **Participant Management**: Track participants by adding, editing, and removing participant details including name, college, and contact information.
- **User-friendly Interface**: Intuitive GUI designed using Tkinter for ease of use and navigation.
- **Data Persistence**: Data is stored in a MySQL database for reliable storage and easy retrieval.
- **Customizable**: Easily extend and customize the system to meet specific requirements.

### Requirements

- Python 3.x
- Tkinter (usually included with Python)
- MySQL database
- MySQL Connector/Python library (install using `pip install mysql-connector-python`)
- MySQL server (local or remote)

### Installation and Setup

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/your-username/fest-management-system.git
   ```

2. Install the MySQL Connector/Python library:

   ```
   pip install mysql-connector-python
   ```

3. Import the provided MySQL database dump (`fest_management.sql`) into your MySQL server.


4. Run the application:

   ```
   python fest_management.py
   ```

### Usage

- Launch the application (`fest_management.py`) to open the Fest Management System GUI.
- Use the navigation buttons to access different features such as event management, sponsor management, team management, and participant management.
- Add, edit, and delete records as needed to organize and manage your college fest effectively.


### Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

### Credits

Developed by [Mukund Agrawal](https://github.com/Mukund-Agrawal0906).

---

Feel free to customize the README according to your project's specifics and add any additional sections or information as needed.
