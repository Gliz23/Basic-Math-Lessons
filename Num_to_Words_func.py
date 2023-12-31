num = int(input("Enter a number: "))

def num_to_words_func(num):
    num_to_words={1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven',
    8 : 'eight', 9 : 'nine', 10 : 'ten', 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen',
    14 : 'fourteen', 15 : 'fifteen',16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
    19 : 'nineteen', 20 : 'twenty', 30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
    70 : 'seventy', 80 : 'eighty', 90 : 'ninety', 100 : 'one-hundred', 200: 'two-hundred',
    300: 'three-hundred', 400: 'four-hundred', 500: 'five-hundred', 600: 'six-hundred', 
    700: 'seven-hundred', 800: 'eight-hundred', 900: 'nine-hundred', 1000: 'one-thousand',
    2000: 'two-thousand', 3000: 'three-thousand', 4000: 'four-thousand', 5000: 'five-thousand',
    6000: 'six-thousand', 7000: 'seven-thousand', 8000: 'eight-thousand', 9000: 'nine-thousand',
    10000: 'ten-thousand', 20000: 'twenty thousand', 30000: 'thirty thousand', 40000: 'forty thousand', 
    50000: 'fifty thousand', 60000: 'sixty thousand', 70000: 'seventy thousand', 80000: 'eighty thousand', 
    90000: 'ninety thousand', 100000: 'one hundred thousand', 200000: 'two hundred thousand', 300000: 
    'three hundred thousand', 400000: 'four hundred thousand', 500000: 'five hundred thousand', 
    600000: 'six hundred thousand', 700000: 'seven hundred thousand', 800000: 'eight hundred thousand', 
    900000: 'nine hundred thousand', 1000000: 'one million', 2000000: 'two million', 3000000: 'three million', 
    4000000: 'four million', 5000000: 'five million', 6000000: 'six million', 7000000: 'seven million', 8000000: 
    'eight million', 9000000: 'nine million', 10000000: 'ten million', 20000000: 'twenty million', 30000000: 
    'thirty million', 40000000: 'forty million', 50000000: 'fifty million', 60000000: 'sixty million', 
    70000000: 'seventy million', 80000000: 'eighty million', 90000000: 'ninety million', 100000000: 'one hundred million',
    200000000: 'two hundred million', 300000000: 'three hundred million', 400000000: 'four hundred million', 
    500000000: 'five hundred million', 600000000: 'six hundred million', 700000000: 'seven hundred million', 
    800000000: 'eight hundred million',900000000: 'nine hundred million', 1000000000: 'one billion'}

    

    if num<= 1000000000:
        if num in num_to_words:
            words = num_to_words.get(num)
            ans = words
        else:
            if 0 < num < 100:
                # eg 12
                ones = num%10
                ones = num_to_words.get(ones)
                tens = num//10
                tens = tens * 10
                tens = num_to_words.get(tens)
                tens_in_words = f"{tens} {ones}"
                ans = tens_in_words
            elif 101 < num < 1000:
                # eg 123
                ones = num%10
                ones = num_to_words.get(ones)
                tens = ((num//10) % 10) * 10
                tens = num_to_words.get(tens)
                hunds = num // 100
                hunds = hunds * 100
                hunds = num_to_words.get(hunds)
                hunds_in_words = f"{hunds} and {tens} {ones}"
                ans = hunds_in_words
            elif 1001 < num < 10000:
                # eg 1234
                ones = num%10
                ones = num_to_words.get(ones)
                tens = ((num//10) % 10) * 10
                tens = num_to_words.get(tens)
                hunds = ((num // 100) % 10) * 100
                hunds = num_to_words.get(hunds)
                thnds = (num // 1000) * 1000
                thnds = num_to_words.get(thnds)
                thnds_in_words = f"{thnds} {hunds} and {tens} {ones}"
                ans = thnds_in_words
            elif 10001 < num < 100000:
                # eg 12345
                ones = num%10
                ones = num_to_words.get(ones)

                tens = ((num//10) % 10) * 10
                tens = num_to_words.get(tens)

                hunds = ((num // 100) % 10) * 100
                hunds = num_to_words.get(hunds)

                thnd_s = (num // 1000)
                thnds = (thnd_s % 10) * 1000
                thnds = num_to_words.get(thnds)

                tthd_s = (num // 10000)
                tthds = (tthd_s  * 10000)
                tthds = num_to_words.get(tthds)
                if 10 < thnd_s < 20:
                    thnd_s = num_to_words.get(thnd_s)
                    thnd_s = f"{thnd_s} thousand"
                    tthds_in_words = f"{thnd_s} {hunds} and {tens} {ones}"
                    ans = tthds_in_words
                elif (20 < thnd_s < 30) or (30 < thnd_s < 40) or (40 < thnd_s < 50) or (50 < thnd_s < 60) or (60 < thnd_s < 70) or (70 < thnd_s < 80) or (80 < thnd_s < 90) or (90 < thnd_s < 100):
                    thnds_tens = (thnd_s // 10) * 10
                    thnds_tens = num_to_words.get(thnds_tens)
                    thnds_ones = thnd_s % 10
                    thnds_ones_s = num_to_words.get(thnds_ones)
                    thnds_dgt = f" {thnds_tens} {thnds_ones_s} thousand"
                    tthds_in_words = f"{thnds_dgt} {hunds} and {tens} {ones}"
                    ans = tthds_in_words
                
                else:
                    tthds_in_words = f"{tthds} {thnds} {hunds} and {tens} {ones}"
                ans = tthds_in_words
            elif 100001 < num < 1000000:
                # eg 123456
                ones = num%10
                ones = num_to_words.get(ones)

                tens = ((num//10) % 10) * 10
                tens = num_to_words.get(tens)

                hunds = ((num // 100) % 10) * 100
                hunds = num_to_words.get(hunds)

                thnd_s = (num // 1000)
                T_ones = thnd_s%10
                T_ones = num_to_words.get(T_ones)

                T_tens = ((thnd_s//10) % 10) * 10
                T_tens = num_to_words.get(T_tens)

                T_hunds = ((thnd_s // 100) % 10) * 100
                T_hunds = num_to_words.get(T_hunds)

                H_thnd_s = f"{T_hunds} and {T_tens} {T_ones} thousand"
                H_thds_in_words = f"{H_thnd_s} {hunds} and {tens} {ones}"
                ans = H_thds_in_words

    else:
        ans = num

    print(ans)

num = num_to_words_func(num)
print(num)
