

(define (countDigits num)
 (length (string->list (number->string num)))
)

(define (mergeTwoLists l1 l2)
  (cond
    ((null? l1) l2) 
    ((null? l2) l1); Base cases
    ((<= (car l1)(car l2)); l1 element 1 <= l2 element 1
     (cons (car l1) (mergeTwoLists (cdr l1) l2)))
    (else (cons (car l2) (mergeTwoLists (cdr l2) l1)))
   ))

(define (integer->list num)
  (if (< num 0) '(-);negative -> return '(-)
   (map (lambda (a) (string->number (string a))); character->number
   (string->list (number->string num)))); string ->list
 )



(define (pList myList)
  (if (null? myList) ;list empty? -> palindrome
      #t
      (if (null? (cdr myList)) ;list have 1 item?-> palindrome
          #t
          (let ((reverseList (reverse myList)))
            (if (equal? (car myList) (car reverseList))
                (pList (cdr (reverse (cdr myList))))
                #f)))))

;(define (pList myList)
 ; (if(null? myList)
  ;   #t
   ;  (if(null? (cdr myList))
    ;    #t
     ;   (if(equal? (car myList) (car(reverse myList)))
      ;     (pList (cdr(myList)))
       ;    #f)))
 ;)this does not work at all forget it -attempt 1