
class RectangleOverlap(object):

    def has_overlap(self, coords):
        coords.sort(key=lambda x: x[0])

        return coords[1][0] < coords[0][1]

    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x_overlap = self.has_overlap([(rec1[0], rec1[2]), (rec2[0], rec2[2])])
        y_overlap = self.has_overlap([(rec1[1], rec1[3]), (rec2[1], rec2[3])])

        return x_overlap and y_overlap


if __name__ == '__main__':
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    overlap = RectangleOverlap()
    print(overlap.isRectangleOverlap(rec1, rec2))
    
    
    
    
    