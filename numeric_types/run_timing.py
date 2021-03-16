def run_timing():
    """exercise 3"""
    run_times = []

    while True:
        run_time = input('Enter 6.21mi (10km) run time: ')
        if run_time == '':
            break
        else:
            run_times.append(float(run_time))

    print(f'Average of {sum(run_times)/len(run_times)}, over {len(run_times)} runs.')


if __name__ == '__main__':
    run_timing()
