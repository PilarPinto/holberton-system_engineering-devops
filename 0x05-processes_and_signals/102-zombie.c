#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while -Is a infinite while with sleep
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Is the main function
 * Return: when is sucess
 */
int main(void)
{
	int ind = 0;
	pid_t chi;

	while (ind < 5)
	{
		chi = fork();
		if (chi)
			dprintf(1, "Zombie process created, PID: %d\n", chi);
		else
			return (0);
		ind++;
	}
	infinite_while();
	return (0);
}
