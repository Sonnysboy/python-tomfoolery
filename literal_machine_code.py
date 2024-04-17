import ctypes
import mmap

buf = mmap.mmap(-1, mmap.PAGESIZE, prot=mmap.PROT_READ | mmap.PROT_WRITE | mmap.PROT_EXEC)

ftype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
fpointer = ctypes.c_void_p.from_buffer(buf)

f = ftype(ctypes.addressof(fpointer))

buf.write( # assembly instruction bytes
    b'\x8b\xc7' 
    b'\x83\xc0\x01'  
    b'\xc3'
)

r = f(42)
print(r)

del fpointer
buf.close()