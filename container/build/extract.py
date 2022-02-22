import argparse

parser = argparse.ArgumentParser(description="Extract the resource demand.")
parser.add_argument("methodname", type=str)
args = parser.parse_args()

first = ""
last = ""
search = args.methodname
with open("m5out/ftrace.system.cpu", "r") as trace:
    with open("m5out/ftrace.system.cpu.cleaned", "w") as trace_cleaned:
        while True:
            line = trace.readline()
            if first == "":
                if search in line:
                    first = line
            if search in line:
                last = line
            if not line:
                break
            if not "_end" in line:
                trace_cleaned.write(line)

searchcpu = "system.clk_domain.clock"
searchhddread = "system.mem_ctrl.bytesReadSys"
searchhddwrite = "system.mem_ctrl.bytesWrittenSys"
cpu = ""
hddread = ""
hddwrite = ""
with open("m5out/stats.txt", "r") as trace:
    while True:
            line = trace.readline()
            if searchcpu in line:
                cpu = line
            if searchhddread in line:
                hddread = line
            if searchhddwrite in line:
                hddwrite = line
            if not line:
                break

with open("m5out/ftrace.system.cpu.main", "w") as trace_main:
    trace_main.write(first)
    trace_main.write(last)
    trace_main.write(cpu)
    
    cpustripped = str((int(last.split(":")[0]) - int(first.split(":")[0])) / int(cpu.replace("system.clk_domain.clock", "").replace("# Clock period in ticks (Tick)", "").strip()))
    
    hddreadstripped = int(hddread.replace("system.mem_ctrl.bytesReadSys", "").replace("# Total read bytes from the system interface side (Byte)", "").strip())
    
    hddwritestripped = int(hddwrite.replace("system.mem_ctrl.bytesWrittenSys", "").replace("# Total written bytes from the system interface side (Byte)", "").strip())

    trace_main.write(cpustripped)

    print("Demand:" + "CPU:" + cpustripped + ";" + "HDD:" + str(hddreadstripped + hddwritestripped))


