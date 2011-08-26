# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 /home/tamsyn/code/fj-llvm/parser/fj.g 2011-08-26 12:54:14

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
VARIABLES=29
EMPTY_EXPS=23
ASSIGN=11
THIS=16
RETURN=17
FIELD=25
PROGRAM=19
DIGIT=37
SUPER=15
DOT=4
INIT=24
EXTENDS=14
EXPRESSION=32
METHOD=30
CONSTRUCTOR=20
BASE_EXPRESSION=33

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "DOT", "COMMA", "SEMICOLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
    "ASSIGN", "UNDERSCORE", "CLASS", "EXTENDS", "SUPER", "THIS", "RETURN", 
    "NEW", "PROGRAM", "CONSTRUCTOR", "EMPTY_NAMES", "EMPTY_VARS", "EMPTY_EXPS", 
    "INIT", "FIELD", "FIELDS", "NAMES", "VARIABLE", "VARIABLES", "METHOD", 
    "METHODS", "EXPRESSION", "BASE_EXPRESSION", "DOT_EXPRESSION", "EXPRESSIONS", 
    "LETTER", "DIGIT", "ANY_CHAR", "NAME", "WHITESPACE"
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
    # /home/tamsyn/code/fj-llvm/parser/fj.g:129:1: program : ( classDefinition )+ expression SEMICOLON -> ^( PROGRAM ( classDefinition )+ expression ) ;
    def program(self, ):

        retval = self.program_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMICOLON3 = None
        classDefinition1 = None

        expression2 = None


        SEMICOLON3_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_classDefinition = RewriteRuleSubtreeStream(self._adaptor, "rule classDefinition")
        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:131:3: ( ( classDefinition )+ expression SEMICOLON -> ^( PROGRAM ( classDefinition )+ expression ) )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:132:3: ( classDefinition )+ expression SEMICOLON
                pass 
                # /home/tamsyn/code/fj-llvm/parser/fj.g:132:3: ( classDefinition )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == CLASS) :
                        alt1 = 1


                    if alt1 == 1:
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:0:0: classDefinition
                        pass 
                        self._state.following.append(self.FOLLOW_classDefinition_in_program525)
                        classDefinition1 = self.classDefinition()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_classDefinition.add(classDefinition1.tree)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1
                self._state.following.append(self.FOLLOW_expression_in_program528)
                expression2 = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(expression2.tree)
                SEMICOLON3=self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_program530) 
                if self._state.backtracking == 0:
                    stream_SEMICOLON.add(SEMICOLON3)

                # AST Rewrite
                # elements: classDefinition, expression
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 133:5: -> ^( PROGRAM ( classDefinition )+ expression )
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:134:7: ^( PROGRAM ( classDefinition )+ expression )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROGRAM, "PROGRAM"), root_1)

                    # /home/tamsyn/code/fj-llvm/parser/fj.g:134:17: ( classDefinition )+
                    if not (stream_classDefinition.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_classDefinition.hasNext():
                        self._adaptor.addChild(root_1, stream_classDefinition.nextTree())


                    stream_classDefinition.reset()
                    self._adaptor.addChild(root_1, stream_expression.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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
    # /home/tamsyn/code/fj-llvm/parser/fj.g:137:1: classDefinition : CLASS cname= NAME EXTENDS pname= NAME LBRACE fields constructor methods RBRACE -> ^( CLASS $cname $pname fields constructor methods ) ;
    def classDefinition(self, ):

        retval = self.classDefinition_return()
        retval.start = self.input.LT(1)

        root_0 = None

        cname = None
        pname = None
        CLASS4 = None
        EXTENDS5 = None
        LBRACE6 = None
        RBRACE10 = None
        fields7 = None

        constructor8 = None

        methods9 = None


        cname_tree = None
        pname_tree = None
        CLASS4_tree = None
        EXTENDS5_tree = None
        LBRACE6_tree = None
        RBRACE10_tree = None
        stream_CLASS = RewriteRuleTokenStream(self._adaptor, "token CLASS")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_EXTENDS = RewriteRuleTokenStream(self._adaptor, "token EXTENDS")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_methods = RewriteRuleSubtreeStream(self._adaptor, "rule methods")
        stream_fields = RewriteRuleSubtreeStream(self._adaptor, "rule fields")
        stream_constructor = RewriteRuleSubtreeStream(self._adaptor, "rule constructor")
        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:138:3: ( CLASS cname= NAME EXTENDS pname= NAME LBRACE fields constructor methods RBRACE -> ^( CLASS $cname $pname fields constructor methods ) )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:139:3: CLASS cname= NAME EXTENDS pname= NAME LBRACE fields constructor methods RBRACE
                pass 
                CLASS4=self.match(self.input, CLASS, self.FOLLOW_CLASS_in_classDefinition566) 
                if self._state.backtracking == 0:
                    stream_CLASS.add(CLASS4)
                cname=self.match(self.input, NAME, self.FOLLOW_NAME_in_classDefinition570) 
                if self._state.backtracking == 0:
                    stream_NAME.add(cname)
                EXTENDS5=self.match(self.input, EXTENDS, self.FOLLOW_EXTENDS_in_classDefinition572) 
                if self._state.backtracking == 0:
                    stream_EXTENDS.add(EXTENDS5)
                pname=self.match(self.input, NAME, self.FOLLOW_NAME_in_classDefinition576) 
                if self._state.backtracking == 0:
                    stream_NAME.add(pname)
                LBRACE6=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_classDefinition578) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE6)
                self._state.following.append(self.FOLLOW_fields_in_classDefinition580)
                fields7 = self.fields()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_fields.add(fields7.tree)
                self._state.following.append(self.FOLLOW_constructor_in_classDefinition582)
                constructor8 = self.constructor()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_constructor.add(constructor8.tree)
                self._state.following.append(self.FOLLOW_methods_in_classDefinition584)
                methods9 = self.methods()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_methods.add(methods9.tree)
                RBRACE10=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_classDefinition586) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE10)

                # AST Rewrite
                # elements: fields, methods, cname, CLASS, constructor, pname
                # token labels: pname, cname
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0
                    stream_pname = RewriteRuleTokenStream(self._adaptor, "token pname", pname)
                    stream_cname = RewriteRuleTokenStream(self._adaptor, "token cname", cname)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 140:5: -> ^( CLASS $cname $pname fields constructor methods )
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:141:7: ^( CLASS $cname $pname fields constructor methods )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_CLASS.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_cname.nextNode())
                    self._adaptor.addChild(root_1, stream_pname.nextNode())
                    self._adaptor.addChild(root_1, stream_fields.nextTree())
                    self._adaptor.addChild(root_1, stream_constructor.nextTree())
                    self._adaptor.addChild(root_1, stream_methods.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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
    # /home/tamsyn/code/fj-llvm/parser/fj.g:144:1: fields : ( field SEMICOLON )* -> ^( FIELDS ( field )* ) ;
    def fields(self, ):

        retval = self.fields_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMICOLON12 = None
        field11 = None


        SEMICOLON12_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_field = RewriteRuleSubtreeStream(self._adaptor, "rule field")
        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:145:3: ( ( field SEMICOLON )* -> ^( FIELDS ( field )* ) )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:146:3: ( field SEMICOLON )*
                pass 
                # /home/tamsyn/code/fj-llvm/parser/fj.g:146:3: ( field SEMICOLON )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == NAME) :
                        LA2_1 = self.input.LA(2)

                        if (LA2_1 == NAME) :
                            alt2 = 1




                    if alt2 == 1:
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:146:4: field SEMICOLON
                        pass 
                        self._state.following.append(self.FOLLOW_field_in_fields630)
                        field11 = self.field()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_field.add(field11.tree)
                        SEMICOLON12=self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_fields632) 
                        if self._state.backtracking == 0:
                            stream_SEMICOLON.add(SEMICOLON12)


                    else:
                        break #loop2

                # AST Rewrite
                # elements: field
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 147:5: -> ^( FIELDS ( field )* )
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:148:7: ^( FIELDS ( field )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FIELDS, "FIELDS"), root_1)

                    # /home/tamsyn/code/fj-llvm/parser/fj.g:148:16: ( field )*
                    while stream_field.hasNext():
                        self._adaptor.addChild(root_1, stream_field.nextTree())


                    stream_field.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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
    # /home/tamsyn/code/fj-llvm/parser/fj.g:151:1: field : t= NAME n= NAME -> ^( FIELD $t $n) ;
    def field(self, ):

        retval = self.field_return()
        retval.start = self.input.LT(1)

        root_0 = None

        t = None
        n = None

        t_tree = None
        n_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:152:3: (t= NAME n= NAME -> ^( FIELD $t $n) )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:153:3: t= NAME n= NAME
                pass 
                t=self.match(self.input, NAME, self.FOLLOW_NAME_in_field670) 
                if self._state.backtracking == 0:
                    stream_NAME.add(t)
                n=self.match(self.input, NAME, self.FOLLOW_NAME_in_field674) 
                if self._state.backtracking == 0:
                    stream_NAME.add(n)

                # AST Rewrite
                # elements: t, n
                # token labels: t, n
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0
                    stream_t = RewriteRuleTokenStream(self._adaptor, "token t", t)
                    stream_n = RewriteRuleTokenStream(self._adaptor, "token n", n)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 154:5: -> ^( FIELD $t $n)
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:155:7: ^( FIELD $t $n)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FIELD, "FIELD"), root_1)

                    self._adaptor.addChild(root_1, stream_t.nextNode())
                    self._adaptor.addChild(root_1, stream_n.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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
    # /home/tamsyn/code/fj-llvm/parser/fj.g:158:1: constructor : cname= NAME LPAREN vs= vars RPAREN LBRACE SUPER LPAREN ns= names RPAREN SEMICOLON ins= inits RBRACE -> ^( CONSTRUCTOR $cname $vs $ns $ins) ;
    def constructor(self, ):

        retval = self.constructor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        cname = None
        LPAREN13 = None
        RPAREN14 = None
        LBRACE15 = None
        SUPER16 = None
        LPAREN17 = None
        RPAREN18 = None
        SEMICOLON19 = None
        RBRACE20 = None
        vs = None

        ns = None

        ins = None


        cname_tree = None
        LPAREN13_tree = None
        RPAREN14_tree = None
        LBRACE15_tree = None
        SUPER16_tree = None
        LPAREN17_tree = None
        RPAREN18_tree = None
        SEMICOLON19_tree = None
        RBRACE20_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_SUPER = RewriteRuleTokenStream(self._adaptor, "token SUPER")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_vars = RewriteRuleSubtreeStream(self._adaptor, "rule vars")
        stream_inits = RewriteRuleSubtreeStream(self._adaptor, "rule inits")
        stream_names = RewriteRuleSubtreeStream(self._adaptor, "rule names")
        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:159:3: (cname= NAME LPAREN vs= vars RPAREN LBRACE SUPER LPAREN ns= names RPAREN SEMICOLON ins= inits RBRACE -> ^( CONSTRUCTOR $cname $vs $ns $ins) )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:160:3: cname= NAME LPAREN vs= vars RPAREN LBRACE SUPER LPAREN ns= names RPAREN SEMICOLON ins= inits RBRACE
                pass 
                cname=self.match(self.input, NAME, self.FOLLOW_NAME_in_constructor713) 
                if self._state.backtracking == 0:
                    stream_NAME.add(cname)
                LPAREN13=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_constructor715) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN13)
                self._state.following.append(self.FOLLOW_vars_in_constructor719)
                vs = self.vars()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_vars.add(vs.tree)
                RPAREN14=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_constructor721) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN14)
                LBRACE15=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_constructor723) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE15)
                SUPER16=self.match(self.input, SUPER, self.FOLLOW_SUPER_in_constructor725) 
                if self._state.backtracking == 0:
                    stream_SUPER.add(SUPER16)
                LPAREN17=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_constructor727) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN17)
                self._state.following.append(self.FOLLOW_names_in_constructor731)
                ns = self.names()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_names.add(ns.tree)
                RPAREN18=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_constructor733) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN18)
                SEMICOLON19=self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_constructor735) 
                if self._state.backtracking == 0:
                    stream_SEMICOLON.add(SEMICOLON19)
                self._state.following.append(self.FOLLOW_inits_in_constructor739)
                ins = self.inits()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_inits.add(ins.tree)
                RBRACE20=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_constructor741) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE20)

                # AST Rewrite
                # elements: cname, vs, ins, ns
                # token labels: cname
                # rule labels: retval, ns, ins, vs
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0
                    stream_cname = RewriteRuleTokenStream(self._adaptor, "token cname", cname)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if ns is not None:
                        stream_ns = RewriteRuleSubtreeStream(self._adaptor, "rule ns", ns.tree)
                    else:
                        stream_ns = RewriteRuleSubtreeStream(self._adaptor, "token ns", None)


                    if ins is not None:
                        stream_ins = RewriteRuleSubtreeStream(self._adaptor, "rule ins", ins.tree)
                    else:
                        stream_ins = RewriteRuleSubtreeStream(self._adaptor, "token ins", None)


                    if vs is not None:
                        stream_vs = RewriteRuleSubtreeStream(self._adaptor, "rule vs", vs.tree)
                    else:
                        stream_vs = RewriteRuleSubtreeStream(self._adaptor, "token vs", None)


                    root_0 = self._adaptor.nil()
                    # 161:5: -> ^( CONSTRUCTOR $cname $vs $ns $ins)
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:162:7: ^( CONSTRUCTOR $cname $vs $ns $ins)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CONSTRUCTOR, "CONSTRUCTOR"), root_1)

                    self._adaptor.addChild(root_1, stream_cname.nextNode())
                    self._adaptor.addChild(root_1, stream_vs.nextTree())
                    self._adaptor.addChild(root_1, stream_ns.nextTree())
                    self._adaptor.addChild(root_1, stream_ins.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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
    # /home/tamsyn/code/fj-llvm/parser/fj.g:165:1: vars : ( var ( COMMA var )* -> ^( VARIABLES ( var )+ ) | -> EMPTY_VARS );
    def vars(self, ):

        retval = self.vars_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA22 = None
        var21 = None

        var23 = None


        COMMA22_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_var = RewriteRuleSubtreeStream(self._adaptor, "rule var")
        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:166:3: ( var ( COMMA var )* -> ^( VARIABLES ( var )+ ) | -> EMPTY_VARS )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == NAME) :
                    alt4 = 1
                elif (LA4_0 == RPAREN) :
                    alt4 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:167:3: var ( COMMA var )*
                    pass 
                    self._state.following.append(self.FOLLOW_var_in_vars784)
                    var21 = self.var()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_var.add(var21.tree)
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:167:7: ( COMMA var )*
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == COMMA) :
                            alt3 = 1


                        if alt3 == 1:
                            # /home/tamsyn/code/fj-llvm/parser/fj.g:167:8: COMMA var
                            pass 
                            COMMA22=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_vars787) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA22)
                            self._state.following.append(self.FOLLOW_var_in_vars789)
                            var23 = self.var()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_var.add(var23.tree)


                        else:
                            break #loop3

                    # AST Rewrite
                    # elements: var
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 168:5: -> ^( VARIABLES ( var )+ )
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:169:7: ^( VARIABLES ( var )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VARIABLES, "VARIABLES"), root_1)

                        # /home/tamsyn/code/fj-llvm/parser/fj.g:169:19: ( var )+
                        if not (stream_var.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_var.hasNext():
                            self._adaptor.addChild(root_1, stream_var.nextTree())


                        stream_var.reset()

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt4 == 2:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:171:5: 
                    pass 
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 171:5: -> EMPTY_VARS
                        self._adaptor.addChild(root_0, self._adaptor.createFromType(EMPTY_VARS, "EMPTY_VARS"))



                        retval.tree = root_0


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
    # /home/tamsyn/code/fj-llvm/parser/fj.g:174:1: var : t= NAME n= NAME -> ^( VARIABLE $t $n) ;
    def var(self, ):

        retval = self.var_return()
        retval.start = self.input.LT(1)

        root_0 = None

        t = None
        n = None

        t_tree = None
        n_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:175:3: (t= NAME n= NAME -> ^( VARIABLE $t $n) )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:176:3: t= NAME n= NAME
                pass 
                t=self.match(self.input, NAME, self.FOLLOW_NAME_in_var839) 
                if self._state.backtracking == 0:
                    stream_NAME.add(t)
                n=self.match(self.input, NAME, self.FOLLOW_NAME_in_var843) 
                if self._state.backtracking == 0:
                    stream_NAME.add(n)

                # AST Rewrite
                # elements: n, t
                # token labels: t, n
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0
                    stream_t = RewriteRuleTokenStream(self._adaptor, "token t", t)
                    stream_n = RewriteRuleTokenStream(self._adaptor, "token n", n)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 177:5: -> ^( VARIABLE $t $n)
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:178:7: ^( VARIABLE $t $n)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(VARIABLE, "VARIABLE"), root_1)

                    self._adaptor.addChild(root_1, stream_t.nextNode())
                    self._adaptor.addChild(root_1, stream_n.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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
    # /home/tamsyn/code/fj-llvm/parser/fj.g:181:1: names : ( NAME ( COMMA NAME )* -> ^( NAMES ( NAME )+ ) | -> EMPTY_NAMES );
    def names(self, ):

        retval = self.names_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME24 = None
        COMMA25 = None
        NAME26 = None

        NAME24_tree = None
        COMMA25_tree = None
        NAME26_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:182:3: ( NAME ( COMMA NAME )* -> ^( NAMES ( NAME )+ ) | -> EMPTY_NAMES )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == NAME) :
                    alt6 = 1
                elif (LA6_0 == RPAREN) :
                    alt6 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:183:3: NAME ( COMMA NAME )*
                    pass 
                    NAME24=self.match(self.input, NAME, self.FOLLOW_NAME_in_names880) 
                    if self._state.backtracking == 0:
                        stream_NAME.add(NAME24)
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:183:8: ( COMMA NAME )*
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == COMMA) :
                            alt5 = 1


                        if alt5 == 1:
                            # /home/tamsyn/code/fj-llvm/parser/fj.g:183:9: COMMA NAME
                            pass 
                            COMMA25=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_names883) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA25)
                            NAME26=self.match(self.input, NAME, self.FOLLOW_NAME_in_names885) 
                            if self._state.backtracking == 0:
                                stream_NAME.add(NAME26)


                        else:
                            break #loop5

                    # AST Rewrite
                    # elements: NAME
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 184:5: -> ^( NAMES ( NAME )+ )
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:185:7: ^( NAMES ( NAME )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(NAMES, "NAMES"), root_1)

                        # /home/tamsyn/code/fj-llvm/parser/fj.g:185:15: ( NAME )+
                        if not (stream_NAME.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_NAME.hasNext():
                            self._adaptor.addChild(root_1, stream_NAME.nextNode())


                        stream_NAME.reset()

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt6 == 2:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:187:5: 
                    pass 
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 187:5: -> EMPTY_NAMES
                        self._adaptor.addChild(root_0, self._adaptor.createFromType(EMPTY_NAMES, "EMPTY_NAMES"))



                        retval.tree = root_0


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
    # /home/tamsyn/code/fj-llvm/parser/fj.g:190:1: inits : ( init SEMICOLON )* ;
    def inits(self, ):

        retval = self.inits_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMICOLON28 = None
        init27 = None


        SEMICOLON28_tree = None

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:191:3: ( ( init SEMICOLON )* )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:192:3: ( init SEMICOLON )*
                pass 
                root_0 = self._adaptor.nil()

                # /home/tamsyn/code/fj-llvm/parser/fj.g:192:3: ( init SEMICOLON )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == THIS) :
                        alt7 = 1


                    if alt7 == 1:
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:192:4: init SEMICOLON
                        pass 
                        self._state.following.append(self.FOLLOW_init_in_inits934)
                        init27 = self.init()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, init27.tree)
                        SEMICOLON28=self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_inits936)


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

    # $ANTLR end "inits"

    class init_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.init_return, self).__init__()

            self.tree = None




    # $ANTLR start "init"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:195:1: init : THIS DOT f= NAME ASSIGN v= NAME -> ^( INIT $f $v) ;
    def init(self, ):

        retval = self.init_return()
        retval.start = self.input.LT(1)

        root_0 = None

        f = None
        v = None
        THIS29 = None
        DOT30 = None
        ASSIGN31 = None

        f_tree = None
        v_tree = None
        THIS29_tree = None
        DOT30_tree = None
        ASSIGN31_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_THIS = RewriteRuleTokenStream(self._adaptor, "token THIS")
        stream_ASSIGN = RewriteRuleTokenStream(self._adaptor, "token ASSIGN")

        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:196:3: ( THIS DOT f= NAME ASSIGN v= NAME -> ^( INIT $f $v) )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:197:3: THIS DOT f= NAME ASSIGN v= NAME
                pass 
                THIS29=self.match(self.input, THIS, self.FOLLOW_THIS_in_init954) 
                if self._state.backtracking == 0:
                    stream_THIS.add(THIS29)
                DOT30=self.match(self.input, DOT, self.FOLLOW_DOT_in_init956) 
                if self._state.backtracking == 0:
                    stream_DOT.add(DOT30)
                f=self.match(self.input, NAME, self.FOLLOW_NAME_in_init960) 
                if self._state.backtracking == 0:
                    stream_NAME.add(f)
                ASSIGN31=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_init962) 
                if self._state.backtracking == 0:
                    stream_ASSIGN.add(ASSIGN31)
                v=self.match(self.input, NAME, self.FOLLOW_NAME_in_init966) 
                if self._state.backtracking == 0:
                    stream_NAME.add(v)

                # AST Rewrite
                # elements: v, f
                # token labels: f, v
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0
                    stream_f = RewriteRuleTokenStream(self._adaptor, "token f", f)
                    stream_v = RewriteRuleTokenStream(self._adaptor, "token v", v)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 198:5: -> ^( INIT $f $v)
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:199:7: ^( INIT $f $v)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(INIT, "INIT"), root_1)

                    self._adaptor.addChild(root_1, stream_f.nextNode())
                    self._adaptor.addChild(root_1, stream_v.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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
    # /home/tamsyn/code/fj-llvm/parser/fj.g:202:1: methods : ( method )* -> ^( METHODS ( method )* ) ;
    def methods(self, ):

        retval = self.methods_return()
        retval.start = self.input.LT(1)

        root_0 = None

        method32 = None


        stream_method = RewriteRuleSubtreeStream(self._adaptor, "rule method")
        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:203:3: ( ( method )* -> ^( METHODS ( method )* ) )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:204:3: ( method )*
                pass 
                # /home/tamsyn/code/fj-llvm/parser/fj.g:204:3: ( method )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == NAME) :
                        alt8 = 1


                    if alt8 == 1:
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:0:0: method
                        pass 
                        self._state.following.append(self.FOLLOW_method_in_methods1003)
                        method32 = self.method()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_method.add(method32.tree)


                    else:
                        break #loop8

                # AST Rewrite
                # elements: method
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 205:5: -> ^( METHODS ( method )* )
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:206:7: ^( METHODS ( method )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(METHODS, "METHODS"), root_1)

                    # /home/tamsyn/code/fj-llvm/parser/fj.g:206:17: ( method )*
                    while stream_method.hasNext():
                        self._adaptor.addChild(root_1, stream_method.nextTree())


                    stream_method.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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
    # /home/tamsyn/code/fj-llvm/parser/fj.g:209:1: method : type= NAME name= NAME LPAREN vs= vars RPAREN LBRACE RETURN exp= expression SEMICOLON RBRACE -> ^( METHOD $type $name $vs $exp) ;
    def method(self, ):

        retval = self.method_return()
        retval.start = self.input.LT(1)

        root_0 = None

        type = None
        name = None
        LPAREN33 = None
        RPAREN34 = None
        LBRACE35 = None
        RETURN36 = None
        SEMICOLON37 = None
        RBRACE38 = None
        vs = None

        exp = None


        type_tree = None
        name_tree = None
        LPAREN33_tree = None
        RPAREN34_tree = None
        LBRACE35_tree = None
        RETURN36_tree = None
        SEMICOLON37_tree = None
        RBRACE38_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_SEMICOLON = RewriteRuleTokenStream(self._adaptor, "token SEMICOLON")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_RETURN = RewriteRuleTokenStream(self._adaptor, "token RETURN")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_vars = RewriteRuleSubtreeStream(self._adaptor, "rule vars")
        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:210:3: (type= NAME name= NAME LPAREN vs= vars RPAREN LBRACE RETURN exp= expression SEMICOLON RBRACE -> ^( METHOD $type $name $vs $exp) )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:211:3: type= NAME name= NAME LPAREN vs= vars RPAREN LBRACE RETURN exp= expression SEMICOLON RBRACE
                pass 
                type=self.match(self.input, NAME, self.FOLLOW_NAME_in_method1040) 
                if self._state.backtracking == 0:
                    stream_NAME.add(type)
                name=self.match(self.input, NAME, self.FOLLOW_NAME_in_method1044) 
                if self._state.backtracking == 0:
                    stream_NAME.add(name)
                LPAREN33=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_method1046) 
                if self._state.backtracking == 0:
                    stream_LPAREN.add(LPAREN33)
                self._state.following.append(self.FOLLOW_vars_in_method1050)
                vs = self.vars()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_vars.add(vs.tree)
                RPAREN34=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_method1052) 
                if self._state.backtracking == 0:
                    stream_RPAREN.add(RPAREN34)
                LBRACE35=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_method1054) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE35)
                RETURN36=self.match(self.input, RETURN, self.FOLLOW_RETURN_in_method1056) 
                if self._state.backtracking == 0:
                    stream_RETURN.add(RETURN36)
                self._state.following.append(self.FOLLOW_expression_in_method1060)
                exp = self.expression()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expression.add(exp.tree)
                SEMICOLON37=self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_method1062) 
                if self._state.backtracking == 0:
                    stream_SEMICOLON.add(SEMICOLON37)
                RBRACE38=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_method1064) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE38)

                # AST Rewrite
                # elements: name, type, exp, vs
                # token labels: name, type
                # rule labels: exp, retval, vs
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0
                    stream_name = RewriteRuleTokenStream(self._adaptor, "token name", name)
                    stream_type = RewriteRuleTokenStream(self._adaptor, "token type", type)

                    if exp is not None:
                        stream_exp = RewriteRuleSubtreeStream(self._adaptor, "rule exp", exp.tree)
                    else:
                        stream_exp = RewriteRuleSubtreeStream(self._adaptor, "token exp", None)


                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if vs is not None:
                        stream_vs = RewriteRuleSubtreeStream(self._adaptor, "rule vs", vs.tree)
                    else:
                        stream_vs = RewriteRuleSubtreeStream(self._adaptor, "token vs", None)


                    root_0 = self._adaptor.nil()
                    # 212:5: -> ^( METHOD $type $name $vs $exp)
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:213:7: ^( METHOD $type $name $vs $exp)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(METHOD, "METHOD"), root_1)

                    self._adaptor.addChild(root_1, stream_type.nextNode())
                    self._adaptor.addChild(root_1, stream_name.nextNode())
                    self._adaptor.addChild(root_1, stream_vs.nextTree())
                    self._adaptor.addChild(root_1, stream_exp.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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
    # /home/tamsyn/code/fj-llvm/parser/fj.g:216:1: expression : ( baseExpression ( dotExpression )* -> ^( EXPRESSION baseExpression ( dotExpression )* ) | THIS ( dotExpression )+ -> ^( EXPRESSION THIS ( dotExpression )+ ) );
    def expression(self, ):

        retval = self.expression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        THIS41 = None
        baseExpression39 = None

        dotExpression40 = None

        dotExpression42 = None


        THIS41_tree = None
        stream_THIS = RewriteRuleTokenStream(self._adaptor, "token THIS")
        stream_baseExpression = RewriteRuleSubtreeStream(self._adaptor, "rule baseExpression")
        stream_dotExpression = RewriteRuleSubtreeStream(self._adaptor, "rule dotExpression")
        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:217:3: ( baseExpression ( dotExpression )* -> ^( EXPRESSION baseExpression ( dotExpression )* ) | THIS ( dotExpression )+ -> ^( EXPRESSION THIS ( dotExpression )+ ) )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == LPAREN or LA11_0 == NEW or LA11_0 == NAME) :
                    alt11 = 1
                elif (LA11_0 == THIS) :
                    alt11 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:218:3: baseExpression ( dotExpression )*
                    pass 
                    self._state.following.append(self.FOLLOW_baseExpression_in_expression1107)
                    baseExpression39 = self.baseExpression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_baseExpression.add(baseExpression39.tree)
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:218:18: ( dotExpression )*
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == DOT) :
                            LA9_2 = self.input.LA(2)

                            if (self.synpred9_fj()) :
                                alt9 = 1




                        if alt9 == 1:
                            # /home/tamsyn/code/fj-llvm/parser/fj.g:0:0: dotExpression
                            pass 
                            self._state.following.append(self.FOLLOW_dotExpression_in_expression1109)
                            dotExpression40 = self.dotExpression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_dotExpression.add(dotExpression40.tree)


                        else:
                            break #loop9

                    # AST Rewrite
                    # elements: baseExpression, dotExpression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 219:5: -> ^( EXPRESSION baseExpression ( dotExpression )* )
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:220:7: ^( EXPRESSION baseExpression ( dotExpression )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPRESSION, "EXPRESSION"), root_1)

                        self._adaptor.addChild(root_1, stream_baseExpression.nextTree())
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:220:35: ( dotExpression )*
                        while stream_dotExpression.hasNext():
                            self._adaptor.addChild(root_1, stream_dotExpression.nextTree())


                        stream_dotExpression.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt11 == 2:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:221:5: THIS ( dotExpression )+
                    pass 
                    THIS41=self.match(self.input, THIS, self.FOLLOW_THIS_in_expression1137) 
                    if self._state.backtracking == 0:
                        stream_THIS.add(THIS41)
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:221:10: ( dotExpression )+
                    cnt10 = 0
                    while True: #loop10
                        alt10 = 2
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == DOT) :
                            LA10_2 = self.input.LA(2)

                            if (LA10_2 == NAME) :
                                LA10_3 = self.input.LA(3)

                                if (self.synpred11_fj()) :
                                    alt10 = 1






                        if alt10 == 1:
                            # /home/tamsyn/code/fj-llvm/parser/fj.g:0:0: dotExpression
                            pass 
                            self._state.following.append(self.FOLLOW_dotExpression_in_expression1139)
                            dotExpression42 = self.dotExpression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_dotExpression.add(dotExpression42.tree)


                        else:
                            if cnt10 >= 1:
                                break #loop10

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(10, self.input)
                            raise eee

                        cnt10 += 1

                    # AST Rewrite
                    # elements: dotExpression, THIS
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 222:5: -> ^( EXPRESSION THIS ( dotExpression )+ )
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:223:7: ^( EXPRESSION THIS ( dotExpression )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPRESSION, "EXPRESSION"), root_1)

                        self._adaptor.addChild(root_1, stream_THIS.nextNode())
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:223:25: ( dotExpression )+
                        if not (stream_dotExpression.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_dotExpression.hasNext():
                            self._adaptor.addChild(root_1, stream_dotExpression.nextTree())


                        stream_dotExpression.reset()

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


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

    class baseExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.baseExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "baseExpression"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:226:1: baseExpression : ( NAME -> ^( BASE_EXPRESSION NAME ) | NEW NAME LPAREN expressions RPAREN -> ^( BASE_EXPRESSION NEW NAME expressions ) | LPAREN NAME RPAREN expression -> ^( BASE_EXPRESSION NAME expression ) );
    def baseExpression(self, ):

        retval = self.baseExpression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME43 = None
        NEW44 = None
        NAME45 = None
        LPAREN46 = None
        RPAREN48 = None
        LPAREN49 = None
        NAME50 = None
        RPAREN51 = None
        expressions47 = None

        expression52 = None


        NAME43_tree = None
        NEW44_tree = None
        NAME45_tree = None
        LPAREN46_tree = None
        RPAREN48_tree = None
        LPAREN49_tree = None
        NAME50_tree = None
        RPAREN51_tree = None
        stream_NEW = RewriteRuleTokenStream(self._adaptor, "token NEW")
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        stream_expressions = RewriteRuleSubtreeStream(self._adaptor, "rule expressions")
        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:227:3: ( NAME -> ^( BASE_EXPRESSION NAME ) | NEW NAME LPAREN expressions RPAREN -> ^( BASE_EXPRESSION NEW NAME expressions ) | LPAREN NAME RPAREN expression -> ^( BASE_EXPRESSION NAME expression ) )
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
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:228:3: NAME
                    pass 
                    NAME43=self.match(self.input, NAME, self.FOLLOW_NAME_in_baseExpression1176) 
                    if self._state.backtracking == 0:
                        stream_NAME.add(NAME43)

                    # AST Rewrite
                    # elements: NAME
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 229:5: -> ^( BASE_EXPRESSION NAME )
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:230:7: ^( BASE_EXPRESSION NAME )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BASE_EXPRESSION, "BASE_EXPRESSION"), root_1)

                        self._adaptor.addChild(root_1, stream_NAME.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt12 == 2:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:231:5: NEW NAME LPAREN expressions RPAREN
                    pass 
                    NEW44=self.match(self.input, NEW, self.FOLLOW_NEW_in_baseExpression1201) 
                    if self._state.backtracking == 0:
                        stream_NEW.add(NEW44)
                    NAME45=self.match(self.input, NAME, self.FOLLOW_NAME_in_baseExpression1203) 
                    if self._state.backtracking == 0:
                        stream_NAME.add(NAME45)
                    LPAREN46=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_baseExpression1205) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN46)
                    self._state.following.append(self.FOLLOW_expressions_in_baseExpression1207)
                    expressions47 = self.expressions()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expressions.add(expressions47.tree)
                    RPAREN48=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_baseExpression1209) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN48)

                    # AST Rewrite
                    # elements: expressions, NAME, NEW
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 232:5: -> ^( BASE_EXPRESSION NEW NAME expressions )
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:233:7: ^( BASE_EXPRESSION NEW NAME expressions )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BASE_EXPRESSION, "BASE_EXPRESSION"), root_1)

                        self._adaptor.addChild(root_1, stream_NEW.nextNode())
                        self._adaptor.addChild(root_1, stream_NAME.nextNode())
                        self._adaptor.addChild(root_1, stream_expressions.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt12 == 3:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:234:5: LPAREN NAME RPAREN expression
                    pass 
                    LPAREN49=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_baseExpression1238) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN49)
                    NAME50=self.match(self.input, NAME, self.FOLLOW_NAME_in_baseExpression1240) 
                    if self._state.backtracking == 0:
                        stream_NAME.add(NAME50)
                    RPAREN51=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_baseExpression1242) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN51)
                    self._state.following.append(self.FOLLOW_expression_in_baseExpression1244)
                    expression52 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression52.tree)

                    # AST Rewrite
                    # elements: NAME, expression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 235:5: -> ^( BASE_EXPRESSION NAME expression )
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:236:7: ^( BASE_EXPRESSION NAME expression )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BASE_EXPRESSION, "BASE_EXPRESSION"), root_1)

                        self._adaptor.addChild(root_1, stream_NAME.nextNode())
                        self._adaptor.addChild(root_1, stream_expression.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


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

    class dotExpression_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.dotExpression_return, self).__init__()

            self.tree = None




    # $ANTLR start "dotExpression"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:239:1: dotExpression : DOT NAME ( LPAREN expressions RPAREN )? -> ^( DOT_EXPRESSION NAME ( expressions )? ) ;
    def dotExpression(self, ):

        retval = self.dotExpression_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOT53 = None
        NAME54 = None
        LPAREN55 = None
        RPAREN57 = None
        expressions56 = None


        DOT53_tree = None
        NAME54_tree = None
        LPAREN55_tree = None
        RPAREN57_tree = None
        stream_RPAREN = RewriteRuleTokenStream(self._adaptor, "token RPAREN")
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")
        stream_LPAREN = RewriteRuleTokenStream(self._adaptor, "token LPAREN")
        stream_expressions = RewriteRuleSubtreeStream(self._adaptor, "rule expressions")
        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:240:3: ( DOT NAME ( LPAREN expressions RPAREN )? -> ^( DOT_EXPRESSION NAME ( expressions )? ) )
                # /home/tamsyn/code/fj-llvm/parser/fj.g:241:3: DOT NAME ( LPAREN expressions RPAREN )?
                pass 
                DOT53=self.match(self.input, DOT, self.FOLLOW_DOT_in_dotExpression1280) 
                if self._state.backtracking == 0:
                    stream_DOT.add(DOT53)
                NAME54=self.match(self.input, NAME, self.FOLLOW_NAME_in_dotExpression1282) 
                if self._state.backtracking == 0:
                    stream_NAME.add(NAME54)
                # /home/tamsyn/code/fj-llvm/parser/fj.g:241:12: ( LPAREN expressions RPAREN )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == LPAREN) :
                    alt13 = 1
                if alt13 == 1:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:241:13: LPAREN expressions RPAREN
                    pass 
                    LPAREN55=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_dotExpression1285) 
                    if self._state.backtracking == 0:
                        stream_LPAREN.add(LPAREN55)
                    self._state.following.append(self.FOLLOW_expressions_in_dotExpression1287)
                    expressions56 = self.expressions()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expressions.add(expressions56.tree)
                    RPAREN57=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_dotExpression1289) 
                    if self._state.backtracking == 0:
                        stream_RPAREN.add(RPAREN57)




                # AST Rewrite
                # elements: NAME, expressions
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 242:5: -> ^( DOT_EXPRESSION NAME ( expressions )? )
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:243:7: ^( DOT_EXPRESSION NAME ( expressions )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(DOT_EXPRESSION, "DOT_EXPRESSION"), root_1)

                    self._adaptor.addChild(root_1, stream_NAME.nextNode())
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:243:29: ( expressions )?
                    if stream_expressions.hasNext():
                        self._adaptor.addChild(root_1, stream_expressions.nextTree())


                    stream_expressions.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



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

    class expressions_return(ParserRuleReturnScope):
        def __init__(self):
            super(fjParser.expressions_return, self).__init__()

            self.tree = None




    # $ANTLR start "expressions"
    # /home/tamsyn/code/fj-llvm/parser/fj.g:246:1: expressions : ( ( expression ( COMMA expression )* ) -> ^( EXPRESSIONS ( expression )+ ) | -> EMPTY_EXPS );
    def expressions(self, ):

        retval = self.expressions_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA59 = None
        expression58 = None

        expression60 = None


        COMMA59_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_expression = RewriteRuleSubtreeStream(self._adaptor, "rule expression")
        try:
            try:
                # /home/tamsyn/code/fj-llvm/parser/fj.g:247:3: ( ( expression ( COMMA expression )* ) -> ^( EXPRESSIONS ( expression )+ ) | -> EMPTY_EXPS )
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == LPAREN or LA15_0 == THIS or LA15_0 == NEW or LA15_0 == NAME) :
                    alt15 = 1
                elif (LA15_0 == RPAREN) :
                    alt15 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae

                if alt15 == 1:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:248:3: ( expression ( COMMA expression )* )
                    pass 
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:248:3: ( expression ( COMMA expression )* )
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:248:4: expression ( COMMA expression )*
                    pass 
                    self._state.following.append(self.FOLLOW_expression_in_expressions1329)
                    expression58 = self.expression()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expression.add(expression58.tree)
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:248:15: ( COMMA expression )*
                    while True: #loop14
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if (LA14_0 == COMMA) :
                            alt14 = 1


                        if alt14 == 1:
                            # /home/tamsyn/code/fj-llvm/parser/fj.g:248:16: COMMA expression
                            pass 
                            COMMA59=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_expressions1332) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA59)
                            self._state.following.append(self.FOLLOW_expression_in_expressions1334)
                            expression60 = self.expression()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_expression.add(expression60.tree)


                        else:
                            break #loop14




                    # AST Rewrite
                    # elements: expression
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 249:5: -> ^( EXPRESSIONS ( expression )+ )
                        # /home/tamsyn/code/fj-llvm/parser/fj.g:250:7: ^( EXPRESSIONS ( expression )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPRESSIONS, "EXPRESSIONS"), root_1)

                        # /home/tamsyn/code/fj-llvm/parser/fj.g:250:21: ( expression )+
                        if not (stream_expression.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_expression.hasNext():
                            self._adaptor.addChild(root_1, stream_expression.nextTree())


                        stream_expression.reset()

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt15 == 2:
                    # /home/tamsyn/code/fj-llvm/parser/fj.g:252:5: 
                    pass 
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 252:5: -> EMPTY_EXPS
                        self._adaptor.addChild(root_0, self._adaptor.createFromType(EMPTY_EXPS, "EMPTY_EXPS"))



                        retval.tree = root_0


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

    # $ANTLR end "expressions"

    # $ANTLR start "synpred9_fj"
    def synpred9_fj_fragment(self, ):
        # /home/tamsyn/code/fj-llvm/parser/fj.g:218:18: ( dotExpression )
        # /home/tamsyn/code/fj-llvm/parser/fj.g:218:18: dotExpression
        pass 
        self._state.following.append(self.FOLLOW_dotExpression_in_synpred9_fj1109)
        self.dotExpression()

        self._state.following.pop()


    # $ANTLR end "synpred9_fj"



    # $ANTLR start "synpred11_fj"
    def synpred11_fj_fragment(self, ):
        # /home/tamsyn/code/fj-llvm/parser/fj.g:221:10: ( dotExpression )
        # /home/tamsyn/code/fj-llvm/parser/fj.g:221:10: dotExpression
        pass 
        self._state.following.append(self.FOLLOW_dotExpression_in_synpred11_fj1139)
        self.dotExpression()

        self._state.following.pop()


    # $ANTLR end "synpred11_fj"




    # Delegated rules

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

    def synpred9_fj(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred9_fj_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_classDefinition_in_program525 = frozenset([7, 13, 16, 18, 39])
    FOLLOW_expression_in_program528 = frozenset([6])
    FOLLOW_SEMICOLON_in_program530 = frozenset([1])
    FOLLOW_CLASS_in_classDefinition566 = frozenset([39])
    FOLLOW_NAME_in_classDefinition570 = frozenset([14])
    FOLLOW_EXTENDS_in_classDefinition572 = frozenset([39])
    FOLLOW_NAME_in_classDefinition576 = frozenset([9])
    FOLLOW_LBRACE_in_classDefinition578 = frozenset([39])
    FOLLOW_fields_in_classDefinition580 = frozenset([39])
    FOLLOW_constructor_in_classDefinition582 = frozenset([10, 39])
    FOLLOW_methods_in_classDefinition584 = frozenset([10])
    FOLLOW_RBRACE_in_classDefinition586 = frozenset([1])
    FOLLOW_field_in_fields630 = frozenset([6])
    FOLLOW_SEMICOLON_in_fields632 = frozenset([1, 39])
    FOLLOW_NAME_in_field670 = frozenset([39])
    FOLLOW_NAME_in_field674 = frozenset([1])
    FOLLOW_NAME_in_constructor713 = frozenset([7])
    FOLLOW_LPAREN_in_constructor715 = frozenset([8, 39])
    FOLLOW_vars_in_constructor719 = frozenset([8])
    FOLLOW_RPAREN_in_constructor721 = frozenset([9])
    FOLLOW_LBRACE_in_constructor723 = frozenset([15])
    FOLLOW_SUPER_in_constructor725 = frozenset([7])
    FOLLOW_LPAREN_in_constructor727 = frozenset([8, 39])
    FOLLOW_names_in_constructor731 = frozenset([8])
    FOLLOW_RPAREN_in_constructor733 = frozenset([6])
    FOLLOW_SEMICOLON_in_constructor735 = frozenset([10, 16])
    FOLLOW_inits_in_constructor739 = frozenset([10])
    FOLLOW_RBRACE_in_constructor741 = frozenset([1])
    FOLLOW_var_in_vars784 = frozenset([1, 5])
    FOLLOW_COMMA_in_vars787 = frozenset([39])
    FOLLOW_var_in_vars789 = frozenset([1, 5])
    FOLLOW_NAME_in_var839 = frozenset([39])
    FOLLOW_NAME_in_var843 = frozenset([1])
    FOLLOW_NAME_in_names880 = frozenset([1, 5])
    FOLLOW_COMMA_in_names883 = frozenset([39])
    FOLLOW_NAME_in_names885 = frozenset([1, 5])
    FOLLOW_init_in_inits934 = frozenset([6])
    FOLLOW_SEMICOLON_in_inits936 = frozenset([1, 16])
    FOLLOW_THIS_in_init954 = frozenset([4])
    FOLLOW_DOT_in_init956 = frozenset([39])
    FOLLOW_NAME_in_init960 = frozenset([11])
    FOLLOW_ASSIGN_in_init962 = frozenset([39])
    FOLLOW_NAME_in_init966 = frozenset([1])
    FOLLOW_method_in_methods1003 = frozenset([1, 39])
    FOLLOW_NAME_in_method1040 = frozenset([39])
    FOLLOW_NAME_in_method1044 = frozenset([7])
    FOLLOW_LPAREN_in_method1046 = frozenset([8, 39])
    FOLLOW_vars_in_method1050 = frozenset([8])
    FOLLOW_RPAREN_in_method1052 = frozenset([9])
    FOLLOW_LBRACE_in_method1054 = frozenset([17])
    FOLLOW_RETURN_in_method1056 = frozenset([7, 16, 18, 39])
    FOLLOW_expression_in_method1060 = frozenset([6])
    FOLLOW_SEMICOLON_in_method1062 = frozenset([10])
    FOLLOW_RBRACE_in_method1064 = frozenset([1])
    FOLLOW_baseExpression_in_expression1107 = frozenset([1, 4])
    FOLLOW_dotExpression_in_expression1109 = frozenset([1, 4])
    FOLLOW_THIS_in_expression1137 = frozenset([4])
    FOLLOW_dotExpression_in_expression1139 = frozenset([1, 4])
    FOLLOW_NAME_in_baseExpression1176 = frozenset([1])
    FOLLOW_NEW_in_baseExpression1201 = frozenset([39])
    FOLLOW_NAME_in_baseExpression1203 = frozenset([7])
    FOLLOW_LPAREN_in_baseExpression1205 = frozenset([7, 8, 16, 18, 39])
    FOLLOW_expressions_in_baseExpression1207 = frozenset([8])
    FOLLOW_RPAREN_in_baseExpression1209 = frozenset([1])
    FOLLOW_LPAREN_in_baseExpression1238 = frozenset([39])
    FOLLOW_NAME_in_baseExpression1240 = frozenset([8])
    FOLLOW_RPAREN_in_baseExpression1242 = frozenset([7, 16, 18, 39])
    FOLLOW_expression_in_baseExpression1244 = frozenset([1])
    FOLLOW_DOT_in_dotExpression1280 = frozenset([39])
    FOLLOW_NAME_in_dotExpression1282 = frozenset([1, 7])
    FOLLOW_LPAREN_in_dotExpression1285 = frozenset([7, 8, 16, 18, 39])
    FOLLOW_expressions_in_dotExpression1287 = frozenset([8])
    FOLLOW_RPAREN_in_dotExpression1289 = frozenset([1])
    FOLLOW_expression_in_expressions1329 = frozenset([1, 5])
    FOLLOW_COMMA_in_expressions1332 = frozenset([7, 16, 18, 39])
    FOLLOW_expression_in_expressions1334 = frozenset([1, 5])
    FOLLOW_dotExpression_in_synpred9_fj1109 = frozenset([1])
    FOLLOW_dotExpression_in_synpred11_fj1139 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("fjLexer", fjParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
