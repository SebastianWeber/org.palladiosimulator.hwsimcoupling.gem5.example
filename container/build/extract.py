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

search = "system.clk_domain.clock"
stat = ""
with open("m5out/stats.txt", "r") as trace:
    while True:
            line = trace.readline()
            if search in line:
                stat = line
            if not line:
                break

with open("m5out/ftrace.system.cpu.main", "w") as trace_main:
    trace_main.write(first)
    trace_main.write(last)
    trace_main.write(stat)

    trace_main.write(str((int(last.split(":")[0]) - int(first.split(":")[0])) / int(stat.replace("system.clk_domain.clock", "").replace("# Clock period in ticks (Tick)", "").strip())))

    print("Demand:" + str((int(last.split(":")[0]) - int(first.split(":")[0])) / int(stat.replace("system.clk_domain.clock", "").replace("# Clock period in ticks (Tick)", "").strip())))


