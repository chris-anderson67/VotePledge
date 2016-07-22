#Vote Pledge App experiment 0.3.5
###Chris Anderson
- Users will pledge to vote on election day

#### Current: 
Migrated to SQL lite, deploying to Heroku

##Plan:
- v0.1: users should be able to sign up - and be verified by email
        - no password or login, simply adding their email

- v0.2: users should be emailed on signing up
- v0.3: make the site look good, add some css, fancy stuff, colors, etc
    - 0.3.0: basic bootstrap styles
    - 0.3.1: custom css for login page
    - 0.3.2: format login page as home page with two columns
- v0.3.5: Swith to SQLlite
    - Merge into Heroku
- v0.4: users reminded via email about voting
- v0.5: users should be able to login with a password and create profile
- v0.6: provide option for users to share votePledge with their friends
- v0.7: progress indication for how many people users have refered

##Possible features: 
- verfiy paypal payment of 10$ which will go through only
        if they do not vote. ? no


The purpose of this webapp is to mess around with html and python,
and hopefully eventually turn it into something useful.

Boiler plate code and Flask know-how from Miguel Grinberg's book,
*Flask Web Development*, which has been a great resource that I 
highly recomend. 
