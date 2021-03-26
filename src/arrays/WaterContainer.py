
def max_area(height):
    """
    Container With Most Water
    """
    left = 0
    right = len(height)-1
    area = 0
    max_area = 0

    while left < right:
        if height[left] < height[right]:
            area = (right-left)*height[left]
            if(area > max_area):
                max_area = area
            left += 1
        else:
            area = (right-left)*height[right]
            if(area > max_area):
                max_area = area
            right -= 1
    
    print(max_area)
    
if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    max_area(height=height)
    