def largest_histogram(histogram):
    data = histogram[:]  # to see the data when I will debug it in VS Code
    rectangles = []
    rectangles.append(min(data) * len(data))  # Check the bottom

    # Cut from the top
    max_elem = max(data)
    for i in range(0, max_elem):
        cur_rectangle = 0
        for j in range(0, len(data)):
            if data[j] == max_elem:
                cur_rectangle += max_elem
            elif j > 1 and data[j-1] == max_elem:
                rectangles.append(cur_rectangle)
                cur_rectangle = 0
        data = [max_elem - 1 if x == max_elem else x for x in data]
        max_elem -= 1

    return max(rectangles)

if __name__ == '__main__':
    assert largest_histogram([5]) == 5
    assert largest_histogram([5, 3]) == 6
    assert largest_histogram([1, 1, 4, 1]) == 4
    assert largest_histogram([1, 1, 3, 1]) == 4
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8
    assert largest_histogram([2, 1, 4, 5, 4, 3, 3]) == 12
