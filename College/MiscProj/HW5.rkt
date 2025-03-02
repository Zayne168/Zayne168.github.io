;; Zayne Bonner & Lacey Boltz

(define (getIndex toFind matrix) ;recursively find where B is in the matrix and return the index of it(0-8)
  (define (loop myList index)
    (if (equal? toFind (car myList)) 
        index                      
        (loop (cdr myList) (+ index 1))) 
    )
  (loop matrix 0))

(define (replace matrix index n)
  (if(null? matrix)
     '()
     (cons( if(= index 0)
              n
              (car matrix))
          (replace (cdr matrix)(if(= index 0) -1 (- index 1)) n))))

(define (up matrix)
  (let* ((b(getIndex 'B matrix)))
  (if(< b 3) '()
    (let* ((aboveIndex (- b 3))
           (aboveVal (list-ref matrix aboveIndex)))
      (let ((temp (replace matrix b aboveVal)))
        (replace temp aboveIndex 'B))))))

(define (down matrix)
  (let* ((b(getIndex 'B matrix)))
  (if(> b 5) '()
    (let* ((aboveIndex (+ b 3))
           (aboveVal (list-ref matrix aboveIndex)))
      (let ((temp (replace matrix b aboveVal)))
        (replace temp aboveIndex 'B))))))

              
(define (left matrix)
  (let* ((b(getIndex 'B matrix)))
  (if(= 0 (modulo b 3)) '()
    (let* ((aboveIndex (- b 1))
           (aboveVal (list-ref matrix aboveIndex)))
      (let ((temp (replace matrix b aboveVal)))
        (replace temp aboveIndex 'B))))))

(define (right matrix)
  (let* ((b(getIndex 'B matrix)))
  (if(or (= b 2) (= b 5) (= b 8)) '()
    (let* ((aboveIndex (+ b 1))
           (aboveVal (list-ref matrix aboveIndex)))
      (let ((temp (replace matrix b aboveVal)))
        (replace temp aboveIndex 'B))))))



(define bfs
  (λ (init goal)
    (do ( (path-list (list (list init))) ) ;; initialize the vars, we only have path-list, which is the Q
      
        ((or (null? path-list) (equal? goal (caar path-list))) ;; terminal condition
         (if (null? path-list) '() (reverse (car path-list)))) ;; return either empty or reverse of 1st path
        (set! path-list (extend path-list))) ;; loop body
                                             ;; path-list = extend(path-list);
   )
)
(define 8puzzle bfs)

(define getFirstNode caar)

(define op-list '(up down left right))


(define in 
  (lambda (a l)
    (cond ((null? l) #f)
          ((equal? a (car l)) #t)
          ((list? (car l)) 
           (or (in a (car l))(in a (cdr l))))
          (else (in a (cdr l))))))

(define extend 
   (lambda (L) ;; L is the local name for path-list in fwgc
     (do ((ops op-list (cdr ops)) ;; local name for the op-list, allowing us to walk through the op-list
          (cur-node (getFirstNode L)) ;; cur-node contains the list describing the current state such as (w w w w)
          (new-node '())) ;; initialize
       
       ((null? ops) (cdr L))         ;; terminal condition, remove cur-node when return
       (set! new-node ((eval (car ops)) cur-node)) ;; this calls the function on cur-node

       ;(when (and (not (in new-node L)) (not (null? new-node))) ;; if new-node is not unsafe and not a repeat
       ;    (set! L (append L (list (cons new-node (car L)))))) ; adding a new path at the end of lst
       (when (and (not (null? new-node)) 
           (not (in new-node L))) ;; Check against existing states
  (set! L (append L (list (cons new-node (car L)))))) ;; adding new path
     )
   )
)

(define (print8puzzle sol)
  (do ((l sol (cdr l)))
      ((null? l))
    (do ((i 0 (+ i 3)))
        ((>= i 9))
      (let ((c1 (list-ref (car l) i))
            (c2 (list-ref (car l) (+ i 1)))
            (c3 (list-ref (car l) (+ i 2))))
        (display (if (equal? c1 'B) " " c1))
        (display " ")
        (display (if (equal? c2 'B) " " c2))
        (display " ")
        (display (if (equal? c3 'B) " " c3)))
      (newline))
    (newline))
  (display (length sol)))

;;Zayne Bonner & Lacey Boltz