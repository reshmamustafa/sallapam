# -*- coding: utf_8 -*-
from nltk import sent_tokenize
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import re
f1 = open('/home/reshma/Desktop/travelbot/data/Malayalam_Tourism_TextCorpus_Sample/Malayalam_Tourism_Monolingual_TextCorpus_Samples.txt')
cnt = f1.read()
#cnt = 'നിയമസഭാ തിരഞ്ഞെടുപ്പ് ഫലപ്രഖ്യാപനത്തിന് ശേഷം ത്രിപുരയിലുണ്ടായ ആക്രമണത്തില്‍ . പ്രതിഷേധിച്ച് സിപിഎം തിരഞ്ഞെടുപ്പ് ബഹിഷ്‌ക്കരിച്ചിരുന്നു.'
#cnt = 'സീമ ഒരു മണ്ടിയാണ്. സീമക്ക് എന്നോട് സ്നേഹമില്ല. പഴയ പോലെ അല്ല സീമ. വെറും ഉഡായിപ്പ് ആണ്.'
#snt = sent_tokenize(cnt)
c=re.split('\.\s|\?\s',cnt)
for i in c:
	print i
	print "\n"