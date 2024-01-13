import sys

for arg in sys.argv[1:]:
    print('\n', arg)
    with open(arg) as f:
        sensor_history = [list(map(int, line.split())) for line in f.readlines()]

    def extrapolate_next(history):
        extrapolated_history = [history]

        for cur_ext_history in extrapolated_history:
            next_ext_history = []
            for id, _ in enumerate(cur_ext_history[:-1]):
                next_ext_history.append(cur_ext_history[id+1] - cur_ext_history[id])
            
            extrapolated_history.append(next_ext_history)
            if len(next_ext_history) == next_ext_history.count(0):
                break


        return sum([each_ext_history[-1] for each_ext_history in extrapolated_history])

    def extrapolate_prev(history):
        extrapolated_history = [history]

        for cur_ext_history in extrapolated_history:
            next_ext_history = []
            for id, _ in enumerate(cur_ext_history[:-1]):
                next_ext_history.append(cur_ext_history[id+1] - cur_ext_history[id])

            extrapolated_history.append(next_ext_history)
            if len(next_ext_history) == next_ext_history.count(0):
                break
        
        next = 0
        for each_ext_history in extrapolated_history[-1::-1]:
            next = each_ext_history[0] - next

        return next
    
    total = 0
    for each_sensor_history in sensor_history:
        total += extrapolate_next(each_sensor_history)
    
    total_2 = 0
    for each_sensor_history in sensor_history:
        total_2 += extrapolate_prev(each_sensor_history)

    print("part 1: ", total)
    print("part 2: ", total_2)