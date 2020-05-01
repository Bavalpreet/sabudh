from flask import Flask, request ,render_template
from flask_mysqldb import  MySQL
from flask import jsonify



app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'test'
app.config['MYSQL_DB'] = 'book_db'

mysql = MySQL(app)



@app.route('/create', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        book_details = request.form
        book_titl = book_details['title']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO book_info(book_title) VALUES(%s)",(book_titl,))
        result=cur.execute("SELECT LAST_INSERT_ID()")
        if result > 0:
            last_id = cur.fetchall()
        mysql.connection.commit()

        cur.close()
        return render_template('return_record.html',last_bookid=last_id)
    return render_template('create.html')

@app.route('/update',methods=['GET','POST'])
def update_data():
    if request.method == 'POST':
        update_Details = request.form
        book_id= update_Details['id']
        tit_up = update_Details['up_title']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE book_info SET book_title = %s WHERE serial_no = %s",(tit_up,book_id))
        mysql.connection.commit()
        cur.close()
        return 'update '
    return render_template('update_book.html')


@app.route('/prime', methods = ['GET','POST'])
def prime():
    flag=1
    if request.method== 'POST':
        prime_Details = request.form
        number_check= prime_Details['prime_no']
        number_check=int(number_check)

        flag = 0
        i = 2
        if number_check > 1000000:
            while i < number_check:
                if float(number_check % i) == 0:
                    flag = 1
                    print('not a prime')
                    break
                i = i + 1
            if flag == 1:
                return 'not prime'
            else:
                return 'prime'
        else:
            return 'enter number greater then 1m'

        # if my_res==1:
        #     return 'not prime'
        # elif my_res==2:
        #     return ' enter number greater then 1m'
        # else:
        #     return 'prime'
    return render_template('check_prime.html')


@app.route('/class/<int:roll>')
def roll_num(roll):
    return 'roll number: %s'% roll

def check_prime(n):
    flag=0
    i=2
    if n>1000000:
        while i<n:
            if float(n%i)==0:
                flag=1
                print(i)
                print(n%i)
                print('not a prime')
                break
            i=i+1
        if flag==1:
            return 'not prime'
        else:
            return 'prime'
    else:
        return 'enter number greater then 1m'






if __name__ == '__main__':
    app.run(debug=True)

