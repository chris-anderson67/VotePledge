#Vote Pledge App experiment 0.3.5
## <a href="http://votepledge.us">votepledge.us</a>
### Chris Anderson
- Users pledge to vote in major election

## Changes:
- v0.1: Users should be able to sign up
        - no password or login, simply adding their email
- v0.2: Users emailed on signing up
- v0.3: Make the site look good, add some css, fancy stuff, colors, etc
    - 0.3.0: basic bootstrap styles
    - 0.3.1: custom css for login page
    - 0.3.2: format login page as home page with two columns
- v0.3.5: Switch to SQLlite
    - Merge into Heroku
    - Database Functional

## Possible future options:
- Move deployment to DigitalOcean
- Improve email response reliability (authentication to votepledge email still shoddy).

The purpose of this webapp was to mess around with html and python, and
increase voter turnout.

## Project Structure
- Boiler plate code and Flask know-how from Miguel Grinberg's book,
*Flask Web Development*, which has been a great resource that I 
highly recomend. 
- Main views, pages defined in /app/views.py
