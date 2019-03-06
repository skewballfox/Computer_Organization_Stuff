def get_mips(CPI, clock_rate,hertz="ghz"):
     """returns the MIPS (millions of instructions per second) given a clock rate
     and CPI(cycles per instruction)"""
     if hertz is "ghz":
         clock_rate*=10**9
     elif hertz is "mhz":
         clock_rate*=10**6
     MIPS = clock_rate/CPI/10**6
     return MIPS

def get_total_instructions_executed(CPI,time_in_seconds,clock_rate, hz="ghz"):
     if hz is "ghz":
         clock_rate*=10**9
     elif hz is "mhz":
         clock_rate*=10**6
     total_instructions_executed=(clock_rate*time_in_seconds)/CPI
     return total_instructions_executed

def get_clock_cycles(cpi_a,cpi_f,cpi_m,cpi_b,i_count_a,i_count_f,i_count_m,i_count_b):
     clock_cycle=cpi_a*i_count_a+cpi_f*i_count_f+cpi_m*i_count_m+cpi_b*i_count_b
     return clock_cycle