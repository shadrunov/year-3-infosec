hashcat -m 3000 -a 3 --outfile lm_alex.out --potfile-path=lm_alex.pot lm_alex.txt
hashcat -m 3000 -a 3  -i --outfile lm_alex.out --potfile-path=lm_alex.pot1 D150630C44CEB678AAD3B435B51404EE ?a?a?a?a?a?a?a
hashcat -m 3000 -a 3 --keep-guessing --outfile lm_alex.out --potfile-path=lm_alex.pot1 875FBACE27462DB2AAD3B435B51404EE ?a?a?a?a?a
hashcat -m 3000 -a 3 --keep-guessing --outfile lm_alex.out --potfile-path=lm_alex.pot1 B267DF22CB945E3EAAD3B435B51404EE ?a?a?a?a?a?a
hashcat -m 3000 -a 3 --keep-guessing --outfile lm_alex.out --potfile-path=lm_alex.pot1 B267DF22CB945E3EAAD3B435B51404EE ?l?l?l?l?l?l

hashcat -m 3000 -a 3 --keep-guessing --outfile lm_alex.out --potfile-path=lm_alex.pot --outfile-format=1,2,3,4,5,6 lm_alex.txt ?a?a?a?a?a
hashcat -m 3000 -a 3 -i --outfile lm_alex.out --potfile-path=lm_alex.pot --outfile-format=1,2,3,4,5,6 lm_alex.txt ?a?a?a?a?a?a?a
