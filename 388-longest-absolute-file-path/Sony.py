class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        file_entries = input.split('\n')
        if len(file_entries) == 0:
            return 0
        max_len = cur_depth = cur_dir_len = 0
        dir_stack = [0]

        for file_entry in file_entries:
            file_depth = file_entry.count('\t') + 1
            file_len = len(file_entry) - file_depth + 1
            if file_entry.find('.') == -1:
                #it is a directory
                if file_depth <= cur_depth:
                    #not in current directory, step back
                    dir_stack = dir_stack[:file_depth]
                    cur_dir_len = dir_stack[-1] + file_len + 1
                elif file_depth == cur_depth + 1:
                    #sub directory
                    cur_dir_len += file_len + 1
                else:
                    #weired situation
                    raise BaseException
                dir_stack.append(cur_dir_len)
                cur_depth = file_depth
            else:
                #it is a file
                if file_depth <= cur_depth:
                    #not in current directory, step back
                    dir_stack = dir_stack[:file_depth]
                    cur_depth = file_depth - 1
                    cur_dir_len = dir_stack[-1]
                elif file_depth > cur_depth + 1:
                    #weired situation
                    raise BaseException
                total_len = file_len + cur_dir_len
                if total_len > max_len:
                    max_len = total_len
        return max_len

if __name__ == '__main__':

    sol = Solution()
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    print sol.lengthLongestPath(input)