from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile



strings = "abcdefghijklmnopqrstuvwxyz0123456789"
base = 99999  # don't change this


class Kyrie():

    def encrypt(e: str):
        e = Kyrie._ekyrie(e)
        return Kyrie._encrypt(e)

    def decrypt(e: str):
        text = Kyrie._decrypt(e)
        return Kyrie._dkyrie(text)

    def _ekyrie(text: str):

        r = ""
        for a in text:
            if a in strings:
                a = strings[strings.index(a)-1]
            r += a
        return r

    def _dkyrie(text: str):
        r = ""
        for a in text:
            if a in strings:
                i = strings.index(a)+1
                if i >= len(strings):
                    i = 0
                a = strings[i]
            r += a
        return r

    def _encrypt(text: str, key: str = None):
        if key is None:
            key = base
        if type(key) == str:
            key = sum(ord(i) for i in key)
        t = [chr(ord(t)+key)if t != "\n" else "ζ" for t in text]
        return "".join(t)

    def _decrypt(text: str, key: str = None):
        if key is None:
            key = base
        if type(key) == str:
            key = sum(ord(i) for i in key)
        return "".join(chr(ord(t)-key) if t != "ζ" else "\n" for t in text)


class Key:

    def encrypt(e: str, key: str):
        e1 = Kyrie._ekyrie(e)
        return Kyrie._encrypt(e1, key=key)

    def decrypt(e: str, key: str):
        text = Kyrie._decrypt(e, key=key)
        return Kyrie._dkyrie(text)




def Nuclear(content: str, key: int) -> str:

    _content_ = Key.encrypt(content, key=key)

    _lines_sep_, _spaces_sep_ = choice(list("~|-/=")), choice(list("¤§^*¨"))



    _hey_num_ = randint(69, 356)
    _hey_num_ = len(content)

    content = _lines_sep_.join(str(ord(x)+_hey_num_) if x != 'ζ' else _spaces_sep_ for x in _content_)

    _names_ = ["_eval", "_exec", "_byte", "_bytes", "_bit", "_bits", "_system", "_encode", "_decode", "_delete", "_exit", "_rasputin", "_boom"]
    _names_ = ["self." + name for name in _names_]
    shuffle(_names_)

    for k in range(12):
        globals()[f'n_{str(k+1)}'] = _names_[k]

    _ran_int_ = _hey_num_
    while _ran_int_ == _hey_num_:
        _ran_int_ = str(randint(69, 356))
    

    _types_ = ("str","float","bool","int")

    def _find(chars: str): return "+".join(f"_n7_[{list('abcdefghijklmnopqrstuvwxyz0123456789').index(c)}]" for c in chars)

    _1_ = fr"""_n5_""",fr"""lambda _n9_:"".join(chr(int(_n10_)-len(_n9_.split('{_lines_sep_}')))if _n10_!='{_spaces_sep_}'else'ζ'for _n10_ in str(_n9_).split('{_lines_sep_}'))"""
    _2_ = fr"""_n6_""",r"""lambda _n1_:str(_n4_[_n2_](f"{_n7_[4]+_n7_[-13]+_n7_[4]+_n7_[2]}(''.join(%s),{_n7_[6]+_n7_[11]+_n7_[14]+_n7_[1]+_n7_[0]+_n7_[11]+_n7_[18]}())"%list(_n1_))).encode(_n7_[20]+_n7_[19]+_n7_[5]+_n7_[34])if _n4_[_n2_]==eval else exit()"""
    _3_ = fr"""_n4_[_n2_]""",fr"""eval"""
    _4_ = fr"""_n1_""",fr"""lambda _n1_:exit()if _n7_[15]+_n7_[17]+_n7_[8]+_n7_[13]+_n7_[19] in open(__file__, errors=_n7_[8]+_n7_[6]+_n7_[13]+_n7_[14]+_n7_[17]+_n7_[4]).read() or _n7_[8]+_n7_[13]+_n7_[15]+_n7_[20]+_n7_[19] in open(__file__, errors=_n7_[8]+_n7_[6]+_n7_[13]+_n7_[14]+_n7_[17]+_n7_[4]).read()else"".join(_n1_ if _n1_ not in _n7_ else _n7_[_n7_.index(_n1_)+1 if _n7_.index(_n1_)+1<len(_n7_)else 0]for _n1_ in "".join(chr(ord(t)-{key})if t!="ζ"else"\n"for t in _n5_(_n1_)))"""
    _5_ = fr"""_n7_""",fr"""exit()if _n1_ else'abcdefghijklmnopqrstuvwxyz0123456789'"""
    _6_ = fr"""_n8_""",fr"""lambda _n12_:_n1_(_n12_)"""
    _all_ = [_1_, _2_, _3_, _4_, _5_, _6_]
   
    shuffle(_all_)

    _vars_content_ = ",".join(s[0] for s in _all_)
    _valors_content_ = ",".join(s[1] for s in _all_)
    _vars_ = _vars_content_ + "=" + _valors_content_
    _final_content_ = fr"""class Nuclear():
 def __init__(self:object,_n1_:{choice(_types_)}=False,_n2_:{choice(_types_)}=0,*_n3_:{choice(_types_)},**_n4_:{choice(_types_)})->exec:
  {_vars_}
  return self.__decode__(_n4_[(_n7_[-1]+'_')[-1]+_n7_[18]+_n7_[15]+_n7_[0]+_n7_[17]+_n7_[10]+_n7_[11]+_n7_[4]])
 def __decode__(self,_execute: str)->exec:return(None,_n6_(_n8_(_execute)))[0]
Nuclear(_n1_=False,_sparkle='''{content}''')""".strip().replace("_n1_",n_1.removeprefix("self.")).replace("_n2_",n_2.removeprefix("self.")).replace("_n3_",n_3.removeprefix("self.")).replace("_n4_",n_4.removeprefix("self.")).replace("_n5_",n_5).replace("_n6_",n_6).replace("_n7_",n_7).replace("_n8_",n_8).replace("_n9_",n_9.removeprefix("self.")).replace("_n10_",n_10.removeprefix("self.")).replace("_n12_",n_12.removeprefix("self."))
    return _final_content_



System.Clear()
System.Title("Nuclear Obfuscator")
System.Size(140, 40)


graphics = """
                         __    _
                    _wr""        "-q__
                 _dP                 9m_
               _#P                     9#_
              d#@                       9#m
             d##                         ###
            J###                         ###L
            {###K                       J###K
            ]####K      ___aaa___      J####F
        __gmM######_  w#P""   ""9#m  _d#####Mmw__
     _g##############mZ_         __g##############m_
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_
  a###""          ,Z"#####@" '######"\g          ""M##m
 J#@"             0L  "*##     ##@"  J#              *#K
 #"               `#    "_gmwgm_~    dF               `#_
7F                 "#_   ]#####F   _dK                 JE
]                    *m__ ##### __g@"                   F
                       "PJ#####LP"
 `                       0######_                      '
                       _0########_
     .               _d#####^#####m__              ,
      "*w_________am#####P"   ~9#####mw_________w*"
          ""9@#####@M""           ""P@#####@M""


███╗   ██╗██╗   ██╗ ██████╗██╗     ███████╗ █████╗ ██████╗ 
████╗  ██║██║   ██║██╔════╝██║     ██╔════╝██╔══██╗██╔══██╗
██╔██╗ ██║██║   ██║██║     ██║     █████╗  ███████║██████╔╝
██║╚██╗██║██║   ██║██║     ██║     ██╔══╝  ██╔══██║██╔══██╗
██║ ╚████║╚██████╔╝╚██████╗███████╗███████╗██║  ██║██║  ██║
╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                           """[1:]

banner = r"""                                                                                                                                                                                                                                                                   

                    .:+sydmmmmmmmmmmmmmmmmmmh                           
               .:oyhmmmmmmmmmmmmmmmmmmmmmmmmm.                          
            :ohmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm/                          
         /ydmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmms                          
        +mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmd`                         
        `hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm:                         
         .dmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmms         -/osyyo         
          /mmmmmmmmmmmmmmmmmmmmmmmmmdhysso+/:yd`    -+yddmmmmmd`        
           ymmmmmmmmmmmmmmmmmdhyo+:-.``      :m+-/shdmmmmmmmds.         
           .dmmmmmmmmmmdhyo/-.`           `.:+mddmmmmmmmmdy+.           
            /mmmmmdhy+:.`         `..-/+syhddmmmmmmmdhyo:.`             
            `ymdy+-.    ``..-:/+syhhdmmmmmmmmmmmdyo/-.                  
   ..-:::::--/hy://++osyyhhdmmmmmmmmmmmmddhhs++m:                                                                                                                                                                                         
.ohdmmmmdddhhhhhhdddmmmdhhhhmmdddddhyso++/:.` .h:`                                                                                                      
smmmmmmhsydyhhhhydysdmdsyhhys+/::-.`  -yhshd+``/o/-`                                                                
`+yddddyshyhysoyyhhsdmdso`           `ohmdhhy`` .+s++/`                 
    `.......`  -ydysdmdys`           `/hdyhhs       -+oo+`              
               `ddhhdmmmd:             /syy+`          ./yy/`           
                ommmmmmmmh`                               .+ho.         
                .dmmmmmmmms                                 `/ys.       
                 /mmmmmmmmms`                                 `/yo`     
                  ommmmmmmmmhyyyhhhhyyysssoo+/::-.`             `oh:    
                  `ommmmmmmmmmmy-...........-::/+ooso+:-`         :h+   
                    /dmmmmmmmmmdho/:----:://++++++++++syys/-`      -ho                                                                                          
                     -mmmmmmmmmmmmmmmmmds+/:------:://++oyhhho:.    -ho 
                    `+mmmmmmmmmmmmmmmmm/                  `.-/sss/.` -d:
                   -smmmmmmmmmmmmmmmmmms`                      `./ss++ds
                 `+dmmmmmmmmmmmmmmmmmmmmh:`                        .:/:`
                `ymmmmmmmmmmmmmmmmmmmmmmmmy:`                           
                `oddmmmmmmmmmmmmmmmmmmmmmmmmy                           
                   -/oydmdmmmmmmmmmmmmmmhyo/.                           
                         ..-::::::::-..                [PLAGUE LOGO]                                                                         
"""[1:]




Anime.Fade(Center.XCenter(banner), Colors.green_to_cyan, Colorate.Vertical, enter=True)

def main():
    System.Clear()

    print("\n"*2)
    print(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter(graphics)))
    print("\n"*5)


    file = Write.Input("Put your python file here -> ", Colors.green_to_cyan, interval=0.005)

    if not file.strip() or not isfile(file):
        Colorate.Error("This file does not exist!")
        return

    print()
    key = Write.Input("Enter your encryption key (6 - 1000000) -> ", Colors.blue_to_purple, interval=0.005)
    key = randint(3, 1000001)

    try:
        key = int(key)
    except ValueError:
        Colorate.Error("Invalid key!")
        return
    if key < 3 or key > 1000000:
        Colorate.Error("Invalid key!")
        return

    content = open(file, encoding='utf-8').read()
    file = file.removesuffix(".py") + "-nuclear.py" 

    content = Nuclear(content=content, key=key)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

    print('\n')

    print(Colorate.Diagonal(Colors.green_to_blue, f"""Crypting with Kyrie Eleison...
Using key {key}...
Creatings vars
Getting vars...
Separate spaces...
Separate lines...
Crypting in ASCII...
Shufflings all vars...
Adding all vars...
Adding "-nuclear.py" name of the file...
Making the final content...
Creating...

Thanks to Berseker !
"""))

    print('\n')
    Write.Input("Well, i'm done! Thanks using NUCLEAR <3", Colors.green_to_blue, interval=0.005)
    return exit()


if __name__ == '__main__':
    while True:
        main()