/* *************************************************** *
 * sender.c:                                           *
 *                                                     *
 * September 3, 2024                                   *
 *                                                     *
 * *************************************************** */

#include <stdio.h>         // for printf
#include <stdlib.h>        // for sleep()
#include <time.h>          // for srand
#include <sys/types.h>     // for message queue
#include <sys/ipc.h>       // for message queue
#include <sys/msg.h>       // for message queue

#include <unistd.h>        // for sleep()

#define NUM_REPEATS   100  // the number of the messages

#define MSG_key_01   8910  // (unique) message queue key #1
#define MSG_key_02   8911  // (unique) message queue key #2

#define BUFFER_SIZE   256  // max. message size

int main (void)
{
   int  i;                 // loop counter

   int  status_01;         // result status
   int  status_02;         // result status

   int  msqid_01;          // message queue ID (#1)
   int  msqid_02;          // message queue ID (#2)

   key_t msgkey_01;        // message-queue key (#1)
   key_t msgkey_02;        // message-queue key (#2)

   unsigned int       rand_num;
   float             temp_rand; 
   unsigned char eight_bit_num; 

   int   counter      = 0; 
   int   even_counter = 0;  
   int   odd_counter  = 0; 

   /* Use current time as seed for random generator */
   srand(time(0)); 

   /* definition of message ------------------- */
   struct message{
        long mtype;
        char mtext[BUFFER_SIZE];
   };

   /* instantiate the message buffer ------------*/
   struct message buf_01;   // for #1
   struct message buf_02;   // for #2

   msgkey_01 = MSG_key_01;  // the messge-que ID key (#1)
   msgkey_02 = MSG_key_02;  // the messge-que ID key (#2)

   /* create a new message queue -------------- */
   msqid_01 = msgget(msgkey_01, 0666 | IPC_CREAT);
   msqid_02 = msgget(msgkey_02, 0666 | IPC_CREAT);

   /* error check ----------------------------- */
   if ((msqid_01 <= -1)||(msqid_02 <= -1))
   {
        if (msqid_01 <= -1)
        {  printf ("your new message queue (#1) is not created ....\n");  }
        else
        {  printf ("your new message queue (#2) is not created ....\n");  }

        printf ("process is terminating ... \n\a");
   }
   else
   {    printf("your new message queues are both successfully created ....\n"); }

   /* confirm the start of the two receivers --- */
   printf("start M1 and M2, then start the final receiver ... press any key when ready ....\n\n");

   /* wait for a key stroke at the keyboard ---- */
   eight_bit_num = getchar();  

   /* take care of "mtype" --------------------- */
   buf_01.mtype = 1;  // UNIX standard says, any number
   buf_02.mtype = 1;  // UNIX standard says, any number

   /* send one eigh-bit number, one at a time  ------------ */
   for (i = 0; i < NUM_REPEATS; i++)
   {
      /* generate an 8-bit random number (0-255) ---------- */
      temp_rand = ((float)rand()/(float)RAND_MAX)*255.0;   
      rand_num = (int)temp_rand;
      eight_bit_num = (unsigned char)rand_num; 

      if ((i % 2) == 0)  
      {
         printf("Even number: %d\n", eight_bit_num);   
         even_counter = even_counter + (int) eight_bit_num;
      }
      else
      {
         printf("Odd number:       %d\n", eight_bit_num);    
         odd_counter = odd_counter + (int) eight_bit_num;
      }

      /* update the counters ------------------------------ */  
      counter = counter + (int) eight_bit_num;
      
      // if((i % 2) == 0)  
      // {  even_counter = even_counter + eight_bit_num;  }
      // else
      // {  odd_counter = odd_counter + eight_bit_num;   }    

      /* ser the new eight-bit number to the message buffers ------ */  
      buf_01.mtext[0] = eight_bit_num;   // copy the 8-bit number     
      buf_02.mtext[0] = eight_bit_num;   // copy the 8-bit number      
      buf_01.mtext[1] = '\0';            // null-terminate it
      buf_02.mtext[1] = '\0';            // null-terminate it

      /* send a 8-bit number to the two message queues --- */
      status_01 = msgsnd(msqid_01, (struct msgbuf *)&buf_01, sizeof(buf_01.mtext), 0);
      status_02 = msgsnd(msqid_02, (struct msgbuf *)&buf_02, sizeof(buf_02.mtext), 0); 

      /* detect a message transmission error ------------- */
      if ((status_01 <= -1) || (status_02 <= -1))
      {
         if (status_01 <= -1)
         {  printf("sending a number over the 1st queue failed ... \n\a"); }
         else
         {  printf("sending a number over the 2nd queue failed ... \n\a"); }
         break;
      }
   }

   /* give everyone else enough time to complete their tasks --- */
   sleep(3);  

   /* delete the emsage queue ----------------------------- */
   status_01 = msgctl(msqid_01, IPC_RMID, NULL);
   status_02 = msgctl(msqid_02, IPC_RMID, NULL);

   /* error check ----------------------------- */
   if ((status_01 <= -1)||(status_02 <= -1))
   {
      if (status_01 <= -1)
      {  printf("deleting the first message queue failed ...\n\a");  }
      else
      {  printf("deleting the second message queue failed ...\n\a"); }
   }

   else
   {
      printf("the sender process completes ..... \n");
      printf("Total: %d, Even: %d, Odd: %d\n", counter, even_counter, odd_counter);   
   }
}
