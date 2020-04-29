from flask import Flask,request,jsonify
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'todo2'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)




@app.route('/', methods=['GET'])
def testHello():
   print("=================================")
   return "hello there !!"


#user registration
@app.route('/registration',methods=['GET','POST'])
def user_registration():
    fname=request.json['fname']
    lname=request.json['lname']
    school=request.json['school']
    grade=request.json['grade']
    dob=request.json['dob']
    email=request.json['email']
    username=request.json['username']
    password=request.json['password']
    
    ecryptedPassword=sha256_crypt.encrypt(str(password))

    cur =mysql.connection.cursor()

    cur.execute("INSERT INTO users(fname,lname,school,grade,dob,email, username,password) VALUES (%s, %s,%s,%s,%s,%s,%s,%s )" ,(fname,lname,school,grade,dob, email,username ,password))
    
    mysql.connection.commit()
  
    
    cur.close()
    print(request)
    print("this is user registration")
    return "sucessfully registered to todos2 !!"
#log in

@app.route('/login',methods=['GET','POST'])
def user_login():
    
    email=request.json['email']
    password=request.json['password']
    print(password)
    ecryptedPassword=sha256_crypt.encrypt(str(password))
    print(ecryptedPassword)
    cur =mysql.connection.cursor()
    result = cur.execute("SELECT password from users WHERE email=%s " ,[email])
    if (result>0):
        pw = cur.fetchone()
        print(pw)
        return "sucessfully logged in !!"
    else:
        print("There is no user in this email")
        return "sucessfully logged in !!"
        

    
    
    #return "sucessfully logged in !!"

#create Subject
@app.route('/createSubject',methods=['GET','POST'])
def create_subjects():
    Name=request.json['Name']
    color=request.json['color']
    User_ID = request.json['User_ID']
    print(color)

    cur =mysql.connection.cursor()
    cur.execute("INSERT INTO subjects(Name,color,User_ID) VALUES (%s, %s,%s )" ,(Name,color,User_ID))
    mysql.connection.commit()
    
    print("Added a new subject")
    return "sucessfully added a new subject !!"

#get subjects

#create Todos
@app.route('/createTodos',methods=['GET','POST'])
def create_todos():
    title=request.json['title']
    description=request.json['description']
    dueDate=request.json['due_date']
    Subject_ID = request.json['Subject_ID']
    print(dueDate)
    print("Added a new todo")
    return "sucessfully added a new subject !!"

#delete todos

#get todos



if __name__ =='__main__':
     app.run(debug=True)