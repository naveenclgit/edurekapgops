import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session,jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
from fractions import Fraction

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    trans = db.execute(
        "SELECT symbol,sum(shares) as shares,  round(sum(shares * price),2) as price  FROM assets WHERE user_id = ? group by symbol having sum(shares) > 0",
        session["user_id"],
    )
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    transcahs = db.execute(
        "SELECT  round(sum(shares * price),2) as acv  FROM assets WHERE user_id = ?",
        session["user_id"],
    )
    acbalance = round(float(cash[0]["cash"]), 2)

    if not trans:
        return render_template("index.html", trans=trans, cash=float(acbalance), total=0)
    else:
        total = round(float(cash[0]["cash"]), 2) + round(float(transcahs[0]["acv"]), 2)
        return render_template("index.html", trans=trans, cash=float(acbalance), total=float(total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        symbol = symbol.upper()

        if not symbol:
            return apology("What do you want?")

        company = lookup(symbol.upper())
        if not company:
            return apology("No such Symbol")


        sharesp = request.form.get("shares")
        try:
            tmvalue = int(float(sharesp))
            tmvalue = (float(tmvalue) % (int(float(tmvalue))))
        except:
            return apology("No fractional, negative, and non-numeric",400)

        if not sharesp or (int(float(sharesp)) < 1) :
            return apology("No fractional, negative, and non-numeric",400)

        shint = isinstance(sharesp, int)

        if shint or (float(sharesp) % (int(float(sharesp))) == 0):
            shares = int(float(request.form.get("shares")))
            cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        # print(cash)
            totalprice = shares * float(company["price"])
            acbalance = float(cash[0]["cash"])
            if totalprice > acbalance:
                return apology("Insufficient Funds")
            else:
                db.execute(
                    "INSERT INTO purchase (user_id, symbol,shares,price) VALUES(?,?,?,?)",
                    session["user_id"],
                    symbol,
                    shares,
                    float(company["price"]),
                )
                db.execute(
                    "UPDATE users set cash = (?) WHERE id= (?)",
                    acbalance - totalprice,
                    session["user_id"],
                )
                flash("Transaciton completed. ")
                return redirect("/")
        else:
            return apology("No fractional, negative, and non-numeric",400)
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    trans = db.execute(
        "SELECT *  FROM assets WHERE user_id = ? order by date", session["user_id"]
    )
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    transcahs = db.execute(
        "SELECT  round(sum(shares * price),2) as acv  FROM assets WHERE user_id = ?",
        session["user_id"],
    )
    acbalance = round(float(cash[0]["cash"]), 2)
    total = round(float(cash[0]["cash"]), 2) + round(float(transcahs[0]["acv"]), 2)
    return render_template("history.html", trans=trans, cash=acbalance, total=total)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("What do you want?")
        company = lookup(symbol.upper())
        if not company:
            return apology("No such Symbol")
        # print(company)
        # return render_template("quoted.html", name=company["symbol"], price=company["price"], symbol=company["symbol"], fthigh=company["week52High"], ftlow=company["week52Low"], avgttlv=company["avgTotalVolume"] )
        return render_template(
            "quoted.html",
            name=company["symbol"],
            price=company["price"],
            symbol=company["symbol"],
        )
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form.get("username")
        if not name:
            return apology("You can't exist without a username !")

        password = request.form.get("password")
        if not password:
            return apology("No Password?  No way!")

        confirmation = request.form.get("confirmation")
        if not confirmation or password != confirmation:
            return apology("Same Passwords please!")

        usernamecnt = db.execute("select *  from users where username = ?", name)
        if not usernamecnt:
            try:
                hash = generate_password_hash(password)
                db.execute(
                    "INSERT INTO users (username, hash) VALUES(?, ?)", name, hash
                )
                return redirect("/")
            except:
                return apology("Sorry, its not you , its us.!")
        else:
            return apology("This username already exists")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("What do you want?")
        print(len(symbol))
        company = lookup(symbol.upper())
        print(company)
        if not company:
            return apology("No such Symbol")

        shares = int(request.form.get("shares"))
        if shares < 1:
            return apology("Need to sell something")

        symboltosell = db.execute(
            "SELECT sum(shares) as stock FROM assets WHERE user_id = ? and symbol = ? ",
            session["user_id"],
            symbol,
        )
        # print(symboltosell)
        syminhand = float(symboltosell[0]["stock"])

        if syminhand < shares:
            return apology("Insufficient Shares")
        else:
            totalprice = shares * float(company["price"])
            cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            acbalance = float(cash[0]["cash"])
            db.execute(
                "INSERT INTO sales (user_id, symbol,shares,price) VALUES(?,?,?,?)",
                session["user_id"],
                symbol,
                shares,
                float(company["price"]),
            )
            db.execute(
                "UPDATE users set cash = (?) WHERE id= (?)",
                acbalance + totalprice,
                session["user_id"],
            )
            flash("Transaciton completed. ")
        return redirect("/")
    else:
        availsysm = db.execute(
            "SELECT  symbol, sum(shares) as stock FROM assets WHERE user_id = ? GROUP BY symbol having sum(shares) > 0",
            session["user_id"],
        )
        return render_template("sell.html", availsysm=availsysm)
