{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a6abb663-ebcd-476d-993c-f8586a56c07f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "v = 5  #variable declaration \n",
    "v"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "287cfb4c-aba9-48e1-9e39-61c1fe40cf39",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "140728920517176"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "id(v) # address of the memory location "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0b7242a1-0cff-43a7-a2c8-34486c3abdf2",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "cannot assign to literal here. Maybe you meant '==' instead of '='? (237110408.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[3], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    5 = v\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m cannot assign to literal here. Maybe you meant '==' instead of '='?\n"
     ]
    }
   ],
   "source": [
    "5 = v"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c731773d-fa37-4cdc-a0f5-cfe8c4d2ea28",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid decimal literal (1833180177.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[4], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    1v = 9\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid decimal literal\n"
     ]
    }
   ],
   "source": [
    "1v = 9 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f0bcebf6-0288-4008-b370-4155ecd97847",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "v1 = 9\n",
    "v1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "895969d3-b5f4-4424-89b3-2285e42861f4",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'A2' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[6], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m a2 \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m10\u001b[39m\n\u001b[1;32m----> 2\u001b[0m A2\n",
      "\u001b[1;31mNameError\u001b[0m: name 'A2' is not defined"
     ]
    }
   ],
   "source": [
    "a2 = 10\n",
    "A2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "bc9e719a-d46f-477b-8530-346a5866bec2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f9de9b37-6917-4c75-a35f-50ed64d3824a",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3413766975.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[8], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    v@ = 78\u001b[0m\n\u001b[1;37m       ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "v@ = 78\n",
    "v@ "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "bd1108ae-d586-439c-a010-713edb576bd5",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2797271626.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[9], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    v* = 78\u001b[0m\n\u001b[1;37m       ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "v* = 78\n",
    "v* "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1c4e7394-a88d-4da6-80cd-ceb1073c578c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "v_ = 10\n",
    "v_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ecf350d7-5a6d-466c-88fb-0e049f2ebdad",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3475252196.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[11], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    if = 78\u001b[0m\n\u001b[1;37m       ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "if = 78"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f0d30759-0913-4e33-9d0e-15be8f19d4a7",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2831858405.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[12], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    else = 80\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "else = 80"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a25324fe-c883-48b0-9aa7-75c4b0ebd68d",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (198613559.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[13], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    for = 89\u001b[0m\n\u001b[1;37m        ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "for = 89"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "8d3b4f97-95e9-4b37-9b6c-f9edd7e1bcb4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['False',\n",
       " 'None',\n",
       " 'True',\n",
       " 'and',\n",
       " 'as',\n",
       " 'assert',\n",
       " 'async',\n",
       " 'await',\n",
       " 'break',\n",
       " 'class',\n",
       " 'continue',\n",
       " 'def',\n",
       " 'del',\n",
       " 'elif',\n",
       " 'else',\n",
       " 'except',\n",
       " 'finally',\n",
       " 'for',\n",
       " 'from',\n",
       " 'global',\n",
       " 'if',\n",
       " 'import',\n",
       " 'in',\n",
       " 'is',\n",
       " 'lambda',\n",
       " 'nonlocal',\n",
       " 'not',\n",
       " 'or',\n",
       " 'pass',\n",
       " 'raise',\n",
       " 'return',\n",
       " 'try',\n",
       " 'while',\n",
       " 'with',\n",
       " 'yield']"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import keyword\n",
    "keyword.kwlist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "da087bf4-738e-4636-af1b-4d68951362d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "35"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(keyword.kwlist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "765c6ab2-23ac-4dbe-9d1c-3d84f71eea69",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (460896517.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[16], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    else = 6\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "else = 6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "1f11c375-49b4-4393-a92c-4d85cbf8e40a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ELSE = 6\n",
    "ELSE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "ac3b72ce-eb08-49c4-aa7e-c6311514cc84",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1257806994.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[18], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    for = 78\u001b[0m\n\u001b[1;37m        ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "for = 78\n",
    "for"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "44896c23-1347-4b63-8e6f-2de8157296f8",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'FOR' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[20], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m For \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m90\u001b[39m\n\u001b[1;32m----> 2\u001b[0m FOR\n",
      "\u001b[1;31mNameError\u001b[0m: name 'FOR' is not defined"
     ]
    }
   ],
   "source": [
    "For = 90\n",
    "FOR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "4c1255ca-5345-485b-8e27-a40a8af588af",
   "metadata": {},
   "outputs": [],
   "source": [
    "prefix = 'py'\n",
    "prefix = 'thon'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "2eb93d63-e5a6-4b6e-9bca-1765e0c25024",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'thon'"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prefix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "3eb071c5-b2de-413e-af83-30ec38c9a3fe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'python'"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'py' + prefix"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b2b61c2a-eba7-443c-b9ce-779486f302ac",
   "metadata": {},
   "source": [
    "# 19th "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "e210bf85-77d2-4051-8213-b7c744560341",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "32"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "i = 32\n",
    "i"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "17b35222-1fd4-4555-8d78-e2e19d0a7489",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "cca28076-4008-4df6-b29a-27984e27f49d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "110.32"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f = 110.32 \n",
    "f"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "95504b11-0b0d-46be-a1ca-00b26a7314bc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "42da120a-8090-4560-9e22-cb51d83d7fe5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f1 = 1e0\n",
    "f1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "05578de0-39e2-4732-82e2-cd784648732b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10.0"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f2 = 1e1\n",
    "f2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "23cf29ed-ec81-4766-bfa4-4be3f45944a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100.0"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f3 = 1e2\n",
    "f3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "9627ca3f-fdb4-43aa-be6d-f75e33ff49f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1000.0"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f4 = 1e3\n",
    "f4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "ef7b8fc5-77b1-46de-b215-38e78829f9cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1000.0"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f5 = 1E3\n",
    "f5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "018c5d10-fdd0-4158-8566-fb6685b88ed4",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 10 \n",
    "b = 20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "eb6b4d85-4d4c-4875-a289-75b9e2548dce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a + b\n",
    "a - b\n",
    "a * b\n",
    "a / b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "debc9045-e2f8-4e64-875c-a65669bdb065",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n",
      "-10\n",
      "200\n",
      "0.5\n"
     ]
    }
   ],
   "source": [
    "print(a+b)\n",
    "print(a-b)\n",
    "print(a*b)\n",
    "print(a/b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "3d64dfc7-1199-4039-a4a8-39e2a4e58850",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The addition of two number 20 and 30 is= 50\n"
     ]
    }
   ],
   "source": [
    "num1=20 \n",
    "num2=30\n",
    "add=num1+num2\n",
    "print('The addition of two number',num1,'and',num2,'is=',add)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "52de6a34-7717-4f6c-85a2-b7db09f6209f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The addition of 20 and 30 is= 50\n"
     ]
    }
   ],
   "source": [
    "num1=20 \n",
    "num2=30\n",
    "add=num1+num2\n",
    "print('The addition of {} and {} is= {}'.format(num1,num2,add))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "dc84df1e-cb9d-45b0-862d-98e688b5760f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The addition of 20 and 30 and 40 is= 90\n"
     ]
    }
   ],
   "source": [
    "num1=20 \n",
    "num2=30\n",
    "num3 = 40\n",
    "\n",
    "add=num1+num2+num3\n",
    "\n",
    "print('The addition of {} and {} and {} is= {}'.format(num1,num2,num3,add))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "2b8a2812-da73-476d-9472-b7aad142187d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1+2j)"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c = 1 + 2j\n",
    "c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "13b8ef9e-388a-47b6-a9b8-bb1585f9f5e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "complex"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "f2a0175a-3695-4664-bf32-b542695c7be2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1+2j)"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "ee2c4040-f583-459b-a919-cc5b201e8788",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.real"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "e7b2df37-1fbf-41e1-8b1e-3e53a2156cfa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.0"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.imag"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "d46ab1fd-a690-4091-b345-8d624ea84024",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(15+30j)\n",
      "(-5-10j)\n"
     ]
    }
   ],
   "source": [
    "c = 5 + 10j\n",
    "d = 10 + 20j\n",
    "\n",
    "print(c+d)\n",
    "print(c-d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "1c7f50fd-02ce-45e7-977b-4ae15489124b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def team():\n",
    "    print('helo')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "81c02c7d-2863-41b3-8d64-9348a952358b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5+10j)"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c2 = 5 + 10j\n",
    "c2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "3969ec8f-71e8-4405-89d0-17b9074fcc45",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'true' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[71], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m b \u001b[38;5;241m=\u001b[39m true\n\u001b[0;32m      2\u001b[0m b\n",
      "\u001b[1;31mNameError\u001b[0m: name 'true' is not defined"
     ]
    }
   ],
   "source": [
    "b = true\n",
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "e0f6407c-740c-4875-8e6c-aa1bedf17778",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['False',\n",
       " 'None',\n",
       " 'True',\n",
       " 'and',\n",
       " 'as',\n",
       " 'assert',\n",
       " 'async',\n",
       " 'await',\n",
       " 'break',\n",
       " 'class',\n",
       " 'continue',\n",
       " 'def',\n",
       " 'del',\n",
       " 'elif',\n",
       " 'else',\n",
       " 'except',\n",
       " 'finally',\n",
       " 'for',\n",
       " 'from',\n",
       " 'global',\n",
       " 'if',\n",
       " 'import',\n",
       " 'in',\n",
       " 'is',\n",
       " 'lambda',\n",
       " 'nonlocal',\n",
       " 'not',\n",
       " 'or',\n",
       " 'pass',\n",
       " 'raise',\n",
       " 'return',\n",
       " 'try',\n",
       " 'while',\n",
       " 'with',\n",
       " 'yield']"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import keyword\n",
    "keyword.kwlist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "179b56e1-e7b7-46f4-a277-ac3ab42f5e9d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b = True\n",
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "7859d3d8-e202-4cdc-a3a0-9b11ed8a6f7f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b1 = False\n",
    "b1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "8b1ce5a9-c9a4-4711-b2f9-d175446b18ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int(True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "deb9395d-c6fb-443c-bdef-5e7995177bd0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int(False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "9862b7b9-9fa4-4db3-b7ef-fafb10ddb280",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "True + True "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "14d8df3f-3da6-4be2-b566-468841baf29d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "True-False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "f3935549-41dc-489c-9fcb-f84b545d9a39",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "False-True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "e7b98eb9-8f7d-44b0-80f6-f94c2eb29aaf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "True-True*False+False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c5bed1b8-4382-4b41-8763-3d1ce8d1e8e2",
   "metadata": {},
   "outputs": [],
   "source": [
    "p = 20\n",
    "q = 20\n",
    "r = 20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "c324c094-2652-4cac-b002-9a04eb9be15f",
   "metadata": {},
   "outputs": [],
   "source": [
    "p = q = r = 20 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "c6f62b0e-c728-42b3-82f3-3c0c59ad9fc2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "140728920517656\n",
      "140728920517656\n",
      "140728920517656\n"
     ]
    }
   ],
   "source": [
    "print(id(p))\n",
    "print(id(q))\n",
    "print(id(r))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "481ff1c2-5063-4cfc-9a6a-d08529bffec6",
   "metadata": {},
   "outputs": [],
   "source": [
    "p1,q1,r1 = 20, 25, 30"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "060f5dd4-da68-4ed6-9d8f-1642ff7b63b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "140728920517656\n",
      "140728920517816\n",
      "140728920517976\n"
     ]
    }
   ],
   "source": [
    "print(id(p1))\n",
    "print(id(q1))\n",
    "print(id(r1))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "89b22486-355b-42b9-a3c1-bd251784f0a3",
   "metadata": {},
   "source": [
    "# string "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "cacf8628-4b45-4fda-99db-e037a84849e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello python'"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = 'hello python'\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "5096ef83-3e12-42ee-9299-cb314d7929f7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(s) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "0b660523-7fe8-4af6-b405-7d159fb77133",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello python'"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "67e20093-8718-49ff-acb5-05acb31405f1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'h'"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[0] #forward indexing "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "3101ad3a-38ff-41cc-9c19-cc0cbc2f4e77",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'n'"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[-1] # backward indexing "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "cd2a2dab-9d18-4df9-ba79-6da5502aa92f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello python'"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "46f08444-f7cf-42c7-b818-fb642cd667bb",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "string index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[102], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m s[\u001b[38;5;241m13\u001b[39m]\n",
      "\u001b[1;31mIndexError\u001b[0m: string index out of range"
     ]
    }
   ],
   "source": [
    "s[13]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "9c33739d-cbe4-4ed6-a37f-a106c16e5bd5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello python'"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "a0b32f30-9de7-465b-92d9-4f9bbc749062",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello python'"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "eae141ce-eb78-42aa-bd7e-d3928882be68",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello'"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[0:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "27c58725-7643-431c-a3dd-abfbf02c459f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'pyt'"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[6:9]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "4c23c68d-d744-4ecb-9435-5a62ec94386f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello python'"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "82fcabd7-2aaf-424d-9870-ba8948f42f87",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ytho'"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[-5:-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "57987234-01f8-4479-9fd7-abc1a1e01e17",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello python'"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "e211d358-5372-41e9-960d-398f42baa0eb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'llo python'"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[2:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "4bc4165b-b2f3-4e81-aea6-8b18f27e2018",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello python'"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "b3ad38db-7f30-4919-9ec5-61ace10aa7e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello '"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[:6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "71a01cfa-14b1-4b3a-aded-9944dd4d9435",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello python'"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "52522dc4-0daf-4537-83c4-2236bd107d8c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'nohtyp olleh'"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[::-1] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "94dcb470-418b-4851-bf38-d4cf3326a2be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello python'"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "3df45087-5caf-424e-9c5d-4dec13c2ef2e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hlph'"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[0:13:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "0906c408-4335-43b0-a098-30f2c0bf80df",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello python'"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "7a0cbaca-de46-4f30-b58d-4b8fe7b4bf61",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'h '"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s[0:10:5] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "8f67a6bb-ee9d-456c-9405-48d70c47487d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'nareshit'"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1 = 'nareshit' \n",
    "s1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4746a68f-c84a-4ee5-9e3d-f4a8cc616660",
   "metadata": {},
   "outputs": [],
   "source": [
    "s1[0:10]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "57b0de6e-dfb0-4f0c-bcc6-844a82ae60f3",
   "metadata": {},
   "source": [
    "# python data types we are completed\n",
    "# variable create we are completed"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "003c0016-7252-40c8-a6b8-29720ff683c3",
   "metadata": {},
   "source": [
    "# python type casting or type conversion"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "392da4d7-803d-492f-a2ec-1bd9d54f37fb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int(2.3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f0e7abfb-162d-48eb-a5d0-b2e30cae8a98",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'float' object cannot be interpreted as an integer",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28mint\u001b[39m(\u001b[38;5;241m2.3\u001b[39m, \u001b[38;5;241m4.5\u001b[39m)\n",
      "\u001b[1;31mTypeError\u001b[0m: 'float' object cannot be interpreted as an integer"
     ]
    }
   ],
   "source": [
    "int(2.3, 4.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7e6b1443-34c8-4e9e-afe2-cdaf1ff58dcc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int(True) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "29f7add5-5e6d-4427-b738-630fb34539e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int(False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "364cafe6-9c47-482b-b988-ac599f15d940",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "int() can't convert non-string with explicit base",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[5], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28mint\u001b[39m(\u001b[38;5;28;01mTrue\u001b[39;00m,\u001b[38;5;28;01mFalse\u001b[39;00m)\n",
      "\u001b[1;31mTypeError\u001b[0m: int() can't convert non-string with explicit base"
     ]
    }
   ],
   "source": [
    "int(True,False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5db4efd6-5a1b-43bd-af62-f36d698876c4",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'true' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[6], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28mint\u001b[39m(true)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'true' is not defined"
     ]
    }
   ],
   "source": [
    "int(true)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c58ca57b-0040-4763-86bc-992ef33e7dc4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "1\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "print(int(2.3)) # float - int \n",
    "print(int(True)) # bool - int \n",
    "print(int('10')) # string - int "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a37d3b86-c8fa-4740-a931-cde9e0948f05",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "int() argument must be a string, a bytes-like object or a real number, not 'complex'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[11], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;28mint\u001b[39m(\u001b[38;5;241m1\u001b[39m\u001b[38;5;241m+\u001b[39m\u001b[38;5;241m2\u001b[39mj))\n",
      "\u001b[1;31mTypeError\u001b[0m: int() argument must be a string, a bytes-like object or a real number, not 'complex'"
     ]
    }
   ],
   "source": [
    "print(int(1+2j)) # complex - int not possible "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "1310270a-3f83-457f-b66b-99633d5b6d10",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int('1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4b88568b-4c60-4f6e-82d5-dead06365c6f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.0\n"
     ]
    }
   ],
   "source": [
    "print(float(2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "9f543b58-a5ce-4d21-b354-d3044776e4e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.0\n"
     ]
    }
   ],
   "source": [
    "print(float(False))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "2ad731a8-9a17-4d7c-b4e2-db1b47f15258",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "float() argument must be a string or a real number, not 'complex'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[18], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;28mfloat\u001b[39m(\u001b[38;5;241m2\u001b[39m \u001b[38;5;241m+\u001b[39m \u001b[38;5;241m3\u001b[39mj))\n",
      "\u001b[1;31mTypeError\u001b[0m: float() argument must be a string or a real number, not 'complex'"
     ]
    }
   ],
   "source": [
    "print(float(2 + 3j))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "f0bb2c93-f076-4cfe-bacf-65ed22030b8a",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "could not convert string to float: 'two'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[19], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;28mfloat\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtwo\u001b[39m\u001b[38;5;124m'\u001b[39m))\n",
      "\u001b[1;31mValueError\u001b[0m: could not convert string to float: 'two'"
     ]
    }
   ],
   "source": [
    "print(float('two'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "6e5fb033-ab64-43fe-807e-92371f0940ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.0\n"
     ]
    }
   ],
   "source": [
    "print(float('2'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "8bd9a06a-7154-46e0-ace4-849a99722ed2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10+0j)"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "complex(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "6741e7eb-65af-4ffa-9bfa-2a4efca96223",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10+20j)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "complex(10,20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "999e5a44-e322-49cf-849a-f4ed85c0d80d",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "complex() takes at most 2 arguments (3 given)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[23], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28mcomplex\u001b[39m(\u001b[38;5;241m10\u001b[39m,\u001b[38;5;241m20\u001b[39m,\u001b[38;5;241m30\u001b[39m)\n",
      "\u001b[1;31mTypeError\u001b[0m: complex() takes at most 2 arguments (3 given)"
     ]
    }
   ],
   "source": [
    "complex(10,20,30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "a7b7ab0c-5693-4a71-a5f9-210433ed9483",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2.3+5.6j)"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "complex(2.3, 5.6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "6342b22b-9e01-4588-ba42-0cdd2b6dc177",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2.3+5j)"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "complex(2.3, 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "779c0fe3-93c1-46be-8823-b1a2c71f36da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5+2.3j)"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "complex(5, 2.3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "2e1a617e-44b1-44ee-a9ab-e5eab7058693",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0j"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "complex(False, False) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "806c9ce4-960a-4eac-ac3c-4ccc19bb09c7",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "complex() can't take second arg if first is a string",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[28], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28mcomplex\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m1\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;241m23\u001b[39m)\n",
      "\u001b[1;31mTypeError\u001b[0m: complex() can't take second arg if first is a string"
     ]
    }
   ],
   "source": [
    "complex('1', 23)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "14eefe33-eea5-4469-9930-b6d9065019c0",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "complex() can't take second arg if first is a string",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[30], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28mcomplex\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m1\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m23\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "\u001b[1;31mTypeError\u001b[0m: complex() can't take second arg if first is a string"
     ]
    }
   ],
   "source": [
    "complex('1', '23')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "eb033ea0-3a90-4868-91c0-7ba2618ef871",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1+0j)"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "complex('1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "78535038-cfe9-451d-9e50-3601c46ae66d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "print(bool(1))\n",
    "print(bool(1.1))\n",
    "print(bool(1+2j))\n",
    "print(bool('nit'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "2779ab3f-78f0-4741-a683-054808c6ab92",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bool( ) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "b3827e41-2a2b-469e-8dd5-776cb023c988",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2'"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "5f19cf0c-f59c-487c-bcf6-7de3a1148ed2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2.2'"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str(2.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "6b928f46-e298-4c42-8de7-f3bba7793115",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'True'"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str(True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "e30473b9-f13e-44cd-8cea-72c1f02e5e6a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'(1+2j)'"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str(1+2j)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "71cdfac5-2fe0-4cfa-8906-d8a12c89b182",
   "metadata": {},
   "source": [
    "# python type casting "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "f15f5b8c-81de-4d4f-aa45-857e4d77cb1a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 7.7\n",
    "type(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "770ead39-cbbd-47ae-941b-7913c2e2b8f7",
   "metadata": {},
   "source": [
    "# list datastructure "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6a7ed316-c3c7-43cb-83b7-b68e087a05f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l = [] \n",
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "a1c34319-87a7-44ca-95b9-a4c3ccbf505a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "644bca11-2585-453d-bb8c-cee8cbb80263",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'list'>\n"
     ]
    }
   ],
   "source": [
    "print(type(l))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "61fbc7bc-91d0-4e94-b1a9-96f575f4ef6d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e823cb47-16d4-4a3d-830f-3a05e6cc3e9f",
   "metadata": {},
   "outputs": [],
   "source": [
    "l.append(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e20927c9-9837-4ee4-9e2a-c73a9b87aa5c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 10]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0a11670e-76e5-4351-83d0-a334a74a3c7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "l.append(20)\n",
    "l.append(30)\n",
    "l.append(40)\n",
    "l.append(50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0b68b448-d92e-410a-b5ac-8481c8091527",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 10, 20, 30, 40, 50]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "1d0b7c21-1546-4e4e-b878-615f9336a6c2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f0ceb0ab-b692-4b3a-a9c7-58db6f6e7ba9",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "list.append() takes exactly one argument (2 given)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[9], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m l\u001b[38;5;241m.\u001b[39mappend(\u001b[38;5;241m10\u001b[39m,\u001b[38;5;241m20\u001b[39m)\n",
      "\u001b[1;31mTypeError\u001b[0m: list.append() takes exactly one argument (2 given)"
     ]
    }
   ],
   "source": [
    "l.append(10,20)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9696b5ab-971b-4be9-bb31-1c411f39fe2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ae2223f-910f-42c7-8e06-5e1128b3da1f",
   "metadata": {},
   "outputs": [],
   "source": [
    "l.append(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "6732e191-418a-4043-a089-2e4d79df2aa8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 10, 20, 30, 40, 50]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8d27be63-ef44-4b9d-8216-1cafab5ff542",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 10, 20, 30, 40, 50]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9ad7aa1f-7eac-4ddf-8d7c-dc144a454819",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "69150a51-f25f-4aca-8c7e-8502f2f5975d",
   "metadata": {},
   "outputs": [],
   "source": [
    "l[0] = 100 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "90ad3b34-e67e-4528-88d0-8a7ddff1ad08",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 20, 30, 40, 50]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "e8281838-2611-4128-97f7-e4812a28fccb",
   "metadata": {},
   "outputs": [],
   "source": [
    "l[-1] = -50"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "8cd70ea2-9e98-41dc-bdbc-b2123e0d4005",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 20, 30, 40, -50]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "7cbc14f2-6696-4641-a4aa-25c86120671f",
   "metadata": {},
   "outputs": [],
   "source": [
    "l1 = l.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "93acf276-998d-4f28-9d8d-d6e6b617f368",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 20, 30, 40, -50]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "9b0553de-793b-418f-9d99-618a73aae8bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[100, 10, 20, 30, 40, -50]\n",
      "[100, 10, 20, 30, 40, -50]\n"
     ]
    }
   ],
   "source": [
    "print(l)\n",
    "print(l1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "4f1b0955-115d-4234-8d09-198865da77be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l == l1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "88352ac6-8327-4115-abaf-5176f09467d6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "id(l) == id(l1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "9a23f3d4-3649-4800-9af3-53e5cfe41758",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "id(l) != id(l1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "db61dabf-f4c7-4714-ae1c-f053295c9f7e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 20, 30, 40, -50]"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "8156985a-6507-4b29-a049-4d375e6b53bd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.count(20) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "291abd63-6c28-479d-b7a5-36d15a7b0d8e",
   "metadata": {},
   "outputs": [],
   "source": [
    "l.append(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "d0bf493b-f3c6-4eb4-a50c-f9909e4e7fbf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 20, 30, 40, -50, 20]"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "e396bd64-a12c-4d68-aae8-510d1b699178",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.count(20) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "cd113134-7121-42d1-8917-e09c8c8b562c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 20, 30, 40, -50]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "3c367412-fc7f-429e-9694-0654da5caaa5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(l1) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "df6586f3-441b-4a52-b07b-ddfb640fd7cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 20, 30, 40, -50]"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "34bdb572-223a-4c9d-8cae-bf9fa1c35f79",
   "metadata": {},
   "outputs": [],
   "source": [
    "l1.clear()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "13be69c6-70d9-4fbb-8b07-24a37a385b16",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "d64377a4-b221-48a6-892e-65616690d50d",
   "metadata": {},
   "outputs": [],
   "source": [
    "del l1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "02c18583-579a-419c-99f2-c21ad8e067d3",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'l1' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[35], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m l1\n",
      "\u001b[1;31mNameError\u001b[0m: name 'l1' is not defined"
     ]
    }
   ],
   "source": [
    "l1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "a73277d6-2892-4ad5-9baa-e7d2f70ce8e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 20, 30, 40, -50, 20]"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "2e13e359-3aed-4f2a-b3a9-968656a131ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "l2 = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "d1706a0c-9dad-4d4e-9786-95c1ffcf22ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "l2.append(9)\n",
    "l2.append('nit')\n",
    "l2.append(True)\n",
    "l2.append(1+2j)\n",
    "l2.append(9.3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "0cc5d1f3-08e9-4c62-b12d-53050d99867d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 'nit', True, (1+2j), 9.3]"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "13fec934-3c83-417b-a66a-b7b9ba3e0996",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[100, 10, 20, 30, 40, -50, 20]\n",
      "[9, 'nit', True, (1+2j), 9.3]\n"
     ]
    }
   ],
   "source": [
    "print(l)\n",
    "print(l2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "02f8f4eb-1adf-44e1-aa89-1b7766607ba8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 20, 30, 40, -50, 20]"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "573a4fa9-7a01-4f93-81ee-470b3c542ed5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.index(100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "90c4f988-6f00-4d17-8a82-305c2a54ce56",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.index(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "a469f8c2-4811-4c7b-8fb1-8cdf06170ad8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 'nit', True, (1+2j), 9.3]"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "b4db48c7-ed98-49be-91c2-14ed2e61fee9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'nit'"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "964ec0a6-a840-4e84-9f62-e8a2178465bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'n'"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2[1][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "3b98768e-5c6a-45a6-97df-8baef81357dc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 'nit', True, (1+2j), 9.3]"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "c51c31a5-9b57-47d9-920a-3023e8d3cb49",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "nit\n"
     ]
    }
   ],
   "source": [
    "print(l2[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "ef069007-de92-4d53-a743-faf1f146063c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "n\n",
      "i\n",
      "t\n"
     ]
    }
   ],
   "source": [
    "print(l2[1][0])\n",
    "print(l2[1][1])\n",
    "print(l2[1][2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "d7911918-6e11-47df-a3ca-324a853d5a28",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 20, 30, 40, -50, 20]"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "31b33b2d-d0ad-4b3a-b5fa-768ddda72c2a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 20, 30, 40, -50, 20]"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l[:] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "b22775eb-4b6b-413a-9dcf-ba6822872145",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[30, 40, -50, 20]"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l[3:] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "87968041-7632-4729-bf1e-7897b91d3f7e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 20, 30, 40, -50, 20]"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "c5494ce3-052b-425d-a19f-cc5104934d61",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 20, 30, 40, -50, 20]"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l[:10] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "67fb0958-5487-4724-8ed3-0106214b3eb7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 20, 30, 40, -50, 20]"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "63af359d-d38a-4f2b-8647-875f9e772977",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 30, 20]"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l[0:8:3] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "48816ef9-fb41-4066-9e05-3078551e4175",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 'nit', True, (1+2j), 9.3]"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "2d86e6d9-001c-4b7e-9851-4b5359afd73f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['nit', (1+2j)]"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2[1:6:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "7a6ad0fc-50f9-4ca7-9ee4-e8555caa09cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 20, 30, 40, -50, 20]"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "7aeab353-569a-4987-b335-695b85d71c9f",
   "metadata": {},
   "outputs": [],
   "source": [
    "l.insert(15,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "d17cb9c7-7ac1-461a-9975-48665507a103",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 20, 30, 40, -50, 20, 2]"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "337f13c3-7fc1-4c3d-8c38-157fdcb9a86f",
   "metadata": {},
   "outputs": [],
   "source": [
    "l.insert(2, 15) # 2nd index position & 15 is called value "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "6d70929f-13e2-44bc-bbc5-5301ffbd2124",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 15, 20, 30, 40, -50, 20, 2]"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "25a3ea6c-462d-4896-a0f4-a7321654dd48",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "a9387629-fbb9-4ddf-9548-09cf53053e42",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 15, 20, 30, 40, -50, 20]"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "1dc49806-107f-482a-b3b2-ced6a849d31a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "69d83b2a-9e36-4e32-b315-43f3a4806b42",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 15, 20, 30, 40, -50]"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "cc8af3ac-a9af-4486-86ba-2b64c6d223ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-50"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "b955f00c-ea27-4c18-bd6e-b7b54fc70c29",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 15, 20, 30, 40]"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "397fc45f-a366-4c81-bdbd-127e80cb17b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 'nit', True, (1+2j), 9.3]"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "2765d3cb-c981-4890-bfe2-5ab6ff61b34c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1+2j)"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2.pop(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "a8efd11d-680e-4d47-ab82-34dac079fda2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 'nit', True, 9.3]"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "ec4ece49-cf5d-4832-a531-84961bacfcac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 'nit', True, 9.3]"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "e8540d7c-3a7c-4463-a444-b49877764ad3",
   "metadata": {},
   "outputs": [],
   "source": [
    "l2.remove('nit')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "1602da63-f59b-4d7e-b997-2c0d743bcb4c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, True, 9.3]"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3e8ddb4b-7c91-4640-9f3e-d83189f814bf",
   "metadata": {},
   "source": [
    "# 25th "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "841ff5ea-7f65-480a-a43e-25375f070449",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 15, 20, 30, 40]"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "838e7cc0-b959-4fe1-b429-5db962401e4f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "100 in l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "401af3d9-5fe7-4012-8028-deba045127b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "1000 in l "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "43d7445c-305e-49dc-a6e9-410064ffd4f7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 15, 20, 30, 40]"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "83fc77c5-c94b-48c0-8b66-5624427d7058",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "10\n",
      "15\n",
      "20\n",
      "30\n",
      "40\n"
     ]
    }
   ],
   "source": [
    "for i in l:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "711ea328-e0ee-4e63-9158-846c32d177b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 15, 20, 30, 40]"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "b01ac680-f477-467a-b550-be7435316bca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(0, 100)\n",
      "(1, 10)\n",
      "(2, 15)\n",
      "(3, 20)\n",
      "(4, 30)\n",
      "(5, 40)\n"
     ]
    }
   ],
   "source": [
    "for i in enumerate(l):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "4e0952db-23a8-4915-8fbc-180504a2b225",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[100, 10, 15, 20, 30, 40]\n",
      "[9, True, 9.3]\n"
     ]
    }
   ],
   "source": [
    "print(l)\n",
    "print(l2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "d0486008-ee27-4b08-b00b-033f22c1a68c",
   "metadata": {},
   "outputs": [],
   "source": [
    "l2.extend(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "5bf410d2-fe81-45d2-b54a-e294b340982f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, True, 9.3, 100, 10, 15, 20, 30, 40]"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "96b63499-84de-4edd-a583-2896342494fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 10, 15, 20, 30, 40]"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "f8af4ad1-6f2b-435b-bf50-2cdd64131491",
   "metadata": {},
   "outputs": [],
   "source": [
    "l.sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "0408d3df-96dd-4b1a-9d2d-32f703c8bc3b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 15, 20, 30, 40, 100]"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "4bd9d7dc-0909-4ac4-9ae6-9247c6100c5a",
   "metadata": {},
   "outputs": [],
   "source": [
    "l.sort(reverse=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "e31a35bc-9efa-404d-bf78-c35af9d53ab4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 40, 30, 20, 15, 10]"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "7a2dcb21-b465-4285-9e0c-d92cb353f261",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, True, 9.3, 100, 10, 15, 20, 30, 40]"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "da71d946-9634-462b-8416-fcdcc7bf94fb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2.3, 'nit', True]"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l3 = [1, 2.3, 'nit', True]\n",
    "l3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "2944347e-4841-40c4-9705-505f43bb1e82",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'<' not supported between instances of 'str' and 'float'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[99], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m l3\u001b[38;5;241m.\u001b[39msort()\n",
      "\u001b[1;31mTypeError\u001b[0m: '<' not supported between instances of 'str' and 'float'"
     ]
    }
   ],
   "source": [
    "l3.sort() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "4125bcc6-2a55-47de-b069-afddd05b86dd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'z', 'n', 'm']"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l4 = ['a', 'z', 'n', 'm']\n",
    "l4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "b53a3646-f8e7-465a-be5b-3ae1b8d66086",
   "metadata": {},
   "outputs": [],
   "source": [
    "l4.sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "e4c3fb53-2a9e-40b4-85f8-c934d2f731a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'm', 'n', 'z']"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "218bb5fc-8640-44f1-a460-97ee0dddbcaa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'm', 'n', 'z']"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "fb5de7ef-c87d-4fbd-ac60-d1f10dd27d50",
   "metadata": {},
   "outputs": [],
   "source": [
    "l4.reverse()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "d6b5e1e1-04cd-4cc4-bbdb-34808bc3b301",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['z', 'n', 'm', 'a']"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l4"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4e6d4e17-45ff-450c-8fe1-7eb88506b044",
   "metadata": {},
   "source": [
    "# LIST  Datastructure has completed "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17356a48-03cf-461b-83ce-b4747261c8a6",
   "metadata": {},
   "source": [
    "# ALL & ANY"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "bb8b978b-1d56-485b-a20d-54f6bb51afbc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 40, 30, 20, 15, 10]"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "c50c24d4-5a41-44ca-a5d9-868449584b4f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "all(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "10e008a5-ecb2-43e4-b989-2f3a0ef03338",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "any(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "ede7e662-3f44-4dbb-af15-b573b2927b3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "l.append(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "3264bf89-cbc7-4585-937a-07fb3ecd8d60",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 40, 30, 20, 15, 10, 0]"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "6998f062-9848-43f9-8348-7eb477ea1edf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "all(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "7703829a-1272-4eb3-b93c-a499070d910d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "any(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "8151f1aa-7b35-463a-b1e2-c591812f4b6b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "()"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t = () \n",
    "t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "bffa9ae6-6841-45df-bb8a-82c82b44b8b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "tuple"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "51aef105-b2e5-4637-9827-bc253c612f5a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10, 20, 30)"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t1 = (10, 20, 30)\n",
    "t1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "20d473b0-d75e-4893-b6cf-fc68fbef7c81",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('alex', 123456789, 'cizp567', 4567)"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sbi = ('alex', 123456789, 'cizp567', 4567)\n",
    "sbi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "id": "ef05fa22-2f39-4d51-a32b-2c5445d888f8",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'tuple' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[120], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m sbi[\u001b[38;5;241m1\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m20\u001b[39m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'tuple' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "sbi[1] = 20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "b1756568-87c6-4da0-aa95-3660aa49b9e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10, 20, 30)"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "cbe4ac4d-6fd4-4da5-aab5-5246e1a0a446",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t1.count(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "5d1275c1-12c7-4d66-870d-fd785b16296a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t1.index(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "729354c4-d9e2-4792-a3a7-92197f303c98",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10, 20, 30)"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "231c8ce8-720f-45b8-a6cc-7e750840b7e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "20\n",
      "30\n"
     ]
    }
   ],
   "source": [
    "for i in t1:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "c86513d6-7aa4-45c8-8370-bc0d3b1f36b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(0, 10)\n",
      "(1, 20)\n",
      "(2, 30)\n"
     ]
    }
   ],
   "source": [
    "for i in enumerate(t1):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "a7d4808b-04bb-40b7-9291-61616f36fe84",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10, 20, 30)"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "7c2984a4-6216-467f-9a32-88683994f3ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10, 20, 30, 10, 20, 30, 10, 20, 30)"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t2 = t1 * 3\n",
    "t2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "fc73a7f8-41ef-4c77-ba4a-d5ca44747376",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10, 20, 30, 10, 20, 30, 10, 20, 30)"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "d908b8a0-f593-4b68-99f3-53942acbfd50",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(30, 10, 20, 30)"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t2[2:6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "id": "83a57946-82c2-430f-8711-81024b55f89f",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'tuple' object has no attribute 'remove'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[134], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m t2\u001b[38;5;241m.\u001b[39mremove(\u001b[38;5;241m20\u001b[39m)\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'tuple' object has no attribute 'remove'"
     ]
    }
   ],
   "source": [
    "t2.remove(20)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f626b6dd-268a-4072-99e4-8fe333aae9d8",
   "metadata": {},
   "source": [
    "# tuple also we are completed "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "id": "bb0cd035-0b12-4265-a1e3-2a67eac93f02",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "()"
      ]
     },
     "execution_count": 136,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "06827878-cb14-4d01-96cc-251f5a6be92c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10, 20, 30)"
      ]
     },
     "execution_count": 137,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "id": "cbb075ec-e064-4e92-941c-8f64102c8d56",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10, 20, 30, 10, 20, 30, 10, 20, 30)"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "50450226-1d94-437c-bf12-f8e9869e592b",
   "metadata": {},
   "outputs": [],
   "source": [
    "del t2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "id": "753c5fc1-856c-4b72-94f5-e0cf17c68ef8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10, 19, 19)"
      ]
     },
     "execution_count": 141,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t1 = (0, 0, 0)\n",
    "t1= (10, 19, 19)\n",
    "t1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "6576e580-069c-4c6e-920f-18d73823bc4f",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'tuple' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[143], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m t1[\u001b[38;5;241m0\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m100\u001b[39m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'tuple' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "t1[0] = 100"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8de009b7-3cdd-45e5-b933-89aef413c76d",
   "metadata": {},
   "source": [
    "# 26th set "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f181cae8-4b79-40a5-9519-35ae1ac66a29",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{}"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = {} \n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "549d56de-3b2a-401c-a90d-749895e17bad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e1ebed10-7205-4a4c-a54a-49ef4039af53",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "set()"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1 = set()\n",
    "s1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b0add6aa-e983-458b-bb1e-e61f20f0a959",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "set"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(s1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "303902d9-ecda-474c-9ef5-90ef62d9099c",
   "metadata": {},
   "outputs": [],
   "source": [
    "s1.add(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "316e32be-11cc-41de-bae4-e4eb3c32d81c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{20}"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b5539b08-16b9-4d14-9ea5-b47acbc66d3d",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "set.add() takes exactly one argument (2 given)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[9], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m s1\u001b[38;5;241m.\u001b[39madd(\u001b[38;5;241m30\u001b[39m,\u001b[38;5;241m10\u001b[39m)\n",
      "\u001b[1;31mTypeError\u001b[0m: set.add() takes exactly one argument (2 given)"
     ]
    }
   ],
   "source": [
    "s1.add(30,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "29577c64-a1e5-458c-810e-c7ce18dacc13",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{20}"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9bfd4aba-cbbc-4e60-904e-6cbf4601ce22",
   "metadata": {},
   "outputs": [],
   "source": [
    "s1.add(10)\n",
    "s1.add(100)\n",
    "s1.add(25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3a9ab5bd-b232-4547-9cd5-b06bfcc064bd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{10, 20, 25, 100}"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "ed75d31e-3bf2-4808-8ea9-1c7b5bb22b7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "s1.add(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c17eaba5-ec32-4307-bec1-1bf897e33956",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{10, 20, 25, 100}"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "caff2213-63a4-4543-8af1-97f55c538e47",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'set' object is not subscriptable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[16], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m s1[\u001b[38;5;241m0\u001b[39m]\n",
      "\u001b[1;31mTypeError\u001b[0m: 'set' object is not subscriptable"
     ]
    }
   ],
   "source": [
    "s1[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "40d710a8-2c8b-47e0-ba23-5a8a501d1961",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{10, 20, 25, 100}"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "7b4f685e-4a19-4e30-9951-72deb447a097",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'set' object is not subscriptable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[18], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m s1[:]\n",
      "\u001b[1;31mTypeError\u001b[0m: 'set' object is not subscriptable"
     ]
    }
   ],
   "source": [
    "s1[:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "f08e005c-f05b-4693-8546-5a73f66c3aac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{10, 20, 25, 100}"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "ba03c795-22d5-45d4-ab23-939d3f2a163f",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unhashable type: 'list'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[20], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m s1\u001b[38;5;241m.\u001b[39madd([\u001b[38;5;241m1\u001b[39m,\u001b[38;5;241m2\u001b[39m,\u001b[38;5;241m3\u001b[39m])\n",
      "\u001b[1;31mTypeError\u001b[0m: unhashable type: 'list'"
     ]
    }
   ],
   "source": [
    "s1.add([1,2,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "491a8094-980d-4e3d-9a41-927e7c2b94b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "set()"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2 = set()\n",
    "s2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "43ef0068-6ca6-4170-bcae-b1976db5d98f",
   "metadata": {},
   "outputs": [],
   "source": [
    "s2.add(10)\n",
    "s2.add(1.2)\n",
    "s2.add(1+2j)\n",
    "s2.add(True)\n",
    "s2.add('nit')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "5016c4a0-b5aa-4e78-be3f-d8a6deace4cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{(1+2j), 1.2, 10, True, 'nit'}"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "d7da6cc3-03f2-4680-a795-8c935d109b33",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{100, 25, 10, 20}\n",
      "{1.2, True, (1+2j), 'nit', 10}\n"
     ]
    }
   ],
   "source": [
    "print(s1)\n",
    "print(s2) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "71becbc3-6c70-489a-9492-41630d9b7b94",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "id(s1) == id(s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "bc640d23-b000-4a04-9890-0bf4f80e6228",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{(1+2j), 1.2, 10, True, 'nit'}"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s3 = s2.copy()\n",
    "s3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "ba2e1399-4488-46f7-bed2-c36ba30aa8b4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2 == s3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "ca18abfe-d246-48e0-8583-ea71e2676096",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{100, 25, 10, 20}\n",
      "{1.2, True, (1+2j), 'nit', 10}\n",
      "{1.2, True, (1+2j), 'nit', 10}\n"
     ]
    }
   ],
   "source": [
    "print(s1)\n",
    "print(s2) \n",
    "print(s3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "f3505589-6246-42f7-a9da-5e1325d4606c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{(1+2j), 1.2, 10, True, 'nit'}"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "7f280788-2969-49d0-87ea-ed9c468447cc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.2"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "f7a480aa-c818-4169-8d93-d59572f17331",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{(1+2j), 10, True, 'nit'}"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "bbf3bcaa-37f8-49a7-aea3-8cc52ff427e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "31800d60-10d1-43b5-a4ee-b4f02d079304",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{(1+2j), 10, 'nit'}"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "86f78d11-55ad-4930-94bf-5cdfed84d14c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{10, 20, 25, 100}"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "86688060-748a-4203-8a39-c613ae702837",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{(1+2j), 10, 'nit'}"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "9676e60f-7202-4d36-85be-93cc238b3e44",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{}"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "aa23c877-6c6b-4f21-a5f1-b3959609e13d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{(1+2j), 1.2, 10, True, 'nit'}"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "03b0fe9f-f14d-49da-bda9-bfa4778f1824",
   "metadata": {},
   "outputs": [],
   "source": [
    "s3.remove((1+2j))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "659eec60-47cf-471a-b101-e5709eb8b249",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1.2, 10, True, 'nit'}"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "51063359-bedd-455a-b0c4-21cc0f36dfe6",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "1000",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[43], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m s3\u001b[38;5;241m.\u001b[39mremove(\u001b[38;5;241m1000\u001b[39m)\n",
      "\u001b[1;31mKeyError\u001b[0m: 1000"
     ]
    }
   ],
   "source": [
    "s3.remove(1000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "aaf6dba7-e9b4-48f6-9741-5a70c62794fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "s3.discard(1000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "7d0c290c-ef58-4c22-849e-cfa62334dfcd",
   "metadata": {},
   "outputs": [],
   "source": [
    "s3.discard(True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "c1d9f3c2-8a30-4dc1-b1c6-98f65cf6f528",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1.2, 10, 'nit'}"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "87e2ba20-e9a3-4328-aba8-e92d07967b05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{100, 25, 10, 20}\n",
      "{(1+2j), 'nit', 10}\n",
      "{1.2, 'nit', 10}\n"
     ]
    }
   ],
   "source": [
    "print(s1)\n",
    "print(s2)\n",
    "print(s3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "6c713e06-9035-4924-9214-ba51b0775d0c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "25\n",
      "10\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "for i in s1:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "47382bae-de3b-4a4e-bd99-a1c9f9dd9a35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(0, 100)\n",
      "(1, 25)\n",
      "(2, 10)\n",
      "(3, 20)\n"
     ]
    }
   ],
   "source": [
    "for i in enumerate(s1):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b5bfc89b-e4f9-405d-9111-f5b9247192a4",
   "metadata": {},
   "source": [
    "# set basic we are completed "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "9ee08f2b-aaf9-4099-8bb0-5626e1865024",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = {1,2,3,4,5}\n",
    "b = {4,5,6,7,8}\n",
    "c = {8,9,10}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "52fbd686-cfa3-4790-a3e1-f5a9307c874e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 5, 6, 7, 8}"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.union(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "2b4337ae-d75c-4881-8706-c7f63bef0d95",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 5, 8, 9, 10}"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a | c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "3cd8fb48-90fe-4257-8647-d1b7e5f99caf",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = {1,2,3,4,5}\n",
    "b = {4,5,6,7,8}\n",
    "c = {8,9,10}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "45260514-3956-40fa-a7c4-f62ee106486e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{4, 5, 6, 7, 8, 9, 10}"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b | c "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "c27c942d-c004-4a75-a175-213582d7cc41",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a | b | c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "5aedb097-8362-49ee-80c1-9f57d3e237c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 4, 5}\n",
      "{4, 5, 6, 7, 8}\n",
      "{8, 9, 10}\n"
     ]
    }
   ],
   "source": [
    "print(a)\n",
    "print(b)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "40df1391-2989-4f3e-9fab-1a30c89619bb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3}"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.difference(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "3f14f393-7393-49e6-b59f-fbd23fe9b311",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 5}"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.difference(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "a5f24513-8068-406c-9e94-e02f42ddd7fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 4, 5}\n",
      "{4, 5, 6, 7, 8}\n",
      "{8, 9, 10}\n"
     ]
    }
   ],
   "source": [
    "print(a)\n",
    "print(b)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "d93eaa60-3271-4475-aa44-34b49e9f20ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{8, 9, 10}"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.difference(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "bb04ff86-a632-4812-8e4c-d7ed7b4f8bae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{9, 10}"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.difference(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "139e38b7-dbc1-402b-a402-6d8a53517089",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "set()"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.difference(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "e5f8940c-6366-4341-b0f6-89968e71a852",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 4, 5}\n",
      "{4, 5, 6, 7, 8}\n",
      "{8, 9, 10}\n"
     ]
    }
   ],
   "source": [
    "print(a)\n",
    "print(b)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "7e309155-225f-47c1-9090-e402793d76b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{8, 9, 10}"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c - a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "c20b86c6-e10e-487f-8b2c-7b84ae68d0a0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 6, 7, 8}"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.symmetric_difference(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "baa33d8a-e1cf-4140-b7b0-7713d3861436",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 4, 5}\n",
      "{4, 5, 6, 7, 8}\n",
      "{8, 9, 10}\n"
     ]
    }
   ],
   "source": [
    "print(a)\n",
    "print(b)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "fe61f0e3-8d77-46f9-895d-ef760b3c180d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 5, 8, 9, 10}"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c ^ a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "5556445b-d91f-469e-acc4-dce15464d6f6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 6, 7, 8}"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b ^ a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "7065b703-0990-41c1-8b7d-fcdc5cbcf274",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 4, 5}\n",
      "{4, 5, 6, 7, 8}\n",
      "{8, 9, 10}\n"
     ]
    }
   ],
   "source": [
    "print(a)\n",
    "print(b)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "71081941-2146-48cd-bdbb-f4ba51b2f18b",
   "metadata": {},
   "outputs": [],
   "source": [
    "a.symmetric_difference_update(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "2caaa8fd-56ee-4312-acb6-14160fa34956",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 6, 7, 8}\n",
      "{4, 5, 6, 7, 8}\n",
      "{8, 9, 10}\n"
     ]
    }
   ],
   "source": [
    "print(a)\n",
    "print(b)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "12a3fe96-b0f1-4c36-91f7-f0662cfd5d02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 6, 7, 8}\n",
      "{4, 5, 6, 7, 8}\n",
      "{8, 9, 10}\n"
     ]
    }
   ],
   "source": [
    "print(a)\n",
    "print(b)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "2fb0abd2-1dfd-4710-b82d-d6fce1c5859b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{6, 7, 8}"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.intersection(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "03942cf4-8b7c-407b-8294-8c301d0ffd86",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{8}"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b & c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "804003fd-aadf-409e-95fe-ad7149b8e9e4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{8}"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a & b & c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "28cc0e40-709e-47a4-9c9d-4e835332e050",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 6, 7, 8}\n",
      "{4, 5, 6, 7, 8}\n",
      "{8, 9, 10}\n"
     ]
    }
   ],
   "source": [
    "print(a)\n",
    "print(b)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "980a5ec4-a8ea-4ab4-bd1d-52bda4707936",
   "metadata": {},
   "outputs": [],
   "source": [
    "c.intersection_update(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "3bee39c6-2029-4de7-a112-036746cfe6cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{8}"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "bf4a651b-5664-4a32-b730-bd4123611c6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "A1 = {1,2,3,4,5,6,7,8,9}\n",
    "B1 = {3,4,5,6,7,8}\n",
    "C1 = {10,20,30,40}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "8bfd1d23-6658-408d-8728-d6a33d55d11a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "B1.issubset(A1) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "2f3f87fe-c98d-4f9a-a791-034bfc1a1893",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A1.issuperset(B1) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "3666a94e-07f1-46d6-a36f-7b1a3d971b16",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "C1.isdisjoint(A1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "b12f7fa4-f20e-416c-9457-0ba6ee346182",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "C1.isdisjoint(B1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "56023e18-18cf-405d-a177-2c6e6c8a0d90",
   "metadata": {},
   "outputs": [],
   "source": [
    "A2 = {15,25,35,45}\n",
    "B2 = {3,4,5,6,7,8}\n",
    "C2 = {10,20,30,40}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "959ba7f2-850e-44a6-b082-386cfde48150",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "B2.issubset(A2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "77d6d075-3330-4745-9f58-1d1cd2391b59",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A2.issuperset(B2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "28fadc81-fdf8-4764-828b-9f2df3e2cec1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "C2.isdisjoint(A2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "3c0f6cc1-4e8a-4551-b5c3-bc8386f48d19",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "C2.isdisjoint(B2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "9e10924b-2f8b-43ee-8749-5dbbba50ee14",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "1a5212b6-1712-4b3f-8b47-85c011ed7100",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{}"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "a502e0cb-266c-4b51-ab3f-a155a851e5cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "2c2751b5-259e-4641-9d0b-77e4fcab37b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1: 'one', 2: 'two', 3: 'three'}"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d1 = {1:'one', 2:'two', 3: 'three'}\n",
    "d1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "9d106e93-21e7-454d-bb25-77108433846a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'one': 1, 'two': 2, 'three': 3}"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d2 = {'one' : 1, 'two':2, 'three' : 3}\n",
    "d2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "7c0a1f66-899c-4f5a-9108-e1aff086be6f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'one': 1, 'two': 2, 'three': 3}"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "3de0f08c-614e-4bc4-85d6-311a29f3b150",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['one', 'two', 'three'])"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d2.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "a9a06df3-a148-4d38-ae74-cd378869a176",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values([1, 2, 3])"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d2.values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "9304f1e8-2b16-40a7-858e-c302b9af1466",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'one': 1, 'two': 2, 'three': 3}"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "62206a10-3a89-4951-b465-217aa1217970",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_items([('one', 1), ('two', 2), ('three', 3)])"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d2.items()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "4eebbb0a-8ced-4aeb-8af4-dd52d24f6991",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(d2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88de3573-bcec-461f-ac64-f3858992280a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
