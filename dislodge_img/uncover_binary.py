def uncover_info(img_bin):
    current_message = ""
    bin_message = []
    # print(img_bin) This checks out, nothing is wrong here. 
    for row in img_bin:
        for pixel in row:
            for bin in pixel:
                if len(current_message) < 8:
                    current_message += bin[-1]
                elif len(current_message) == 8: 
                    if current_message == "10101010":
                        print("We've go an indicator")
                        
                    if current_message == "10101010" and bin_message[-1] == "10101010":
                        return bin_message
                    
                    else:
                        # print("adding message to the bin_ ", current_message)
                        bin_message.append(current_message)
                        if len(bin_message) == 4:
                            print(current_message)
                            print(bin_message)
                        current_message = f"{bin[-1]}"
