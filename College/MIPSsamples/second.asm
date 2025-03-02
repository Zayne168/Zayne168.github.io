# #############################################################################################	#
# Zayne Bonner	
# 800756759		
# #############################################################################################	#
# notes - s0=origin s1 = factor s2 = number of the numbers

.data
	ORIGINSEQ:	.asciiz "Enter the origin of your number sequence: "
	FACTOR: 	.asciiz "Enter the multiple factor:  "
	QUANTITY: 	.asciiz "Enter the total number of numbers:  "
	CHECK: 		.asciiz "Check-sum: "
	SKIPLINE: 	.asciiz "\n"
	COMMA: 		.asciiz ", "
.text
	.globl main

main:
					li $s3, 0
					
	GETORIGIN:		
					li $v0, 4
					la $a0, ORIGINSEQ
					syscall 
					li $v0, 5
					syscall
					move $s0, $v0 					# get origin of sequence
					
					li $v0, 4
					la $a0, SKIPLINE 			#skip a line
					syscall 	
					bgt $s0, 5, GETORIGIN
					blt $s0, 1, GETORIGIN
	GETFACTOR:				
					li $v0, 4
					la $a0, FACTOR
					syscall 
					li $v0, 5
					syscall

					
					move $s1, $v0 					#get multiple factor	
					li $v0, 4
					la $a0, SKIPLINE 			#skip a line
					syscall 	
					bgt $s1, 7, GETFACTOR
					blt $s1, 2, GETFACTOR
	GETQUANT:				
					li $v0, 4
					la $a0, QUANTITY
					syscall 
					li $v0, 5
					syscall
					
					move $s2, $v0 					# get total quantity of numbers
					bgt $s2, 30 GETQUANT
					blt $s2, 3 GETQUANT
					move $s5, $s0
					li $s6, 0
					
					li $v0, 4
					la $a0, SKIPLINE 			#skip a line
					syscall 						
			while:
				beq $s3, $s2, CHECKSUM
				add $s6, $s6, $s5
				
				add $s3, $s3, 1
				
				li $v0, 1
				move $a0, $s5
				syscall 				
				add $s5,$s5,$s1
				bne $s3, $s2, ADDCOMMA

			
			j while
	CHECKSUM: 	
				li $v0, 4
				la $a0, SKIPLINE 			#skip a line
				syscall
				li $v0, 4
				la $a0, SKIPLINE 			#skip a line
				syscall 					
				li $v0, 4
				la $a0, CHECK
				syscall

				li $v0, 1
				move $a0, $s6
				syscall 					
				j EXIT
			
	ADDCOMMA: 		
				li $v0, 4
				la $a0, COMMA
				syscall 
				j while 

	EXIT:			jr $31

# END OF THE LINES ##############################################################################