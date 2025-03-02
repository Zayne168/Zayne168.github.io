# ############################################################### #
# Zayne Bonner
# 800756759
# ############################################################### #   
#
# NOTES
#	
#
#
#xyz is my recursive function found near bottom of page
#
#
#

.data
MAXPRIN: .float	100000.99
FZERO:	.float  0.00
FONE: 	.float 	1.00

PRINTYEAR:    	    .asciiz "year "
NEWL:     	   		.asciiz "\n"
COLON: 				.asciiz ": $"
EPRIN: 				.asciiz "Enter the principal: $"
ERATE: 				.asciiz "Enter the interest rate (0.01 for 1%): "
ETARG: 				.asciiz "Enter the target balance: $"
EDISP: 				.asciiz "Number of the last years for display (-1: all): "
PRINTTAKES: 		.asciiz "It takes "
PRINTYRS: 			.asciiz " years."
TTest:				.asciiz "!TEST!"

.text
.globl main

main:
				subu $sp,$sp,20
				sw $ra, 0($sp)
				swc1 $f30, 4($sp)
				swc1 $f29, 8($sp)
				swc1 $f28, 12($sp)
				li $s2,0			#year counter is 0
				sw $s2, 16($sp)
	EnterPrin:
				li $v0, 4
				la $a0, EPRIN
				syscall 
				li $v0, 6
				syscall
				lwc1 $f1, FZERO
				c.lt.s $f0,$f1
					bc1t EnterPrin		#input must be greater than or equal to zero and less than 100,000.99
				lwc1 $f10, MAXPRIN
				c.lt.s $f10,$f0
					bc1t EnterPrin
				mov.s $f30,$f0
	EnterRate:
				li $v0, 4
				la $a0, ERATE
				syscall 
				li $v0, 6
				syscall
				lwc1 $f2, FONE
				c.le.s $f2,$f0
					bc1t EnterRate 		#input must be between 0 and 1 exclusive
				c.le.s $f0,$f1
					bc1t EnterRate		#input must be less than 100,000.99
				mov.s $f29,$f0
	EnterTarg:
				li $v0, 4
				la $a0, ETARG
				syscall 
				li $v0, 6
				syscall
				c.le.s $f0,$f1
					bc1t EnterTarg		#if the input is less than or equal to zero then get a new new input
				c.lt.s $f10,$f0
					bc1t EnterTarg		#input must be less than 100,000.99
				mov.s $f28,$f0
	EnterYrDP:
				li $v0, 4
				la $a0, EDISP
				syscall 
				li $v0, 5
				syscall
				move $s1, $v0 
				beq $s1, -1, next
				blt $s1, 0, EnterYrDP
				bgt $s1, 250, EnterYrDP
				
				
		next:	
				
				jal xyz

					j FinOUT
				
	FinOUT:		
				li $v0, 4
				la $a0, PRINTTAKES							
				syscall
				li $v0, 1
				move $a0, $s3							
				syscall
				li $v0, 4
				la $a0, PRINTYRS						
				syscall
				#li $v0, 2
				#mov.s $f12, $f26	#This is a fallback test to make sure I am getting proper output following my recursive function			
				#syscall
				
				lw $s2,16($sp)
				lwc1 $f28, 12($sp)
				lwc1 $f29, 8($sp)
				lwc1 $f30,4($sp)
				lw $ra,0($sp)
				addu $sp,$sp,20
				
				
				j EXIT
				
############################################################################################
				
	xyz:												#recursive function start
					subu $sp,$sp,20
					sw $ra, 0($sp)
					swc1 $f30, 4($sp)
					swc1 $f29, 8($sp)
					swc1 $f28, 12($sp)	#any not saved here that are also NOT MENTIONED are likely over-written and do not need saved 
					sw $s2, 16($sp)	
				mul.s $f27, $f29,$f30
				add.s $f30, $f27, $f30
					add $s2,$s2,1
					move $s3, $s2			#store running totals for final output in unused registers reserved for specifically that 
					mov.s $f26, $f30
					la $s7, 0
				c.le.s $f28, $f30			#base case to stop recursion(if target balance <= balance@year then skip recursion)
					bc1t skip
				


				jal xyz					#recursion
				

		skip:
				beq $s1,-1, runprint
				beq $s1,$s7,skipprint
				sub $s1, $s1, 1
		
	runprint:	li $v0, 4									
				la $a0, PRINTYEAR							#print at skip
				syscall
				li $v0, 1
				move $a0, $s2							
				syscall
				li $v0, 4
				la $a0, COLON							
				syscall
				li $v0, 2
				mov.s $f12, $f30				
				syscall
				li $v0, 4
				la $a0, NEWL							
				syscall
	skipprint:		lw $s2,16($sp)			#load stored stuff
					lwc1 $f28, 12($sp)
					lwc1 $f29, 8($sp)
					lwc1 $f30,4($sp)
					lw $ra,0($sp)
					addu $sp,$sp,20
					jr $ra
				

				
				
				
#############################	####################################################			
EXIT:			jr$31
