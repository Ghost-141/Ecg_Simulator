import numpy as np

#P Wave Function
def p_wav(x, a_pwav, d_pwav, t_pwav, li):
    l = li
    a = a_pwav
    x = x + t_pwav
    b = (2 * l) / d_pwav
    n = 100
    
    p1 = 1 / l
    p2 = 0
    
    for i in range(1, n + 1):
        harm1 = ((np.sin((np.pi / (2 * b)) * (b - (2 * i))) / (b - (2 * i)) +
                  np.sin((np.pi / (2 * b)) * (b + (2 * i))) / (b + (2 * i))) * 
                  (2 / np.pi)) * np.cos((i * np.pi * x) / l)
        
        p2 += harm1
    
    pwav1 = p1 + p2
    
    pwav = a * pwav1
    
    return pwav

#Q Wave Function
def q_wav(x, a_qwav, d_qwav, t_qwav, li):
    l = li
    x = x + t_qwav
    a = a_qwav
    b = (2 * l) / d_qwav
    n = 100
    
    q1 = (a / (2 * b)) * (2 - b)
    q2 = 0
    
    for i in range(1, n + 1):
        harm5 = ((2 * b * a) / (i * i * np.pi * np.pi)) * (1 - np.cos((i * np.pi) / b)) * np.cos((i * np.pi * x) / l)
        q2 += harm5
    
    qwav = -1 * (q1 + q2)
    
    return qwav

#QRS Wave Function
def qrs_wav(x, a_qrswav, d_qrswav, li):
    l = li
    a = a_qrswav
    b = (2 * l) / d_qrswav
    n = 100

    qrs1 = (a / (2 * b)) * (2 - b)
    qrs2 = 0
    
    for i in range(1, n + 1):
        harm = ((2 * b * a) / (i * i * np.pi * np.pi)) * (1 - np.cos((i * np.pi) / b)) * np.cos((i * np.pi * x) / l)
        qrs2 += harm

    qrswav = qrs1 + qrs2
    
    return qrswav

#S Wave Function
def s_wav(x, a_swav, d_swav, t_swav, li):
    l = li
    x = x - t_swav
    a = a_swav
    b = (2 * l) / d_swav
    n = 100
    
    s1 = (a / (2 * b)) * (2 - b)
    s2 = 0
    
    for i in range(1, n + 1):
        harm3 = ((2 * b * a) / (i * i * np.pi * np.pi)) * (1 - np.cos((i * np.pi) / b)) * np.cos((i * np.pi * x) / l)
        s2 += harm3

    swav = -1 * (s1 + s2)
    
    return swav

# T Wave Function
def t_wav(x, a_twav, d_twav, t_twav, li):
    l = li
    a = a_twav
    x = x - t_twav - 0.045
    b = (2 * l) / d_twav
    n = 100
    
    t1 = 1 / l
    t2 = 0
    
    for i in range(1, n + 1):
        harm2 = (((np.sin((np.pi / (2 * b)) * (b - (2 * i))) / (b - (2 * i))) +
                  (np.sin((np.pi / (2 * b)) * (b + (2 * i))) / (b + (2 * i)))) * (2 / np.pi)) * np.cos((i * np.pi * x) / l)
        t2 += harm2
    
    twav1 = t1 + t2
    twav = a * twav1
    
    return twav

#U Wave Function
def u_wav(x, a_uwav, d_uwav, t_uwav, li):
    l = li
    a = a_uwav
    x = x - t_uwav
    b = (2 * l) / d_uwav
    n = 100
    
    u1 = 1 / l
    u2 = 0
    
    for i in range(1, n + 1):
        harm4 = (((np.sin((np.pi / (2 * b)) * (b - (2 * i))) / (b - (2 * i))) +
                  (np.sin((np.pi / (2 * b)) * (b + (2 * i))) / (b + (2 * i)))) * (2 / np.pi)) * np.cos((i * np.pi * x) / l)
        u2 += harm4
    
    uwav1 = u1 + u2
    uwav = a * uwav1
    
    return uwav
