#include <unistd.h>
#include <stdio.h>
/**
 * infinite_while - check the code for
 * Return: Always EXIT_SUCCESS.
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
 * main - check the code for
 * Return: Always EXIT_SUCCESS.
 */
int main(void)
{
	pid_t zombie;
	int i;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		printf("Zombie process created, PID: %d\n", zombie);
	}
	infinite_while();
	return (0);
}
