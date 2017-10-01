class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        file_entries = input.split('\n')
        dir_dict = {0:0}
        max_len = 0

        for file_entry in file_entries:
            file_depth = file_entry.count('\t') + 1
            file_len = len(file_entry) - file_depth + 1
            if file_entry.find('.') == -1:
                #directory
                dir_dict[file_depth] = dir_dict[file_depth - 1] + file_len + 1
            else:
                max_len = max(max_len, dir_dict[file_depth - 1] + file_len)
                print file_entry, dir_dict, file_len

        return max_len

if __name__ == '__main__':

    sol = Solution()
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    #input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    print sol.lengthLongestPath(input)