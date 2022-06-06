# Step Parents Unite

[view the live site here](https://step-parents-unite.herokuapp.com/)

[View the GitHub repository here](https://github.com/Mrst12/step-parents-unite)

## Introduction
Step Parents Unite is a blog website designed for step families to chat and support
each other with the ups and downs of either just step children or blended families.
Being a parent to your own biological children can be tough, but the maze of being a step parent is much
more difficult so I was hoping this page could bridge this gap.

![Am I Responsive](./assets/documentation/responsive-view.png)

*We all need moral support*

## Contents 
- [User Experience](#user-experience)
    - [Admin](#admin)
    - [General User](#general-user)
    - [Member User](#member-user)
- [Design](#design)
    - [Wireframes](#wireframes)
    - [Flowcharts](#flowcharts)
    - [Database models](#database-models)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
- [Technologies used](#technologies-used)
    - [Frameworks, Libraries & Tools Used](#frameworks-libraries--tools-used)
- [Testing](#testing)
- [ Fixed Bugs](#fixed-bugs)
- [Known Bugs](#known-bugs)
- [Deployment](#deployment)
- [Credits](#credits)
    - [Acknowledgements](#acknowledgements)

## User Experience
- I designed the site with the design thinking approach, with only neccessary content/information.
- Users can look around the site easily without being bombarded with lots of clutter.
- My User stories can be found [here](https://github.com/Mrst12/step-parents-unite/projects/2)

### Admin

- As Site Admin, I can approve/disapprove blogs and comments so that I can filter out objectionable Content.
- As Site Admin I can create, post, edit or delete blogs so that I can share and manage my blogs.
- As Site Admin I can have all the functionality of a member user so that I can be involved with the blog site.

### General User

- As a general user, I can view a list of blogs so that I can select one to read.
- As a general user, I can click on a blog so that I can read the whole blog.
- As a general user, I can view the number of likes on a blog, so that I can see which is most popular.
- As a general user, I can view comments on individual blogs so I can read the full conversation.
- As a general user, I can register for an account to take full member user benefits.

### Member user

- As a member user, I can create, post, edit or delete blogs so that I can share and manage my blogs.
- As a member user, I can like/unlike blogs so that I can interact with the content.
- As a member user, I can leave comments on a blog, so that I can be involved with the conversation.

## Design
- I have used an agile approach to the project my development board for the project can be viewed 
[here](https://github.com/Mrst12/step-parents-unite/projects/1)

### Wireframes
[wireframes for project](./assets/wireframes/step-parents-unite.pdf)

### Flowcharts
[Admin flowcharts for project](./assets/wireframes/admin-chart.pdf)

[User flowcharts for project](./assets/wireframes/user-flowchart.pdf)

### Database Models

[Table for post model database](./assets/wireframes/post-model.pdf)

[Table for comment model database](./assets/wireframes/comments-model.pdf)

### Colour Scheme
I used a range of colours that complimented each other, and a darker colour for the text so it 
was better for accessibility.

![Colour scheme used for site](./assets/documentation/colours-pp4.png)

![Text colour](./assets/documentation/text-colour.png)

### Typography

- I used Monserrat for the main title, and Catamaran for the rest of the text.

## Features

- Registered users will have full CRUD functionality, They can **C**reate, **R**ead, **U**pdate, and **D**elete blogs.

### Existing Features
- **Home Page**
    - The Home page has minimal content so it is not overcrowded for the user. The page has a navigation bar,
    with the logo that will take you back to the home page, a blog button, to take any user to the blogs page,
    When a user is not logged in there is a register button, and a Login button. On the tablet and mobile sizes the navigation bar collapses to a burger menu. There is a footer across the bottom of every page to indicate the end of the page.

    ![Home page when user is not logged in](./assets/documentation/homepage-loggedout.png)
    
    - When a user is logged in the reister button on the navigation bar is changed to an Acoount button, which takes them to manage their blog page, the Login button becomes a Logout button, so the user knows their status.

    ![Home page when user logged in](./assets/documentation/homepage-loggedin.png)

- **Blog Page**
    - Any user can enter the blog page, It is a showcase of all blogs.
    - The Title, excerpt, author, date and time created on and the number of likes is visible on each blog.

    ![Blog page](./assets/documentation/site-blogpage.png)

- **Blog-details Page**
    - This page is accessible to any user.
    - When the user is not logged in the can view the title, author, content of blog, time and date created, the number of likes and comments, and the comments made by others.

    ![blog details not logged in](./assets/documentation/site-blogdetails-notloggedin.png)

    - when the user is logged in they can view the same as other users but they have the ability to like a post, and to comment on the post.

    ![blog details logged in](./assets/documentation/site-detailloggedin.png)

- **Register page**
    - Users can register for their own account.
    - A registered user has access to more features such as liking and commenting on existing posts as well as publishing  and managing (edit/delete)their own blogs.

    ![Register page](./assets/documentation/site-registerpage.png)

- **Logout**
    - When a user clicks the logout button form the menu or accounts page it triggers a logout modal.
    - The logout modal is used for confirmation the user wants to logout out.

    ![logout modal](./assets/documentation/logout-modal.png)

- **User Account/ Profile Page**
    - Once the user is registered and logged in they have a user profile page.
    - On the profile page they can Publish a blog, manage their blogs, or logout.

    ![profile page](./assets/documentation/site-accountpage.png)

- **Publish page**
    - This page is where the user can publish their own page.
    - Once approved the published blog will appear in the blog page.

    ![publish blog](./assets/documentation/site-publishblog.png)

- **Manage blog page**
    - This page shows the user all of their blogs
    - It displays the status of their blog either awaiting approval or published
    
    ![manage blogs](./assets/documentation/site-manageblogs.png)

    - The user can edit their blogs from this page.
    - The form is already pre populated to make it easier for the user.

    ![edit blog](./assets/documentation/site-editblog.png)

    - The user can also delete blogs from this page.
    - The delete button will trigger a modal used as confirmation they do want to delete the blog.

    ![delete modal](./assets/documentation/delete-modal.png)

### Future Features
- The ability to sign in with social accounts like Facebook, Google etc.
- Members can save blogs they like for easy access in the future.
- The ability to tag other members in posts.
- The ability to follow other users.
- Include a forgotten password function to change or reset password.
- Create a search bar to search for blogs containing a specific word or phrase.


## Technologies used
- HTML
- CSS
- JavaScript
- Python
    - The below modules were used for the development of the project.
        *   asgiref==3.5.1
        *   cloudinary==1.29.0
        *   dj-database-url==0.5.0
        *   dj3-cloudinary-storage==0.0.6
        *   Django==3.2.13
        *   django-allauth==0.50.0
        *   django-crispy-forms==1.14.0
        *   django-summernote==0.8.20.0
        *   gunicorn==20.1.0
        *   oauthlib==3.2.0
        *   psycopg2==2.9.3
        *   PyJWT==2.4.0
        *   python3-openid==3.2.0
        *   pytz==2022.1
        *   requests-oauthlib==1.3.1
        *   sqlparse==0.4.2

### Frameworks, Libraries & Tools Used
- Balsamiq
    - For the wireframes
- Lucid app
    - For the flowchart
- Word
    - For the Database models
- Git 
    - For version control, committing and pushing to GitHub
- GitHub
    - For storing the repository, files and images pushed from Gitpod
- Gitpod
    - IDE used to code my project
- Heroku
    - Used to deploy the application
- Bootstrap
    - Used for grids, layout, columns, cards and forms structure
- Django
    - Used for django frameworks to manage the apps
- Google Fonts
    - Used for the fonts on the site
- Fontawesome
    - Used for the additional icons
- Coolors
    - Used for the colour scheme on the site
- PostgreSQL
    - Used for the database storage of the models
- Cloudinary
    - Used for image and static files
- AmIResponsive
    - used for the responsiveness of the site
- Lighthouse
    - Used for testing site functionality
- W3C Markup Validation Service
    - Used for HTML testing
- W3C CSS Validation Service
    - Used for CSS testing
- PEP8
    - Used for Python testing files
    
## Testing
- *Unit testing*, *Validator testing* and *User story testing* can all be found [here](/TESTING.md)
## Fixed Bugs
- The bugs can be seen documented in my kanban development board in their own column [here](https://github.com/Mrst12/step-parents-unite/projects/1)

- Heroku initial deployment
    - I had an issue where I couldnt do a deployment to Heroku, it was not recognising the projects name.
        - It was fixed by changing the filename in the Procfile from what I had put step-parents-unite to what it should of been step_parents_unite. It was then deployed to Heroku.
- Submit not redirecting
    - When a user wanted to comment on a blog they fill in the body and then click submit, this was redirecting to a page saying "This page is not working, contact the owner, error 405"
        - To fix it I did a google search on error 405, which gave me an idea the problem was in my views.py file,
        I had an indented block of code, the clue came from the problems tab on the terminal, sorted the indentation and the submit worked as it should.
- White gap on footer
    - My footer was not stretching across the whole page I had a white gap on the left hand side.
        - Used developer tools to investigate the problem and found I had added a margin to the body which was causing the issue, restyled and it looked as it should.
- Only one post on my blog page
    - On my manage blog page it was only ever showing the last post that was put there.
        Went through the blog file line by line to see if I could establish the problem, and found I had missed off a closing div element, added it in and the problem was resolved.
- Trailing whitespace
    - When doing the PEP8 testing on my views.py file I found [this error](./assets/documentation/pep8-views.py-bug.png)
        - Did a google search for the problem and came up with [this article](stackoverflow.com/questions/21410075/what-is-trailing-whitespace-and-how-can-i-handle-this) implemented the changes and the error was gone.

## Known bugs
- Page layout
    - On tablet devices I originally wanted 2 cards per row however I was getting
     ![page-layout](./assets/documentation/page-layout.png)
    - It was the same layout all down the page, the pagination was set to six, I spent a good few days trying to research and resolve this issue, on google, stackoverflow, slack all to no avail. I decided to leave the tablet view at 3 per page as it didnt look as squashed as I thought it would when designing the wireframes.
    - Something to revisit in the future when my scope is a bit wider.
    
    
## Deployment

## Credits

### Acknowledgements