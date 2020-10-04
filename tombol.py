def minimumTekan(perintah):
    output = 0
    x = perintah[0]
    while x < perintah[1] or x > perintah[1]:
        x = x < perintah[1] and (x*2-perintah[1] > 1 and x-1 or x*2) or x-1
        
        if x > 1000 or x < 0:
            break;
        else:
            output += 1
    return output

print(minimumTekan([9, 16]))