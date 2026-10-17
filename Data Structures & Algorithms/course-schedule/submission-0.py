class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = {i: [] for i in range(numCourses)}
        for preq in prerequisites:
            prereq_map[preq[0]].append(preq[1])
        
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if prereq_map[course] == []:
                return True
            visit.add(course)
            for preq in prereq_map[course]:
                if not dfs(preq):
                    return False
            visit.remove(course)
            prereq_map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True