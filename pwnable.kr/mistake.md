First the program checks if it can read the password file at `/home/mistake/password`

Then it prints "Do not bruteforce...",
and after that the function sleeps for a while, and then it requests input for the first password, then the second passowrd

It then XORs the second password and uses the strncmp() funciton to compare between the 2 passwords.

Since the XOR is only by 1, we can put whatever bits we want except for the least significant bit

```
XXXXXXX0    XXXXXXX1
00000001    00000001
--------    --------
XXXXXXX1    XXXXXXX0
```

So we can enter whatever password we want (with a length of 10) and it's XOR by 1 value to get the flag

Here's a simple program that does just that.

```c
#include <stdio.h>


void xor(char* str, int len)
{
    for (int i=0;i<len;i++)
    {
        printf("%c  >>  ", str[i]);
        str[i] ^= 1;
        printf("%c\n", str[i]);
    }
}

int main(int argc, char* argv[])
{
    char buffer[10];
    printf("Enter password: ");
    scanf("%10s", buffer);
    xor(buffer, 10);
    printf("Password: %s\n", buffer);

    return 0;
}
``` 
<h3>Example:</h3><br>

```
PS C:\Users\User\Desktop\learning\pwnable> gcc .\test.c
PS C:\Users\User\Desktop\learning\pwnable> .\a.exe     
Enter password: helloworld
h  >>  i
e  >>  d
l  >>  m
l  >>  m
o  >>  n
w  >>  v
o  >>  n
r  >>  s
l  >>  m
d  >>  e
Password: idmmnvnsme
```

<h3>In practice:</h3><br>

```
mistake@pwnable:~$ ./mistake
do not bruteforce...
helloworld
input password : idmmnvnsme
Password OK
Mommy, the operator priority always confuses me :(
```
