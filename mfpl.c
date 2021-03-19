#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[])
{
	if(argc < 2)
	{
		system("python3 src/main.py");
	}
	else if(argc == 2)
	{
		if(strcmp(argv[1], "-h") == 0)
		{
			printf("A simple but frustating esotric programming language. This implementation is called PyMFPL\n");
		}
		else if(strcmp(argv[1], "--help") == 0)
		{
			printf("A simple but frustating esotric programming language. This implementation is called PyMFPL\n");
		}
		else if(strcmp(argv[1], "-v") == 0)
		{
			system("python3 src/main.py -v");
		}	
		else
		{
			char *temp = "python3 src/main.py ", *com;
			sprintf(com, "%s%s", temp, argv[1]);
			system(com);
		}
	return 0;
}
