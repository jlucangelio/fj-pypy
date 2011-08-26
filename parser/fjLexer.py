# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 /home/tamsyn/code/fj-llvm/parser/fj.g 2011-08-26 12:54:15

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EMPTY_NAMES=21
CLASS=13
RBRACE=10
LETTER=36
EMPTY_VARS=22
LBRACE=9
NEW=18
WHITESPACE=40
UNDERSCORE=12
SEMICOLON=6
FIELDS=26
EXPRESSIONS=35
EOF=-1
LPAREN=7
NAMES=27
DOT_EXPRESSION=34
ANY_CHAR=38
RPAREN=8
NAME=39
METHODS=31
VARIABLE=28
COMMA=5
RETURN=17
THIS=16
ASSIGN=11
EMPTY_EXPS=23
VARIABLES=29
PROGRAM=19
FIELD=25
SUPER=15
DIGIT=37
DOT=4
EXTENDS=14
INIT=24
CONSTRUCTOR=20
METHOD=30
EXPRESSION=32
BASE_EXPRESSION=33


class fjLexer(Lexer):

    grammarFileName = "/home/tamsyn/code/fj-llvm/parser/fj.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(fjLexer, self).__init__(input, state)


        self.dfa3 = self.DFA3(
            self, 3,
            eot = self.DFA3_eot,
            eof = self.DFA3_eof,
            min = self.DFA3_min,
            max = self.DFA3_max,
            accept = self.DFA3_accept,
            special = self.DFA3_special,
            transition = self.DFA3_transition
            )






    # $ANTLR start "DOT"
    def mDOT(self, ):

        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:7:5: ( '.' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:7:7: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):

        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:8:7: ( ',' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:8:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "SEMICOLON"
    def mSEMICOLON(self, ):

        try:
            _type = SEMICOLON
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:9:11: ( ';' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:9:13: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SEMICOLON"



    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):

        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:10:8: ( '(' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:10:10: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LPAREN"



    # $ANTLR start "RPAREN"
    def mRPAREN(self, ):

        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:11:8: ( ')' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:11:10: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RPAREN"



    # $ANTLR start "LBRACE"
    def mLBRACE(self, ):

        try:
            _type = LBRACE
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:12:8: ( '{' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:12:10: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LBRACE"



    # $ANTLR start "RBRACE"
    def mRBRACE(self, ):

        try:
            _type = RBRACE
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:13:8: ( '}' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:13:10: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RBRACE"



    # $ANTLR start "ASSIGN"
    def mASSIGN(self, ):

        try:
            _type = ASSIGN
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:14:8: ( '=' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:14:10: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASSIGN"



    # $ANTLR start "UNDERSCORE"
    def mUNDERSCORE(self, ):

        try:
            _type = UNDERSCORE
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:15:12: ( '_' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:15:14: '_'
            pass 
            self.match(95)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UNDERSCORE"



    # $ANTLR start "CLASS"
    def mCLASS(self, ):

        try:
            _type = CLASS
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:16:7: ( 'class' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:16:9: 'class'
            pass 
            self.match("class")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CLASS"



    # $ANTLR start "EXTENDS"
    def mEXTENDS(self, ):

        try:
            _type = EXTENDS
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:17:9: ( 'extends' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:17:11: 'extends'
            pass 
            self.match("extends")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EXTENDS"



    # $ANTLR start "SUPER"
    def mSUPER(self, ):

        try:
            _type = SUPER
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:18:7: ( 'super' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:18:9: 'super'
            pass 
            self.match("super")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SUPER"



    # $ANTLR start "THIS"
    def mTHIS(self, ):

        try:
            _type = THIS
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:19:6: ( 'this' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:19:8: 'this'
            pass 
            self.match("this")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "THIS"



    # $ANTLR start "RETURN"
    def mRETURN(self, ):

        try:
            _type = RETURN
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:20:8: ( 'return' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:20:10: 'return'
            pass 
            self.match("return")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RETURN"



    # $ANTLR start "NEW"
    def mNEW(self, ):

        try:
            _type = NEW
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:21:5: ( 'new' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:21:7: 'new'
            pass 
            self.match("new")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NEW"



    # $ANTLR start "LETTER"
    def mLETTER(self, ):

        try:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:87:3: ( 'a' .. 'z' | 'A' .. 'Z' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "LETTER"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:94:3: ( '0' .. '9' )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:95:3: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "ANY_CHAR"
    def mANY_CHAR(self, ):

        try:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:100:3: ( LETTER | UNDERSCORE | DIGIT )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "ANY_CHAR"



    # $ANTLR start "NAME"
    def mNAME(self, ):

        try:
            _type = NAME
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:107:3: ( ( LETTER | UNDERSCORE ) ( ANY_CHAR )* )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:108:3: ( LETTER | UNDERSCORE ) ( ANY_CHAR )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # /home/tamsyn/code/fj-llvm/parser/fj.g:112:3: ( ANY_CHAR )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or LA1_0 == 95 or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:112:3: ANY_CHAR
                    pass 
                    self.mANY_CHAR()


                else:
                    break #loop1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NAME"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):

        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # /home/tamsyn/code/fj-llvm/parser/fj.g:116:3: ( ( ' ' | '\\t' | '\\r' | '\\n' )+ )
            # /home/tamsyn/code/fj-llvm/parser/fj.g:117:3: ( ' ' | '\\t' | '\\r' | '\\n' )+
            pass 
            # /home/tamsyn/code/fj-llvm/parser/fj.g:117:3: ( ' ' | '\\t' | '\\r' | '\\n' )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((9 <= LA2_0 <= 10) or LA2_0 == 13 or LA2_0 == 32) :
                    alt2 = 1


                if alt2 == 1:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1
            #action start
               
            _channel = HIDDEN;
              
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHITESPACE"



    def mTokens(self):
        # /home/tamsyn/code/fj-llvm/parser/fj.g:1:8: ( DOT | COMMA | SEMICOLON | LPAREN | RPAREN | LBRACE | RBRACE | ASSIGN | UNDERSCORE | CLASS | EXTENDS | SUPER | THIS | RETURN | NEW | NAME | WHITESPACE )
        alt3 = 17
        alt3 = self.dfa3.predict(self.input)
        if alt3 == 1:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:10: DOT
            pass 
            self.mDOT()


        elif alt3 == 2:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:14: COMMA
            pass 
            self.mCOMMA()


        elif alt3 == 3:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:20: SEMICOLON
            pass 
            self.mSEMICOLON()


        elif alt3 == 4:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:30: LPAREN
            pass 
            self.mLPAREN()


        elif alt3 == 5:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:37: RPAREN
            pass 
            self.mRPAREN()


        elif alt3 == 6:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:44: LBRACE
            pass 
            self.mLBRACE()


        elif alt3 == 7:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:51: RBRACE
            pass 
            self.mRBRACE()


        elif alt3 == 8:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:58: ASSIGN
            pass 
            self.mASSIGN()


        elif alt3 == 9:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:65: UNDERSCORE
            pass 
            self.mUNDERSCORE()


        elif alt3 == 10:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:76: CLASS
            pass 
            self.mCLASS()


        elif alt3 == 11:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:82: EXTENDS
            pass 
            self.mEXTENDS()


        elif alt3 == 12:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:90: SUPER
            pass 
            self.mSUPER()


        elif alt3 == 13:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:96: THIS
            pass 
            self.mTHIS()


        elif alt3 == 14:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:101: RETURN
            pass 
            self.mRETURN()


        elif alt3 == 15:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:108: NEW
            pass 
            self.mNEW()


        elif alt3 == 16:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:112: NAME
            pass 
            self.mNAME()


        elif alt3 == 17:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:1:117: WHITESPACE
            pass 
            self.mWHITESPACE()







    # lookup tables for DFA #3

    DFA3_eot = DFA.unpack(
        u"\11\uffff\1\22\6\20\3\uffff\13\20\1\44\3\20\1\50\1\20\1\uffff\1"
        u"\52\1\20\1\54\1\uffff\1\20\1\uffff\1\20\1\uffff\1\57\1\60\2\uffff"
        )

    DFA3_eof = DFA.unpack(
        u"\61\uffff"
        )

    DFA3_min = DFA.unpack(
        u"\1\11\10\uffff\1\60\1\154\1\170\1\165\1\150\2\145\3\uffff\1\141"
        u"\1\164\1\160\1\151\1\164\1\167\1\163\2\145\1\163\1\165\1\60\1\163"
        u"\1\156\1\162\1\60\1\162\1\uffff\1\60\1\144\1\60\1\uffff\1\156\1"
        u"\uffff\1\163\1\uffff\2\60\2\uffff"
        )

    DFA3_max = DFA.unpack(
        u"\1\175\10\uffff\1\172\1\154\1\170\1\165\1\150\2\145\3\uffff\1\141"
        u"\1\164\1\160\1\151\1\164\1\167\1\163\2\145\1\163\1\165\1\172\1"
        u"\163\1\156\1\162\1\172\1\162\1\uffff\1\172\1\144\1\172\1\uffff"
        u"\1\156\1\uffff\1\163\1\uffff\2\172\2\uffff"
        )

    DFA3_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\7\uffff\1\20\1\21\1\11"
        u"\21\uffff\1\17\3\uffff\1\15\1\uffff\1\12\1\uffff\1\14\2\uffff\1"
        u"\16\1\13"
        )

    DFA3_special = DFA.unpack(
        u"\61\uffff"
        )

            
    DFA3_transition = [
        DFA.unpack(u"\2\21\2\uffff\1\21\22\uffff\1\21\7\uffff\1\4\1\5\2\uffff"
        u"\1\2\1\uffff\1\1\14\uffff\1\3\1\uffff\1\10\3\uffff\32\20\4\uffff"
        u"\1\11\1\uffff\2\20\1\12\1\20\1\13\10\20\1\17\3\20\1\16\1\14\1\15"
        u"\6\20\1\6\1\uffff\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\20\7\uffff\32\20\4\uffff\1\20\1\uffff\32\20"),
        DFA.unpack(u"\1\23"),
        DFA.unpack(u"\1\24"),
        DFA.unpack(u"\1\25"),
        DFA.unpack(u"\1\26"),
        DFA.unpack(u"\1\27"),
        DFA.unpack(u"\1\30"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u"\1\32"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u"\1\34"),
        DFA.unpack(u"\1\35"),
        DFA.unpack(u"\1\36"),
        DFA.unpack(u"\1\37"),
        DFA.unpack(u"\1\40"),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u"\12\20\7\uffff\32\20\4\uffff\1\20\1\uffff\32\20"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\12\20\7\uffff\32\20\4\uffff\1\20\1\uffff\32\20"),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\20\7\uffff\32\20\4\uffff\1\20\1\uffff\32\20"),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u"\12\20\7\uffff\32\20\4\uffff\1\20\1\uffff\32\20"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\20\7\uffff\32\20\4\uffff\1\20\1\uffff\32\20"),
        DFA.unpack(u"\12\20\7\uffff\32\20\4\uffff\1\20\1\uffff\32\20"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #3

    class DFA3(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(fjLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
