jobs_as_list = list(map(int, input().split(', ')))
index = int(input())
jobs = dict()

for i in range(0, len(jobs_as_list)):
    jobs[i] = jobs_as_list[i]
sorted_jobs = dict(sorted(jobs.items(), key=lambda x: x[1]))

clock_cycles = 0
for key, value in sorted_jobs.items():
    clock_cycles += value
    if key == index:
        break

print(clock_cycles)
