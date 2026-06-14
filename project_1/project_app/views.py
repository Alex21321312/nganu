from django.shortcuts import render, redirect
from .models import Users
import pyodbc
from encryption import encrypt, decrypt
from django.utils import timezone

def get_connection():

    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-TSG1P6E\\SQLEXPRESS;"
        "DATABASE=DistribusiDB3Gen3Z1;"
        "Trusted_Connection=yes;"
    )

    return conn


def is_logged_in(request):
    return request.session.get('username')

def login_view(request):

    if request.method == 'POST':

        # username = request.POST.get('username')
        # password = request.POST.get('password')

        # encrypted_password = encrypt(password, 'mysecretkey')

        # print("Username entered:", username)
        # print("Password entered:", password)
        # print("Encrypted password:", repr(encrypted_password))

        # user = Users.objects.filter(username=username).first()

        # if user:
        #     print("Stored password:", repr(user.password))
        #     print("Match:", user.password == encrypted_password)
        # else:
        #     print("User not found")

        username = request.POST.get('username')
        password = request.POST.get('password')
        encrypted_password = encrypt(password, 'mysecretkey')

        user = Users.objects.filter(
            password = encrypted_password
            ).first()

        if user and user.username == username:
            # return redirect('/home/')
            request.session['username'] = username
            return render(request, 'home.html', {
                'username' : username
                })
        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')

def home(request):

    if not is_logged_in(request):
        return redirect('login')
    
    username = request.session.get('username')

    context = {
        'username' : username,
    }

    return render(request, 'home.html', context)

def menu(request):

    if not is_logged_in(request):
        return redirect('login')

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM dbo.r_user
    """)

    columns = [column[0].lower() for column in cursor.description]

    users = []

    for row in cursor.fetchall():
        try:
            password = decrypt(row[1], "mysecretkey")
        except Exception as e:
            password = f"ERROR: {e}"

        users.append({
            'username': row[0],
            'password': row[1],
            'id_group_user': row[2],
            'audit_date': row[3],
            'audit_user': row[4]
        })

    conn.close()

    return render(request, 'menu.html', {
        'users': users
    })

def add_user(request):

    if not is_logged_in(request):
        return redirect('login')

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        encrypted_password = encrypt(password, 'mysecretkey')      #
        id_group_user = request.POST.get('id_group_user')
        audit_date = timezone.localtime()
        audit_user = request.session.get('username')

        cursor.execute("""
            INSERT INTO dbo.r_user
            (username, password, id_group_user, audit_date, audit_user)
            VALUES (?, ?, ?, ?, ?)
        """, (
            username,
            encrypted_password,
            id_group_user,
            audit_date,
            audit_user
        ))

        conn.commit()

        return redirect('menu')

    # USER LIST FOR LEFT MENU

    cursor.execute("""
        SELECT username, password, id_group_user
        FROM dbo.r_user
    """)

    columns = [column[0].lower() for column in cursor.description]

    users = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    conn.close()

    return render(request, 'add_user.html', {
        'users': users
    })

def edit_user(request, username):

    if not is_logged_in(request):
        return redirect('login')

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':

        new_username = request.POST.get('username')
        password = request.POST.get('password')
        encrypted_password = encrypt(password, 'mysecretkey')
        id_group_user = request.POST.get('id_group_user')
        audit_date = timezone.localtime()
        audit_user = request.session.get('username')

        cursor.execute("""
            UPDATE dbo.r_user
            SET username=?,
                password=?,
                id_group_user=?,
                audit_date=?,
                audit_user=?
            WHERE username=?
        """, (
            new_username,
            encrypted_password,
            id_group_user,
            audit_date,
            audit_user,
            username
        ))

        conn.commit()
        conn.close()

        return redirect('menu')

    cursor.execute("""
        SELECT *
        FROM dbo.r_user
        WHERE username=?
    """, (username,))

    row = cursor.fetchone()

    user = {
        'username': row[0],
        'password': decrypt(row[1], 'mysecretkey'),
        'id_group_user': row[2],
        'audit_date': row[3],
        'audit_user': row[4]
    }

    cursor.execute("""
        SELECT *
        FROM dbo.r_user
    """)

    columns = [column[0].lower() for column in cursor.description]

    users = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    conn.close()

    return render(request, 'edit_user.html', {
        'user': user,
        'users': users
    })

def delete_user(request, username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM dbo.r_user
        WHERE username=?
    """, (username,))

    conn.commit()
    conn.close()

    return redirect('menu')

def logout_view(request):
    request.session.flush()
    return redirect('login')