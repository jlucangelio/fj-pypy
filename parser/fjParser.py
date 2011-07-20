# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 /home/tamsyn/code/fj-llvm/parser/fj.g 2011-07-20 19:55:42

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *

         
# Copyright 2011 Jorge Lucangeli Obes
#
# This file is part of fj-llvm.
#
# fj-llvm is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# fj-llvm is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with fj-llvm. If not, see <http://www.gnu.org/licenses/>.



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
CLASS=13
RBRACE=10
LETTER=19
LBRACE=9
NEW=18
WHITESPACE=23
UNDERSCORE=12
SEMICOLON=6
EOF=-1
LPAREN=7
ANY_CHAR=21
RPAREN=8
NAME=22
COMMA=5
ASSIGN=11
THIS=16
RETURN=17
DIGIT=20
SUPER=15
DOT=4
EXTENDS=14

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "DOT", "COMMA", "SEMICOLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
    "ASSIGN", "UNDERSCORE", "CLASS", "EXTENDS", "SUPER", "THIS", "RETURN", 
    "NEW", "LETTER", "DIGIT", "ANY_CHAR", "NAME", "WHITESPACE"
]




class fjParser(Parser):
    grammarFileName = "/home/tamsyn/code/fj-llvm/parser/fj.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(fjParser, self).__init__(input, state, *args, **kwargs)






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class program_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.program_return, self).__init__()

            self.tree = None




    # $ANTLR start "program"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:109:1: program : ( classDefinition )+ expression ;
    def program(self, ):

        retval = self.program_return()
        retval.start = self.input.LT(1)

        root_0 = None

        classDefinition1 = None

        expression2 = None



        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:111:3: ( ( classDefinition )+ expression )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:112:3: ( classDefinition )+ expression
                pass 
                root_0 = self._adaptor.nil()

                # /home/tamsyn/code/fj-llvm/parser/fj.g:112:3: ( classDefinition )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == CLASS) :
                        alt1 = 1


                    if alt1 == 1:
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:0:0: classDefinition
                        pass 
                        self._state.following.append(self.FOLLOW_classDefinition_in_program435)
                        classDefinition1 = self.classDefinition()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, classDefinition1.tree)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1
                self._state.following.append(self.FOLLOW_expression_in_program438)
                expression2 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression2.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "program"

    class classDefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.classDefinition_return, self).__init__()

            self.tree = None




    # $ANTLR start "classDefinition"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:115:1: classDefinition : CLASS NAME EXTENDS NAME LBRACE fields constructor methods RBRACE ;
    def classDefinition(self, ):

        retval = self.classDefinition_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CLASS3 = None
        NAME4 = None
        EXTENDS5 = None
        NAME6 = None
        LBRACE7 = None
        RBRACE11 = None
        fields8 = None

        constructor9 = None

        methods10 = None


        CLASS3_tree = None
        NAME4_tree = None
        EXTENDS5_tree = None
        NAME6_tree = None
        LBRACE7_tree = None
        RBRACE11_tree = None

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:116:3: ( CLASS NAME EXTENDS NAME LBRACE fields constructor methods RBRACE )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:117:3: CLASS NAME EXTENDS NAME LBRACE fields constructor methods RBRACE
                pass 
                root_0 = self._adaptor.nil()

                CLASS3=self.match(self.input, CLASS, self.FOLLOW_CLASS_in_classDefinition453)
                if self._state.backtracking == 0:

                    CLASS3_tree = self._adaptor.createWithPayload(CLASS3)
                    self._adaptor.addChild(root_0, CLASS3_tree)

                NAME4=self.match(self.input, NAME, self.FOLLOW_NAME_in_classDefinition455)
                if self._state.backtracking == 0:

                    NAME4_tree = self._adaptor.createWithPayload(NAME4)
                    self._adaptor.addChild(root_0, NAME4_tree)

                EXTENDS5=self.match(self.input, EXTENDS, self.FOLLOW_EXTENDS_in_classDefinition457)
                if self._state.backtracking == 0:

                    EXTENDS5_tree = self._adaptor.createWithPayload(EXTENDS5)
                    self._adaptor.addChild(root_0, EXTENDS5_tree)

                NAME6=self.match(self.input, NAME, self.FOLLOW_NAME_in_classDefinition459)
                if self._state.backtracking == 0:

                    NAME6_tree = self._adaptor.createWithPayload(NAME6)
                    self._adaptor.addChild(root_0, NAME6_tree)

                LBRACE7=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_classDefinition461)
                if self._state.backtracking == 0:

                    LBRACE7_tree = self._adaptor.createWithPayload(LBRACE7)
                    self._adaptor.addChild(root_0, LBRACE7_tree)

                self._state.following.append(self.FOLLOW_fields_in_classDefinition463)
                fields8 = self.fields()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, fields8.tree)
                self._state.following.append(self.FOLLOW_constructor_in_classDefinition465)
                constructor9 = self.constructor()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, constructor9.tree)
                self._state.following.append(self.FOLLOW_methods_in_classDefinition467)
                methods10 = self.methods()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, methods10.tree)
                RBRACE11=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_classDefinition469)
                if self._state.backtracking == 0:

                    RBRACE11_tree = self._adaptor.createWithPayload(RBRACE11)
                    self._adaptor.addChild(root_0, RBRACE11_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "classDefinition"

    class fields_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.fields_return, self).__init__()

            self.tree = None




    # $ANTLR start "fields"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:120:1: fields : ( field SEMICOLON )* ;
    def fields(self, ):

        retval = self.fields_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMICOLON13 = None
        field12 = None


        SEMICOLON13_tree = None

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:121:3: ( ( field SEMICOLON )* )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:122:3: ( field SEMICOLON )*
                pass 
                root_0 = self._adaptor.nil()

                # /home/tamsyn/code/fj-llvm/parser/fj.g:122:3: ( field SEMICOLON )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == NAME) :
                        LA2_1 = self.input.LA(2)

                        if (LA2_1 == NAME) :
                            alt2 = 1




                    if alt2 == 1:
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:122:4: field SEMICOLON
                        pass 
                        self._state.following.append(self.FOLLOW_field_in_fields485)
                        field12 = self.field()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, field12.tree)
                        SEMICOLON13=self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_fields487)
                        if self._state.backtracking == 0:

                            SEMICOLON13_tree = self._adaptor.createWithPayload(SEMICOLON13)
                            self._adaptor.addChild(root_0, SEMICOLON13_tree)



                    else:
                        break #loop2



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fields"

    class field_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.field_return, self).__init__()

            self.tree = None




    # $ANTLR start "field"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:125:1: field : NAME NAME ;
    def field(self, ):

        retval = self.field_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME14 = None
        NAME15 = None

        NAME14_tree = None
        NAME15_tree = None

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:126:3: ( NAME NAME )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:127:3: NAME NAME
                pass 
                root_0 = self._adaptor.nil()

                NAME14=self.match(self.input, NAME, self.FOLLOW_NAME_in_field504)
                if self._state.backtracking == 0:

                    NAME14_tree = self._adaptor.createWithPayload(NAME14)
                    self._adaptor.addChild(root_0, NAME14_tree)

                NAME15=self.match(self.input, NAME, self.FOLLOW_NAME_in_field506)
                if self._state.backtracking == 0:

                    NAME15_tree = self._adaptor.createWithPayload(NAME15)
                    self._adaptor.addChild(root_0, NAME15_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "field"

    class constructor_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.constructor_return, self).__init__()

            self.tree = None




    # $ANTLR start "constructor"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:130:1: constructor : NAME LPAREN vars RPAREN LBRACE SUPER LPAREN names RPAREN SEMICOLON inits RBRACE ;
    def constructor(self, ):

        retval = self.constructor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME16 = None
        LPAREN17 = None
        RPAREN19 = None
        LBRACE20 = None
        SUPER21 = None
        LPAREN22 = None
        RPAREN24 = None
        SEMICOLON25 = None
        RBRACE27 = None
        vars18 = None

        names23 = None

        inits26 = None


        NAME16_tree = None
        LPAREN17_tree = None
        RPAREN19_tree = None
        LBRACE20_tree = None
        SUPER21_tree = None
        LPAREN22_tree = None
        RPAREN24_tree = None
        SEMICOLON25_tree = None
        RBRACE27_tree = None

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:131:3: ( NAME LPAREN vars RPAREN LBRACE SUPER LPAREN names RPAREN SEMICOLON inits RBRACE )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:132:3: NAME LPAREN vars RPAREN LBRACE SUPER LPAREN names RPAREN SEMICOLON inits RBRACE
                pass 
                root_0 = self._adaptor.nil()

                NAME16=self.match(self.input, NAME, self.FOLLOW_NAME_in_constructor521)
                if self._state.backtracking == 0:

                    NAME16_tree = self._adaptor.createWithPayload(NAME16)
                    self._adaptor.addChild(root_0, NAME16_tree)

                LPAREN17=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_constructor523)
                if self._state.backtracking == 0:

                    LPAREN17_tree = self._adaptor.createWithPayload(LPAREN17)
                    self._adaptor.addChild(root_0, LPAREN17_tree)

                self._state.following.append(self.FOLLOW_vars_in_constructor525)
                vars18 = self.vars()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, vars18.tree)
                RPAREN19=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_constructor527)
                if self._state.backtracking == 0:

                    RPAREN19_tree = self._adaptor.createWithPayload(RPAREN19)
                    self._adaptor.addChild(root_0, RPAREN19_tree)

                LBRACE20=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_constructor529)
                if self._state.backtracking == 0:

                    LBRACE20_tree = self._adaptor.createWithPayload(LBRACE20)
                    self._adaptor.addChild(root_0, LBRACE20_tree)

                SUPER21=self.match(self.input, SUPER, self.FOLLOW_SUPER_in_constructor531)
                if self._state.backtracking == 0:

                    SUPER21_tree = self._adaptor.createWithPayload(SUPER21)
                    self._adaptor.addChild(root_0, SUPER21_tree)

                LPAREN22=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_constructor533)
                if self._state.backtracking == 0:

                    LPAREN22_tree = self._adaptor.createWithPayload(LPAREN22)
                    self._adaptor.addChild(root_0, LPAREN22_tree)

                self._state.following.append(self.FOLLOW_names_in_constructor535)
                names23 = self.names()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, names23.tree)
                RPAREN24=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_constructor537)
                if self._state.backtracking == 0:

                    RPAREN24_tree = self._adaptor.createWithPayload(RPAREN24)
                    self._adaptor.addChild(root_0, RPAREN24_tree)

                SEMICOLON25=self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_constructor539)
                if self._state.backtracking == 0:

                    SEMICOLON25_tree = self._adaptor.createWithPayload(SEMICOLON25)
                    self._adaptor.addChild(root_0, SEMICOLON25_tree)

                self._state.following.append(self.FOLLOW_inits_in_constructor541)
                inits26 = self.inits()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, inits26.tree)
                RBRACE27=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_constructor543)
                if self._state.backtracking == 0:

                    RBRACE27_tree = self._adaptor.createWithPayload(RBRACE27)
                    self._adaptor.addChild(root_0, RBRACE27_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "constructor"

    class vars_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.vars_return, self).__init__()

            self.tree = None




    # $ANTLR start "vars"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:135:1: vars : ( var ( COMMA var )* )? ;
    def vars(self, ):

        retval = self.vars_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA29 = None
        var28 = None

        var30 = None


        COMMA29_tree = None

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:136:3: ( ( var ( COMMA var )* )? )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:137:3: ( var ( COMMA var )* )?
                pass 
                root_0 = self._adaptor.nil()

                # /home/tamsyn/code/fj-llvm/parser/fj.g:137:3: ( var ( COMMA var )* )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == NAME) :
                    alt4 = 1
                if alt4 == 1:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:137:4: var ( COMMA var )*
                    pass 
                    self._state.following.append(self.FOLLOW_var_in_vars559)
                    var28 = self.var()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, var28.tree)
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:137:8: ( COMMA var )*
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == COMMA) :
                            alt3 = 1


                        if alt3 == 1:
                            # /home/tamsyn/code/fj-llvm/parser/fj.g:137:9: COMMA var
                            pass 
                            COMMA29=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vars562)
                            if self._state.backtracking == 0:

                                COMMA29_tree = self._adaptor.createWithPayload(COMMA29)
                                self._adaptor.addChild(root_0, COMMA29_tree)

                            self._state.following.append(self.FOLLOW_var_in_vars564)
                            var30 = self.var()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, var30.tree)


                        else:
                            break #loop3






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "vars"

    class var_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.var_return, self).__init__()

            self.tree = None




    # $ANTLR start "var"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:140:1: var : NAME NAME ;
    def var(self, ):

        retval = self.var_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME31 = None
        NAME32 = None

        NAME31_tree = None
        NAME32_tree = None

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:141:3: ( NAME NAME )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:142:3: NAME NAME
                pass 
                root_0 = self._adaptor.nil()

                NAME31=self.match(self.input, NAME, self.FOLLOW_NAME_in_var583)
                if self._state.backtracking == 0:

                    NAME31_tree = self._adaptor.createWithPayload(NAME31)
                    self._adaptor.addChild(root_0, NAME31_tree)

                NAME32=self.match(self.input, NAME, self.FOLLOW_NAME_in_var585)
                if self._state.backtracking == 0:

                    NAME32_tree = self._adaptor.createWithPayload(NAME32)
                    self._adaptor.addChild(root_0, NAME32_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "var"

    class names_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.names_return, self).__init__()

            self.tree = None




    # $ANTLR start "names"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:145:1: names : ( NAME COMMA )* ;
    def names(self, ):

        retval = self.names_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME33 = None
        COMMA34 = None

        NAME33_tree = None
        COMMA34_tree = None

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:146:3: ( ( NAME COMMA )* )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:147:3: ( NAME COMMA )*
                pass 
                root_0 = self._adaptor.nil()

                # /home/tamsyn/code/fj-llvm/parser/fj.g:147:3: ( NAME COMMA )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == NAME) :
                        alt5 = 1


                    if alt5 == 1:
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:147:4: NAME COMMA
                        pass 
                        NAME33=self.match(self.input, NAME, self.FOLLOW_NAME_in_names601)
                        if self._state.backtracking == 0:

                            NAME33_tree = self._adaptor.createWithPayload(NAME33)
                            self._adaptor.addChild(root_0, NAME33_tree)

                        COMMA34=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_names603)
                        if self._state.backtracking == 0:

                            COMMA34_tree = self._adaptor.createWithPayload(COMMA34)
                            self._adaptor.addChild(root_0, COMMA34_tree)



                    else:
                        break #loop5



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "names"

    class inits_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.inits_return, self).__init__()

            self.tree = None




    # $ANTLR start "inits"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:150:1: inits : ( init SEMICOLON )* ;
    def inits(self, ):

        retval = self.inits_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMICOLON36 = None
        init35 = None


        SEMICOLON36_tree = None

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:151:3: ( ( init SEMICOLON )* )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:152:3: ( init SEMICOLON )*
                pass 
                root_0 = self._adaptor.nil()

                # /home/tamsyn/code/fj-llvm/parser/fj.g:152:3: ( init SEMICOLON )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == THIS) :
                        alt6 = 1


                    if alt6 == 1:
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:152:4: init SEMICOLON
                        pass 
                        self._state.following.append(self.FOLLOW_init_in_inits621)
                        init35 = self.init()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, init35.tree)
                        SEMICOLON36=self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_inits623)
                        if self._state.backtracking == 0:

                            SEMICOLON36_tree = self._adaptor.createWithPayload(SEMICOLON36)
                            self._adaptor.addChild(root_0, SEMICOLON36_tree)



                    else:
                        break #loop6



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "inits"

    class init_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.init_return, self).__init__()

            self.tree = None




    # $ANTLR start "init"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:155:1: init : THIS DOT NAME ASSIGN NAME ;
    def init(self, ):

        retval = self.init_return()
        retval.start = self.input.LT(1)

        root_0 = None

        THIS37 = None
        DOT38 = None
        NAME39 = None
        ASSIGN40 = None
        NAME41 = None

        THIS37_tree = None
        DOT38_tree = None
        NAME39_tree = None
        ASSIGN40_tree = None
        NAME41_tree = None

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:156:3: ( THIS DOT NAME ASSIGN NAME )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:157:3: THIS DOT NAME ASSIGN NAME
                pass 
                root_0 = self._adaptor.nil()

                THIS37=self.match(self.input, THIS, self.FOLLOW_THIS_in_init640)
                if self._state.backtracking == 0:

                    THIS37_tree = self._adaptor.createWithPayload(THIS37)
                    self._adaptor.addChild(root_0, THIS37_tree)

                DOT38=self.match(self.input, DOT, self.FOLLOW_DOT_in_init642)
                if self._state.backtracking == 0:

                    DOT38_tree = self._adaptor.createWithPayload(DOT38)
                    self._adaptor.addChild(root_0, DOT38_tree)

                NAME39=self.match(self.input, NAME, self.FOLLOW_NAME_in_init644)
                if self._state.backtracking == 0:

                    NAME39_tree = self._adaptor.createWithPayload(NAME39)
                    self._adaptor.addChild(root_0, NAME39_tree)

                ASSIGN40=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_init646)
                if self._state.backtracking == 0:

                    ASSIGN40_tree = self._adaptor.createWithPayload(ASSIGN40)
                    self._adaptor.addChild(root_0, ASSIGN40_tree)

                NAME41=self.match(self.input, NAME, self.FOLLOW_NAME_in_init648)
                if self._state.backtracking == 0:

                    NAME41_tree = self._adaptor.createWithPayload(NAME41)
                    self._adaptor.addChild(root_0, NAME41_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "init"

    class methods_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.methods_return, self).__init__()

            self.tree = None




    # $ANTLR start "methods"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:160:1: methods : ( method )* ;
    def methods(self, ):

        retval = self.methods_return()
        retval.start = self.input.LT(1)

        root_0 = None

        method42 = None



        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:161:3: ( ( method )* )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:162:3: ( method )*
                pass 
                root_0 = self._adaptor.nil()

                # /home/tamsyn/code/fj-llvm/parser/fj.g:162:3: ( method )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == NAME) :
                        alt7 = 1


                    if alt7 == 1:
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:0:0: method
                        pass 
                        self._state.following.append(self.FOLLOW_method_in_methods663)
                        method42 = self.method()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, method42.tree)


                    else:
                        break #loop7



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "methods"

    class method_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.method_return, self).__init__()

            self.tree = None




    # $ANTLR start "method"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:165:1: method : NAME NAME LPAREN vars RPAREN LBRACE RETURN expression SEMICOLON RBRACE ;
    def method(self, ):

        retval = self.method_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME43 = None
        NAME44 = None
        LPAREN45 = None
        RPAREN47 = None
        LBRACE48 = None
        RETURN49 = None
        SEMICOLON51 = None
        RBRACE52 = None
        vars46 = None

        expression50 = None


        NAME43_tree = None
        NAME44_tree = None
        LPAREN45_tree = None
        RPAREN47_tree = None
        LBRACE48_tree = None
        RETURN49_tree = None
        SEMICOLON51_tree = None
        RBRACE52_tree = None

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:166:3: ( NAME NAME LPAREN vars RPAREN LBRACE RETURN expression SEMICOLON RBRACE )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:167:3: NAME NAME LPAREN vars RPAREN LBRACE RETURN expression SEMICOLON RBRACE
                pass 
                root_0 = self._adaptor.nil()

                NAME43=self.match(self.input, NAME, self.FOLLOW_NAME_in_method679)
                if self._state.backtracking == 0:

                    NAME43_tree = self._adaptor.createWithPayload(NAME43)
                    self._adaptor.addChild(root_0, NAME43_tree)

                NAME44=self.match(self.input, NAME, self.FOLLOW_NAME_in_method681)
                if self._state.backtracking == 0:

                    NAME44_tree = self._adaptor.createWithPayload(NAME44)
                    self._adaptor.addChild(root_0, NAME44_tree)

                LPAREN45=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_method683)
                if self._state.backtracking == 0:

                    LPAREN45_tree = self._adaptor.createWithPayload(LPAREN45)
                    self._adaptor.addChild(root_0, LPAREN45_tree)

                self._state.following.append(self.FOLLOW_vars_in_method685)
                vars46 = self.vars()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, vars46.tree)
                RPAREN47=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_method687)
                if self._state.backtracking == 0:

                    RPAREN47_tree = self._adaptor.createWithPayload(RPAREN47)
                    self._adaptor.addChild(root_0, RPAREN47_tree)

                LBRACE48=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_method689)
                if self._state.backtracking == 0:

                    LBRACE48_tree = self._adaptor.createWithPayload(LBRACE48)
                    self._adaptor.addChild(root_0, LBRACE48_tree)

                RETURN49=self.match(self.input, RETURN, self.FOLLOW_RETURN_in_method691)
                if self._state.backtracking == 0:

                    RETURN49_tree = self._adaptor.createWithPayload(RETURN49)
                    self._adaptor.addChild(root_0, RETURN49_tree)

                self._state.following.append(self.FOLLOW_expression_in_method693)
                expression50 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expression50.tree)
                SEMICOLON51=self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_method695)
                if self._state.backtracking == 0:

                    SEMICOLON51_tree = self._adaptor.createWithPayload(SEMICOLON51)
                    self._adaptor.addChild(root_0, SEMICOLON51_tree)

                RBRACE52=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_method697)
                if self._state.backtracking == 0:

                    RBRACE52_tree = self._adaptor.createWithPayload(RBRACE52)
                    self._adaptor.addChild(root_0, RBRACE52_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "method"

    class expression_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.expression_return, self).__init__()

            self.tree = None




    # $ANTLR start "expression"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:170:1: expression : ( baseExpression | dotExpression );
    def expression(self, ):

        retval = self.expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        baseExpression53 = None

        dotExpression54 = None



        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:171:3: ( baseExpression | dotExpression )
                alt8 = 2
                LA8 = self.input.LA(1)
                if LA8 == NAME:
                    LA8_1 = self.input.LA(2)

                    if (self.synpred8_fj()) :
                        alt8 = 1
                    elif (True) :
                        alt8 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 8, 1, self.input)

                        raise nvae

                elif LA8 == NEW:
                    LA8_2 = self.input.LA(2)

                    if (self.synpred8_fj()) :
                        alt8 = 1
                    elif (True) :
                        alt8 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 8, 2, self.input)

                        raise nvae

                elif LA8 == LPAREN:
                    LA8_3 = self.input.LA(2)

                    if (self.synpred8_fj()) :
                        alt8 = 1
                    elif (True) :
                        alt8 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 8, 3, self.input)

                        raise nvae

                elif LA8 == THIS:
                    alt8 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:172:3: baseExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_baseExpression_in_expression712)
                    baseExpression53 = self.baseExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, baseExpression53.tree)


                elif alt8 == 2:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:173:5: dotExpression
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_dotExpression_in_expression718)
                    dotExpression54 = self.dotExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, dotExpression54.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "expression"

    class dotExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.dotExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "dotExpression"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:176:1: dotExpression : ( baseExpression | THIS ) ( DOT NAME ( parenExpressions )? )+ ;
    def dotExpression(self, ):

        retval = self.dotExpression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        THIS56 = None
        DOT57 = None
        NAME58 = None
        baseExpression55 = None

        parenExpressions59 = None


        THIS56_tree = None
        DOT57_tree = None
        NAME58_tree = None

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:177:3: ( ( baseExpression | THIS ) ( DOT NAME ( parenExpressions )? )+ )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:178:3: ( baseExpression | THIS ) ( DOT NAME ( parenExpressions )? )+
                pass 
                root_0 = self._adaptor.nil()

                # /home/tamsyn/code/fj-llvm/parser/fj.g:178:3: ( baseExpression | THIS )
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == LPAREN or LA9_0 == NEW or LA9_0 == NAME) :
                    alt9 = 1
                elif (LA9_0 == THIS) :
                    alt9 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae

                if alt9 == 1:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:179:5: baseExpression
                    pass 
                    self._state.following.append(self.FOLLOW_baseExpression_in_dotExpression739)
                    baseExpression55 = self.baseExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, baseExpression55.tree)


                elif alt9 == 2:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:180:7: THIS
                    pass 
                    THIS56=self.match(self.input, THIS, self.FOLLOW_THIS_in_dotExpression747)
                    if self._state.backtracking == 0:

                        THIS56_tree = self._adaptor.createWithPayload(THIS56)
                        self._adaptor.addChild(root_0, THIS56_tree)




                # /home/tamsyn/code/fj-llvm/parser/fj.g:182:3: ( DOT NAME ( parenExpressions )? )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == DOT) :
                        LA11_2 = self.input.LA(2)

                        if (self.synpred11_fj()) :
                            alt11 = 1




                    if alt11 == 1:
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:182:4: DOT NAME ( parenExpressions )?
                        pass 
                        DOT57=self.match(self.input, DOT, self.FOLLOW_DOT_in_dotExpression756)
                        if self._state.backtracking == 0:

                            DOT57_tree = self._adaptor.createWithPayload(DOT57)
                            self._adaptor.addChild(root_0, DOT57_tree)

                        NAME58=self.match(self.input, NAME, self.FOLLOW_NAME_in_dotExpression758)
                        if self._state.backtracking == 0:

                            NAME58_tree = self._adaptor.createWithPayload(NAME58)
                            self._adaptor.addChild(root_0, NAME58_tree)

                        # /home/tamsyn/code/fj-llvm/parser/fj.g:182:13: ( parenExpressions )?
                        alt10 = 2
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == LPAREN) :
                            alt10 = 1
                        if alt10 == 1:
                            # /home/tamsyn/code/fj-llvm/parser/fj.g:0:0: parenExpressions
                            pass 
                            self._state.following.append(self.FOLLOW_parenExpressions_in_dotExpression760)
                            parenExpressions59 = self.parenExpressions()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, parenExpressions59.tree)





                    else:
                        if cnt11 >= 1:
                            break #loop11

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "dotExpression"

    class baseExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.baseExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "baseExpression"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:185:1: baseExpression : ( NAME | NEW NAME parenExpressions | LPAREN NAME RPAREN expression );
    def baseExpression(self, ):

        retval = self.baseExpression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME60 = None
        NEW61 = None
        NAME62 = None
        LPAREN64 = None
        NAME65 = None
        RPAREN66 = None
        parenExpressions63 = None

        expression67 = None


        NAME60_tree = None
        NEW61_tree = None
        NAME62_tree = None
        LPAREN64_tree = None
        NAME65_tree = None
        RPAREN66_tree = None

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:186:3: ( NAME | NEW NAME parenExpressions | LPAREN NAME RPAREN expression )
                alt12 = 3
                LA12 = self.input.LA(1)
                if LA12 == NAME:
                    alt12 = 1
                elif LA12 == NEW:
                    alt12 = 2
                elif LA12 == LPAREN:
                    alt12 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:187:3: NAME
                    pass 
                    root_0 = self._adaptor.nil()

                    NAME60=self.match(self.input, NAME, self.FOLLOW_NAME_in_baseExpression779)
                    if self._state.backtracking == 0:

                        NAME60_tree = self._adaptor.createWithPayload(NAME60)
                        self._adaptor.addChild(root_0, NAME60_tree)



                elif alt12 == 2:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:188:5: NEW NAME parenExpressions
                    pass 
                    root_0 = self._adaptor.nil()

                    NEW61=self.match(self.input, NEW, self.FOLLOW_NEW_in_baseExpression785)
                    if self._state.backtracking == 0:

                        NEW61_tree = self._adaptor.createWithPayload(NEW61)
                        self._adaptor.addChild(root_0, NEW61_tree)

                    NAME62=self.match(self.input, NAME, self.FOLLOW_NAME_in_baseExpression787)
                    if self._state.backtracking == 0:

                        NAME62_tree = self._adaptor.createWithPayload(NAME62)
                        self._adaptor.addChild(root_0, NAME62_tree)

                    self._state.following.append(self.FOLLOW_parenExpressions_in_baseExpression789)
                    parenExpressions63 = self.parenExpressions()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, parenExpressions63.tree)


                elif alt12 == 3:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:189:5: LPAREN NAME RPAREN expression
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN64=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_baseExpression796)
                    if self._state.backtracking == 0:

                        LPAREN64_tree = self._adaptor.createWithPayload(LPAREN64)
                        self._adaptor.addChild(root_0, LPAREN64_tree)

                    NAME65=self.match(self.input, NAME, self.FOLLOW_NAME_in_baseExpression798)
                    if self._state.backtracking == 0:

                        NAME65_tree = self._adaptor.createWithPayload(NAME65)
                        self._adaptor.addChild(root_0, NAME65_tree)

                    RPAREN66=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_baseExpression800)
                    if self._state.backtracking == 0:

                        RPAREN66_tree = self._adaptor.createWithPayload(RPAREN66)
                        self._adaptor.addChild(root_0, RPAREN66_tree)

                    self._state.following.append(self.FOLLOW_expression_in_baseExpression802)
                    expression67 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression67.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "baseExpression"

    class parenExpressions_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.parenExpressions_return, self).__init__()

            self.tree = None




    # $ANTLR start "parenExpressions"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:192:1: parenExpressions : LPAREN ( expression ( COMMA expression )* )? RPAREN ;
    def parenExpressions(self, ):

        retval = self.parenExpressions_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LPAREN68 = None
        COMMA70 = None
        RPAREN72 = None
        expression69 = None

        expression71 = None


        LPAREN68_tree = None
        COMMA70_tree = None
        RPAREN72_tree = None

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:193:3: ( LPAREN ( expression ( COMMA expression )* )? RPAREN )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:194:3: LPAREN ( expression ( COMMA expression )* )? RPAREN
                pass 
                root_0 = self._adaptor.nil()

                LPAREN68=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_parenExpressions818)
                if self._state.backtracking == 0:

                    LPAREN68_tree = self._adaptor.createWithPayload(LPAREN68)
                    self._adaptor.addChild(root_0, LPAREN68_tree)

                # /home/tamsyn/code/fj-llvm/parser/fj.g:194:10: ( expression ( COMMA expression )* )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == LPAREN or LA14_0 == THIS or LA14_0 == NEW or LA14_0 == NAME) :
                    alt14 = 1
                if alt14 == 1:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:194:11: expression ( COMMA expression )*
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_parenExpressions821)
                    expression69 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expression69.tree)
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:194:22: ( COMMA expression )*
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == COMMA) :
                            alt13 = 1


                        if alt13 == 1:
                            # /home/tamsyn/code/fj-llvm/parser/fj.g:194:23: COMMA expression
                            pass 
                            COMMA70=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_parenExpressions824)
                            if self._state.backtracking == 0:

                                COMMA70_tree = self._adaptor.createWithPayload(COMMA70)
                                self._adaptor.addChild(root_0, COMMA70_tree)

                            self._state.following.append(self.FOLLOW_expression_in_parenExpressions826)
                            expression71 = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, expression71.tree)


                        else:
                            break #loop13



                RPAREN72=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_parenExpressions832)
                if self._state.backtracking == 0:

                    RPAREN72_tree = self._adaptor.createWithPayload(RPAREN72)
                    self._adaptor.addChild(root_0, RPAREN72_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "parenExpressions"

    # $ANTLR start "synpred8_fj"
    def synpred8_fj_fragment(self, ):
        # /home/tamsyn/code/fj-llvm/parser/fj.g:172:3: ( baseExpression )
        # /home/tamsyn/code/fj-llvm/parser/fj.g:172:3: baseExpression
        pass 
        self._state.following.append(self.FOLLOW_baseExpression_in_synpred8_fj712)
        self.baseExpression()

        self._state.following.pop()


    # $ANTLR end "synpred8_fj"



    # $ANTLR start "synpred11_fj"
    def synpred11_fj_fragment(self, ):
        # /home/tamsyn/code/fj-llvm/parser/fj.g:182:4: ( DOT NAME ( parenExpressions )? )
        # /home/tamsyn/code/fj-llvm/parser/fj.g:182:4: DOT NAME ( parenExpressions )?
        pass 
        self.match(self.input, DOT, self.FOLLOW_DOT_in_synpred11_fj756)
        self.match(self.input, NAME, self.FOLLOW_NAME_in_synpred11_fj758)
        # /home/tamsyn/code/fj-llvm/parser/fj.g:182:13: ( parenExpressions )?
        alt16 = 2
        LA16_0 = self.input.LA(1)

        if (LA16_0 == LPAREN) :
            alt16 = 1
        if alt16 == 1:
            # /home/tamsyn/code/fj-llvm/parser/fj.g:0:0: parenExpressions
            pass 
            self._state.following.append(self.FOLLOW_parenExpressions_in_synpred11_fj760)
            self.parenExpressions()

            self._state.following.pop()





    # $ANTLR end "synpred11_fj"




    # Delegated rules

    def synpred8_fj(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred8_fj_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred11_fj(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred11_fj_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_classDefinition_in_program435 = frozenset([7, 13, 16, 18, 22])
    FOLLOW_expression_in_program438 = frozenset([1])
    FOLLOW_CLASS_in_classDefinition453 = frozenset([22])
    FOLLOW_NAME_in_classDefinition455 = frozenset([14])
    FOLLOW_EXTENDS_in_classDefinition457 = frozenset([22])
    FOLLOW_NAME_in_classDefinition459 = frozenset([9])
    FOLLOW_LBRACE_in_classDefinition461 = frozenset([22])
    FOLLOW_fields_in_classDefinition463 = frozenset([22])
    FOLLOW_constructor_in_classDefinition465 = frozenset([10, 22])
    FOLLOW_methods_in_classDefinition467 = frozenset([10])
    FOLLOW_RBRACE_in_classDefinition469 = frozenset([1])
    FOLLOW_field_in_fields485 = frozenset([6])
    FOLLOW_SEMICOLON_in_fields487 = frozenset([1, 22])
    FOLLOW_NAME_in_field504 = frozenset([22])
    FOLLOW_NAME_in_field506 = frozenset([1])
    FOLLOW_NAME_in_constructor521 = frozenset([7])
    FOLLOW_LPAREN_in_constructor523 = frozenset([8, 22])
    FOLLOW_vars_in_constructor525 = frozenset([8])
    FOLLOW_RPAREN_in_constructor527 = frozenset([9])
    FOLLOW_LBRACE_in_constructor529 = frozenset([15])
    FOLLOW_SUPER_in_constructor531 = frozenset([7])
    FOLLOW_LPAREN_in_constructor533 = frozenset([8, 22])
    FOLLOW_names_in_constructor535 = frozenset([8])
    FOLLOW_RPAREN_in_constructor537 = frozenset([6])
    FOLLOW_SEMICOLON_in_constructor539 = frozenset([10, 16])
    FOLLOW_inits_in_constructor541 = frozenset([10])
    FOLLOW_RBRACE_in_constructor543 = frozenset([1])
    FOLLOW_var_in_vars559 = frozenset([1, 5])
    FOLLOW_COMMA_in_vars562 = frozenset([22])
    FOLLOW_var_in_vars564 = frozenset([1, 5])
    FOLLOW_NAME_in_var583 = frozenset([22])
    FOLLOW_NAME_in_var585 = frozenset([1])
    FOLLOW_NAME_in_names601 = frozenset([5])
    FOLLOW_COMMA_in_names603 = frozenset([1, 22])
    FOLLOW_init_in_inits621 = frozenset([6])
    FOLLOW_SEMICOLON_in_inits623 = frozenset([1, 16])
    FOLLOW_THIS_in_init640 = frozenset([4])
    FOLLOW_DOT_in_init642 = frozenset([22])
    FOLLOW_NAME_in_init644 = frozenset([11])
    FOLLOW_ASSIGN_in_init646 = frozenset([22])
    FOLLOW_NAME_in_init648 = frozenset([1])
    FOLLOW_method_in_methods663 = frozenset([1, 22])
    FOLLOW_NAME_in_method679 = frozenset([22])
    FOLLOW_NAME_in_method681 = frozenset([7])
    FOLLOW_LPAREN_in_method683 = frozenset([8, 22])
    FOLLOW_vars_in_method685 = frozenset([8])
    FOLLOW_RPAREN_in_method687 = frozenset([9])
    FOLLOW_LBRACE_in_method689 = frozenset([17])
    FOLLOW_RETURN_in_method691 = frozenset([7, 16, 18, 22])
    FOLLOW_expression_in_method693 = frozenset([6])
    FOLLOW_SEMICOLON_in_method695 = frozenset([10])
    FOLLOW_RBRACE_in_method697 = frozenset([1])
    FOLLOW_baseExpression_in_expression712 = frozenset([1])
    FOLLOW_dotExpression_in_expression718 = frozenset([1])
    FOLLOW_baseExpression_in_dotExpression739 = frozenset([4])
    FOLLOW_THIS_in_dotExpression747 = frozenset([4])
    FOLLOW_DOT_in_dotExpression756 = frozenset([22])
    FOLLOW_NAME_in_dotExpression758 = frozenset([1, 4, 7])
    FOLLOW_parenExpressions_in_dotExpression760 = frozenset([1, 4])
    FOLLOW_NAME_in_baseExpression779 = frozenset([1])
    FOLLOW_NEW_in_baseExpression785 = frozenset([22])
    FOLLOW_NAME_in_baseExpression787 = frozenset([7])
    FOLLOW_parenExpressions_in_baseExpression789 = frozenset([1])
    FOLLOW_LPAREN_in_baseExpression796 = frozenset([22])
    FOLLOW_NAME_in_baseExpression798 = frozenset([8])
    FOLLOW_RPAREN_in_baseExpression800 = frozenset([7, 16, 18, 22])
    FOLLOW_expression_in_baseExpression802 = frozenset([1])
    FOLLOW_LPAREN_in_parenExpressions818 = frozenset([7, 8, 16, 18, 22])
    FOLLOW_expression_in_parenExpressions821 = frozenset([5, 8])
    FOLLOW_COMMA_in_parenExpressions824 = frozenset([7, 16, 18, 22])
    FOLLOW_expression_in_parenExpressions826 = frozenset([5, 8])
    FOLLOW_RPAREN_in_parenExpressions832 = frozenset([1])
    FOLLOW_baseExpression_in_synpred8_fj712 = frozenset([1])
    FOLLOW_DOT_in_synpred11_fj756 = frozenset([22])
    FOLLOW_NAME_in_synpred11_fj758 = frozenset([1, 7])
    FOLLOW_parenExpressions_in_synpred11_fj760 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("fjLexer", fjParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
