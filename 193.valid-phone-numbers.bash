###
 # @Author: your name
 # @Date: 2020-11-13 21:23:00
 # @LastEditTime: 2020-11-13 21:23:01
 # @LastEditors: Please set LastEditors
 # @Description: In User Settings Edit
 # @FilePath: /leetcode-python/leetcode-python/193.valid-phone-numbers.bash
### 
# Read from the file file.txt and output all valid phone numbers to stdout.
grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt