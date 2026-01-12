# =========================
# STUDENT MANAGEMENT SYSTEM WITH ENHANCED AI FEATURES
# =========================

from PIL import Image
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import numpy as np

# =========================
# LOGIN SYSTEM
# =========================
users = {"admin":"admin123", "user1":"pass123"}
attempts = 0
MAX_ATTEMPTS = 3

while attempts < MAX_ATTEMPTS:
    user_id = input("Enter User ID: ").strip()
    password = input("Enter Password: ").strip()
    if user_id in users and users[user_id]==password:
        print(f"\nLogin successful! Welcome {user_id} ✅\n")
        break
    else:
        attempts += 1
        print(f"Invalid ID or Password! Attempts left: {MAX_ATTEMPTS - attempts}\n")
else:
    print("Maximum login attempts reached. Exiting program ❌")
    exit()

# =========================
# DATA STORAGE
# =========================
students = []

# =========================
# STUDENT CRUD
# =========================
def add_student(students, student):
    for s in students:
        if s['roll']==student['roll']:
            return False
    students.append(student)
    return True

def update_student(students, roll, updates):
    for s in students:
        if s['roll']==roll:
            s.update(updates)
            return True
    return False

def delete_student(students, roll):
    for s in students:
        if s['roll']==roll:
            students.remove(s)
            return True
    return False

def display_students(students):
    if not students:
        print("No records available")
        return
    for s in students:
        print(s)
        show_photo(s.get('photo',''))

# =========================
# PHOTO DISPLAY
# =========================
def show_photo(photo_path):
    try:
        img = Image.open(photo_path)
        img.show()
    except:
        print("Photo not found or invalid path!")

# =========================
# AI FEATURES
# =========================
def grade_from_marks(m):
    if m>=85:
        return 'A'
    elif m>=70:
        return 'B'
    elif m>=50:
        return 'C'
    else:
        return 'D'

def predict_grade():
    if not students:
        print("No data for prediction ❌")
        return
    X = np.array([[s['marks']] for s in students])
    y = np.array([grade_from_marks(s['marks']) for s in students])
    clf = DecisionTreeClassifier()
    clf.fit(X,y)
    mark = float(input("Enter marks to predict grade: "))
    pred = clf.predict([[mark]])
    print(f"Predicted grade: {pred[0]} ✅")
    if mark < 50:
        print("⚠ Warning: Student at risk of failing!")

def cluster_students():
    if not students:
        print("No data for clustering ❌")
        return
    X = np.array([[s['marks']] for s in students])
    kmeans = KMeans(n_clusters=3, random_state=0)
    labels = kmeans.fit_predict(X)
    print("Students clustered into 3 performance groups:")
    for s, label in zip(students, labels):
        group = ["Low","Medium","High"][label]
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}, Group: {group}")

def predict_marks_for_student():
    """Linear Regression to predict expected marks based on age."""
    if len(students)<2:
        print("Not enough data for prediction ❌")
        return
    X = np.array([[s['age']] for s in students])
    y = np.array([s['marks'] for s in students])
    model = LinearRegression()
    model.fit(X, y)
    age = int(input("Enter student age for marks prediction: "))
    pred = model.predict([[age]])
    print(f"Predicted expected marks for age {age}: {pred[0]:.2f}")

def top_performers():
    if not students:
        print("No data available ❌")
        return
    sorted_students = sorted(students, key=lambda s: s['marks'], reverse=True)
    top = sorted_students[:3]  # Top 3 students
    print("Top Performers:")
    for s in top:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")

# =========================
# MAIN MENU
# =========================
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM (AI) =====")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Display Students")
    print("5. Predict Grade (AI)")
    print("6. Cluster Students (AI)")
    print("7. Predict Expected Marks (AI)")
    print("8. Show Top Performers (AI)")
    print("9. Exit")
    
    choice = input("Enter choice: ").strip()
    
    if choice=='1':
        try:
            roll = int(input("Roll: "))
            name = input("Name: ")
            age = int(input("Age: "))
            branch = input("Branch: ")
            marks = float(input("Marks: "))
            photo = input("Photo path: ").strip()
            ok = add_student(students, {
                'roll':roll,'name':name,'age':age,'branch':branch,'marks':marks,'photo':photo
            })
            print("Added ✅" if ok else "Roll already exists ❌")
        except:
            print("Invalid input ❌")
    elif choice=='2':
        try:
            roll = int(input("Enter roll to update: "))
            field = input("Field to update (name/age/branch/marks/photo): ").strip()
            if field not in ['name','age','branch','marks','photo']:
                print("Invalid field")
                continue
            value = input("New value: ")
            if field=='age': value=int(value)
            if field=='marks': value=float(value)
            ok = update_student(students, roll, {field:value})
            print("Updated ✅" if ok else "Roll not found ❌")
        except:
            print("Invalid input ❌")
    elif choice=='3':
        try:
            roll=int(input("Enter roll to delete: "))
            ok=delete_student(students, roll)
            print("Deleted ✅" if ok else "Roll not found ❌")
        except:
            print("Invalid input ❌")
    elif choice=='4':
        display_students(students)
    elif choice=='5':
        predict_grade()
    elif choice=='6':
        cluster_students()
    elif choice=='7':
        predict_marks_for_student()
    elif choice=='8':
        top_performers()
    elif choice=='9':
        print("Exiting program ✅")
        break
    else:
        print("Invalid choice ❌")