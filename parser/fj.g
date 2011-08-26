/*
 * Copyright 2011 Jorge Lucangeli Obes
 *
 * This file is part of fj-llvm.
 *
 * fj-llvm is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * fj-llvm is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with fj-llvm. If not, see <http://www.gnu.org/licenses/>.
 */
grammar fj;

options {
  language  = Python;
  output    = AST;
  backtrack = true;
//  k        = 2;
}

tokens {
  DOT        = '.';
  COMMA      = ',';
  SEMICOLON  = ';';
  LPAREN     = '(';
  RPAREN     = ')';
  LBRACE     = '{';
  RBRACE     = '}';
  ASSIGN     = '=';
  UNDERSCORE = '_';
  CLASS      = 'class';
  EXTENDS    = 'extends';
  SUPER      = 'super';
  THIS       = 'this';
  RETURN     = 'return';
  NEW        = 'new';

  // Imaginary tokens for AST construction
  PROGRAM;
  CONSTRUCTOR;
  EMPTY_NAMES;
  EMPTY_VARS;
  EMPTY_EXPS;
  INIT;
  FIELD;
  FIELDS;
  NAMES;
  VARIABLE;
  VARIABLES;
  METHOD;
  METHODS;
  EXPRESSION;
  BASE_EXPRESSION;
  DOT_EXPRESSION;
  EXPRESSIONS;
}

@header {
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
}

/********* LEXER ******************************************************/
fragment
LETTER
  :
  'a'..'z'
  | 'A'..'Z'
  ;

fragment
DIGIT
  :
  '0'..'9'
  ;

fragment
ANY_CHAR
  :
  LETTER
  | UNDERSCORE
  | DIGIT
  ;

NAME
  :
  (
    LETTER
    | UNDERSCORE
  )
  ANY_CHAR*
  ;

WHITESPACE
  :
  (
    ' '
    | '\t'
    | '\r'
    | '\n'
  )+
  
  {
   $channel = HIDDEN;
  }
  ;

/********* PARSER *****************************************************/
program
  :
  classDefinition+ expression SEMICOLON
    ->
      ^(PROGRAM classDefinition+ expression)
  ;

classDefinition
  :
  CLASS cname=NAME EXTENDS pname=NAME LBRACE fields constructor methods RBRACE
    ->
      ^(CLASS $cname $pname fields constructor methods)
  ;

fields
  :
  (field SEMICOLON)*
    ->
      ^(FIELDS field*)
  ;

field
  :
  t=NAME n=NAME
    ->
      ^(FIELD $t $n)
  ;

constructor
  :
  cname=NAME LPAREN vs=vars RPAREN LBRACE SUPER LPAREN ns=names RPAREN SEMICOLON ins=inits RBRACE
    ->
      ^(CONSTRUCTOR $cname $vs $ns $ins)
  ;

vars
  :
  var (COMMA var)*
    ->
      ^(VARIABLES var+)
  |
    -> EMPTY_VARS
  ;

var
  :
  t=NAME n=NAME
    ->
      ^(VARIABLE $t $n)
  ;

names
  :
  NAME (COMMA NAME)*
    ->
      ^(NAMES NAME+)
  |
    -> EMPTY_NAMES
  ;

inits
  :
  (init SEMICOLON!)*
  ;

init
  :
  THIS DOT f=NAME ASSIGN v=NAME
    ->
      ^(INIT $f $v)
  ;

methods
  :
  method*
    ->
      ^(METHODS method*)
  ;

method
  :
  type=NAME name=NAME LPAREN vs=vars RPAREN LBRACE RETURN exp=expression SEMICOLON RBRACE
    ->
      ^(METHOD $type $name $vs $exp)
  ;

expression
  :
  baseExpression dotExpression*
    ->
      ^(EXPRESSION baseExpression dotExpression*)
  | THIS dotExpression+
    ->
      ^(EXPRESSION THIS dotExpression+)
  ;

baseExpression
  :
  NAME
    ->
      ^(BASE_EXPRESSION NAME) // variable
  | NEW NAME LPAREN expressions RPAREN
    ->
      ^(BASE_EXPRESSION NEW NAME expressions) // new object
  | LPAREN NAME RPAREN expression
    ->
      ^(BASE_EXPRESSION NAME expression) // cast
  ;

dotExpression
  :
  DOT NAME (LPAREN expressions RPAREN)? // field or method call
    ->
      ^(DOT_EXPRESSION NAME expressions?)
  ;

expressions
  :
  (expression (COMMA expression)*)
    ->
      ^(EXPRESSIONS expression+)
  |
    -> EMPTY_EXPS
  ;
