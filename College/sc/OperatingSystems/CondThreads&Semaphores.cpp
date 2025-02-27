//Zayne Bonner
#include <string.h>                     // for strerror()
#include <stdio.h>                      // for printf ()                 
#include <signal.h>                     // for interrupt handling     
#include <unistd.h>                     // for "alarm"                 
#include <pthread.h>                    // pthread implementation  
#include <time.h>						// for timer
#include <stdlib.h>						// not sure, just felt right to include


#define SLOWDOWN_FACTOR    6000000     /* child thread display slowdown */
#define SCHEDULE_INTERVAL  1           /* scheduling interval in second */



// GLOBAL VARIABLES ###############################
int schedule_vector[5];            // the required thread schedule vector
pthread_mutex_t  condition_mutex;  // pthread mutex_condition
pthread_cond_t       t_condition[6];  // pthread condition
int                 loop_counter;  // loop counter for the interrupt handler
int					   active= -1; 
// END GLOBALS ####################################
void clock_interrupt_handler(int num);
void* child_thread_routine (void * arg);


/* The main (the parent thread) -------------------------------------- */
int main(int argc,char *argv[])
{   schedule_vector[0] = 2;        // the first thread
    schedule_vector[1] = 4;        // the second thread
    schedule_vector[2] = 0;        // the third thread
    schedule_vector[3] = 3;        // the fourth thread
    schedule_vector[4] = 1;        // the fifth thread

	pthread_t        thread;       // thread IDs (assigned by OS)
    pthread_attr_t     attr;       // thread attributes 
    int                 ids[4];       // thread arguments

    int i = 0;   // the loop counter for the parent thread    
    loop_counter = 0; // initialize the loop counter for the interrupt hanlder

    /* specify the clock interrupt to be sent to this process --- */
    signal(SIGALRM,(clock_interrupt_handler));

    /* set the interrupt interval to 1 second --- */
    alarm(SCHEDULE_INTERVAL);

    /* initialize pthread mutex variables ----------------------- */
    pthread_mutex_init (&condition_mutex, NULL);

    /* initialize pthread condition variables ------------------- */
	for(int z=0; z<=4;z++)
    	pthread_cond_init (&t_condition[z], NULL);
		

	// create child threads ################
		for(int j=0; j<=4;j++){
    		pthread_create (                 // xreate a child thread   
               &thread,              // thread ID (system assigned)
               NULL,                 // default thread attributes
               (child_thread_routine), // thread routine name
               &schedule_vector[j]);                // arguments to be passed
		}
	// #####################################


    /* inifinite loop for the parent thread ===================== */
    while (1)
    {
       /* for debug use only ------------------------------------ */
       //printf("the parent thread is here (%d) ....\n", i);

       /* just for keeping the parent thread sleep forever ------ */
       pthread_mutex_lock(&condition_mutex);
          pthread_cond_wait(&t_condition[5], &condition_mutex);
       pthread_mutex_unlock(&condition_mutex);

       /* increase the loop counter ----------------------------- */
       i = i + 1; 
    }

    /* The main (parent) thread terminates itself ------------------ */
    return(0);
}

/* child thread implementation ---------------------------------------- */
void* child_thread_routine (void * arg)  {

   int  myid = *(int *) arg;   // child thread number (not ID)
   int  my_counter = 0;        // local loop counter

   /* -------------------------------------------------------- */
   /* if you would like to add your local variable(s), you can */
   /* add one (them) here.                                     */
   /* -------------------------------------------------------- */

   /* declarare the start of this child thread (required) ---- */
   printf("Child thread %d started ...\n", myid);   

   /* -------------------------------------------------------- */
   /* if you would like to peform some initialization to your  */
   /*  local variable(s), you can do so here.                  */


		pthread_mutex_lock(&condition_mutex);
				pthread_cond_wait(&t_condition[myid], &condition_mutex);
        pthread_mutex_unlock(&condition_mutex);


   /* infinite loop (required) ------------------------------- */
   while (1)
   {
      /* declare working of myself (required) ---------------- */
      my_counter ++;
      if ((my_counter % SLOWDOWN_FACTOR) == 0)
      {  printf("Thread: %d is running ...\n", myid);  }

   /* -------------------------------------------------------- */
   /* Here is your working space (to implement some mechanism) */
   /* to synchronize with the interrupt handeler.              */
   /* -------------------------------------------------------- */
		pthread_mutex_lock(&condition_mutex);
    		if(myid != schedule_vector[active]){
				pthread_cond_wait(&t_condition[myid], &condition_mutex);
			}
        pthread_mutex_unlock(&condition_mutex);   
	}
}
/* END OF A CHILD THREAD ============================================== */



/* The interrupt handler for SIGALM interrupt ---------------------- */
void clock_interrupt_handler(int num){
pthread_mutex_lock(&condition_mutex);

   	/* to be displayed at each time I woke up ---------------- */
   		printf("I woke up on the timer interrupt (%d) .... \n", loop_counter);
		active=(active+1) %5;
		pthread_cond_signal(&t_condition[schedule_vector[active]]);

	pthread_mutex_unlock(&condition_mutex);
	loop_counter++; /* increase the loop counter for the interrupt handler --- */

   /* scheduler wakes up again one second later -------------------- */  
   alarm(SCHEDULE_INTERVAL);
	
}