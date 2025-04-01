from myApp import db, app, User

def setupDatabase():
    with app.app_context():
        db.create_all()
        
        adminUser = User.query.filter_by(username="admin").first()
        if not adminUser:
            admin = User(username="admin", password="dubai2020!")
            testUser = User(username="patson", password="patson123")
            db.session.add(admin)
            db.session.add(testUser)
            db.session.commit()
            print("Admin user and test user created.")
            print(f"\nadmin creds: \n\tu:{admin.username}\n\tp:{admin.password}")
            print(f"test user creds: \n\tu:{testUser.username}\n\tp:{testUser.password}")
        else:
            print("Admin user already exists.")

if __name__ == "__main__":
    setupDatabase()
    print("\nDatabase setup complete.")
