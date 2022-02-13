<h1>fd - File Descriptor</h1>

ssh to the machine

```
fd@pwnable:~$ ls -l
total 16
-r-sr-x--- 1 fd_pwn fd   7322 Jun 11  2014 fd
-rw-r--r-- 1 root   root  418 Jun 11  2014 fd.c
-r--r----- 1 fd_pwn root   50 Jun 11  2014 flag
```

* fd.c
```c
#include <stdio.h>18C (Why is there 18C? must be a mistake...)
#include <stdlib.h>
#include <string.h>
char buf[32];
int main(int argc, char* argv[], char* envp[]){
        if(argc<2){
                printf("pass argv[1] a number\n");
                return 0;
        }
        int fd = atoi( argv[1] ) - 0x1234;
        int len = 0;
        len = read(fd, buf, 32);
        if(!strcmp("LETMEWIN\n", buf)){
                printf("good job :)\n");
                system("/bin/cat flag");
                exit(0);
        }
        printf("learn about Linux file IO\n");
        return 0;

}
```

Executing `./fd` outputs:

```bash
fd@pwnable:~$ ./fd
pass argv[1] a number
fd@pwnable:~$ ./fd 1000
learn about Linux file IO
```

Looking back at the source code, I see [atoi()](https://www.tutorialspoint.com/c_standard_library/c_function_atoi.htm) which turns out to be a char array pointer (or string?) to integer.<br> and that it is being substracted by an hexadecimal (base-16) value `0x1234` which is equal to `4660` in decimal (base-10).

So I enter 4660 and

```bash
fd@pwnable:~$ ./fd 4660

```

Now I am getting to the [read()](https://man7.org/linux/man-pages/man2/read.2.html) which is a function that takes a file descriptor, a buffer, and a count (length of the buffer)<br>
But what is a file descriptor? [Wikipedia got me covered](https://en.wikipedia.org/wiki/File_descriptor)<br>
Apparently, it is an identifier for a file or I/O.<br>
The standard file descriptors are:
* 0 STDIN_FILENO
* 1 STDOUT_FILENO
* 2 STDERR_FILENO

So if we get the the file descriptor to be equal to `0` we can input whatever we want into the buffer!<br>
Below the read() function we can see the [strcmp()](https://www.programiz.com/c-programming/library-function/string.h/strcmp) which well, compares between 2 strings.<br> If the 2 strings are equal, then the strcmp() function will output 0, which is equal to false. That is why there is a ! sign before, to flip the boolean from true to false and vice versa.<br>

Since we we need to input "LETMEWIN\n" in order to get a true value in the if statement, we wish to enter 4660 as the argument to the executable and then write "LETMEIN" and press enter (which acts as '\n') to get the flag!

```bash
fd@pwnable:~$ ./fd 4660
LETMEWIN
good job :)
mommy! I think I know what a file descriptor is!!
```

And voilà! We've gotten the flag.
We've taken our first step into pwnable.kr challenges.
