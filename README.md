# EXPENCE

## Description

This project is built using `django`, a python framework and `VueJS`, a frontend framework.
It's divided into two directories namely, expense(which contains django API) and expence(which contains a VueJS app)

## Installation

## Django Project/API

<i>Assuming you already have python, pip and pipenv installed</i>

1. Clone the project from `https://github.com/izamha/XPENCE.git`
2. Navigate to its directory/folder: `cd <directory-name>`
3. Activate the pipenv shell by typing `pipenv shell` into the terminal.
4. After the shell has been activated,
5. Type `pipenv install` to install all the dependencies used in this project.
6. In case <b>Step 5</b> throws an error about the python version used with project not being the same as the one installed on your PC, navigate into the project folder `expense` and look for a file called `Pipfile` and change to your python's version i.e `python_version = "3.8"`
7. To stop/exit the pipenv shell, type `CTRL + C`

## API Documentation

https://documenter.getpostman.com/view/12136698/UVRHh2nb

## Frontend with VueJS + Vuetify

Assuming you already have `npm` or `yarn` and Node.js installed
if not refer to `https://docs.npmjs.com/downloading-and-installing-node-js-and-npm`


1. Install Vue CLI by `npm install -g @vue/cli` or `yarn global add @vue/cli`
2. Navigate into the `expence` folder and type in your terminal `npm install`.
3. Run the project by `npm run serve`


