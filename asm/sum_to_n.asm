; Implements the same logic as sum_to_n in workloads.py

global _start
section .text
_start:
    mov rbx, 1      ; rbx = i (loop counter)
    mov rcx, 5      ; rcx = n (target number)
    mov rax, 0      ; rax = total sum

loop:
    add rax, rbx    ; total += i
    inc rbx         ; i++
    cmp rbx, rcx    ; compare i with n
    jg done         ; if i > n, exit loop
    jmp loop        ; else, repeat loop

done:
    mov rax, 60     ; exit syscall
    mov rdi, 0
    syscall