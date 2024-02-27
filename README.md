# PP3 BATTLESHIPS

# Site 
Battleship is a game where you challenge computer to sink the 3 ships thats randomly placed on the board before your shots run out. Everyship has 1 placement so each time you make a hit you will sink the ship & you need to find all 3 ships to win the game.

# Table Of Contents

* [Site](#site)
* [Project Goals](#project-goals)
   * [Site Goals](#site-goals)
* [Features](#features)
   * [Start Menu](#start-menu)
   * [Functions](#functions)
* [Validator Testing](#validator-testing)
   * [CI Python Linter](#ci-python-linter)
   * [Unfixed Bugs](#unfixed-bugs)
* [Deployment](#deployment)
   * [Link to live website](#live-website)
* [Credits](#credits)



# Project Goals

## Site Goals

Battleship is a well known game for a long time but nowadays it feels like it disappeared from the game section. I want to provide this game so more people get to know about it and let it become mainstream again.

# Features

## Start Menu

This is the first interaction you get when you run the program.

![Main menu](/images/Skärmbild%202024-02-25%20114705.png)



## Functions

If you hit a boat

![Hit](/images/hit%20boat.png)

If you miss a boat

![Miss](/images/you%20missed.png)

If you try to shot at the same target

![Same Target](/images/if%20i%20try%20to%20shot%20at%20same%20position.png)

If you ran out of shots

![Game Over](/images/game%20over,%20want%20to%20try%20again.png)

If you try to shot outside the board

![Miss the board](/images/invalid%20shot.png)


# Validator Testing

## CI Python Linter

![CI Python Linter](/images/CI%20Python%20Linter%20.png)


## Unfixed Bugs

* Can't type or do anything in the terminal with my Iphone.

# Testing

What i have tested.

* I have tried to break the program by using wrong inputs without any fails.
* I have ran the program thru CI Python Linter without and problems.
* The code is tested in both console on Gitpod and Heroku without problems.
* Tested the website in Firefox, Chrome & Safari without problems .
* Can't do anything in the terminal with my Iphone.

# Deployment

This project was deployed using Code Institute's mock terminal for Heroku following the steps outlined below:

* In Heroku account choose 'Create new app' from the 'New' menu
* In 'Settings' configure 'Config Vars', scroll down to the 'Buildpack' section and add Python and NodeJS buildpacks
* In the 'Deploy' tab select 'GitHub' to connect to your GitHub repository
* Choose the repository to deploy
* Scroll down the page and press 'Deploy' button
* Once the web app has been successfully deployed, you will see a link to the deployed app. This link can be used to access and test the application

<br>
<br>

## Live Website

Link to the live platform - [Battleships PP3](https://pp3-battleships-viktor-1c43cb2d6445.herokuapp.com/)


# Credits

* I want to give a huge thanks to my mentor Oluwafemi Medale that realised i tried to do my own templates.
* Want to thank [Dr Codie](https://www.youtube.com/watch?v=Ej7I8BPw7Gk&list=PLpeS0xTwoWAsn3SwQbSsOZ26pqZ-0CG6i) for helping me get a structure of the game.
* Also i wanna thank [Code Institute](https://codeinstitute.net/se/) for the templates









