#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 *  * infinite - a function that runs forever and returns nothing
 *   * Return: 0 in the end
 *    */
int infinite(void)
{
		while (1)
					sleep(1);
			return (0);
}

/**
 *  * main - the entry to a program that creates 5 zombie process
 *   * Return: 0 on success
 *    */
int main(void)
{
		int child = 0;
			pid_t pid;

				while (child < 5)
						{
									pid = fork();
											if (!pid)
															break;
													printf("Zombie process created, PID: %i\n", (int)pid);
															child++;
																}
					if (pid != 0)
								infinite();
						return (0);
}
