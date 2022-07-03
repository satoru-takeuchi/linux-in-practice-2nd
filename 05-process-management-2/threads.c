#include <unistd.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <err.h>
#include <time.h>

#define NSECS_PER_SEC 1000000000UL
#define NTHREAD 10000

static void * thread_fn(void *arg)
{
	return NULL;
}

int main(int argc, char *argv[])
{
	char *progname = argv[0];
	if (argc != 2) {
		fprintf(stderr, "使いかた: %s <メモリ使用量[MiB]>\n",
			progname);
		exit(EXIT_FAILURE);
	}
	int n = NTHREAD;
	int load = atoi(argv[1]);
        char *buf = malloc(1024 * 1024 * load);
        int i;
        for (i = 0; i < load * 1024 * 1024; i += 4 * 1024)
                buf[i] = 0;
	long sum = 0;
	for (i = 0; i < n; i++) {
		pthread_t tid;
		if (pthread_create(&tid, NULL, thread_fn, NULL))
			err(EXIT_FAILURE, "pthread_create() failed");
	}
	exit(EXIT_SUCCESS);
}
