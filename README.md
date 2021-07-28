# jwt-helper
JWT Helper Tool 4 Pentests.



## About


 #### Capabilities

- brute force a jwt tokens secret key
- forge a jwt token with secret key
- decrypt a jwt token with provided secret key
- generate a jwt token brute forcer list with secret key, for idor vuln.


#### Needs

- job to do: brute-force[1], forge jwt[2], decrypt jwt[3], generate jwts[4]
- sometimes the jwt token itself
- sometimes the secret key of token also
- files for bruteforce and generation


### Usage, Technically
```

python3 <thescript> <brute> <jwt_key> <wordlist> <encryption_algorithm>  --> [1] brute force --
python3 <thescript> <forge> <the_payloads> <secret_key> <encryption_algorithm>  --> [2] forge a jwt --
python3 <thescript> <decrypt> <jwt_key> <secret_key> <encryption_algorithm>  --> [3] decrypt a jwt --
python3 <thescript> <generate> <original_jwt> <secret_key> <encryption_algorithm> <parameter_to_change> <min_number> <max_number> <out_file>  --> [4] generate a jwt list w/ diffrent param values --

```

### Usage, Examples
```

python3 jwtript.py brute eyJh.eyJzdWIiOiIx.SflKxwR /usr/rockyou.txt HS256  --> [1] brute force --
python3 jwtript.py forge int:id:1,str:name:jack,bool:admin:false,flo:age:23.57,list:notes:1-2-3-abcd mysecretkey HS512  --> [2] forge a jwt --
python3 jwtript.py decrypt eyJh.eyJzdWIiOiIx.SflKxwR mymegasecretkey HS256  --> [3] decrypt a jwt --
python3 jwtript.py generate eyJh.eyJzdWIiOiIx.SflKxwR secretpass HS512 user_id 1 1234 /usr/newjwts.txt  --> [4] generate a jwt list w/ diffrent user_id values --

```

#### developed with love & py3 <3.

