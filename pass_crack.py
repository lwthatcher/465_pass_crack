import crypt
import random
import string
import argparse

def getsalt():
    chars = (string.ascii_letters + string.digits)
    # generate a random 2-character 'salt'
    return random.choice(chars) + random.choice(chars) + random.choice(chars) + random.choice(chars) + random.choice(chars) + random.choice(chars) + random.choice(chars) + random.choice(chars)
def getcrypt(_password, _salt):
    result = crypt.crypt(_password, _salt)
    return result

def getuser():
    return 'user'+str(user_id)

def uid():
    return str(user_id+1)

def group():
    return '1'+uid().rjust(3, '0')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('password')
    parser.add_argument('user_id', default=1,type=int)
    args = parser.parse_args()
    user_id = args.user_id
    user = getuser()
    password = args.password
    salt = getsalt()
    encrypted_password = getcrypt(password, salt)
    print(user)
    with open('etc/passwd', 'a') as f:
        print(user+':x:'+uid()+':'+group()+':GECOS:directory:shell'+uid(), file=f)
    
    with open('etc/shadow', 'a') as f:
        print(user+':$1$'+salt+'$'+encrypted_password+':14538:0:99999:7:::', file=f)

