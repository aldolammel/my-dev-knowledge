

PROGRAMMING CONCEPTS > PASSWORDS: HOW TO STORAGE PASSWORD SAFETY


    >> Early 90's - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        Passwords were stored as plaintext, then they were too easy to be retrieved by database accesses.

        >> Solution:
            With "Hash algorithm" like "md5", it created a mask to storage passwords without to show the password characters.

            E.g.
                ./password-1-90s-hash.png
                
                Pwd:                  Hash func:          Hash:
                "pass123"     ->      md5(pwd)     ->     32250170a0dca92d53ec9624f336ca24
    

    
    >> Late 90's - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        
        Passwords converted to hash were still easy to figure them out, doing loops to comparing known hashes with those already in the database. 
        
        As MD5 and SHA-1 are super fast hash functions, using brute force attack, hashed passwords can be tested by billions per second, unfortunately.

        >> Solution:
            Make the checking loop hard for crackers, appending a "salt" not-secret-string to this password hash, forcing it to have a unknown final hash and make it impossible to be compared with cracker's most used password databases.

            E.g.
                ./password-2-90s-hash-salt.png

                salt = "aRandomStringToAddAsPwdSuffix"

                Pwd:                 Hash func + salt:           Hash:
                "pass123"     ->     md5(pwd . salt)     ->      5dabc7b296808978d06c2e3c40a008d6

            

    >> Late 2000's - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        
        Encrypted passwords introduced the 'CPU hard' concept once simple loops were not efficient to find out the most common password hashes equivalents. 
        
        As multi-core CPUs work in parallel, crackers kept breaking the password secure, testing millions of hashes per second, unfortunately. 

        >> Solution:
            Force the decryption to be slow, make not possible to check too much passwords per second as in the past using CPU multi-core-parallelism. The 'secret' of this solution is to include in the calc a CPU 'cost' multiplier to force CPU cores get busy during the password reading.

            E.g.
                ./password-3-2000s-bcrypt.png
                ./password-4-2000s-bcrypt-detail.png

        Pwd:            Hash func:            Hash:
        "pass123"  ->   bcrypt(pwd)    ->     $2a
                                              $12
                                              $oX0lTMOuJa0cfbj4e92Btei2mzw7zFRHarmsBiLHR242JQG8vCcgi



    >> Mid 2010's - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        
        bcrypt and PBKDF2 brought CPU hard cost to avoid crackers to test too much hashes per second, even using multi-core-parallelism.

        But with modern GPUs with thousands of nano-cores specialized for calculations, crackers can have GPU farms with millions of cores available to test billions of hashes again.

        >> Solution:
            Once GPUs has limited VRAM each one, the solution is to force not only multi-core CPUs and GPUs to calc slowly, but force GPU VRAM to be completely load if multiple password hashes are tested at once.

            Basically, the new solution force the hash test stay around 3 tests by GPU per second.

            E.g.
                ./password-5-2010s-argon.png
                ./password-6-2010s-argon-detail.png

                Pwd:            Hash func:          Hash:
                "pass123"  ->   argon2(pwd)    ->   $argon2i
                                                    $v=19
                                                    $m=64,t=3,p=4
                                                    $YVJhbmRvbVN0cmluZ1RvQWRkQXNQd2RTdWZmaXg
                                                    $Z6sv5rzK+GmYNkEBWaqknw

