**OVERVIEW**\
This project represents an implemention of a web photo gallery. Users who create an account are able to publish photos, visibile on the home page of the website.

**Frontend**\
The frontend of the website is implemented using HTML, CSS, Flask, Jinja2 and Bootstrap. All website pages feature a collapsible navigation bar that transforms into a hamburger menu when the page is minimized. An unauthenicated user can access the following pages:
* Home: the main page of the website; all of the photos uploaded on the website are displayed on the home page by category.
* Sign Up: a page that allows users to create an account
* Login: a page where users with an existing account can log in
* About Me: page that outlines the purpose of this website
  
After logging into the account, the user is granted access to the following web pages:
* Photo Gallery: a page that displays by category all of the photos updated by the use
* Upload: a page that allows users to upload new photos
* Logout: a page where the user can log out of their account
  
Photos are displayed as a thumbnail; by clicking on the thumbnail, the full-sized photo is shown.

**Backend**\
The backend of the website was developed using Python, using some Flask configurations as well. Information about users and uploaded photos is stored in a SQLite database. The project includes multiple Python files, used in implementing the website functionalities: log in / log out, sign up, upload photo, display photo and thumbnails

**Docker Containerization**\
The project contains a Dockerfile, used for building and running the server.
