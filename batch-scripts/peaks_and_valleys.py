from __future__ import print_function

from pyspark import SparkContext

sc = SparkContext(appName='VladsApp')

# Kind of works. haven't treated the edge cases
def find_peaks_and_valleys(accu, current_elem):
    prev_uniq_elem, before_prev_uniq_elem, peaks, valleys = accu

    if current_elem == prev_uniq_elem:
        return prev_uniq_elem, before_prev_uniq_elem, peaks, valleys

    if current_elem < prev_uniq_elem > before_prev_uniq_elem:
        # Found a peak!
        peaks.append(prev_uniq_elem)

    if current_elem > prev_uniq_elem < before_prev_uniq_elem:
        # Found a valley!
        valleys.append(prev_uniq_elem)

    return current_elem, prev_uniq_elem, peaks, valleys


if __name__ == '__main__':
    results = sc.parallelize([1,10,20,30,20,40,50,60,80,5,5,5,6,5,5,5,4,5],1).fold((None, None, [], []), find_peaks_and_valleys )

    print("Peaks", results[0][2])
    print("Valleys", results[0][3])
