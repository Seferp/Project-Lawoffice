# Project-Lawoffice

Hello!

Project-Lawoffice is my first big project in Python.
Project was develop in Django. For frontend part I used HTML5 and CSS.
Project was made at the request of my wife. You can visit this address to try live version of my app: 

https://kancelaria-seferyniak.pl

Project is divided by 3 apps: site, blog and shop.
At this moment shop is in progress so I will tell about site and blog.

# Site

The following views are included in this application: 
- Main site (Strona główna)
- About me(O mnie)
- Specializations(Specjalizacje)
- FAQ
- Contact(Contact)

In Specialization we can what see what the law firm does. 
Each specialization has been added to the database and displayed on the website.
We can add them in admin panel

![image](https://github.com/Seferp/Project-Lawoffice/assets/111074557/99ba0454-b093-48f9-b932-982be5510372)

In specialization view we can see name of specialization, image and short descirption(excerpt)

![image](https://github.com/Seferp/Project-Lawoffice/assets/111074557/74a19c48-961b-4630-a0a4-62aaddee78a6)

In FAQ we can find question and answer. All of them has been added in database.

In Contact we have contact form. Using it, we send a message to the owner. The owner received this message on his own inbox(gmail or another)

![image](https://github.com/Seferp/Project-Lawoffice/assets/111074557/5f7f932c-6e43-49c6-9a6c-cb1a33e0cbca)

# Blog

With this app we can add new post on the our website.
The posts have been added on admin panel.

![image](https://github.com/Seferp/Project-Lawoffice/assets/111074557/d7f1ad13-fbde-40a1-bf64-a8a66070751e)

We can add tags which are in another model and they are conncected to model Post with relation many-to-many.
All posts are displayed in blog view. On the main site we can see three the last added posts. 
