CS50 Final Project

# Tour Bus Ticket Booking
#### Video Demo:  https://www.youtube.com/watch?v=g2KEYOqjydk
#### Description:
Hosted at http://calappurackal.com:8080, my project is a simple bus ticket booking system. The system is built on mysql, flask,html, javascript, jinja.

**Here I have also adopted and reused code,  helper.py and layout.html,  from cs50x Finance problem set, with enhancement and modificaitons to fit for this project's requirement.**

The application is hosted on Oracle Cloud Infrastructre, allways free tier. Conists of 1 LBaaS,
3 VM - which is 2 Appliction tier, and one DB Tier running mySQL, running in two seprate subnets for security reasons.
Middle tier VMs run Oracle Linux Server release 7.9 , and DB Tier is running Oracle Linux Server release 8.8.

Also, there is connection provided  to Oracle Cloud Infrastructre Object Store for backup, as and when required. Also a connection to Free Tier Autonomous Data Warehouse is provided for data loading.

The Mysql database schema design as shown here in the phpmyadmin.  http://calappurackal.com/phpmyadmin

##### Applicaiton Features
1. Allows new travellers to register and login, and admins to login
2. Default Admin seeded.
3. Admin can
    - register new admins,
    - Add new buses
    - Register new routes
    - Update buses, and routes, (planned feature)
    - View Dynamic Reports on buses , bookings, and routes at the same page.
4. Travellers can
    - Log in / Logout
    - Book Trips
    - Cancel Trips,
    - View reports on Trips , present and past.
    - Update profile (planned feature)

5. Dynmaic Navigations based on role of user/admin login
6. Login required to perfrom any function.

##### Files:
+ app.py
    >_This file is the main applicatio file used for Flask_
+ helpers.py
    >_This file is reused from cs50x Problem Set 9 - Finance, and modified to include adloginrequired funcation to suite this project_
+ template/add_buses.html
    >_This template is used for admin user to add new buses to the system_
+ template/add_routes.html
    >_This template is used for admin user to add new routes to the system_
+ template/admin_login.html
    >_This template is used as login page for admin user_
+ template/admin_register.html
    >_This template is used for admin user to register new administrators to the system_
+ template/book_tickets.html
    >_This template is used for travellers  to book tickets for routes_
+ template/cancel_tickets.html
    >_This template is used for travellers  to cancelled booked tickets for routes. User can cancel only his own tickets._
+ template/dashboard.html
    >_This template is used as default home page post login_
+ template/history.html
    >_This template is used for travellers  to see his own  booked and cancelled tickets for various routes._
+ template/index.html
    >_This template is used as default home page prelogin_
+ template/layout.html
    >_Layout Template, This file is reused from cs50x Problem Set 9 - Finance, and modified to fit this project_
+ template/login.html
    >_This template is used as login page for traveller user_
+ template/register.html
    >_This template is used as selft register page for traveller user_
+ template/reports.html
    >_This template is used as dynamic reprts  page for admin user_
+ cs50db.sql
    >_This is a dump of export of tables from "cs50db" database _
+ cs50db.pdf
    >_This is the export of schema from cs50db in PDF format_