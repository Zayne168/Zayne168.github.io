# #############################################################################################	#
# Zayne Bonner	
# 800756759		
# #############################################################################################	#

.data
	CURRSPEED:	.asciiz "Enter your current driving speed in MPH (1 to 200): "
	SPEEDLIM: 	.asciiz "Enter the absolute speed limit specified for the road you are currently running on (15 to 70): "
	CURRERROR: 	.asciiz "You made an invalid input for your current driving speed. Enter a valid input for your current driving speed.\n"
	LIMITERROR:	.asciiz "You made an invalid input for the absolute speed limit. Enter a valid input for the speed limit.\n"
	OUTPUTONE: 	.asciiz "You are a safe driver!"
	OUTPUTTWO: 	.asciiz "$120 fine\n" #1-20 mph over
	OUTPUTTHREE:.asciiz "$140 fine\n"#21-25 mph over
	OUTPUTFOUR:	.asciiz "Class B misdemeanor and carries up to six month in jail and a maximum $1,500 in fines.\n" # 26-34 mph over
	OUTPUTFIVE:	.asciiz "Class A misdemeanor and carries up to one year in jail and a maximum $2,500 in fines.\n" #35+ mph over
.text
	.globl main

main:
					la $s5, 200
					la $s6, 1
					la $s7, 70
					la $s4, 15
													# define limits
					
	GETSPEED:		
					li $v0, 4
					la $a0, CURRSPEED
					syscall 
					li $v0, 5
					syscall
					move $s0, $v0 					# get current speed
					bgt $s0, $s5 SPEEDERROR
					blt $s0, $s6 SPEEDERROR
					j GETLIMIT
	
	GETLIMIT:
					li $v0, 4
					la $a0, SPEEDLIM
					syscall 
					li $v0, 5
					syscall
					move $s1, $v0 					# get speed limit
					bgt $s1, $s7 SPEEDLIMITERROR
					blt $s1, $s4 SPEEDLIMITERROR
													#s0 is current speed s1 is speed limit
					bgt $s0, $s1 IF_SPEEDING		#if speeding, calculate the punishment, if not go to output
						la $a0, OUTPUTONE
						j MYOUTPUT
						
	IF_SPEEDING:
					subu $t3, $s0, $s1
					blt $t3, 21 LESSA
					blt $t3, 26 LESSB
					blt $t3, 35 LESSC
					j LESSD
					
	LESSA:			la $a0, OUTPUTTWO
					j MYOUTPUT
	LESSB:			la $a0, OUTPUTTHREE
					j MYOUTPUT
	LESSC:			la $a0, OUTPUTFOUR
					j MYOUTPUT
	LESSD:			la $a0, OUTPUTFIVE				#assign the desired punishment to temporary register
					j MYOUTPUT
					
					
					
	SPEEDERROR: 	
					li $v0, 4
					la $a0, CURRERROR
					syscall 
					j GETSPEED
					
	SPEEDLIMITERROR: 	
					li $v0, 4
					la $a0, LIMITERROR
					syscall 
					j GETLIMIT					
	
	MYOUTPUT: 
					li $v0, 4
					syscall 
	EXIT:			jr $31

# END OF THE LINES ##############################################################################