## Contents
- [Unit Testing](#unit-testing)
    - [Testing Views](#testing-views)
    - [Testing Forms](#testing-forms)
- [Validator Testing](#validator-testing)
    - [Lighthouse Test](#lighthouse-test)
    - [W3C Markup Validation](#w3c-markup-validation)
    - [W3C CSS Validation](#w3c-css-validation)
    - [PEP8 validation](#pep8-validaton)
- [User Story Testing](#user-story-testing)
    - [Admin](#admin)
    - [General User](#general-user)
    - [Member User](#member-user)

## Unit Testing

- I have used Django TestCase for automated testing for Views, and form files

### Testing Views
- Tested views to see if they are functioning as expected and returns the page the user needs to be at.
    
- Home page

![testing home page views](./assets/documentation/indexpage-test.png)


- Blog page

![testing blog page views](./assets/documentation/blogpage-test.png)

- Profile Page

![testing for profile page views](./assets/documentation/profilepage-test.png)

- Publishing Blogs Page

![testing for publishing blog views](./assets/documentation/publishpage-test.png)

Result :

![result for views tests](./assets/documentation/test-for-views-result.png)

### Testing Forms
- Tested forms for comment form and blog form to make sure fields are expected and the form is submitted to where it should be.

- Testing blogform

![test for blogform](./assets/documentation/test-blogform.png)

- Testing Comment forms

![tests for comment form](./assets/documentation/test-commentform.png)

Result:

![result for form tests](./assets/documentation/formstests-results.png)

## Validator Testing

### Lighthouse Test

- Lighthouse result for desktop

![lighthouse report desktop](./assets/documentation/lighthouse-score.png)

- Lighthose only gave a score of 92 for best practice, this was a problem beyond my scope at the moment

![lighthouse low score](./assets/documentation/lighthouse-testproblem.png)

- Lighthouse result for mobile

![lighthouse result for mobile](./assets/documentation/lighthouse-mobile.png)

### W3C Markup Validation

- Home page

![home page HTML test](./assets/documentation/html-indexpage.png)

- Blog page

![blog page HTML test](./assets/documentation/html-blogpage.png)

- Blog detail page

![blog-detail page HTML test](./assets/documentation/html-blogdetail-page.png)

- Register Page

![register page HTML test](./assets/documentation/html-registerpage.png)

- Login Page

![login page HTML test](./assets/documentation/html-loginpage.png)

- My Blogs Page

![My blogs page HTML test](./assets/documentation/html-myblogspage.png)

- Profile page

![Profile page HTML test](./assets/documentation/html-profilepage.png)

- Publish page

![publish page HTML test](./assets/documentation/html-publishpage.png)

### W3C CSS Validation

- No errors or warnings found

![Css validation test](./assets/documentation/css-check.png)

### PEP8 validation

## User Story Testing

### Admin

### General User

### Member User