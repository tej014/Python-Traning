#break (Exit the Loop Immediately)
# i = 1
# while i<=10:
#     print("LALA")
#     if i==4:
#         print("hello")
#         break
#     i+=1

#continue (Skip the Current Iteration)
i=0
while i<=10:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1