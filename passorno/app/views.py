from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import FileForm
from django.urls import path
from . import views
from django.shortcuts import render
from .models import DocFile
import os
from passorno.settings import BASE_DIR
import json
from timeit import timeit
import re
import itertools
import hashlib
import hmac
import base64
import array
from sklearn.utils.extmath import cartesian
import numpy as np
from collections import Iterable
from numpy import empty, uint8
from math import factorial

# Create your views here.
def index(request):
    # TODO
    # get it from db
    
    thisFile=DocFile.objects.latest('id').filepath
    thisFileName=DocFile.objects.latest('id').filename
    data_file = open(os.path.abspath(os.path.dirname(__name__)) + thisFile, 'r')

    data = data_file.readlines()

    dict = {}
    for entry in data:
        temp = entry.split(',')
        dict[temp[0]]=temp[1]

    return render(request, "index.html",
    {
        'filename': thisFileName,
        'content': dict

    })



def fileupload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            newDoc = DocFile(file=request.FILES['file'])
            newDoc.filename = newDoc.file.name
            newDoc.filepath = newDoc.file.url
                        
            newDoc.save()
            
            return render(request, "index.html",{'a': 'b'})
    else:
        form = FileForm()
        return render(request, 'fileupload.html', {            
            'form': form
        })

def contententry(request):
    if request.method == "POST":
        body = request.body
        body=json.loads(request.body)

        
    return render(request, "index.html", {
        "blog": Blog.objects.all(),
        "test": request.body
    })

def results(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        
        # get params
        body = request.body
        body=json.loads(request.body)
        
        # perform calc
        separator = body["separator"]
        includenumbers = body["includenumbers"]
        includesmalls = body["includesmalls"]
        includefirstcap = body["includefirstcap"]
        includecaps = body["includecaps"]
        passlength = body["passlength"]        

        thisFile=DocFile.objects.latest('id').filepath
        thisFileName=DocFile.objects.latest('id').filename
        data_file = open(os.path.abspath(os.path.dirname(__name__)) + thisFile, 'r')

        data = data_file.read()
        
        # generate passwords
        test = '0123456789'
        test2 = 'abcdefghijklmnopqrstuvwxyz'
        test3 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        test4 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        test5 = 'abcdefghijklmnopqrstuvwxyz0123456789'
        #combs = itertools.product(test, repeat=4)
        #combs = itertools.permutations(test5, 5)
        set1 = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
        set2 = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
        set3 = (0,1,"a")
        #combs = cartesian([set2, set2, set2,set2,set2,set2])
        #y = [''.join(i) for i in combs]
        #combs = thisProduct(*{'ab','BA'})
        # convert to HMACSHA1
        # Test
        #z= makehash("1234", "1234")

        #combs = thisPerm(test, passlength)

        #dict = {}
        # for x in combs:
        #     if  x in data:
        #         dict[x] = x

        # for x in combs:
        #     dict[x] = makehash(x,x)
        
          
        #aaa =@ generate_permutations(test5, 8)
        return render(request, "results.html",{'a':gen_window_product()})
    else:
        # return result
        return render(request, "results.html",{'a': 'b'})


def best_find(string, text):
    if text in string:
       return "aaaa"
    else:
        return "bbb"

def makehash(password, key):
    
    p2 = password.encode('utf-16-le')
    # Case key is the password so save one operation and use pass
    k2 = key.encode('utf-16-le')
    #hash = hmac.new(p2, k2, hashlib.sha1).digest()
    hash = hmac.new(p2, p2, hashlib.sha1).digest()
    return base64.b64encode(hash).decode()

def generate_permutations(s, n, prefix=""):
    if n == 0:
        return [prefix]
    perms = []
    data = loadData()
    for i in range(len(s)):
        thisPerm = generate_permutations(s[:i] + s[i+1:], n-1, prefix+s[i])        
        perms.extend(thisPerm)
        for j in thisPerm:
            thisHash = makehash(j, j)
            if thisHash in data:
                dict[j]=thisHash
    return perms
    

def loadData():
    thisFile=DocFile.objects.latest('id').filepath
    thisFileName=DocFile.objects.latest('id').filename
    data_file = open(os.path.abspath(os.path.dirname(__name__)) + thisFile, 'r')

    return data_file.read()

def gen_window_product():

    test = '0123456789'
    test2 = 'abcdefghijklmnopqrstuvwxyz'
    test3 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    test4 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    test5 = 'abcdefghijklmnopqrstuvwxyz0123456789'
    test6 = '!@#$%&'
    f = open("myfile.txt", "w")
    data = loadData()
    # generate cartesian product for 4 small letters with repeat=2
    pr = generate_permutations(test2,4)
    endlist = []
    #First capital letter
    for i in test3:
        for j in pr:
            for k in test:
                for l in test:
                    for m in test6:
                        theHash = makehash(i+j+k+l+m, i+j+k+l+m)
                        if theHash in data:
                            f.write(i+j+k+l+m +"\n"+": "+theHash)
                            endlist.append(i+j+k+l+m)

    return endlist

dict = {}


