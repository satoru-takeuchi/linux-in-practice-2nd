#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <err.h>
#include <signal.h>
#include <time.h>

#define NSECS_PER_SEC 1000000000UL
#define NPROCESS 10000

int main(int argc, char *argv[])
{
	char *progname = argv[0];
	if (argc != 2) {
		fprintf(stderr, "使い方: %s <メモリ使用量[MiB]>\n",
			progname);
		exit(EXIT_FAILURE);
	}
	int n = NPROCESS;
	int load = atoi(argv[1]);
	char *buf = malloc(1024 * 1024 * load);
	int i;
	for (i = 0; i < load * 1024 * 1024; i += 4 * 1024)
		buf[i] = 0;
	struct timespec before, after;
	long sum = 0;
	for (i = 0; i < n; i++) {
		pid_t pid;
		pid = fork();
		if (pid == -1)
			err(EXIT_FAILURE, "fork() failed");
		else if (pid == 0)
			exit(0);
		wait(NULL);
	}
	return 0;
}
