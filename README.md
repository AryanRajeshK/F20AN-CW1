# F20AN-CW1  

### SQL Injection Project – Ethical Hacking Coursework  

This project demonstrates SQL injection vulnerabilities as part of an ethical hacking course.  

## Contributors  
- Aryan R  
- Patson D  
- Abdirahim W  

## Setup & Execution  

1. **Install Dependencies**  
   Ensure you have a Python environment set up, then install the required dependencies:  
   ```bash
   pip install -r requirements.txt 
   ```

2. **Set Up the Database**  
Navigate to the 'flask app' directory and run:
    ```bash
   python setupDatabase.py
   ```
   The following output should be generated during its first execution:
   ```bash
    Admin user and test user created.

    admin creds: 
            u:admin
            p:dubai2020!
    test user creds: 
            u:patson
            p:patson123

    Database setup complete.
   ```
   This initializes the SQL database.

3. **Run the Application**  
Start the Flask app: 
    ```bash
    python myApp.py
    ```
    Then, open your browser and go to:  
    http://127.0.0.1:5000/

---
This project is intended for the f20an coursework.