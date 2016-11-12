import random, string, hashlib, hmac

#Helper functions for hashing and cookies

#Hashing
def make_salt():
    sal = ""
    for i in range(0,5):
        sal += random.choice(string.letters)
    return sal

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()

    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
    salt = h.split(',')[1]
    return h == make_pw_hash(name, pw, salt)

#Hashing cookies
SECRET = 'czUv86iAN9GXA3MTUYHJDQ039TRYWPZ89UITHGAL3TYGZROUIQRA9W8EITUGYqiuGTLU3QYPQyp92ijr3qILYEGUautiuwkGYQRFO)&Q73YO2IATUWGUoizjupoyups94uyap4oiw'
def hash_str(s):
    return hmac.new(SECRET,s).hexdigest()

def make_secure_val(s):
    return '%s|%s' % (s, hash_str(s))

def check_secure_val(h):
    s = h.split('|')[0]
    if h == make_secure_val(s):
        return s
