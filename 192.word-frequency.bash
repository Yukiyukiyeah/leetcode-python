###
 # @Author: your name
 # @Date: 2020-12-08 14:38:26
 # @LastEditTime: 2020-12-08 14:38:26
 # @LastEditors: Please set LastEditors
 # @Description: In User Settings Edit
 # @FilePath: /leetcode-python/192.word-frequency.bash
### 
# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr -s ' ' '\n'|sort|uniq -c |sort -r|awk '{print $2" "$1}'