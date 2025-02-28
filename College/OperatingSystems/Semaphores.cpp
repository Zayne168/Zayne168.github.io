/*
	Zayne Bonner
	800756759
	The Packet given has a bit of ambiguity. The output does not show the 
	""..would like to read" and "..would like to update" messages, however it also says its required, 
	so I have them in my code, but commented out, so if you would like them, please uncomment them.
*/
#include <stdio.h>
#include <stdlib.h> 
#include <sys/types.h>
#include <unistd.h> 
#include <string.h> 
#include <stdbool.h>
#include <sys/wait.h>
#include <time.h>
// the followings are for semaphores ----- 
#include <sys/sem.h>
#include <sys/ipc.h>

// the followings are for shared memory ----
#include <sys/shm.h>

#define NUM_REPEATS           10      // number of loops for the high-priority processes
#define MAX_MSG_SIZE          512      // the max. msg size (this paramter will NOT be changed for testing)

				       //for usleep(*time*) usage -> I use microsleep so that 300000 = .3 seconds. if millisleep it would be 30 seconds I believe?.
#define H1_TIME_IN         300000      //   300 ms = 0.300 seconds (inside of the critical section)
#define H1_TIME_OUT       2000000      //  2000 ms = 2.000 seconds (outside of the critical section)

#define H2_TIME_IN         300000      //   300 ms = 0.300 seconds (inside of the critical section)
#define H2_TIME_OUT       3000000      //  2000 ms = 2.000 seconds (outside of the critical section)

#define L1_TIME_IN        1000000      //  1000 ms = 1.000 seconds (inside of the critical section)
#define L1_TIME_OUT        200000      //   200 ms = 0.200 seconds (outside of the critical section)

#define L2_TIME_IN        1000000      //  1000 ms = 1.000 seconds (inside of the critical section)
#define L2_TIME_OUT        200000      //   200 ms = 0.200 seconds (outside of the critical section)

#define L3_TIME_IN        1000000      //  1000 ms = 1.000 seconds (inside of the critical section)
#define L3_TIME_OUT        200000      //   200 ms = 0.200 seconds (outside of the critical section)


#define SEM_KEY        8310       // the semaphore key
#define SEM_KEY2       8810       // the semaphore key 2
#define SEM_KEY3       9310
#define SEM_KEY4       9610
#define SHM_KEY        6315       // the shared memory key 

struct my_mem {
        long int counter;
	char MSG[MAX_MSG_SIZE];
	bool hpRunning;
};// shared memory definition ----

void semWait(int sem_id) {
    struct sembuf operations[1];
    operations[0].sem_num = 0;
    operations[0].sem_op = -1; // Wait operation
    operations[0].sem_flg = 0;  
    if (semop(sem_id, operations, 1) != 0) {
        fprintf(stderr, "P-OP(wait) failed ....\a\n");
    }
}

void semSignal(int sem_id) {
    struct sembuf operations[1];
    operations[0].sem_num = 0;
    operations[0].sem_op = 1; // Signal operation
    operations[0].sem_flg = 0;  
    if (semop(sem_id, operations, 1) != 0) {
        fprintf(stderr, "V-OP(signal) failed ...\a\n");
    }
}
//semaphore operations as function for readability 


void highPriority(struct my_mem *p_shm, int sem_id, int sem_id3, int id) {

	for(int i=0; i<NUM_REPEATS; i++){

	   if(id==1)
		usleep(H1_TIME_OUT);
	   else
		usleep(H2_TIME_OUT);
	   p_shm->hpRunning = true;
	   //printf("H%d would like to update..\n",id);				//COMMENTED OUT
	   semWait(sem_id);//start critical section ###############
		printf("H%d starts updating..\n",id);
		if(i==0)
		   for(int k=0; k<4;k++)
	   		semSignal(sem_id3);
		if(id==1)
		   strncpy(p_shm->MSG, "I am H1", MAX_MSG_SIZE);
		else
		   strncpy(p_shm->MSG, "I am H2", MAX_MSG_SIZE);
		if(id==1)
		   usleep(H1_TIME_IN);
	   	else
		   usleep(H2_TIME_IN);

		printf("H%d finishes updating...\n",id);
	   semSignal(sem_id);//end critical section ################
	   //usleep(10*(rand() % 50000));
	}
   p_shm->hpRunning = false;
}

void lowPriority(struct my_mem *p_shm, int sem_id, int sem_id2, int id) {
	while(p_shm->hpRunning){

	   if(id==1) 				//HERE IS "RANDOM SLEEP"
		usleep(L1_TIME_OUT);
	   else if(id==2)
		usleep(L2_TIME_OUT);
	   else
		usleep(L3_TIME_OUT);
	   //printf("L%d would like to read...\n",id);				//COMMENTED OUT
	   semWait(sem_id2);
	   p_shm->counter++;
	   if(p_shm->counter==1)
		semWait(sem_id);
	   semSignal(sem_id2);
	   printf("L%d starts reading...\n",id);
	    printf("\t\tL%d READ:%s\n",id,p_shm->MSG);
	      if(id==1)
		usleep(L1_TIME_IN);
	      else if(id==2)
		usleep(L2_TIME_IN);
	      else
		usleep(L3_TIME_IN);
	    printf("L%d finishes reading...\n",id);
	   semWait(sem_id2);
	   p_shm->counter--;
	   if(p_shm->counter==0)
		semSignal(sem_id);
	   semSignal(sem_id2);
	  //usleep(10*(rand() % 50000));

	}
}


int main (void)
{
printf("the parent process starts ...\n");
   pid_t  process_id;     
   int id = 0;

   int    sem_id,sem_id2,sem_id3,sem_id4;                // the semaphore IDs 
   struct sembuf operations[1];  // Define semaphore operations 
   int    ret_val;               // system-call return value    

   int    shm_id;                // the shared memory ID 
   int    shm_size;              // the size of the shared memory  
   struct my_mem * p_shm;        // pointer to the attached shared memory 

   union semun {
        int    val;  
        struct semid_ds  *buf;  
        ushort * arry;
   } argument; 
   argument.val = 1;   // the initial value of the semaphore   
// find the shared memory size in bytes ----
   shm_size = sizeof(my_mem);   
   if (shm_size <= 0)
   {  
      fprintf(stderr, "sizeof error in acquiring the shared memory size. Terminating ..\n");
      exit(0); 
   }    
   
// create a new semaphore -----
   sem_id = semget(SEM_KEY, 1, 0666 | IPC_CREAT); 
   if (sem_id < 0)
   {
      fprintf(stderr, "Failed to create a new semaphore. Terminating ..\n"); 
      exit(0);
   }
   printf("a semaphore is created ...\n");

   sem_id2 = semget(SEM_KEY2, 1, 0666 | IPC_CREAT); 
   if (sem_id2 < 0)
   {
      fprintf(stderr, "Failed to create a new semaphore. Terminating ..\n"); 
      exit(0);
   }
   printf("a semaphore is created ...\n");

   sem_id3 = semget(SEM_KEY3, 1, 0666 | IPC_CREAT); 
   if (sem_id3 < 0)
   {
      fprintf(stderr, "Failed to create a new semaphore. Terminating ..\n"); 
      exit(0);
   }
   printf("a semaphore is created ...\n");

   sem_id4 = semget(SEM_KEY4, 1, 0666 | IPC_CREAT); 
   if (sem_id4 < 0)
   {
      fprintf(stderr, "Failed to create a new semaphore. Terminating ..\n"); 
      exit(0);
   }
   printf("a semaphore is created ...\n");

// initialize the new semapahore by 1 (zero) ----
   if (semctl(sem_id, 0, SETVAL, argument) < 0)
   {
      fprintf(stderr, "Failed to initialize the semaphore by 1. Terminating ..\n"); 
      exit(0);  
   }
   if (semctl(sem_id2, 0, SETVAL, argument) < 0) {
	fprintf(stderr, "Failed to initialize the semaphore sem_id2 to 0. Terminating ..\n"); 
    	exit(0);  
   }
	argument.val=0;
if (semctl(sem_id3, 0, SETVAL, argument) < 0) {
	fprintf(stderr, "Failed to initialize the semaphore sem_id2 to 0. Terminating ..\n"); 
    	exit(0);  
   }
if (semctl(sem_id4, 0, SETVAL, argument) < 0) {
	fprintf(stderr, "Failed to initialize the semaphore sem_id2 to 0. Terminating ..\n"); 
    	exit(0);  
   }

   // create a shared memory ----
   shm_id = shmget(SHM_KEY, shm_size, 0666 | IPC_CREAT);         
   if (shm_id < 0) 
   {
      fprintf(stderr, "Failed to create the shared memory. Terminating ..\n");  
      exit(0);  
   } 
printf("the shared memory is created ...\n");
   // attach the new shared memory ----
   p_shm = (struct my_mem *)shmat(shm_id, NULL, 0);     
   if (p_shm == (struct my_mem*) -1)
   {
      fprintf(stderr, "Failed to attach the shared memory.  Terminating ..\n"); 
      exit(0);   
   }

   p_shm->counter  = 0;  
   p_shm->hpRunning = false;
//#######################initializations, creations, and definitions done. implementation below.###############
	for(int i = 0; i < 4; i++) {
	   if(process_id !=0){
        	process_id = fork();
		if(process_id ==0)
		   id = i+1;
        	if (process_id < 0) {
            	   perror("Fork failed");
            	   exit(0);
		}
		
	   }else 
		break;
	}

	if(id==1){ 														//LP1
	   printf("L%d starts...\n",id);

	   printf("L%d starts waiting for two high-priority processes are active\n",id);
	   semWait(sem_id3);
	   lowPriority(p_shm, sem_id, sem_id2, id);
	   printf("L%d is terminating...\n",id);
	   exit(0);
	}
	else if(id==2){														//LP2
           printf("L%d starts...\n",id);

	   printf("L%d starts waiting for two high-priority processes are active\n",id);
	   semWait(sem_id3);
	   lowPriority(p_shm, sem_id, sem_id2, id);
	   printf("L%d is terminating...\n",id);
	   exit(0);
	}
	else if(id==3){														//LP3
           printf("L%d starts...\n",id);

	   printf("L%d starts waiting for two high-priority processes are active\n",id);
	   
	   semSignal(sem_id4);
	   semSignal(sem_id4);
	   semWait(sem_id3);
	   lowPriority(p_shm, sem_id, sem_id2, id);
	   printf("L%d is terminating...\n",id);
	   exit(0);
	}
	else if(id==4){														//HP2
	   semWait(sem_id4);
	   printf("H%d starts...\n",2);
	   printf("H%d is the last high-priority process...\n",2);
	   
           highPriority(p_shm, sem_id, sem_id3, 2);
	   printf("H%d is terminating...\n",2);
	   exit(0);	
	}
	else{															//HP1
	   semWait(sem_id4);
	   printf("H%d starts...\n",1);
	   
	   highPriority(p_shm, sem_id, sem_id3, 1);
	   printf("H%d is terminating...\n",1);
	   
	}


 
	printf("the parent process now waits for all children...\n");
	
	for (int j = 0; j < 4; j++) {
    	   wait(NULL); // Wait for any child to terminate
	   //printf("child terminated");
	}
//#####################End of implementation. Clean up everything ################################
	//delete shared mem and semaphores
	ret_val = shmdt(p_shm);  
        if (ret_val != 0) 
        {  printf ("shared memory detach failed ....\n"); }
	
        ret_val = shmctl(shm_id, IPC_RMID, 0); 
        if (ret_val != 0)
        {  printf("shared memory ID remove ID failed ... \n"); } 

        ret_val = semctl(sem_id, IPC_RMID, 0);  
        if (ret_val != 0)
        {  printf("semaphore remove ID failed ... \n"); }
        ret_val = semctl(sem_id2, IPC_RMID, 0);  
        if (ret_val != 0)
        {  printf("semaphore remove ID failed ... \n"); }
        ret_val = semctl(sem_id3, IPC_RMID, 0);  
        if (ret_val != 0)
        {  printf("semaphore remove ID failed ... \n"); }

        ret_val = semctl(sem_id4, IPC_RMID, 0);  
        if (ret_val != 0)
        {  printf("semaphore remove ID failed ... \n"); }

 	printf("the parent process is terminating...\n");
        exit(0);
};