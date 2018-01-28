class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        class Course(object):
            def __init__(self, num):
                self.num = num
                self.former = set()
                self.later = set()
        
        course_list = []    
        for i in xrange(numCourses):
            course_list.append(Course(i))
            
        for i in prerequisites:
            k = i[0]
            l = i[1]
            course_list[k].former.add(course_list[l])
            course_list[l].later.add(course_list[k])
        
        result_list = []
        cand_course = []
        other_course = []
        for course in course_list:
            if len(course.former) == 0:
                cand_course.append(course)
        
        while len(cand_course) > 0:
            course = cand_course.pop(0)
            result_list.append(course.num)
            for later_course in course.later:
                later_course.former.discard(course)
                if len(later_course.former) == 0:
                    cand_course.append(later_course)
        
        return result_list if len(result_list) == numCourses else []
