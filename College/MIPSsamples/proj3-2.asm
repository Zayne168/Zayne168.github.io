# ############################################################### #
# Zayne Bonner
# 800756759
# ############################################################### #   
#
# NOTES
#
#
#
#
#
#
#

.data

PrinH:	.float  1000000.00
PrinL: 	.float	100.00
IntH:	.float	0.399
IntL:	.float 	0.005
PayH:	.float 2000.0
PayL:   .float 1.00


ASKPRINC:    	    .asciiz "Enter the principal in $ (100.00 - 1,000,000.00): "
ASKRATE:     		.asciiz "Enter the annual interest rate (0.005 - 0.399): "
ASKPAYMENT:      	.asciiz "Enter the monthly payment amount in $ (1.00 - 2,000.00): "
MONTH: 				.asciiz "\nmonth "
CURPRIN:			.asciiz ": current principal = "
FIRST: 				.asciiz "\nIt will take "
LAST: 				.asciiz " months to complete the loan."
NEWLINE: 			.asciiz "\n"

.text
.globl main

main:
	GETPRIN:		
				li $v0, 4
				la $a0, ASKPRINC
				syscall 
				li $v0, 6
				syscall
				lwc1 $f1, PrinH
				lwc1 $f2, PrinL
				c.lt.s $f1,$f0
					bc1t GETPRIN
				c.lt.s $f0,$f2
					bc1t GETPRIN
				mov.s $f30,$f0
					
	GETRATE:	
				li $v0, 4
				la $a0, ASKRATE
				syscall 
				li $v0, 6
				syscall
				lwc1 $f4, IntH
				lwc1 $f5, IntL
				c.lt.s $f4,$f0
					bc1t GETRATE
				c.lt.s $f0,$f5
					bc1t GETRATE
				mov.s $f29,$f0
	GETPAY: 			
				li $v0, 4
				la $a0, ASKPAYMENT
				syscall 
				li $v0, 6
				syscall
				lwc1 $f9, PayH
				lwc1 $f10, PayL
				c.lt.s $f9,$f0
					bc1t GETPAY
				c.lt.s $f0,$f10
					bc1t GETPAY
				mov.s $f28,$f0
				
	CALC:		
				li.s $f6, 30.0
				li.s $f7, 365.0
				li.s $f8, 0.0
				li $s1, 1
		while:	

			li $v0, 4
			la $a0, MONTH
			syscall 
			li $v0, 1
			move $a0, $s1
			syscall 		
			li $v0, 4
			la $a0, CURPRIN
			syscall 
			li $v0, 2
			mov.s $f12, $f30
			syscall
			
				div.s $f27,	$f6, $f7 		#fact check this shit
				mul.s $f27, $f27, $f30
				mul.s $f27, $f27, $f29 		# monthly interest
				sub.s $f26, $f28,$f27
				sub.s $f30, $f30, $f26 		# remaining principal			
			
				add $s1, $s1, 1
		c.le.s $f8,$f30
			bc1t while
				sub $s1, $s1, 1
				li $v0, 4
				la $a0, FIRST
				syscall 
				li $v0, 1
				move $a0, $s1
				syscall 
				li $v0, 4
				la $a0, LAST
				syscall 				
	EXIT:			jr$31
