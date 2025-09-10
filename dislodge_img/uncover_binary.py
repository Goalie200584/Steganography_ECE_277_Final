def uncover_info(img_bin):
    current_message = ""
    bin_message = []
    for row in img_bin:
        for pixel in row:
            for bin in pixel:
                if len(current_message) < 8:
                    current_message += bin[-1]
                elif len(current_message) == 8:
                    if current_message == "10101010" and bin_message[-1] == "10101010":
                        return bin_message
                    else:
                        bin_message.append(current_message)
                        current_message = f"{bin[-1]}"