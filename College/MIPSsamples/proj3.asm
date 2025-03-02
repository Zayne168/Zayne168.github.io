# ################################################################
# Zayne Bonner
# 800756759
# ################################################################

.data

MESSAGE1: .asciiz "Enter an IP address\n"
MESSAGE2: .asciiz "First: "
MESSAGE3: .asciiz "Second: "
MESSAGE4: .asciiz "Third: "
MESSAGE5: .asciiz "Fourth: "
MESSAGE6: .asciiz "The IP address you entered: "
MESSAGE7: .asciiz "."
MESSAGE8: .asciiz "\nClass A address\n"
MESSAGE9: .asciiz "\nClass B address\n"
MESSAGE10: .asciiz "\nClass C address\n"
MESSAGE11: .asciiz "\nClass D address\n"
MESSAGE12: .asciiz "\nInvalid domain class\n"
MESSAGE13: .asciiz "\nProgram successfully completed . . .\n"
MESSAGE14: .asciiz "\n"
MESSAGE15: .asciiz "Matching domain found at: "
MESSAGE16: .asciiz "Matching domain was NOT found . . . \n"
ERROROVER: .asciiz "The entered number is larger than 255.\n"
ERRORUNDER: .asciiz "The entered number is smaller than 0.\n"

IP_ROUTING_TABLE_SIZE:
		.word	26

IP_ROUTING_TABLE:
		# line #, x.x.x.x -------------------------------------
		.byte  25,  10, 153,   1,   8	# 10.153.1.8
		.byte  24, 191,  28, 255, 255	# 191.28.255.255
		.byte  23, 191,  28,  88,  90	# 191.28.88.90
		.byte  22, 192, 151, 100,  56	# 192.151.100.56
		.byte  21, 192, 951, 100, 100	# 192.151.100.100
		.byte  20,  82, 163, 140,  80	# 82.163.140.80
		.byte  19,  82, 163, 147,  80	# 146.163.147.80
		.byte  10, 201,  88, 102,  80	# 201.88.102.1
		.byte  11, 148, 163, 170,  80	# 146.163.170.80
		.byte  12, 193,  77,  77,  10	# 193.77.77.10
		.byte	0, 146,  92, 255, 255	# 146.92.255.255
		.byte	1, 147, 163, 255, 255	# 147.163.255.255
		.byte	2, 201,  88,  88,  90	# 201.88.88.90
		.byte	3, 182, 151,  44,  56	# 182.151.44.56
		.byte	4,  24, 125, 100, 100	# 24.125.100.100
		.byte	5, 146, 163, 140,  80	# 146.163.170.80
		.byte	6, 146, 163, 147,  80	# 146.163.147.80
		.byte   7, 201,  88, 102,  80	# 201.88.102.1
		.byte   8, 148, 163, 170,  80	# 146.163.170.80
		.byte   9, 193,  77,  77,  10	# 193.77.77.10
		.byte  30,  22,   8,   5,   1	# 22.8.5.1
		.byte  31,  22,  12, 188, 192	# 22.12.188.192
		.byte  32, 201,  88, 102,   1	# 201.88.102.1
		.byte  33, 148, 200, 170,  80	# 146.163.170.80
		.byte  34, 193,  77,  78,  10	# 193.77.78.10
		.byte  35, 225,  77,  78,  10
			# 
	
.text
.globl main

main:       
			la $s1, 0
			la $s2, 256
			li $s7, 400
	
			
				
	GETNUM1:		
					li $v0, 4
					la $a0, MESSAGE1
					syscall 
		e1:			li $v0, 4
					la $a0, MESSAGE2
					syscall 
					li $v0, 5
					syscall
					move $s0, $v0 					# get first address number
					bgt $s2, $s0 next
					li $v0, 4
					la $a0, ERROROVER				#input >255
													 
					syscall 
					j e1
		next:		ble $s1, $s0 GETNUM2
					li $v0, 4
					la $a0, ERRORUNDER				#input<0 #the error message does not make sense I am well aware, but I am just following the rubric which states that each number collected needs to be between 0 and 255 inclusive(even the first number which isnt valid)
					syscall
					j e1
	
	

	GETNUM2:		 
		e2:			li $v0, 4
					la $a0, MESSAGE3
					syscall 
					li $v0, 5
					syscall
					move $s3, $v0 					# get second address number
					bgt $s2, $s3 next3
					li $v0, 4
					la $a0, ERROROVER				#input >255						 
					syscall 
					j e2
		next3:		ble $s1, $s3 GETNUM3
					li $v0, 4
					la $a0, ERRORUNDER				#input<0
					syscall
					j e2
	
	GETNUM3:		 
		e3:			li $v0, 4
					la $a0, MESSAGE4
					syscall 
					li $v0, 5
					syscall
					move $s4, $v0 					# get third address number
					bgt $s2, $s4 next4
					li $v0, 4
					la $a0, ERROROVER				#input >255						 
					syscall 
					j e3
		next4:		ble $s1, $s4 GETNUM4
					li $v0, 4
					la $a0, ERRORUNDER				#input<0
					syscall
					j e3	
					
	GETNUM4:		 
		e4:			li $v0, 4
					la $a0, MESSAGE5
					syscall 
					li $v0, 5
					syscall
					move $s5, $v0 					# get fourth address number
					bgt $s2, $s5 next5
					li $v0, 4
					la $a0, ERROROVER				#input >255						 
					syscall 
					j e4
		next5:		ble $s1, $s5 GETCLASS
					li $v0, 4
					la $a0, ERRORUNDER				#input<0
					syscall
					j e4
	
	GETCLASS:		j printmine
			back:	bgt $s0, 239 unavail
					bgt $s0, 223 classD
					bgt $s0, 191 classC
					bgt $s0, 127 classB
					bgt $s0, 0 	 classA
					j unavail				#this catches if first number ==0, since the rubric says to allow it as acceptable input
					
		classA:		li $v0, 4
					la $a0, MESSAGE8
					syscall
					li $t6, 1
					j tsize
					
		classB:		li $v0, 4
					la $a0, MESSAGE9
					syscall
					li $t6, 2
					j tsize
					
		classC:		li $v0, 4
					la $a0, MESSAGE10
					syscall
					li $t6, 3
					j tsize

		classD:		li $v0, 4
					la $a0, MESSAGE11		
					syscall
					li $t6, 4			#unsure of if all 4 numbers need to match for class d or if I need to check at all
					j tsize
					
		unavail:	li $v0, 4
					la $a0, MESSAGE12
					syscall
					li $v0, 4
					la $a0, MESSAGE13
					syscall
					j EXIT
				
	tsize:		lw 	$s2, IP_ROUTING_TABLE_SIZE
				addi $s2,$s2,1
				j loop2

	loop2:			la $t7, IP_ROUTING_TABLE
		next2:	
				addi $s1, $s1, 1
				lbu $s6, ($t7)
				addi $t7,$t7,1
				lbu $t1, ($t7)
				addi $t7,$t7,1
				lbu $t2, ($t7)
				addi $t7,$t7,1
				lbu $t3, ($t7)
				addi $t7,$t7,1
				lbu $t4, ($t7)
				addi $t7,$t7,1
		beq $s1, $s2, final		
		printlist:	li $v0, 1
					move $a0, $t1
					syscall
						li $v0, 4
						la $a0, MESSAGE7
						syscall
					li $v0, 1
					move $a0, $t2
					syscall
						li $v0, 4
						la $a0, MESSAGE7
						syscall
					li $v0, 1
					move $a0, $t3
					syscall
						li $v0, 4
						la $a0, MESSAGE7
						syscall
					li $v0, 1
					move $a0, $t4
					syscall
					li $v0, 4
					la $a0, MESSAGE14
					syscall
				
		
					j compare
		
#s0=num1
#s1=0=>counter for the loop to go through lines
#s2=256constant=>tablesize counter
#s3=num2
#s4=num3
#s5=num4
#
#s7=last match
#
#

	printmine:		li $v0, 4
					la $a0, MESSAGE6
					syscall
					li $v0, 1
					move $a0, $s0
					syscall
						li $v0, 4
						la $a0, MESSAGE7
						syscall
					li $v0, 1
					move $a0, $s3
					syscall
						li $v0, 4
						la $a0, MESSAGE7
						syscall
					li $v0, 1
					move $a0, $s4
					syscall
						li $v0, 4
						la $a0, MESSAGE7
						syscall
					li $v0, 1
					move $a0, $s5
					syscall
					li $v0, 4
					la $a0, MESSAGE14
					syscall
					j back
	
	compare:
		beq $t6, 1 comp1
		beq $t6, 2 comp2
		beq $t6, 3 comp3
		beq $t6, 4 comp4
		
		comp1: 	
				beq $s0, $t1 match
				j next2
		comp2:
				beq $s0, $t1 p2
				j next2
			p2: beq $s3, $t2 match	
				j next2
		comp3:
				beq $s0, $t1 p22
				j next2
			p22: beq $s3, $t2 p3
				j next2
			p3:  beq $s4, $t3 match
				j next2
		comp4:	
				beq $s0, $t1 p5
				j next2
			p5: beq $s3, $t2 p6
				j next2
			p6:  beq $s4, $t3 p7
				j next2
			p7:  beq $s5, $t4 match
				j next2
				
		match:
				move $s7, $s6
				j next2
		
	final:
				beq $s7, 400 nomatch
				li $v0, 4
				la $a0, MESSAGE15
				syscall
				li $v0, 1
				move $a0, $s7
				syscall
				j EXIT
				
	nomatch:	li $v0, 4
				la $a0, MESSAGE16
				syscall

	
	EXIT:		jr $31