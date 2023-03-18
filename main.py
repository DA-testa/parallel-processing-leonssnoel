# Leons Jūlijs Strupītis 13. gr 1k. 221RDB402

import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)] # (time, thread index)
    heapq.heapify(threads)

    for job_time in data:
        time, thread_index = heapq.heappop(threads)
        output.append((thread_index, time))
        heapq.heappush(threads, (time + job_time, thread_index))

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)
    
    for res in result:
        print(res[0], res[1])

if __name__ == "__main__":
    main()
