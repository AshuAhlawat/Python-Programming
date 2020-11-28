def count_substring(string, sub_string):
    count=0
    i=string.find(sub_string)
    while 1!=-1:
        count+=1
        i=string.find(sub_string,i+1)
    return count
def main():
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)