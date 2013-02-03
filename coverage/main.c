#include <stdio.h>
#include <string.h>

static int paramGTThreeFunction()
{
    return 1;
}

static int paramLTFourFunction()
{
    return 2;
}

static int someFunction(int param)
{
    if (param > 3) {
        return paramGTThreeFunction();
    } else {
        return paramLTFourFunction();
    }
}

int main()
{
    int length = strlen("hey");
    if (someFunction(length) > 1) {
        printf("hello\n");
    }
    return 0;
}


