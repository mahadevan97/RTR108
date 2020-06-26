{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "chuck\n",
      "chuck\n",
      "chuck\n"
     ]
    }
   ],
   "source": [
    "stuff = list()\n",
    "stuff.append('python')\n",
    "stuff.append('chuck')\n",
    "stuff.sort()\n",
    "print (stuff[0])\n",
    "print (stuff.__getitem__(0))\n",
    "print (list.__getitem__(stuff,0))\n",
    "\n",
    "# Code: http://www.py4e.com/code3/party1.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "chuck\n"
     ]
    }
   ],
   "source": [
    "print (stuff.__getitem__(0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "chuck\n"
     ]
    }
   ],
   "source": [
    "print (list.__getitem__(stuff,0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__add__',\n",
       " '__class__',\n",
       " '__contains__',\n",
       " '__delattr__',\n",
       " '__delitem__',\n",
       " '__dir__',\n",
       " '__doc__',\n",
       " '__eq__',\n",
       " '__format__',\n",
       " '__ge__',\n",
       " '__getattribute__',\n",
       " '__getitem__',\n",
       " '__gt__',\n",
       " '__hash__',\n",
       " '__iadd__',\n",
       " '__imul__',\n",
       " '__init__',\n",
       " '__iter__',\n",
       " '__le__',\n",
       " '__len__',\n",
       " '__lt__',\n",
       " '__mul__',\n",
       " '__ne__',\n",
       " '__new__',\n",
       " '__reduce__',\n",
       " '__reduce_ex__',\n",
       " '__repr__',\n",
       " '__reversed__',\n",
       " '__rmul__',\n",
       " '__setattr__',\n",
       " '__setitem__',\n",
       " '__sizeof__',\n",
       " '__str__',\n",
       " '__subclasshook__',\n",
       " 'append',\n",
       " 'clear',\n",
       " 'copy',\n",
       " 'count',\n",
       " 'extend',\n",
       " 'index',\n",
       " 'insert',\n",
       " 'pop',\n",
       " 'remove',\n",
       " 'reverse',\n",
       " 'sort']"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    ">>> stuff = list()\n",
    ">>> dir(stuff)\n",
    "['__add__', '__class__', '__contains__', '__delattr__',\n",
    "'__delitem__', '__dir__', '__doc__', '__eq__',\n",
    "'__format__', '__ge__', '__getattribute__', '__getitem__',\n",
    "'__gt__', '__hash__', '__iadd__', '__imul__', '__init__',\n",
    "'__iter__', '__le__', '__len__', '__lt__', '__mul__',\n",
    "'__ne__', '__new__', '__reduce__', '__reduce_ex__',\n",
    "'__repr__', '__reversed__', '__rmul__', '__setattr__',\n",
    "'__setitem__', '__sizeof__', '__str__', '__subclasshook__',\n",
    "'append', 'clear', 'copy', 'count', 'extend', 'index',\n",
    "'insert', 'pop', 'remove', 'reverse', 'sort']\n",
    ">>>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the US Floor Number: 4\n",
      "Non-US Floor Number is 3\n"
     ]
    }
   ],
   "source": [
    "usf = input('Enter the US Floor Number: ')\n",
    "wf = int(usf) - 1\n",
    "print('Non-US Floor Number is',wf)\n",
    "\n",
    "# Code: http://www.py4e.com/code3/elev.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter - 1\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "unknown url type: '1'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-6-62896733c664>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m \u001b[0murl\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Enter - '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 15\u001b[1;33m \u001b[0mhtml\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0murllib\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mctx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     16\u001b[0m \u001b[0msoup\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mBeautifulSoup\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhtml\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'html.parser'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     17\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\urllib\\request.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(url, data, timeout, cafile, capath, cadefault, context)\u001b[0m\n\u001b[0;32m    220\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    221\u001b[0m         \u001b[0mopener\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_opener\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 222\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0mopener\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    223\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    224\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0minstall_opener\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mopener\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\urllib\\request.py\u001b[0m in \u001b[0;36mopen\u001b[1;34m(self, fullurl, data, timeout)\u001b[0m\n\u001b[0;32m    508\u001b[0m         \u001b[1;31m# accept a URL or a Request object\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    509\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfullurl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 510\u001b[1;33m             \u001b[0mreq\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mRequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfullurl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    511\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    512\u001b[0m             \u001b[0mreq\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfullurl\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\urllib\\request.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, url, data, headers, origin_req_host, unverifiable, method)\u001b[0m\n\u001b[0;32m    326\u001b[0m                  \u001b[0morigin_req_host\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0munverifiable\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mFalse\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    327\u001b[0m                  method=None):\n\u001b[1;32m--> 328\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfull_url\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    329\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mheaders\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    330\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0munredirected_hdrs\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\urllib\\request.py\u001b[0m in \u001b[0;36mfull_url\u001b[1;34m(self, url)\u001b[0m\n\u001b[0;32m    352\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_full_url\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0munwrap\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    353\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_full_url\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfragment\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msplittag\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_full_url\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 354\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parse\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    355\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    356\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0mfull_url\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdeleter\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\urllib\\request.py\u001b[0m in \u001b[0;36m_parse\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    381\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtype\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrest\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msplittype\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_full_url\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    382\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtype\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 383\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"unknown url type: %r\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfull_url\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    384\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhost\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mselector\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msplithost\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mrest\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    385\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhost\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: unknown url type: '1'"
     ]
    }
   ],
   "source": [
    "# To run this, download the BeautifulSoup zip file\n",
    "# http://www.py4e.com/code3/bs4.zip\n",
    "# and unzip it in the same directory as this file\n",
    "\n",
    "import urllib.request, urllib.parse, urllib.error\n",
    "from bs4 import BeautifulSoup\n",
    "import ssl\n",
    "\n",
    "# Ignore SSL certificate errors\n",
    "ctx = ssl.create_default_context()\n",
    "ctx.check_hostname = False\n",
    "ctx.verify_mode = ssl.CERT_NONE\n",
    "\n",
    "url = input('Enter - ')\n",
    "html = urllib.request.urlopen(url, context=ctx).read()\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "# Retrieve all of the anchor tags\n",
    "tags = soup('a')\n",
    "for tag in tags:\n",
    "    print(tag.get('href', None))\n",
    "\n",
    "# Code: http://www.py4e.com/code3/urllinks.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter - http://www.py4e.com/code3/urllinks.py\n"
     ]
    },
    {
     "ename": "HTTPError",
     "evalue": "HTTP Error 403: Forbidden",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mHTTPError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-7-62896733c664>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m \u001b[0murl\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Enter - '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 15\u001b[1;33m \u001b[0mhtml\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0murllib\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mctx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     16\u001b[0m \u001b[0msoup\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mBeautifulSoup\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhtml\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'html.parser'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     17\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\urllib\\request.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(url, data, timeout, cafile, capath, cadefault, context)\u001b[0m\n\u001b[0;32m    220\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    221\u001b[0m         \u001b[0mopener\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_opener\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 222\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0mopener\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    223\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    224\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0minstall_opener\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mopener\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\urllib\\request.py\u001b[0m in \u001b[0;36mopen\u001b[1;34m(self, fullurl, data, timeout)\u001b[0m\n\u001b[0;32m    529\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mprocessor\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprocess_response\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mprotocol\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    530\u001b[0m             \u001b[0mmeth\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mprocessor\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmeth_name\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 531\u001b[1;33m             \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmeth\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    532\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    533\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\urllib\\request.py\u001b[0m in \u001b[0;36mhttp_response\u001b[1;34m(self, request, response)\u001b[0m\n\u001b[0;32m    639\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m200\u001b[0m \u001b[1;33m<=\u001b[0m \u001b[0mcode\u001b[0m \u001b[1;33m<\u001b[0m \u001b[1;36m300\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    640\u001b[0m             response = self.parent.error(\n\u001b[1;32m--> 641\u001b[1;33m                 'http', request, response, code, msg, hdrs)\n\u001b[0m\u001b[0;32m    642\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    643\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\urllib\\request.py\u001b[0m in \u001b[0;36merror\u001b[1;34m(self, proto, *args)\u001b[0m\n\u001b[0;32m    567\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mhttp_err\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    568\u001b[0m             \u001b[0margs\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mdict\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'default'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'http_error_default'\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0morig_args\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 569\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_call_chain\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    570\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    571\u001b[0m \u001b[1;31m# XXX probably also want an abstract factory that knows when it makes\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\urllib\\request.py\u001b[0m in \u001b[0;36m_call_chain\u001b[1;34m(self, chain, kind, meth_name, *args)\u001b[0m\n\u001b[0;32m    501\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mhandler\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mhandlers\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    502\u001b[0m             \u001b[0mfunc\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhandler\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmeth_name\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 503\u001b[1;33m             \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    504\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mresult\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    505\u001b[0m                 \u001b[1;32mreturn\u001b[0m \u001b[0mresult\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\urllib\\request.py\u001b[0m in \u001b[0;36mhttp_error_default\u001b[1;34m(self, req, fp, code, msg, hdrs)\u001b[0m\n\u001b[0;32m    647\u001b[0m \u001b[1;32mclass\u001b[0m \u001b[0mHTTPDefaultErrorHandler\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mBaseHandler\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    648\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mhttp_error_default\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mreq\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfp\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcode\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mhdrs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 649\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0mHTTPError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfull_url\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcode\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mhdrs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfp\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    650\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    651\u001b[0m \u001b[1;32mclass\u001b[0m \u001b[0mHTTPRedirectHandler\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mBaseHandler\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mHTTPError\u001b[0m: HTTP Error 403: Forbidden"
     ]
    }
   ],
   "source": [
    "# To run this, download the BeautifulSoup zip file\n",
    "# http://www.py4e.com/code3/bs4.zip\n",
    "# and unzip it in the same directory as this file\n",
    "\n",
    "import urllib.request, urllib.parse, urllib.error\n",
    "from bs4 import BeautifulSoup\n",
    "import ssl\n",
    "\n",
    "# Ignore SSL certificate errors\n",
    "ctx = ssl.create_default_context()\n",
    "ctx.check_hostname = False\n",
    "ctx.verify_mode = ssl.CERT_NONE\n",
    "\n",
    "url = input('Enter - ')\n",
    "html = urllib.request.urlopen(url, context=ctx).read()\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "# Retrieve all of the anchor tags\n",
    "tags = soup('a')\n",
    "for tag in tags:\n",
    "    print(tag.get('href', None))\n",
    "\n",
    "# Code: http://www.py4e.com/code3/urllinks.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "So far 1\n",
      "So far 2\n",
      "So far 3\n",
      "So far 4\n"
     ]
    }
   ],
   "source": [
    "class PartyAnimal:\n",
    "   x = 0\n",
    "\n",
    "   def party(self) :\n",
    "     self.x = self.x + 1\n",
    "     print(\"So far\",self.x)\n",
    "\n",
    "an = PartyAnimal()\n",
    "an.party()\n",
    "an.party()\n",
    "an.party()\n",
    "PartyAnimal.party(an)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I am constructed\n",
      "So far 1\n",
      "So far 2\n",
      "I am destructed 2\n",
      "an contains 42\n"
     ]
    }
   ],
   "source": [
    "class PartyAnimal:\n",
    "   x = 0\n",
    "\n",
    "   def __init__(self):\n",
    "     print('I am constructed')\n",
    "\n",
    "   def party(self) :\n",
    "     self.x = self.x + 1\n",
    "     print('So far',self.x)\n",
    "\n",
    "   def __del__(self):\n",
    "     print('I am destructed', self.x)\n",
    "\n",
    "an = PartyAnimal()\n",
    "an.party()\n",
    "an.party()\n",
    "an = 42\n",
    "print('an contains',an)\n",
    "\n",
    "# Code: http://www.py4e.com/code3/party4.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sally constructed\n",
      "Jim constructed\n",
      "Sally party count 1\n",
      "Jim party count 1\n",
      "Sally party count 2\n"
     ]
    }
   ],
   "source": [
    "class PartyAnimal:\n",
    "   x = 0\n",
    "   name = ''\n",
    "   def __init__(self, nam):\n",
    "     self.name = nam\n",
    "     print(self.name,'constructed')\n",
    "\n",
    "   def party(self) :\n",
    "     self.x = self.x + 1\n",
    "     print(self.name,'party count',self.x)\n",
    "\n",
    "s = PartyAnimal('Sally')\n",
    "j = PartyAnimal('Jim')\n",
    "\n",
    "s.party()\n",
    "j.party()\n",
    "s.party()\n",
    "\n",
    "# Code: http://www.py4e.com/code3/party5.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'party'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-11-8bf6d40ff449>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mparty\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mPartyAnimal\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mclass\u001b[0m \u001b[0mCricketFan\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mPartyAnimal\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m    \u001b[0mpoints\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m    \u001b[1;32mdef\u001b[0m \u001b[0msix\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'party'"
     ]
    }
   ],
   "source": [
    "from party import PartyAnimal\n",
    "\n",
    "class CricketFan(PartyAnimal):\n",
    "   points = 0\n",
    "   def six(self):\n",
    "      self.points = self.points + 6\n",
    "      self.party()\n",
    "      print(self.name,\"points\",self.points)\n",
    "\n",
    "s = PartyAnimal(\"Sally\")\n",
    "s.party()\n",
    "j = CricketFan(\"Jim\")\n",
    "j.party()\n",
    "j.six()\n",
    "print(dir(j))\n",
    "\n",
    "# Code: http://www.py4e.com/code3/party6.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sally constructed\n"
     ]
    }
   ],
   "source": [
    "s = PartyAnimal('Sally')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'nam' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-13-f7a1fced79aa>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mname\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnam\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'nam' is not defined"
     ]
    }
   ],
   "source": [
    "self.name = nam"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'party'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-14-8bf6d40ff449>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mparty\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mPartyAnimal\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mclass\u001b[0m \u001b[0mCricketFan\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mPartyAnimal\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m    \u001b[0mpoints\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m    \u001b[1;32mdef\u001b[0m \u001b[0msix\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'party'"
     ]
    }
   ],
   "source": [
    "from party import PartyAnimal\n",
    "\n",
    "class CricketFan(PartyAnimal):\n",
    "   points = 0\n",
    "   def six(self):\n",
    "      self.points = self.points + 6\n",
    "      self.party()\n",
    "      print(self.name,\"points\",self.points)\n",
    "\n",
    "s = PartyAnimal(\"Sally\")\n",
    "s.party()\n",
    "j = CricketFan(\"Jim\")\n",
    "j.party()\n",
    "j.six()\n",
    "print(dir(j))\n",
    "\n",
    "# Code: http://www.py4e.com/code3/party6.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
