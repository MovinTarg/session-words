# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from time import strftime

# Create your views here.
def index(req):
    if 'wordLog' not in req.session:
        req.session['wordLog'] = []
    context = {
        'wordLog': req.session['wordLog'],
    }
    return render(req, 'session_words/index.html', context)

def addWord(req):

    form = req.POST
    req.session['word'] = form.get('word')
    req.session['color'] = form.get('color')
    req.session['time'] = strftime("%Y-%m-%d %H:%M %p")
    if 'size' in form:
        req.session['size'] = 'big'
    else:
        req.session['size'] = ''
    
    context = {
        'word': req.session['word'],
        'color': req.session['color'],
        'size': req.session['size'],
        "time": strftime("%Y-%m-%d %H:%M %p"),
    }
    print context
    req.session['wordLog'].append(context)
    print req.session['wordLog']

    return redirect('/')

def clear(req):
    req.session['wordLog'] = []
    return redirect('/')