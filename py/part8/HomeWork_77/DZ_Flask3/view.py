import sqlite3
import os
import flask_login

from DataDB import DataDB
from flask import render_template, url_for, request, flash, session, redirect, abort, g
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from UserLogin import UserLogin
from app import app

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
login_manager.login_message_category = 'success'


@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().from_db(user_id, dbase)


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sql_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


dbase = None


@app.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = DataDB(db)


@app.route("/")
def index():
    return render_template('index.html', title="Главная", mh=dbase.get_menu_header(), mf=dbase.get_menu_footer(),
                           posts=dbase.get_post_annonce())


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        user = dbase.get_user_by_email(request.form['email'])
        if user and check_password_hash(user['psw'], request.form['psw']):
            user_login = UserLogin().create(user)
            rm = True if request.form.get('remember') else False
            login_user(user_login, remember=rm)
            return redirect(request.args.get("next") or url_for('profile'))
        flash("Неверная пара логин/пароль", "error")
    return render_template('login.html', title="Авторизация", mh=dbase.get_menu_header(), mf=dbase.get_menu_footer())


@app.route("/add_posts", methods=["POST", "GET"])
@login_required
def add_posts():
    if request.method == 'POST':
        if len(request.form['name']) < 20 and len(request.form['price']) < 10 \
                and (20 > len(request.form['url']) >= 1) and (15 > len(request.form['resort']) >= 1) \
                and len(request.form['star']) >= 1 and (5 > len(request.form['duration']) >= 1) \
                and (15 > len(request.form['nutrition']) >= 1) and len(request.form['post']) > 10:
            res = dbase.add_post(request.form['name'], request.form['price'], request.form['url'],
                                 request.form['resort'], request.form['star'], request.form['duration'],
                                 request.form['nutrition'], request.form['post'])
            if not res:
                flash("Ошибка добавления тура", category='error')
            else:
                flash("Тур успешно добавлен", category='success')
        else:
            flash("Ошибка добавления", category='error')
    return render_template('add_posts.html', title="Добавить тур", mh=dbase.get_menu_header(),
                           mf=dbase.get_menu_footer())


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if len(request.form["name"]) > 4 and len(request.form['email']) > 4 and len(request.form['psw']) > 4 and \
                request.form['psw'] == request.form['psw2']:
            hash = generate_password_hash(request.form['psw'])
            res = dbase.add_user(request.form["name"], request.form['email'], hash)
            if res:
                flash("Вы успешно зарегистрированы", "success")
                return redirect(url_for('login'))
            else:
                flash("Пользователь с таким email уже существует", "error")
        else:
            flash("Неверно заполнены поля", "error")
    return render_template('register.html', title="Регистрация", mh=dbase.get_menu_header(), mf=dbase.get_menu_footer())


@app.route('/profile')
@login_required
def profile():
    return render_template("profile.html", title="Профиль", mh=dbase.get_menu_header(), mf=dbase.get_menu_footer())


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Вы вышли из аккаунта", "success")
    return redirect(url_for('login'))


@app.route('/userava')
@login_required
def userava():
    img = current_user.get_avatar(app)
    if not img:
        return ""
    h = app.make_response(img)
    h.headers['Content-Type'] = 'image/png'
    return h


@app.route('/upload', methods=["POST", "GET"])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and current_user.verify_ext(file.filename):
            try:
                img = file.read()
                res = dbase.update_user_avatar(img, current_user.get_id())
                if not res:
                    flash("Ошибка обновления аватара", "error")
                flash("Аватар обновлен", "success")
            except FileNotFoundError as e:
                flash("Ошибка чтения файла", "error")
        else:
            flash("Ошибка обновления аватара", "error")

    return redirect(url_for('profile'))


@app.route("/contacts")
def contacts():
    return render_template('contacts.html', title='Контакты', mh=dbase.get_menu_header(), mf=dbase.get_menu_footer())


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена",
                           mh=dbase.get_menu_header(), mf=dbase.get_menu_footer())


@app.route("/support", methods=["POST", "GET"])
def support():
    return render_template('support.html', title='Обратная связь', mh=dbase.get_menu_header(),
                           mf=dbase.get_menu_footer())


@app.route("/post/<alias>")
@login_required
def show(alias):
    country, text, resort, post = dbase.get_post(alias)
    if not country:
        abort(404)
    return render_template('post.html', country=country, text=text, resort=resort, post=post,
                           mh=dbase.get_menu_header(), mf=dbase.get_menu_footer())
