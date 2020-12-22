import time
import random

def insertion_sort(arr):
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j-1] > cur:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = cur

def selection_sort(arr):
    for k in range(len(arr)):
        j = k
        min_of_arr = k
        while j+1 < len(arr):
            j = j+1
            if arr[min_of_arr] > arr[j]:
                min_of_arr = j
        temp = arr[k]
        arr[k] = arr[min_of_arr]
        arr[min_of_arr] = temp


if __name__ == '__main__':
    for a in [1000, 2500, 5000, 7500, 10000]:

        arr_ran= [random.randint(0, 100000) for x in range(1, a+1)]
        arr_ran_sel = list(arr_ran)
        arr_inc = [i for i in range(1, a+1)]
        arr_inc_sel = list(arr_inc)
        arr_dec = [i for i in range(a,0,-1)]
        arr_dec_sel = list(arr_dec)

        start_ran_ins = time.process_time()
        insertion_sort(arr_ran)
        end_ran_ins = time.process_time()

        start_ran_sel = time.process_time()
        selection_sort(arr_ran_sel)
        end_ran_sel = time.process_time()

        start_inc_ins = time.process_time()
        insertion_sort(arr_inc)
        end_inc_ins = time.process_time()

        start_inc_sel = time.process_time()
        selection_sort(arr_inc_sel)
        end_inc_sel = time.process_time()

        start_dec_ins = time.process_time()
        insertion_sort(arr_dec)
        end_dec_ins = time.process_time()

        start_dec_sel = time.process_time()
        selection_sort(arr_dec_sel)
        end_dec_sel = time.process_time()

        if a == 1000:
            name = 'One Thousand '
        elif a == 2500:
            name = 'Two Thousands and Five Hundreds '
        elif a == 5000:
            name = 'Five Thousands '
        elif a == 7500:
            name = 'Seven Thousands and Five Hundreds '
        else:
            name = 'Ten Thousands '

        print( name + 'Increasing Insertion for Random Values: ' + '{:.6f}'.format(end_ran_ins-start_ran_ins))
        print( name + 'Increasing Selection for Random Values: ' + '{:.6f}'.format(end_ran_sel-start_ran_sel))
        print( name + 'Increasing Insertion for Increasing Values: ' + '{:.6f}'.format(end_inc_ins-start_inc_ins))
        print( name + 'Increasing Selection for Increasing Values: ' + '{:.6f}'.format(end_inc_sel-start_inc_sel))
        print( name + 'Increasing Insertion for Decreasing Values: ' + '{:.6f}'.format(end_dec_ins-start_dec_ins))
        print( name + 'Increasing Selection for Decreasing Values: ' + '{:.6f}'.format(end_dec_sel-start_dec_sel))
