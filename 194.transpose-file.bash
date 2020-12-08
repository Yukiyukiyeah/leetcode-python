###
 # @Author: your name
 # @Date: 2020-12-08 14:35:58
 # @LastEditTime: 2020-12-08 14:36:00
 # @LastEditors: Please set LastEditors
 # @Description: In User Settings Edit
 # @FilePath: /leetcode-python/194.transpose-file.bash
### 
# Read from the file file.txt and print its transposed content to stdout.
awk '{
    for (i=1;i<=NF;i++){
        if (NR==1){
            res[i]=$i
        }
        else{
            res[i]=res[i]" "$i
        }
    }
}END{
    for(j=1;j<=NF;j++){
        print res[j]
    }
}' file.txt