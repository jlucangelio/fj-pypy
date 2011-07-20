/*
 * Copyright 2011 Jorge Lucángeli Obes
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
}

@header {
# Copyright 2011 Jorge Lucángeli Obes
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
  classDefinition+ expression
  ;

classDefinition
  :
  CLASS NAME EXTENDS NAME LBRACE fields constructor methods RBRACE
  ;

fields
  :
  (field SEMICOLON)*
  ;

field
  :
  NAME NAME
  ;

constructor
  :
  NAME LPAREN vars RPAREN LBRACE SUPER LPAREN names RPAREN SEMICOLON inits RBRACE
  ;

vars
  :
  (var (COMMA var)*)?
  ;

var
  :
  NAME NAME
  ;

names
  :
  (NAME COMMA)*
  ;

inits
  :
  (init SEMICOLON)*
  ;

init
  :
  THIS DOT NAME ASSIGN NAME
  ;

methods
  :
  method*
  ;

method
  :
  NAME NAME LPAREN vars RPAREN LBRACE RETURN expression SEMICOLON RBRACE
  ;

expression
  :
  baseExpression
  | dotExpression
  ;

dotExpression
  :
  (
    baseExpression
    | THIS
  )
  (DOT NAME parenExpressions?)+ // field or method call
  ;

baseExpression
  :
  NAME
  | NEW NAME parenExpressions // new object
  | LPAREN NAME RPAREN expression // cast
  ;

parenExpressions
  :
  LPAREN (expression (COMMA expression)*)? RPAREN
  ;
