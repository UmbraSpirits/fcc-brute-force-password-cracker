import hashlib


def crack_sha1_hash(hash, use_salts=False):
    with open('top-10000-passwords.txt', 'r') as file1:
        passwords = [line.strip() for line in file1]

    with open('known-salts.txt', 'r') as file2:
        salts = [line.strip() for line in file2]

    for item in passwords:
        testcase = item
        if use_salts == True:
            for y in salts:
                testcase = item + y
                code = bytes(testcase, encoding='utf-8')
                hashedpassword = hashlib.sha1(code).hexdigest()
                if hashedpassword == hash:
                    return item
                testcase = y + item
                code = bytes(testcase, encoding='utf-8')
                hashedpassword = hashlib.sha1(code).hexdigest()
                if hashedpassword == hash:
                    return item
        else:
            code = bytes(testcase, encoding='utf-8')
            hashedpassword = hashlib.sha1(code).hexdigest()
            if hashedpassword == hash:
                return item
    return "PASSWORD NOT IN DATABASE"
