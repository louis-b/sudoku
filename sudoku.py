#!/usr/bin/python2

"""

Sudoku

Sept. 2015

"""

from calendar import HTMLCalendar, TextCalendar
from copy import deepcopy
#from Crypto.Cipher import AES
#from Crypto import Random
from datetime import date, datetime, timedelta
from flask import Flask, render_template, request
from flask import flash, redirect, session, url_for, g
#from flask.ext.login import LoginManager, UserMixin
#from flask.ext.login import login_user, logout_user, current_user, login_required
#from flask.ext.wtf import Form
from os.path import commonprefix
#from passlib.hash import sha256_crypt
from random import choice, randint
from urlparse import urljoin
#from werkzeug.contrib.atom import AtomFeed
#from wtforms import StringField
#from wtforms.validators import DataRequired
import math, os, pickle, random, re, requests, sqlite3, string, sys
import json
from datetime import date
import matplotlib
matplotlib.use('Agg')
import matplotlib.animation as animation
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import random as rnd


GREY = '#E0E0E0'
YELLOW = 'Yellow'
TITLE = 'Website of Louis Byron-Brown'

class Sudoku():
    a = 3
    c = range(1, 1 + a * a)
    n = len(c) * len(c)
    c =[str(i) for i in c]
    empty = '0'
    path = 'data/'
    """
    def __init__(self, file1, n):
        self.ans = []
        #self.rp = rp
        self.stop = False
        file1 = Sudoku.path + file1
        self.grid = open(file1).read().split('Grid')[1:]
        l = len(self.grid) - 1
        rnd = randint(1, l)
        self.grid = self.grid[n]
        self.grid = self.grid.split('\n')[1:len(Sudoku.c) + 1]
        self.grid = [list(i) for i in self.grid]
        self.solve(self.grid, 0)
    """
    def __init__(self, file1, rp):
        self.ans = []
        self.rp = rp
        self.stop = False
        file1 = Sudoku.path + file1
        self.grid = open(file1).read().split('Grid')[1:]
        l = len(self.grid) - 1
        rnd = randint(1, l)
        self.grid = self.grid[rnd]
        self.grid = self.grid.split('\n')[1:len(Sudoku.c) + 1]
        self.grid = [list(i) for i in self.grid]
        self.solve(self.grid, 0)            
 
    def show(self):
        ans = """
        <div class=sudoku>
        <b>Input:</b>
        {}<p>
        </div>
        <div class=sudoku>
        <b>Output:</b>
        {}</div>
        <div>"""\
        .format(self.display(self.grid), self.display(self.ans))
        return ans

    def solve(self, grid, n):
        # solve using recursion
        x = n % (Sudoku.a * Sudoku.a)
        y = n / (Sudoku.a * Sudoku.a)
        if self.stop == True: 
            pass
        elif n == Sudoku.n:
            self.stop = True
            self.ans = grid
        elif grid[y][x] != Sudoku.empty:
            # if cell is occupied, advance to next one
            self.solve(grid, n + 1)
        else:
            l = self.drat(grid, y, x)
            for i in l:
                grid2 = deepcopy(grid)
                grid2[y][x] = str(i)
                self.solve(grid2, n + 1)
    
    def drat(self, grid, y, x):
        # calculate possible candidates for a cell
        xx = (x / Sudoku.a) * Sudoku.a
        yy = (y / Sudoku.a) * Sudoku.a
        row = list(grid[y])
        col = [i[x] for i in grid]
        box = [grid[i][j] for i in range(yy, yy + Sudoku.a) for j in range(xx, xx + Sudoku.a)]
        l = set(row + col + box)
        return set(Sudoku.c) - l
    
    def display(self, grid):
        g1 = deepcopy(grid)
        g2 = deepcopy(grid)
        a = Sudoku.a
        tag = 'style=background-color:'
        tag = tag + GREY, tag + ''
        ans = '<table>'
        for i, i2 in enumerate(g2):
            for j, j2 in enumerate(i2):
                if g2[i][j] == Sudoku.empty:
                    g2[i][j] = '_'
                t1, t2 = j / a == 1, i / a == 1
                if (t1 or t2) and not (t1 and t2): 
                    tmp = tag[0]
                else:
                    tmp = tag[1]
                g2[i][j] = '<td {}>{}</td>'.format(tmp, g2[i][j])
            ans += '<tr>{}</tr>'.format(''.join([str(ii) for ii in i2]))
        return '{}</table>'.format(ans)
    
    def test(self, ans, msg, n):
        #global ans
        print ans, msg
        if n == 0:
            pass
            #return ans, msg
        else:
            for i in range(3):
                msg2 = msg[:] + [i]
                return test(ans, msg2, n - 1)

#################### end of classes #########################################
app = Flask(__name__)   
app.secret_key = 'W178bYGrRMQbHidSWmNtXMAr'
BR = '<br>'
P = '<p>'
RESET = 5

######################## sudoku ##############################################
@app.route('/6')
def index6():
    rp = request.path
    s = Sudoku('sudoku.txt', rp)
    outpt = """
    <li>Click <a href={}>[reset]</a> to randomise the input</li><br>
    <li>To solve Sudoku, I used a brute-force algorithm that keeps
    testing possible solutions until it finds the correct one</li><br>
    """.format(rp)
    outpt += s.show()
    return render_template('index.html', title=TITLE, outpt=outpt)

#################### default: index page #####################################
@app.route('/')
def index0():
    outpt = """
    <img src=../static/python2.png>
    <a href=6>Sudoku</a>   
    """
    return render_template('index.html', mascot=False, title=TITLE, outpt=outpt)

#################### Main ####################################################
if __name__ == "__main__":
    if len(sys.argv) == 1:
        app.run()
    else:
        pass
