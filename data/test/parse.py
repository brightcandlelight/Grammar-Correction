import re, sys
import sentencepiece as spm
sp = spm.SentencePieceProcessor()
sp.Load("../../../sentencepiece/python/test/test_model.model")



with open(sys.argv[1], "r") as ins:
    for sentence in ins:
        a = sp.EncodeAsPieces(sentence)
        newSentence = ""
        for i in a:
            i = re.sub("[^\s\w\d\?><;,.\{\}\[\]\-_\+=!@\#\$%^&\*\|\'\\\"\(\):\/`~]", "", i)
            newSentence = newSentence+" "+i
        newSentence=newSentence.strip()
        
        aa = re.findall("<[a-zA-Z \/]*>", newSentence)
        for i in aa:
            j = re.sub(" ", "", i)
            newSentence = re.sub(i, j, newSentence)
        newSentence=re.sub("  +", " ", newSentence)

        print(newSentence)